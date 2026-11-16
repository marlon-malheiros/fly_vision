"""Independent saved-array/arithmetic review of the GPU development checkpoint."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "results/validation_hardware_v1"
OUT = RUN / "cuda_deployment_review_v1"


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    with Path(path).open("x") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def verify_manifest(path):
    count = 0
    for row in read(path)["files"]:
        p = ROOT / row["path"]
        assert p.stat().st_size == row["size_bytes"], p
        assert hashlib.sha256(p.read_bytes()).hexdigest() == row["sha256"], p
        count += 1
    return count


def main():
    OUT.mkdir(parents=True, exist_ok=False)
    manifests = [RUN / "prospective_manifest.json", RUN / "frontend_memory_v3/before_execution.json"]
    numerical = []
    for version, directory in (("v1", RUN / "cuda_driver_v1/preflight_r2"), ("v2", RUN / "cuda_driver_v2/preflight_r1"), ("v3", RUN / "cuda_driver_v3/preflight_r1")):
        manifests.append(directory / "before_execution.json")
        if version != "v1":
            manifests.append(directory.parent / f"{directory.name}_implementation_before_execution.json")
        completion = read(directory / "preflight.json")
        assert completion["status"] == "DECLARED_CUDA_NUMERICAL_PREFLIGHT_PASS"
        assert len(completion["cases"]) == 11
        ptx = directory / "kernel.ptx" if version == "v1" else directory.parent / f"{directory.name}_kernel_{version}.ptx"
        ptx_hash = hashlib.sha256(ptx.read_bytes()).hexdigest()
        if version != "v1":
            selection = read(directory.parent / f"{directory.name}_implementation_before_execution.json")
            assert selection["ptx_sha256"] == ptx_hash
            assert selection["selected_factory"] == "CudaCircuitV" + version[-1]
        with np.load(directory / "activation.npz") as z:
            activation_error = float(np.max(abs(z["actual"] - np.tanh(z["x"]))))
        assert activation_error <= 1e-12
        assert activation_error == completion["maximum_activation_error"]
        for case in completion["cases"]:
            assert case["ptx_sha256"] == ptx_hash
            with np.load(directory / f'{case["case"]}.npz') as z:
                rate_error = float(np.max(abs(z["rate"] - z["cpu_rate"])))
                state_error = float(np.max(abs(z["final_state"] - z["cpu_final_state"])))
                observed_maximum = float(z["cumulative_maximum_state_error"].max())
                assert rate_error <= 1e-10 and state_error <= observed_maximum <= 1e-10
                assert case["maximum_rate_error"] == rate_error
                assert case["maximum_state_error"] == observed_maximum
            numerical.append(dict(version=version, case=case["case"], rate_error=rate_error,
                                  final_state_error=state_error, cumulative_state_error=observed_maximum))
    with np.load(RUN / "hardware_frontend_benchmark_v3/raw_measurements.npz") as z:
        reference_rate = z["cpu_strict_frontend_v2_r0_rate"]
        reference_state = z["cpu_strict_frontend_v2_r0_final_state"]
    benchmarks = []
    for name in ("hardware_cuda_benchmark_v1", "hardware_cuda_benchmark_v2", "hardware_frontend_benchmark_v3"):
        directory = RUN / name
        manifests.append(directory / "before_execution.json")
        report = read(directory / "benchmark.json")
        assert not report["physical_camera_tested"] and not report["hard_real_time_guarantee"]
        with np.load(directory / "raw_measurements.npz") as z:
            for row in report["records"]:
                key = f'{row["backend"]}_r{row["repeat"]}'
                ms = z[key + "_update_s"] * 1000
                # Independent scalar nearest-rank interpolation of quantiles.
                ordered = sorted(ms.tolist())
                def quantile(q):
                    position = (len(ordered) - 1) * q
                    low, high = int(np.floor(position)), int(np.ceil(position))
                    return ordered[low] + (position - low) * (ordered[high] - ordered[low])
                for field, expected in (("median_ms", quantile(.5)), ("p95_ms", quantile(.95)),
                                        ("p99_ms", quantile(.99)), ("maximum_ms", ordered[-1]), ("first_update_ms", float(ms[0]))):
                    assert abs(row[field] - expected) <= 1e-10, (name, key, field)
                assert row["samples"] == len(ms) == 40
                assert row["missed_10ms"] == sum(v > 10. for v in ordered)
                rate_error = float(np.max(abs(z[key + "_rate"] - reference_rate)))
                state_error = float(np.max(abs(z[key + "_final_state"] - reference_state)))
                assert max(rate_error, state_error) <= 1e-10
                benchmarks.append(dict(benchmark=name, **row))
    verified = {str(p.relative_to(ROOT)): verify_manifest(p) for p in manifests}
    write(OUT / "numerical_comparisons.json", numerical)
    write(OUT / "timing_comparisons.json", benchmarks)
    os.environ.setdefault("MPLCONFIGDIR", str(OUT / "matplotlib_cache"))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), layout="constrained", sharey=True)
    titles = ("Driver dispatch / product factorization", "Shared-memory ordered long rows", "Equivalent frontend memory access")
    for ax, name, title in zip(axes, ("hardware_cuda_benchmark_v1", "hardware_cuda_benchmark_v2", "hardware_frontend_benchmark_v3"), titles, strict=True):
        group = [r for r in benchmarks if r["benchmark"] == name]
        labels = list(dict.fromkeys(r["backend"] for r in group))
        for repeat in range(3):
            rows = [next(r for r in group if r["backend"] == label and r["repeat"] == repeat) for label in labels]
            x = np.arange(len(labels)) + (repeat - 1) * .18
            median = np.array([r["median_ms"] for r in rows])
            ax.errorbar(x, median, yerr=[np.zeros(len(rows)), np.array([r["p95_ms"] for r in rows]) - median],
                        fmt="o", capsize=3, label=f"Repeat {repeat + 1}; median–p95")
        ax.axhline(10., linestyle="--", color="black", linewidth=1)
        ax.set_xticks(range(len(labels)), [s.replace("_", "\n") for s in labels], fontsize=7)
        ax.set_title(title, fontsize=10)
        ax.set_ylim(0, max(32., max(r["p95_ms"] for r in benchmarks) + 1))
    axes[0].set_ylabel("Two retinal frames + one neural update (ms)")
    axes[0].legend(fontsize=7)
    fig.suptitle("Original 1-ms solver: separate interleaved short replay tests under concurrent load\nTiming misses remain; camera acquisition and projection excluded", fontsize=11)
    for extension in ("png", "pdf"):
        fig.savefig(OUT / f"timing_progress.{extension}", dpi=160)
    plt.close(fig)
    write(OUT / "independent_review.json", dict(status="SAVED_ARRAY_AND_TIMING_ARITHMETIC_REVIEW_PASS",
          completed_utc=datetime.now(timezone.utc).isoformat(), numerical_cases=len(numerical),
          timing_records=len(benchmarks), timing_updates=sum(r["samples"] for r in benchmarks),
          maximum_cumulative_state_error=max(r["cumulative_state_error"] for r in numerical),
          maximum_rate_error=max(r["rate_error"] for r in numerical), verified_manifest_entries=verified,
          production_solver_or_timing_helpers_imported=False,
          scope="independent_saved_array_and_summary_arithmetic; full_state_every_time_step_comparison_was_in_the_recorded_preflight_runner",
          physiological_validation_established=False, physical_camera_tested=False))
    print("REVIEW PASS", len(numerical), len(benchmarks), flush=True)


if __name__ == "__main__":
    main()
