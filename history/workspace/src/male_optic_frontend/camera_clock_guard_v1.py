"""Explicit camera/host clock bounds and expiring, reset-aware perception results.

This wrapper validates supplied timing assertions; it does not calibrate clocks
or establish real-time execution. Own the wrapped pipeline exclusively.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from numbers import Integral
import threading
import time
from typing import Callable

import numpy as np

FRAME_RESPONSE_BUDGET_NS = 5_000_000
IMAGE_AGE_BUDGET_NS = 5_000_000


def integer_ns(value, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral) or value < 0:
        raise ValueError(f'{name} must be a nonnegative integer')
    return int(value)


@dataclass(frozen=True)
class CameraHostClockMapping:
    camera_anchor_ns: int
    host_anchor_ns: int
    rate_numerator: int
    rate_denominator: int
    uncertainty_ns: int
    valid_camera_min_ns: int
    valid_camera_max_ns: int
    status: str
    provenance: str
    timestamp_semantics: str = 'exposure_midpoint'

    def __post_init__(self):
        for name in ('camera_anchor_ns', 'host_anchor_ns', 'rate_numerator', 'rate_denominator',
                     'uncertainty_ns', 'valid_camera_min_ns', 'valid_camera_max_ns'):
            object.__setattr__(self, name, integer_ns(getattr(self, name), name))
        if min(self.rate_numerator, self.rate_denominator) == 0:
            raise ValueError('Clock rate must be a positive rational number')
        if self.valid_camera_min_ns > self.valid_camera_max_ns:
            raise ValueError('Clock validity endpoints are reversed')
        if self.status not in ('MEASURED_CLOCK_MAPPING', 'SYNTHETIC_TEST_ONLY'):
            raise ValueError('Clock mapping status must be explicit')
        if not isinstance(self.provenance, str) or not self.provenance.strip():
            raise ValueError('Clock mapping provenance is required')
        if self.timestamp_semantics != 'exposure_midpoint':
            raise ValueError('Convert camera timestamps to exposure midpoints before this interface')
        # Affine monotonicity makes the earliest endpoint the smallest bound.
        if self._bounds(self.valid_camera_min_ns)[0] < 0:
            raise ValueError('Declared mapping permits negative host clock values')

    def _bounds(self, camera_ns):
        numerator = (camera_ns - self.camera_anchor_ns) * self.rate_numerator
        lower = self.host_anchor_ns + numerator // self.rate_denominator - self.uncertainty_ns
        upper = self.host_anchor_ns - (-numerator // self.rate_denominator) + self.uncertainty_ns
        return lower, upper

    def bounds(self, camera_ns):
        camera_ns = integer_ns(camera_ns, 'camera timestamp')
        if not self.valid_camera_min_ns <= camera_ns <= self.valid_camera_max_ns:
            raise ValueError('Camera timestamp is outside the clock mapping validity interval')
        return self._bounds(camera_ns)


@dataclass(frozen=True)
class EpisodeDecision:
    role: str
    score_deg_s: float
    decision: int
    cutoff: float


@dataclass(frozen=True)
class FreshCameraResult:
    time_s: float
    rate: np.ndarray | None
    new_episode_detection: tuple[EpisodeDecision, ...]
    camera_timestamps_ns: tuple[int, int]
    source_host_bounds_ns: tuple[tuple[int, int], tuple[int, int]]
    ready_host_ns: int
    entered_host_ns: int
    checked_host_ns: int
    valid_until_host_ns: int
    generation: int
    sequence: int
    clock_mapping_status: str
    calibration_status: str
    _owner: object = field(repr=False, compare=False)


class CameraTimingFault(RuntimeError):
    def __init__(self, record):
        self.record = dict(record)
        super().__init__(f"{record['phase']}: {record['reason']}")


class StaleCameraResult(ValueError):
    pass


class _Violation(ValueError):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


class ClockGuardedCameraPipeline:
    """Serialized one-pair API; explicit reset is required after any step fault.

    ready_host_ns is recorded by the producer once both complete arrays are
    available on the same monotonic host clock used here. Camera timestamps
    denote exposure midpoints in the mapping's common camera clock. No driver,
    synchronization estimator, automatic recovery or motor action is provided.
    """
    def __init__(self, pipeline, clock_mapping: CameraHostClockMapping, *,
                 host_clock_ns: Callable[[], int] = time.perf_counter_ns):
        if not isinstance(clock_mapping, CameraHostClockMapping):
            raise ValueError('An explicit validated camera-to-host mapping is required')
        if pipeline.adapter.period_ns != FRAME_RESPONSE_BUDGET_NS:
            raise ValueError('This wrapper preserves the frozen 5-ms frontend cadence')
        self._pipeline = pipeline
        self._mapping = clock_mapping
        self._clock = host_clock_ns
        self._lock = threading.RLock()
        self._owner = object()
        self._generation = 0
        self._last_host_ns = None
        self._last_ready_ns = None
        self._emitted_detection = False
        self._sequence = 0
        self._requires_reset = True
        self._last_fault = None
        self._counts = dict(accepted_frames=0, rejected_frames=0, resets=0, consumer_rejections=0)
        self.reset()

    @property
    def requires_reset(self):
        with self._lock:
            return self._requires_reset

    def _observe(self):
        now = integer_ns(self._clock(), 'host clock')
        if self._last_host_ns is not None and now < self._last_host_ns:
            raise _Violation('HOST_CLOCK_ROLLBACK', 'Host monotonic clock moved backwards')
        self._last_host_ns = now
        return now

    def _latch(self, exc, phase, *, entered=None, checked=None, deadline=None):
        self._requires_reset = True
        self._generation += 1
        self._last_fault = dict(phase=phase, reason=str(exc)[:1024],
            code=getattr(exc, 'code', 'PIPELINE_ERROR'), error_type=type(exc).__name__,
            entered_host_ns=entered, checked_host_ns=checked, valid_until_host_ns=deadline,
            generation=self._generation, last_observed_host_ns=self._last_host_ns)
        return CameraTimingFault(self._last_fault)

    def reset(self, clock_mapping=None):
        with self._lock:
            try:
                if clock_mapping is not None and not isinstance(clock_mapping, CameraHostClockMapping):
                    raise ValueError('Replacement clock mapping must be explicitly validated')
                self._pipeline.reset()
                self._observe()
            except BaseException as exc:
                fault = self._latch(exc, 'reset')
                if not isinstance(exc, Exception):
                    raise
                raise fault from exc
            if clock_mapping is not None:
                self._mapping = clock_mapping
            self._generation += 1
            self._last_ready_ns = None
            self._emitted_detection = False
            self._sequence = 0
            self._requires_reset = False
            self._last_fault = None
            self._counts['resets'] += 1

    @staticmethod
    def _payload(sample, emitted):
        model_time = float(sample['time_s'])
        if not np.isfinite(model_time) or model_time < 0:
            raise _Violation('INVALID_OUTPUT', 'Nonfinite or negative model output time')
        value = sample['rate']
        rate = None if value is None else np.array(value, copy=True)
        if rate is not None:
            if rate.ndim != 1 or not rate.size or not np.isfinite(rate).all():
                raise _Violation('INVALID_OUTPUT', 'Neural rates must be a finite nonempty vector')
            rate.setflags(write=False)
        detection = sample.get('episode_detection')
        decisions = []
        if detection is not None and not emitted:
            if rate is None:
                raise _Violation('INVALID_OUTPUT', 'New episode decisions require a published source-time rate')
            for role, item in detection.items():
                decision = item['decision']
                if isinstance(decision, (bool, np.bool_)) or not isinstance(decision, Integral) or decision not in (-1, 0, 1):
                    raise _Violation('INVALID_OUTPUT', 'Invalid episode decision')
                score, cutoff = float(item['score_deg_s']), float(item['cutoff'])
                if not np.isfinite([score, cutoff]).all() or cutoff < 0:
                    raise _Violation('INVALID_OUTPUT', 'Invalid episode score or cutoff')
                decisions.append(EpisodeDecision(str(role), score, int(decision), cutoff))
        return model_time, rate, tuple(decisions)

    def step(self, left, right, timestamps_ns, acquisition_modes, *, ready_host_ns):
        with self._lock:
            if self._requires_reset:
                self._counts['rejected_frames'] += 1
                raise CameraTimingFault(self._last_fault)
            phase = 'admission'; entered = checked = deadline = None
            try:
                entered = self._observe()
                ready = integer_ns(ready_host_ns, 'image availability time')
                if ready > entered:
                    raise _Violation('FUTURE_AVAILABILITY', 'Image availability is later than the host observation')
                if self._last_ready_ns is not None and ready < self._last_ready_ns:
                    raise _Violation('REORDERED_AVAILABILITY', 'Image availability moved backwards')
                if len(timestamps_ns) != 2:
                    raise ValueError('Two camera exposure timestamps are required')
                stamps = tuple(integer_ns(t, 'camera timestamp') for t in timestamps_ns)
                bounds = tuple(self._mapping.bounds(t) for t in stamps)
                if max(b[1] for b in bounds) > ready:
                    raise _Violation('FUTURE_EXPOSURE', 'Exposure midpoint is not definitely before image availability')
                deadline = min(ready + FRAME_RESPONSE_BUDGET_NS,
                    min(b[0] for b in bounds) + IMAGE_AGE_BUDGET_NS)
                if entered > deadline:
                    raise _Violation('STALE_INPUT', 'Input already exceeds the response or image-age bound')
                phase = 'processing'
                sample = self._pipeline.step(left, right, stamps, acquisition_modes)
                model_time, rate, detection = self._payload(sample, self._emitted_detection)
                phase = 'completion'
                checked = self._observe()
                if checked > deadline:
                    raise _Violation('LATE_RESULT', 'Computed result exceeds the response or image-age bound')
                result = FreshCameraResult(model_time, rate, detection, stamps, bounds, ready, entered,
                    checked, deadline, self._generation, self._sequence, self._mapping.status,
                    str(sample['calibration_status']), self._owner)
            except BaseException as exc:
                self._counts['rejected_frames'] += 1
                fault = self._latch(exc, phase, entered=entered, checked=checked, deadline=deadline)
                if not isinstance(exc, Exception):
                    raise
                raise fault from exc
            self._sequence += 1
            self._counts['accepted_frames'] += 1
            self._last_ready_ns = ready
            self._emitted_detection = self._emitted_detection or bool(detection)
            return result

    def require_fresh(self, result):
        """Check a result immediately before consumption; certifies this instant only."""
        with self._lock:
            try:
                now = self._observe()
            except BaseException as exc:
                fault = self._latch(exc, 'consumer')
                if not isinstance(exc, Exception):
                    raise
                raise fault from exc
            if (not isinstance(result, FreshCameraResult) or result._owner is not self._owner or
                    self._requires_reset or result.generation != self._generation or
                    now < result.checked_host_ns or now > result.valid_until_host_ns):
                self._counts['consumer_rejections'] += 1
                raise StaleCameraResult('Foreign, invalidated, future or expired camera result')
            return result

    def status(self):
        with self._lock:
            return dict(schema='camera_clock_guard_v1', requires_reset=self._requires_reset,
                generation=self._generation, next_sequence=self._sequence,
                frame_response_budget_ns=FRAME_RESPONSE_BUDGET_NS, image_age_budget_ns=IMAGE_AGE_BUDGET_NS,
                clock_mapping_status=self._mapping.status, clock_mapping_provenance=self._mapping.provenance,
                counts=dict(self._counts), last_fault=None if self._last_fault is None else dict(self._last_fault),
                physical_clock_mapping_validated=False, physical_camera_validated=False,
                hard_real_time_certified=False)
