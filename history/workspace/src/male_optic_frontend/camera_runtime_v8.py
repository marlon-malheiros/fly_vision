"""Frozen numerical model with explicit publication after complete delayed input."""
from pathlib import Path
import time
from .camera_clock_guard_v1 import CameraHostClockMapping
from .continuing_camera_v1 import ContinuingCameraPipeline
from .camera_runtime_v6 import load_clock_mapping,build
from .hardware_runtime_split_v1 import HardwareRuntimeSplitV1
from .sensor_adapter_v1 import CameraPerceptionPipeline
from .sensor_adapter_v2 import CompiledStereoRetinalAdapter


def create_continuing_pipeline(model,calibration,clock_mapping,*,library_directory=None,
        known_speed=None,host_clock_ns=time.perf_counter_ns):
    if not isinstance(clock_mapping,CameraHostClockMapping):
        raise ValueError('Supply an explicit validated camera/host clock mapping')
    model=Path(model);directory=Path(library_directory or model)
    runtime=HardwareRuntimeSplitV1(model,directory/'neural_cpu.so',directory/'frontend_cpu.so',known_speed=known_speed)
    adapter=CompiledStereoRetinalAdapter(calibration,runtime.metadata['frontend'],directory/'projection_cpu.so')
    return ContinuingCameraPipeline(CameraPerceptionPipeline(adapter,runtime),clock_mapping,host_clock_ns=host_clock_ns)
