"""Run the baseline into a fresh generated directory and compare all traces."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_baseline import verify


def main(destination):
    destination = destination.resolve()
    generated = (ROOT / "generated").resolve()
    if generated not in destination.parents:
        raise RuntimeError("Replay output must be inside this project's generated directory")
    if destination.exists():
        raise RuntimeError("Replay output already exists; choose a new name")
    verify()
    destination.mkdir(parents=True)
    started = time.monotonic()
    subprocess.run([sys.executable, "-B", "scripts/run_experiment.py", "--stage", "all",
                    "--config", "configs/experiment_r2.json", "--calibration", str(destination / "calibration/calibration.json"),
                    "--output", str(destination / "results")], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "-B", "scripts/review_results.py", "--results", str(destination / "results")], cwd=ROOT, check=True)
    reference = json.loads((ROOT / "results/r2/summary.json").read_text(encoding="utf-8"))
    replay = json.loads((destination / "results/summary.json").read_text(encoding="utf-8"))
    if reference["gates"] != replay["gates"] or reference["engineering_status"] != replay["engineering_status"]:
        raise RuntimeError("Replay gates differ from the reference")
    maximum_difference = 0.0
    with np.load(ROOT / "results/r2/traces.npz", allow_pickle=False) as old, np.load(destination / "results/traces.npz", allow_pickle=False) as new:
        if set(old.files) != set(new.files):
            raise RuntimeError("Replay case grid differs")
        for key in old.files:
            if not np.allclose(old[key], new[key], atol=1e-10, rtol=1e-8):
                raise RuntimeError(f"Replay trajectory differs: {key}")
            maximum_difference = max(maximum_difference, float(np.max(np.abs(old[key] - new[key]))))
        cases = len(old.files)
    verify()  # Prove the replay left the reference evidence unchanged.
    receipt = {"passed": True, "cases_compared": cases, "maximum_trace_absolute_difference": maximum_difference,
               "absolute_tolerance": 1e-10, "relative_tolerance": 1e-8,
               "engineering_status": replay["engineering_status"], "biological_validation": "NOT_PERFORMED",
               "elapsed_s": time.monotonic() - started,
               "reference_manifest_sha256": hashlib.sha256((ROOT / "release_manifest_r2.json").read_bytes()).hexdigest()}
    (destination / "baseline_replay_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print("PASS: baseline replay and all 270 saved trajectories match within declared tolerance")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    default = ROOT / "generated" / ("baseline_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    parser.add_argument("--output", type=Path, default=default)
    args = parser.parse_args()
    main(args.output)
