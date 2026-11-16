"""Freeze motor calibration, then evaluate the predeclared closed-loop grid."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import csv
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np

from optomotor.circuit import Circuit
from optomotor.simulation import MotorCalibration, TRACE_COLUMNS, metrics, run_episode

DATA = ROOT / "data/derived"
MODES = ("intact", "bips_silent", "h2_silent", "open_loop", "visual_reference")


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def source_inventory():
    patterns = ("optomotor/*.py", "scripts/*.py", "tests/*.py", "configs/*.json", "docs/PROTOCOL_V1.md", "data/derived/*.json", "data/derived/*.csv")
    files = sorted({p for pattern in patterns for p in ROOT.glob(pattern)})
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def calibrate(config, destination):
    destination.mkdir(parents=True, exist_ok=False)
    write_json(destination / "before_calibration.json", {"sources": source_inventory(), "config": config, "test_scenes_opened": False})
    observations = []
    unit = MotorCalibration(0.0, 0.0)
    omega = np.deg2rad(abs(config["disturbance_deg_s"][0]))
    for seed in config["calibration_seeds"]:
        for sign in (-1, 1):
            trace = run_episode(DATA, config, unit, seed, 0.0, np.rad2deg(omega) * sign, "open_loop")
            window = (trace[:, 0] >= 2.0) & (trace[:, 0] < 3.5)
            observations.append({"seed": seed, "yaw_rad_s": omega * sign, "neural_mean": float(trace[window, 4].mean()),
                                 "visual_mean": float(trace[window, 5].mean())})
    imposed = np.array([r["yaw_rad_s"] for r in observations])
    neural_slope = float(imposed @ np.array([r["neural_mean"] for r in observations]) / (imposed @ imposed))
    visual_slope = float(imposed @ np.array([r["visual_mean"] for r in observations]) / (imposed @ imposed))
    if min(abs(neural_slope), abs(visual_slope)) < 1e-10:
        raise RuntimeError("Calibration did not identify usable visual/descending sensitivity; no truth-based fallback exists")
    calibration = MotorCalibration(config["target_loop_gain"] / neural_slope, config["target_loop_gain"] / visual_slope)
    result = {"parameters": asdict(calibration), "neural_slope_per_rad_s": neural_slope, "visual_slope_per_rad_s": visual_slope,
              "observations": observations, "method": "Zero-intercept pooled least squares; fit motor sign/gain only; fixed target loop gain",
              "stationary_baseline": "Exactly zero for the constant-frame initialized correlation frontend and resting rate network",
              "not_a_fitted_biological_motor_map": True, "sources": source_inventory()}
    write_json(destination / "calibration.json", result)
    print("Motor calibration frozen:", json.dumps(result["parameters"]), flush=True)
    return result


def evaluate(config, calibration_path, destination):
    calibration_data = json.loads(calibration_path.read_text(encoding="utf-8"))
    observed_sources = source_inventory()
    if observed_sources != calibration_data["sources"]:
        changed = [k for k in set(observed_sources) | set(calibration_data["sources"]) if observed_sources.get(k) != calibration_data["sources"].get(k)]
        raise RuntimeError(f"Sources changed after motor calibration: {changed}")
    if set(config["calibration_seeds"]) & set(config["test_seeds"]):
        raise ValueError("Calibration and test scene seeds overlap")
    destination.mkdir(parents=True, exist_ok=False)
    write_json(destination / "before_test.json", {"sources": observed_sources, "config": config, "modes": MODES,
               "calibration_sha256": hashlib.sha256(calibration_path.read_bytes()).hexdigest(), "outcomes_opened": False})
    calibration = MotorCalibration(**calibration_data["parameters"])
    started = time.monotonic()
    records, traces = [], {}
    disturbances = [0.0] + config["disturbance_deg_s"]
    for seed in config["test_seeds"]:
        for speed in config["translation_speeds_m_s"]:
            for disturbance in disturbances:
                for mode in MODES:
                    key = f"s{seed}_v{speed:g}_d{disturbance:g}_{mode}"
                    trace = run_episode(DATA, config, calibration, seed, speed, disturbance, mode)
                    traces[key] = trace
                    records.append({"key": key, "seed": seed, "speed_m_s": speed, "disturbance_deg_s": disturbance,
                                    "mode": mode, **metrics(trace, config)})
        print(f"Completed scene {seed}; {len(records)} paired episodes", flush=True)
    with (destination / "episodes.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    np.savez_compressed(destination / "traces.npz", **traces)
    paired = {(r["seed"], r["speed_m_s"], r["disturbance_deg_s"], r["mode"]): r for r in records}
    mode_results = {}
    for mode in MODES:
        moving = [r for r in records if r["mode"] == mode and r["disturbance_deg_s"] != 0]
        ratios = [r["rms_yaw_deg_s"] / paired[r["seed"], r["speed_m_s"], r["disturbance_deg_s"], "open_loop"]["rms_yaw_deg_s"] for r in moving]
        straight = [r["rms_yaw_deg_s"] for r in records if r["mode"] == mode and r["disturbance_deg_s"] == 0 and r["speed_m_s"] > 0]
        by_direction = {}
        for sign in config["disturbance_deg_s"]:
            values = [r["rms_yaw_deg_s"] / abs(sign) for r in moving if r["disturbance_deg_s"] == sign]
            by_direction[str(sign)] = float(np.median(values))
        mode_results[mode] = {"disturbed_cases": len(moving), "median_rms_ratio_to_open_loop": float(np.median(ratios)),
                              "median_compensation_fraction": float(1 - np.median(ratios)),
                              "cases_improved": int(np.sum(np.array(ratios) < 1)),
                              "worst_rms_ratio": float(max(ratios)), "direction_median_rms_ratios": by_direction,
                              "median_straight_rms_deg_s": float(np.median(straight)), "worst_straight_rms_deg_s": float(max(straight))}
    refinement = []
    seed = config["test_seeds"][0]
    for speed in config["translation_speeds_m_s"]:
        for disturbance in config["disturbance_deg_s"]:
            reference = paired[seed, speed, disturbance, "intact"]
            fine = run_episode(DATA, config, calibration, seed, speed, disturbance, "intact",
                               camera_dt=config["camera_dt_s"] / 2, circuit_dt=config["circuit_dt_s"] / 2)
            fine_metrics = metrics(fine, config)
            error = abs(fine_metrics["rms_yaw_deg_s"] - reference["rms_yaw_deg_s"]) / max(reference["rms_yaw_deg_s"], 1e-12)
            refinement.append({"seed": seed, "speed_m_s": speed, "disturbance_deg_s": disturbance,
                               "coarse_rms_deg_s": reference["rms_yaw_deg_s"], "fine_rms_deg_s": fine_metrics["rms_yaw_deg_s"],
                               "relative_change": error})
    refinement_pass = max(r["relative_change"] for r in refinement) <= 0.05
    intact = mode_results["intact"]
    direction_pass = all(v < 1 for v in intact["direction_median_rms_ratios"].values())
    straight_pass = intact["median_straight_rms_deg_s"] <= config["straight_rms_limit_deg_s"]
    result = {"engineering_status": "PASS" if direction_pass and straight_pass and refinement_pass else "FAIL",
              "biological_validation": "NOT_PERFORMED", "physical_robot_test": "NOT_PERFORMED",
              "episodes": len(records), "scene_seeds": config["test_seeds"], "calibration_seeds": config["calibration_seeds"],
              "modes": mode_results, "gates": {"median_improvement_both_directions": direction_pass,
                       "median_straight_rms_within_limit": straight_pass, "half_step_rms_change_at_most_5_percent": refinement_pass},
              "half_step_checks": refinement, "runtime_s": time.monotonic() - started,
              "trace_columns": TRACE_COLUMNS, "environment": {"python": platform.python_version(), "numpy": np.__version__},
              "structure": Circuit(DATA).structural_summary(),
              "limitations": ["Synthetic planar scenes and noiseless equatorial camera", "Functional pooled T4/T5 source drive",
                              "Clamped T4/T5 excludes their recurrence and central feedback", "Transmitter signs and rate dynamics assumed",
                              "Motor sign/gain calibrated in simulation", "No recording comparison or animal-level validation"]}
    write_json(destination / "summary.json", result)
    plot_results(destination, records, traces, config, mode_results)
    write_report(destination, result)
    print(json.dumps({"engineering_status": result["engineering_status"], "gates": result["gates"], "intact": intact, "runtime_s": result["runtime_s"]}, indent=2), flush=True)
    return result


def plot_results(destination, records, traces, config, mode_results):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    colors = {"intact": "#147d92", "bips_silent": "#d58b32", "h2_silent": "#9a6bb0", "open_loop": "#777777", "visual_reference": "#3457a1"}
    fig, axes = plt.subplots(2, 2, figsize=(12, 7.5), constrained_layout=True)
    modes = list(MODES)
    medians = [mode_results[m]["median_rms_ratio_to_open_loop"] for m in modes]
    axes[0, 0].bar(range(len(modes)), medians, color=[colors[m] for m in modes])
    axes[0, 0].axhline(1, color="black", ls="--", lw=1)
    axes[0, 0].set(xticks=range(len(modes)), xticklabels=[m.replace("_", "\n") for m in modes], ylabel="Median RMS / no-controller RMS", title="A. Disturbance compensation (lower is better)")
    straight = [mode_results[m]["median_straight_rms_deg_s"] for m in modes]
    axes[0, 1].bar(range(len(modes)), straight, color=[colors[m] for m in modes])
    axes[0, 1].axhline(config["straight_rms_limit_deg_s"], color="black", ls="--", lw=1, label="Predeclared engineering limit")
    axes[0, 1].set(xticks=range(len(modes)), xticklabels=[m.replace("_", "\n") for m in modes], ylabel="Median yaw RMS (degrees/s)", title="B. Unwanted turning during straight travel")
    axes[0, 1].legend(fontsize=8)
    seed, speed, disturbance = config["test_seeds"][0], config["translation_speeds_m_s"][-1], config["disturbance_deg_s"][-1]
    for mode in modes:
        trace = traces[f"s{seed}_v{speed:g}_d{disturbance:g}_{mode}"]
        axes[1, 0].plot(trace[:, 0], np.rad2deg(trace[:, 1]), color=colors[mode], label=mode.replace("_", " "))
        axes[1, 1].plot(trace[:, 6], trace[:, 7], color=colors[mode], label=mode.replace("_", " "))
    axes[1, 0].axvspan(config["disturbance_on_s"], config["disturbance_off_s"], color="#dddddd", alpha=0.3)
    axes[1, 0].set(xlabel="Time (s)", ylabel="Actual yaw (degrees/s)", title="C. Preselected example: first test scene, fast travel")
    axes[1, 0].legend(fontsize=8, ncol=2)
    axes[1, 1].set(xlabel="Forward position x (m)", ylabel="Lateral position y (m)", title="D. Closed-loop trajectories for that example")
    axes[1, 1].set_aspect("equal", adjustable="datalim")
    fig.suptitle("MaleCNS-constrained optomotor prototype · simulated engineering test", fontsize=14)
    fig.savefig(destination / "overview.png", dpi=180)
    fig.savefig(destination / "overview.pdf")
    plt.close(fig)


def write_report(destination, result):
    lines = ["# Closed-loop optomotor prototype V1", "", "16 November 2026", "",
             f"Engineering feasibility: **{result['engineering_status']}**. Biological validation and physical-robot testing were not performed.", "",
             "The experiment closes the visual feedback loop: camera images drive motion-sensitive source populations, real MaleCNS chemical counts constrain a recurrent central circuit, and the left/right DNp15 difference controls a simulated motor. Motor sign and gain were calibrated in separate scenes before test outcomes.", "",
             f"Evaluated {result['episodes']} episodes across {len(result['scene_seeds'])} held-out synthetic scenes, three speeds, both disturbance signs and straight controls. Ablations reuse intact motor calibration and normalization.", "",
             "| Mode | Median disturbance RMS / open loop | Cases improved | Median straight yaw RMS (deg/s) |", "|---|---:|---:|---:|"]
    for mode, row in result["modes"].items():
        lines.append(f"| {mode} | {row['median_rms_ratio_to_open_loop']:.4f} | {row['cases_improved']}/{row['disturbed_cases']} | {row['median_straight_rms_deg_s']:.4f} |")
    lines += ["", "## Predeclared gates", ""] + [f"- {k}: {v}" for k, v in result["gates"].items()]
    lines += ["", "## Limits", ""] + ["- " + s for s in result["limitations"]]
    lines += ["", "An ablation effect is a property of this model and fixed motor calibration, not evidence that a cell class is biologically necessary. Inspect all per-case outcomes and numerical refinements in summary.json and episodes.csv.", "",
              "A velocity reflex reduces rotation; this implementation has no heading setpoint and need not return to the original heading after a disturbance.", "", "![Overview](overview.png)", ""]
    (destination / "report.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("calibrate", "evaluate", "all"), default="all")
    parser.add_argument("--output", type=Path, default=ROOT / "results/v1")
    parser.add_argument("--calibration", type=Path, default=ROOT / "results/calibration_v1/calibration.json")
    args = parser.parse_args()
    config = json.loads((ROOT / "configs/experiment_v1.json").read_text())
    if args.stage in ("calibrate", "all"):
        calibrate(config, args.calibration.parent)
    if args.stage in ("evaluate", "all"):
        evaluate(config, args.calibration, args.output)

