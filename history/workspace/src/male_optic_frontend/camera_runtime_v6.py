"""Construct the frozen CPU perception pipeline with explicit clock freshness."""
from __future__ import annotations
import json
from pathlib import Path
import time

from .camera_clock_guard_v1 import CameraHostClockMapping, ClockGuardedCameraPipeline
from .camera_runtime_v5 import build
from .hardware_runtime_split_v1 import HardwareRuntimeSplitV1
from .sensor_adapter_v1 import CameraPerceptionPipeline
from .sensor_adapter_v2 import CompiledStereoRetinalAdapter


def load_clock_mapping(path):
    values = json.loads(Path(path).read_text())
    if not isinstance(values, dict) or values.pop('schema', None) != 'camera_host_clock_mapping_v1':
        raise ValueError('Require an explicit versioned camera-to-host clock mapping')
    try:
        return CameraHostClockMapping(**values)
    except TypeError as exc:
        raise ValueError('Clock mapping fields are missing or unsupported') from exc


def create_guarded_pipeline(model, calibration, clock_mapping, *, library_directory=None,
                            known_speed=None, host_clock_ns=time.perf_counter_ns):
    if not isinstance(clock_mapping, CameraHostClockMapping):
        raise ValueError('Supply a CameraHostClockMapping, without automatic clock inference')
    model = Path(model)
    directory = Path(library_directory or model)
    runtime = HardwareRuntimeSplitV1(model, directory/'neural_cpu.so', directory/'frontend_cpu.so',
                                     solver_dt=.001, known_speed=known_speed)
    adapter = CompiledStereoRetinalAdapter(calibration, runtime.metadata['frontend'], directory/'projection_cpu.so')
    return ClockGuardedCameraPipeline(CameraPerceptionPipeline(adapter, runtime), clock_mapping,
                                      host_clock_ns=host_clock_ns)
