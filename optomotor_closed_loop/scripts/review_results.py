"""Separate arithmetic and integrity review of saved closed-loop evidence.

This is numerical verification by a different calculation, not independent
biological validation or a review by an independent research group.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import numpy as np


def review(folder):
    summary = json.loads((folder / "summary.json").read_text())
    lock = json.loads((folder / "before_test.json").read_text())
    config = lock["config"]
    for path, expected in lock["sources"].items():
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"Frozen source changed: {path}")
    with (folder / "episodes.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    expected_cases = len(config["test_seeds"]) * len(config["translation_speeds_m_s"]) * (1 + len(config["disturbance_deg_s"])) * len(lock["modes"])
    if len(rows) != expected_cases or len({r["key"] for r in rows}) != expected_cases:
        raise RuntimeError("Incomplete or duplicate experiment cases")
    if set(config["calibration_seeds"]) & set(config["test_seeds"]):
        raise RuntimeError("Calibration/test scene overlap")
    with np.load(folder / "traces.npz", allow_pickle=False) as bank:
        if set(bank.files) != {r["key"] for r in rows}:
            raise RuntimeError("Trace/case mismatch")
        maximum_error = 0.0
        for row in rows:
            a = bank[row["key"]]
            values = [float(r[1]) for r in a if config["disturbance_on_s"] <= r[0] < config["disturbance_off_s"]]
            rms = math.degrees(math.sqrt(math.fsum(x * x for x in values) / len(values)))
            maximum_error = max(maximum_error, abs(rms - float(row["rms_yaw_deg_s"])))
            if not np.isfinite(a).all():
                raise RuntimeError("Nonfinite trace")
            if row["mode"] == "open_loop":
                if np.max(np.abs(a[:, 3])) != 0:
                    raise RuntimeError("No-controller trace has motor input")
                np.testing.assert_allclose(a[:, 1], a[:, 8], atol=1e-14)
        if maximum_error > 1e-10:
            raise RuntimeError("Saved metrics do not reproduce")
    ratios_by_mode = {}
    for mode in lock["modes"]:
        disturbed = [r for r in rows if r["mode"] == mode and float(r["disturbance_deg_s"]) != 0]
        ratios = [float(r["rms_yaw_deg_s"]) / abs(float(r["disturbance_deg_s"])) for r in disturbed]
        ratio = float(np.median(ratios))
        if abs(ratio - summary["modes"][mode]["median_rms_ratio_to_open_loop"]) > 1e-12:
            raise RuntimeError("Mode summary differs")
        ratios_by_mode[mode] = ratio
    files = ("summary.json", "episodes.csv", "traces.npz", "overview.png", "overview.pdf", "report.md", "before_test.json")
    receipt = {"passed": True, "scope": "Source integrity, complete case grid, trace arithmetic and no-controller physics; no biological validation",
               "episodes_checked": expected_cases, "maximum_rms_discrepancy_deg_s": maximum_error,
               "engineering_status_preserved": summary["engineering_status"],
               "artifact_hashes": {name: hashlib.sha256((folder / name).read_bytes()).hexdigest() for name in files}}
    (folder / "arithmetic_review.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--results", type=Path, default=ROOT / "results/r2")
    review(p.parse_args().results)
