"""Preserve complete source history while withholding expired perception values."""
from __future__ import annotations
from dataclasses import dataclass
import time
import numpy as np

from .camera_clock_guard_v1 import (
    ClockGuardedCameraPipeline, FreshCameraResult, CameraTimingFault,
    FRAME_RESPONSE_BUDGET_NS, IMAGE_AGE_BUDGET_NS, integer_ns, _Violation)


@dataclass(frozen=True)
class CameraFrameOutcome:
    status: str
    time_s: float
    sequence: int
    state_episode: int
    generation: int
    camera_timestamps_ns: tuple[int, int]
    source_host_bounds_ns: tuple[tuple[int, int], tuple[int, int]]
    ready_host_ns: int
    entered_host_ns: int
    checked_host_ns: int
    valid_until_host_ns: int
    late_at_admission: bool
    computed_neural_rate: bool
    new_episode_event: bool
    episode_event_expired: bool
    fresh_result: FreshCameraResult | None


class ContinuingCameraPipeline(ClockGuardedCameraPipeline):
    """Continue only complete validated history; true faults still require reset.

    A withheld outcome carries timing/status but no neural rate/decision values.
    require_fresh accepts only outcome.fresh_result, never the outcome itself.
    No acquisition buffering, lost-frame reconstruction or motor action occurs.
    """
    def __init__(self, pipeline, clock_mapping, *, host_clock_ns=time.perf_counter_ns):
        self._state_episode = 0
        self._last_delay = None
        self._consecutive_withheld = 0
        super().__init__(pipeline, clock_mapping, host_clock_ns=host_clock_ns)
        self._counts.update(processed_frames=0, withheld_frames=0, computed_neural_rates=0,
            delivered_neural_rates=0, withheld_neural_rates=0, delivered_episode_events=0, expired_episode_events=0)

    def reset(self, clock_mapping=None):
        with self._lock:
            super().reset(clock_mapping)
            self._state_episode += 1
            self._last_delay = None
            self._consecutive_withheld = 0

    def step(self, left, right, timestamps_ns, acquisition_modes, *, ready_host_ns):
        with self._lock:
            if self._requires_reset:
                self._counts['rejected_frames'] += 1
                raise CameraTimingFault(self._last_fault)
            phase='admission';entered=checked=deadline=None
            try:
                entered=self._observe()
                ready=integer_ns(ready_host_ns,'image availability time')
                if ready>entered:
                    raise _Violation('FUTURE_AVAILABILITY','Image availability is later than the host observation')
                if self._last_ready_ns is not None and ready<self._last_ready_ns:
                    raise _Violation('REORDERED_AVAILABILITY','Image availability moved backwards')
                if len(timestamps_ns)!=2:raise ValueError('Two camera exposure timestamps are required')
                stamps=tuple(integer_ns(t,'camera timestamp') for t in timestamps_ns)
                bounds=tuple(self._mapping.bounds(t) for t in stamps)
                if max(b[1] for b in bounds)>ready:
                    raise _Violation('FUTURE_EXPOSURE','Exposure midpoint is not definitely before image availability')
                deadline=min(ready+FRAME_RESPONSE_BUDGET_NS,min(b[0] for b in bounds)+IMAGE_AGE_BUDGET_NS)
                late_entry=entered>deadline
                phase='processing'
                sample=self._pipeline.step(left,right,stamps,acquisition_modes)
                model_time,rate,detection=self._payload(sample,self._emitted_detection)
                calibration_status=sample['calibration_status']
                if calibration_status not in ('MEASURED_CALIBRATION','SYNTHETIC_TEST_ONLY'):
                    raise _Violation('INVALID_OUTPUT','Unrecognized calibration status')
                if rate is not None and not np.issubdtype(rate.dtype,np.floating):
                    raise _Violation('INVALID_OUTPUT','Neural rates must be real floating-point values')
                phase='completion';checked=self._observe()
                late=late_entry or checked>deadline
                has_rate=rate is not None;has_event=bool(detection)
                # Observe even a withheld event, so cached decisions never reappear.
                self._emitted_detection=self._emitted_detection or has_event
                result=None
                if late:
                    self._generation+=1  # Invalidate old output tokens, not neural history.
                    self._last_delay=dict(sequence=self._sequence,state_episode=self._state_episode,
                        entered_host_ns=entered,checked_host_ns=checked,valid_until_host_ns=deadline,
                        late_at_admission=late_entry,episode_event_expired=has_event)
                else:
                    result=FreshCameraResult(model_time,rate,detection,stamps,bounds,ready,entered,checked,
                        deadline,self._generation,self._sequence,self._mapping.status,
                        calibration_status,self._owner)
                outcome=CameraFrameOutcome('withheld' if late else 'fresh',model_time,self._sequence,
                    self._state_episode,self._generation,stamps,bounds,ready,entered,checked,deadline,
                    late_entry,has_rate,has_event,late and has_event,result)
            except BaseException as exc:
                self._counts['rejected_frames']+=1
                fault=self._latch(exc,phase,entered=entered,checked=checked,deadline=deadline)
                if not isinstance(exc,Exception):raise
                raise fault from exc
            self._sequence+=1
            self._counts['processed_frames']+=1
            self._counts['computed_neural_rates']+=int(has_rate)
            self._last_ready_ns=ready
            if late:
                self._counts['withheld_frames']+=1
                self._counts['withheld_neural_rates']+=int(has_rate)
                self._counts['expired_episode_events']+=int(has_event)
                self._consecutive_withheld+=1
            else:
                self._counts['accepted_frames']+=1
                self._counts['delivered_neural_rates']+=int(has_rate)
                self._counts['delivered_episode_events']+=int(has_event)
                self._consecutive_withheld=0
            return outcome

    def status(self):
        with self._lock:
            value=super().status()
            value.update(schema='continuing_camera_v1',state_episode=self._state_episode,
                history_valid=not self._requires_reset,
                consecutive_withheld=self._consecutive_withheld,
                last_delay=None if self._last_delay is None else dict(self._last_delay),
                history_preserved_through_timing_overruns=True,original_timing_gate_changed=False)
            return value
