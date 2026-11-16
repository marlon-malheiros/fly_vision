"""Independent arithmetic review of the completed proxy diagnostics.

Written after their scores existed. This is an implementation review and a
descriptive comparison, not a new prospective biological acceptance test.
It does not import the production normalization, filtering, or scoring code.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import traceback
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.io import loadmat

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "results/validation_hardware_v1"
OLD = RUN / "soma_matched_physiology_v1"
INTERFACE = RUN / "physiological_interface_v2"
SPEED = RUN / "heldout_speed_condition_v1"
OUT = RUN / "physiology_review_v2"
PROXIES = ("coordinate_signed", "coordinate_rectified")
ERRORS: dict[str, float] = {}
TOLERANCE = 1e-10


def read(path):
    return json.loads(Path(path).read_text())


def csv_read(path):
    with Path(path).open(newline="") as stream:
        return list(csv.DictReader(stream))


def csv_write(path, rows):
    with Path(path).open("x", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def save_json(path, value):
    with Path(path).open("x") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def check(label, actual, expected):
    a, b = np.asarray(actual), np.asarray(expected)
    assert a.shape == b.shape, (label, a.shape, b.shape)
    assert np.array_equal(np.isnan(a), np.isnan(b)), label
    finite = np.isfinite(a) & np.isfinite(b)
    assert np.array_equal(np.isfinite(a), np.isfinite(b)), label
    error = float(np.max(abs(a[finite] - b[finite]))) if finite.any() else 0.
    ERRORS[label] = max(ERRORS.get(label, 0.), error)
    assert error <= TOLERANCE, (label, error)


def verify_manifest(path):
    records = read(path)["files"]
    for entry in records:
        source = ROOT / entry["path"]
        assert source.stat().st_size == entry["size_bytes"], source
        assert hashlib.sha256(source.read_bytes()).hexdigest() == entry["sha256"], source
    return len(records)


def independent_filter(values, parameters):
    value = np.asarray(values, float).copy()
    if parameters["rectified"]:
        value[value < 0] = 0.
    for key in ("tau_first", "tau_second"):
        tau = parameters[key]
        if tau:
            alpha = -math.expm1(-.01 / tau)
            output = np.zeros_like(value)
            # A causal filter with the source implementation's one-step delay.
            for i in range(1, len(value)):
                output[i] = (1. - alpha) * output[i - 1] + alpha * value[i - 1]
            value = output
    return value


class Prediction:
    def __init__(self):
        self.networks = {}
        self.filtered = {}

    def predict(self, directory, circuit, stimulus, row, parameters, recorded_time):
        key = (str(directory), circuit, stimulus)
        if key not in self.networks:
            with np.load(directory / "network" / f"{circuit}_{stimulus}.npz") as z:
                self.networks[key] = {k: z[k] for k in ("time_s", "rate", "roles", "sides")}
                assert np.isfinite(z["final_state"]).all()
                check("network_clock", z["time_s"], np.arange(len(z["time_s"])) * .01)
        raw = self.networks[key]
        selected = np.flatnonzero((raw["roles"] == row["role"]) & (raw["sides"] == row["soma_side"]))
        assert len(selected), row
        filter_key = (*key, row["role"], row["soma_side"], parameters["rectified"], parameters["tau_first"], parameters["tau_second"])
        if filter_key not in self.filtered:
            # Explicit scalar cell accumulation avoids mixed advanced indexing.
            average = sum(raw["rate"][:, 0, i] for i in selected) / len(selected)
            self.filtered[filter_key] = independent_filter(average, parameters)
        return np.interp(recorded_time, raw["time_s"], self.filtered[filter_key]) * parameters["gain"]


def review_extraction():
    sessions = read(SPEED / "sessions.json")
    traces = {r["key"]: r for r in read(SPEED / "observed_traces.json")}
    reviewed = 0
    invalid = []
    for session in sessions:
        assert hashlib.sha256(Path(session["path"]).read_bytes()).hexdigest() == session["sha256"]
        loaded = loadmat(session["path"], variable_names=["F_ST", "F_All"])
        field = "F_ST" if "F_ST" in loaded else "F_All"
        raw = loaded[field]
        if raw.ndim == 3:
            raw = raw[..., None]
        t = np.asarray(session["time_s"])
        take = np.flatnonzero((t >= 0) & (t <= 6.))
        t = t[take]
        a, b = [int(np.argmin(abs(t - endpoint))) for endpoint in (1., 2.)]
        for protocol in session["pure_yaw_protocols"]:
            key = hashlib.sha256((session["relative_path"] + "|" + protocol["name"]).encode()).hexdigest()[:20]
            row = traces[key]
            array = np.take(np.take(raw, take, axis=0), protocol["index"], axis=2)
            array = np.take(array, session["roi_indices"], axis=2)
            values, baseline_mean, baseline_sd = [], [], []
            valid = np.zeros(array.shape[1:], bool)
            for trial in range(array.shape[1]):
                means, deviations = [], []
                for roi in range(array.shape[2]):
                    f = array[:, trial, roi]
                    baseline = f[a:b + 1]
                    mu, sigma = np.nanmean(baseline), np.nanstd(baseline, ddof=1)
                    means.append(mu)
                    deviations.append(sigma)
                    accepted = bool(np.isfinite(mu) and np.isfinite(sigma)
                                    and sigma > np.finfo(float).eps * max(1., abs(mu))
                                    and np.isfinite(f).mean() >= .95)
                    valid[trial, roi] = accepted
                    if accepted:
                        values.append((f - mu) / sigma)
                    else:
                        invalid.append(dict(key=key, trial=trial, roi=roi,
                                            baseline_finite=bool(np.isfinite(baseline).all()),
                                            baseline_sd=float(sigma) if np.isfinite(sigma) else None,
                                            finite_fraction=float(np.isfinite(f).mean())))
                baseline_mean.append(means)
                baseline_sd.append(deviations)
            stack = np.asarray(values)
            mean = np.nanmean(stack, axis=0)
            sem = np.nanstd(stack, axis=0, ddof=1) / np.sqrt(np.isfinite(stack).sum(axis=0))
            assert valid.any(axis=1).sum() >= 2
            with np.load(ROOT / row["path"]) as z:
                for label, expected in (("mean", mean), ("sem", sem), ("baseline_mean", baseline_mean), ("baseline_sd", baseline_sd), ("baseline_indices", [a, b])):
                    check("extraction_" + label, z[label], expected)
                assert np.array_equal(z["valid"], valid)
                assert int(z["valid_trials"]) == valid.any(axis=1).sum()
                check("recorded_clock", z["time_s"], t)
            assert row["response_field"] == field
            reviewed += 1
        print("RAW", reviewed, "/", len(traces), flush=True)
    save_json(OUT / "unusable_trial_roi_units.json", invalid)
    assert reviewed == len(traces) == 360
    return dict(sessions=len(sessions), traces=reviewed, unusable_trial_roi_units=len(invalid))


def review_fits_and_thirteen(predictor):
    count = 0
    for proxy in PROXIES:
        directory = INTERFACE / proxy
        models = read(directory / "observation_models_before_test_scoring.json")["models"]
        candidates = read(directory / "observation_candidates.json")
        rows = read(directory / "observed_traces.json")
        lookup = {r["key"]: r for r in rows}
        train_flies = {r["fly"] for r in rows if r["split"] == "calibration"}
        test_flies = {r["fly"] for r in rows if r["split"] == "validation"}
        assert not train_flies & test_flies
        assert len(test_flies) == 28
        assert all(r["previously_tested"] and not r["previously_unused"] for r in rows if r["split"] == "validation")
        for p in models:
            alternatives = [c for c in candidates if (c["cohort"], c["model"]) == (p["cohort"], p["model"])]
            minimum = min(alternatives, key=lambda c: c["calibration_mse"])
            assert p["candidate"] == minimum["candidate"]
            calibration = [lookup[key] for key in p["calibration_traces"]]
            flies = {r["fly"] for r in calibration}
            assert flies == set(p["calibration_flies"]) and flies <= train_flies
            samples = []
            for row in calibration:
                assert row["split"] == "calibration"
                with np.load(ROOT / row["path"]) as z:
                    t, y = z["time_s"], z["mean"]
                unit = dict(p, gain=1.)
                x = predictor.predict(directory, p["model"], row["stimulus"], row, unit, t)
                selected = (t >= 1.) & (t <= 13.) & np.isfinite(y)
                weight = 1. / len(flies) / sum(r["fly"] == row["fly"] for r in calibration)
                samples.append((x[selected], y[selected], weight))
            numerator = sum(w * np.mean(x * y) for x, y, w in samples)
            denominator = sum(w * np.mean(x * x) for x, _, w in samples)
            gain = max(0., numerator / denominator) if denominator else 0.
            loss = sum(w * np.mean((gain * x - y) ** 2) for x, y, w in samples)
            check("selected_fit_gain", p["gain"], gain)
            check("selected_fit_loss", p["calibration_mse"], loss)
        parameters = {(p["model"], p["cohort"]): p for p in models}
        for metric in csv_read(directory / "test_trace_metrics.csv"):
            row = lookup[metric["key"]]
            source = "original" if metric["mode"] == "original_observation_transfer" else metric["model"]
            p = parameters[source, row["cohort"]]
            with np.load(ROOT / row["path"]) as z:
                t, y = z["time_s"], z["mean"]
            x = predictor.predict(directory, metric["model"], row["stimulus"], row, p, t)
            with np.load(directory / "predictions" / f'{metric["model"]}_{metric["mode"]}_{row["key"]}.npz') as z:
                check("thirteen_saved_prediction", z["predicted"], x)
                check("thirteen_saved_observation", z["observed"], y)
            full = (t >= 1.) & (t <= 13.)
            motion = ((t >= 2.) & (t <= 4.)) | ((t >= 9.) & (t <= 11.))
            first, second = (t >= 3.5) & (t <= 4.), (t >= 10.5) & (t <= 11.)
            metrics = dict(mse=np.nanmean((x[full] - y[full]) ** 2),
                           motion_mse=np.nanmean((x[motion] - y[motion]) ** 2),
                           zero_baseline_mse=np.nanmean(y[full] ** 2),
                           mae=np.nanmean(abs(x[full] - y[full])),
                           predicted_epoch_contrast=np.nanmean(x[first]) - np.nanmean(x[second]),
                           observed_epoch_contrast=np.nanmean(y[first]) - np.nanmean(y[second]))
            for name, value in metrics.items():
                check("thirteen_" + name, float(metric[name]), value)
            count += 1
        print("THIRTEEN", proxy, count, flush=True)
    assert count == 760
    return dict(selected_observation_fits=32, rescored_trace_cases=count, reused_test_flies=28)


def review_speed(predictor):
    rows = read(SPEED / "observed_traces.json")
    lookup = {r["key"]: r for r in rows}
    models = {proxy: {(p["model"], p["cohort"]): p for p in read(INTERFACE / proxy / "observation_models_before_test_scoring.json")["models"]} for proxy in PROXIES}
    metrics = csv_read(SPEED / "condition_trace_metrics.csv")
    by_fly = defaultdict(list)
    used = set()
    for metric in metrics:
        row = lookup[metric["key"]]
        assert row["prediction_supported"] and row["velocity"] <= 90.
        hypothesis = int(metric["cw_world_sign"])
        direction = hypothesis if row["direction_flag"] == "CW" else -hypothesis
        stimulus = f'v{row["velocity"]:g}'.replace(".", "p") + ("_positive" if direction > 0 else "_negative")
        source = "original" if metric["mode"] == "original_observation_transfer" else metric["circuit"]
        p = models[metric["proxy"]][source, row["cohort"]]
        with np.load(ROOT / row["path"]) as z:
            t, y = z["time_s"], z["mean"]
        x = predictor.predict(SPEED / metric["proxy"], metric["circuit"], stimulus, row, p, t)
        full, motion, peak = (t >= 1.) & (t <= 6.), (t >= 2.) & (t <= 4.), (t >= 3.5) & (t <= 4.)
        values = dict(mse=np.nanmean((x[full] - y[full]) ** 2),
                      motion_mse=np.nanmean((x[motion] - y[motion]) ** 2),
                      zero_baseline_mse=np.nanmean(y[full] ** 2),
                      observed_peak=np.nanmean(y[peak]), predicted_peak=np.nanmean(x[peak]))
        for name, value in values.items():
            check("speed_" + name, float(metric[name]), value)
        check("speed_rmse", float(metric["rmse"]), np.sqrt(values["mse"]))
        assert metric["split"] == row["split"]
        key = tuple(metric[k] for k in ("proxy", "circuit", "mode", "cw_world_sign", "cohort", "split", "fly"))
        by_fly[key].append(values["mse"])
        used.add((row["key"], metric["proxy"], metric["circuit"], metric["mode"], hypothesis))
    assert len(metrics) == len(used) == 3600
    for row in rows:
        expected = 16 if row["prediction_supported"] else 0
        assert sum(k[0] == row["key"] for k in used) == expected
    for row in csv_read(SPEED / "condition_fly_metrics.csv"):
        key = tuple(row[k] for k in ("proxy", "circuit", "mode", "cw_world_sign", "cohort", "split", "fly"))
        check("speed_fly_mse", float(row["mse"]), np.mean(by_fly[key]))
        assert int(row["traces"]) == len(by_fly[key])
    split_flies = {s: sorted({r["fly"] for r in rows if r["split"] == s}) for s in ("calibration", "validation")}
    assert not set(split_flies["calibration"]) & set(split_flies["validation"])
    assert set(split_flies["calibration"]) | set(split_flies["validation"]) <= {r["fly"] for r in read(OLD / "observed_traces.json")}
    return dict(trace_cases=len(metrics), observed_traces=len(rows), supported_traces=sum(r["prediction_supported"] for r in rows),
                calibration_flies=len(split_flies["calibration"]), reused_test_flies=len(split_flies["validation"]),
                unsupported_traces=sum(not r["prediction_supported"] for r in rows), fly_metric_groups=len(by_fly)), metrics


def descriptive_summaries(metrics):
    groups = defaultdict(list)
    for row in metrics:
        key = tuple(row[k] for k in ("proxy", "circuit", "mode", "cw_world_sign", "cohort", "split", "velocity", "fly"))
        groups[key].append(row)
    fly_rows = []
    for key, rows in groups.items():
        row = dict(zip(("proxy", "circuit", "mode", "cw_world_sign", "cohort", "split", "velocity", "fly"), key))
        row.update(mse=float(np.mean([float(r["mse"]) for r in rows])),
                   zero_mse=float(np.mean([float(r["zero_baseline_mse"]) for r in rows])), traces=len(rows))
        fly_rows.append(row)
    csv_write(OUT / "speed_equal_fly_velocity_metrics.csv", fly_rows)
    combined = defaultdict(list)
    for row in fly_rows:
        key = tuple(row[k] for k in ("proxy", "circuit", "mode", "cw_world_sign", "cohort", "split", "velocity"))
        combined[key].append(row)
    summaries = []
    for key, rows in combined.items():
        row = dict(zip(("proxy", "circuit", "mode", "cw_world_sign", "cohort", "split", "velocity"), key))
        mse = float(np.mean([r["mse"] for r in rows]))
        zero = float(np.mean([r["zero_mse"] for r in rows]))
        row.update(flies=len(rows), traces=sum(r["traces"] for r in rows), rmse=float(np.sqrt(mse)),
                   zero_rmse=float(np.sqrt(zero)), ratio_to_zero=mse / zero if zero else None)
        summaries.append(row)
    csv_write(OUT / "speed_cohort_velocity_summary.csv", summaries)
    thirteen = []
    for proxy, directory in (("legacy_signed", OLD), *((p, INTERFACE / p) for p in PROXIES)):
        groups = defaultdict(list)
        for r in csv_read(directory / "test_fly_metrics.csv"):
            groups[r["model"], r["mode"], r["cohort"]].append(r)
        for (model, mode, cohort), rows in groups.items():
            mse = float(np.mean([float(r["mse"]) for r in rows]))
            zero = float(np.mean([float(r["zero_baseline_mse"]) for r in rows]))
            thirteen.append(dict(proxy=proxy, circuit=model, mode=mode, cohort=cohort, flies=len(rows),
                                 rmse=float(np.sqrt(mse)), zero_rmse=float(np.sqrt(zero)), ratio_to_zero=mse / zero))
    csv_write(OUT / "thirteen_proxy_comparison.csv", thirteen)
    return thirteen, summaries


def figures(thirteen, speed):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figure_dir = OUT / "figures"
    figure_dir.mkdir()
    cohorts = sorted({r["cohort"] for r in thirteen})
    fig, ax = plt.subplots(figsize=(13, 6), layout="constrained")
    colors = dict(legacy_signed="#777777", coordinate_signed="#3177a8", coordinate_rectified="#ad542d")
    for pi, proxy in enumerate(("legacy_signed", *PROXIES)):
        for ci, circuit in enumerate(("original", "expanded")):
            values = [next(r["ratio_to_zero"] for r in thirteen if (r["cohort"], r["proxy"], r["circuit"], r["mode"]) == (cohort, proxy, circuit, "original_observation_transfer")) for cohort in cohorts]
            offset = (pi - 1) * .24 + (ci - .5) * .09
            ax.scatter(np.arange(len(cohorts)) + offset, values, marker="o" if ci == 0 else "s", color=colors[proxy],
                       facecolors=colors[proxy] if ci == 0 else "none", label=f'{proxy}; {circuit}', s=45)
    ax.axhline(1, color="black", linewidth=1, linestyle="--", label="zero-response reference")
    ax.set_xticks(range(len(cohorts)), [c.replace("|", "\n") for c in cohorts], fontsize=8)
    ax.set_ylabel("Equal-fly MSE / zero-response MSE (lower is better)")
    ax.set_title("13-s proxy correction: reused test animals; fixed original-observation transfer")
    ax.legend(fontsize=7, ncols=2)
    for suffix in ("png", "pdf"):
        fig.savefig(figure_dir / f"thirteen_proxy_comparison.{suffix}", dpi=160)
    plt.close(fig)
    for proxy in PROXIES:
        fig, axes = plt.subplots(2, 4, figsize=(15, 7), layout="constrained")
        for ax, cohort in zip(axes.flat, cohorts):
            rows = [r for r in speed if r["proxy"] == proxy and r["cohort"] == cohort and r["split"] == "validation" and r["mode"] == "own_observation_calibration"]
            if not rows:
                ax.text(.5, .5, "No test flies in this condition", ha="center", transform=ax.transAxes)
                ax.set_title(cohort.replace("|", " / "), fontsize=8)
                continue
            for circuit, color in (("original", "#3177a8"), ("expanded", "#ad542d")):
                for hypothesis, style in (("1", "-"), ("-1", ":")):
                    points = sorted((r for r in rows if r["circuit"] == circuit and r["cw_world_sign"] == hypothesis), key=lambda r: float(r["velocity"]))
                    ax.plot([float(r["velocity"]) for r in points], [r["rmse"] for r in points], style, color=color,
                            marker="o", markersize=3, label=f'{circuit}; CW sign {hypothesis}')
            zero = sorted((r for r in rows if r["circuit"] == "original" and r["cw_world_sign"] == "1"), key=lambda r: float(r["velocity"]))
            ax.plot([float(r["velocity"]) for r in zero], [r["zero_rmse"] for r in zero], "--", color="black", label="zero response")
            ax.set_xscale("log", base=2)
            ax.set_xticks([5.625, 11.25, 22.5, 45, 90], ["5.6", "11.3", "22.5", "45", "90"], fontsize=7)
            ax.set_title(cohort.replace("|", " / ") + f'; n={rows[0]["flies"]}', fontsize=8)
            ax.set_xlabel("Nominal yaw speed (deg/s)", fontsize=8)
            ax.set_ylabel("Equal-fly RMSE (baseline SD units)", fontsize=8)
        handles, labels = next(ax for ax in axes.flat if ax.lines).get_legend_handles_labels()
        fig.legend(handles, labels, loc="outside lower center", ncols=5, fontsize=8)
        fig.suptitle(f'New 6-s condition: {proxy}; both unresolved global signs; reused test animals')
        for suffix in ("png", "pdf"):
            fig.savefig(figure_dir / f"speed_condition_{proxy}.{suffix}", dpi=160)
        plt.close(fig)


def main():
    OUT.mkdir(exist_ok=False)
    try:
        manifests = [RUN / "prospective_manifest.json", OLD / "prospective_manifest.json", INTERFACE / "prospective_manifest.json", SPEED / "prospective_manifest.json"]
        protected = {str(p.relative_to(ROOT)): verify_manifest(p) for p in manifests}
        extraction = review_extraction()
        prediction = Prediction()
        thirteen = review_fits_and_thirteen(prediction)
        speed, metrics = review_speed(prediction)
        comparison, summary = descriptive_summaries(metrics)
        figures(comparison, summary)
        save_json(OUT / "independent_review.json", dict(status="NUMERICAL_DATA_HANDLING_REVIEW_PASS",
                  completed_utc=datetime.now(timezone.utc).isoformat(), tolerance=TOLERANCE,
                  implementation_written_after_scores=True, prospective_biological_acceptance_test=False,
                  production_filter_normalizer_scorer_imported=False, unchanged_manifest_entries=protected,
                  extraction=extraction, thirteen_second=thirteen, six_second=speed,
                  maximum_absolute_differences=ERRORS, physiological_validation_established=False,
                  scope="data_handling_selected_fit_arithmetic_soma_prediction_filter_and_metric_review; not_independent_solver_reimplementation"))
        print("REVIEW PASS", extraction, thirteen, speed, ERRORS, flush=True)
    except BaseException:
        save_json(OUT / "failure.json", dict(traceback=traceback.format_exc(), partial_maximum_errors=ERRORS))
        raise


if __name__ == "__main__":
    main()
