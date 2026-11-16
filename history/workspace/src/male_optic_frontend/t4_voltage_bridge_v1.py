"""Experimental T4 voltage-to-drive adapter; not a synaptic release model.

The historical rectified affine mapping is an engineering assumption. This
module does not generate voltages, infer retinal locations, or resample clocks.
"""

from __future__ import annotations

import numpy as np

from .drive_adapter import DriveTable


def insert_t4_voltage(
    baseline: DriveTable,
    voltage_time_s,
    voltage_body_ids,
    voltage_mv,
    *,
    resting_mv: float,
    span_mv: float,
) -> DriveTable:
    """Replace explicitly named T4 columns with a rectified voltage proxy.

    The proxy is max(V - resting_mv, 0) / span_mv; values above one are
    rejected rather than silently clipped. All clocks must match exactly and
    nonselected columns are copied from the supplied baseline unchanged.
    Voltage columns must have the same order as voltage_body_ids.
    """
    time = np.asarray(voltage_time_s, dtype=np.float64)
    voltage = np.asarray(voltage_mv, dtype=np.float64)
    ids = tuple(str(item) for item in voltage_body_ids)
    if not ids or len(ids) != len(set(ids)):
        raise ValueError("Voltage body IDs must be nonempty and unique")
    if time.shape != baseline.time_s.shape or not np.array_equal(time, baseline.time_s):
        raise ValueError("Voltage and baseline clocks must match exactly")
    if voltage.shape != (time.size, len(ids)) or not np.isfinite(voltage).all():
        raise ValueError("Voltage must be finite and match the clock and IDs")
    if not np.isfinite(resting_mv) or not np.isfinite(span_mv) or span_mv <= 0:
        raise ValueError("Resting voltage and positive voltage span must be finite")
    index = {body: i for i, body in enumerate(baseline.body_ids)}
    if any(body not in index for body in ids):
        raise ValueError("Voltage IDs must all be present in the baseline")
    selected = [index[body] for body in ids]
    if any(baseline.layers[i] not in ("T4a", "T4b", "T4c", "T4d") for i in selected):
        raise ValueError("Only explicitly labeled T4 cells can be replaced")
    converted = np.maximum(voltage - resting_mv, 0.0) / span_mv
    if not np.isfinite(converted).all() or np.any(converted > 1):
        raise ValueError("Converted drive exceeds [0, 1]; choose explicit parameters")
    drive = baseline.drive.copy()
    drive[:, selected] = converted
    return DriveTable(baseline.time_s.copy(), baseline.body_ids, baseline.layers, drive)
