"""Bounded portable replay; never writes into the shipped reference evidence."""
from itertools import product
import json
from pathlib import Path

import numpy as np

from .core import rectangle_response, sample_led_images
from .corrected import corrected

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/alignment_assessment_pilot_v1"
KINDS = ("isotropic", "elongated", "double_lobe")
COUNTS = ("single_reject", "set_reject", "set_support", "set_unresolved",
          "true_center_covered", "compatible_total", "oracle_reject", "n")


def write_json(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def synthetic(output):
    """Preserve the frozen seed, observation order, design and corrected rule."""
    rng = np.random.default_rng(20261116)
    centers = np.array(list(product(range(-2, 3), repeat=2)), float)
    bars = np.array([[x-.5, x+.5, -4.5, 4.5] for x in range(-5, 6)])
    patches = np.array([[x-.5, x+.5, y-.5, y+.5] for x, y in centers])
    cal = np.stack([rectangle_response(bars, centers, k) for k in KINDS])
    test = np.stack([rectangle_response(patches, centers, k) for k in KINDS])
    np.savez_compressed(output / "synthetic_design.npz", centers=centers,
                        bars=bars, patches=patches, calibration_predictions=cal,
                        test_predictions=test, model_names=np.array(KINDS))
    summaries, by_center = [], []
    n = 200
    for sigma in (.02, .05, .10):
        for truth in range(3):
            totals = [dict.fromkeys(COUNTS, 0) for _ in KINDS]
            for ti in range(25):
                y = cal[truth, ti] + rng.normal(0, sigma/np.sqrt(3), (n, 11))
                v = test[truth, ti] + rng.normal(0, sigma/np.sqrt(3), (n, 25))
                case = {}
                for candidate, name in enumerate(KINDS):
                    z = corrected(y, v, cal[candidate], test[candidate], sigma)
                    counts = dict(single_reject=int(np.sum(~z["single_pass"])),
                                  **{k: int(np.sum(z[k])) for k in
                                     ("set_reject", "set_support", "set_unresolved")},
                                  true_center_covered=int(np.sum(z["compatible"][:, ti])),
                                  compatible_total=int(z["compatible"].sum()),
                                  oracle_reject=int(np.sum(~z["test_passes"][:, ti])), n=n)
                    for key, value in counts.items():
                        totals[candidate][key] += value
                    case[name] = {k: counts[k] for k in ("n", "single_reject", "set_reject",
                                  "set_support", "set_unresolved", "true_center_covered")}
                by_center.append(dict(noise_sd=sigma, generating_model=KINDS[truth],
                                      true_center=centers[ti].tolist(), candidates=case))
            for candidate, row in enumerate(totals):
                if row["set_reject"] + row["set_support"] + row["set_unresolved"] != row["n"]:
                    raise RuntimeError("Incomplete decision partition")
                row.update(noise_sd=sigma, generating_model=KINDS[truth],
                           assessed_model=KINDS[candidate], generating_family_assessed=truth == candidate)
                row["mean_compatible_alignments"] = row["compatible_total"] / row["n"]
                for stem, key in (("single_rejection", "single_reject"),
                                  ("set_rejection", "set_reject"),
                                  ("set_support", "set_support"),
                                  ("set_unresolved", "set_unresolved"),
                                  ("oracle_rejection", "oracle_reject")):
                    row[stem + "_rate"] = row[key] / row["n"]
                summaries.append(row)
    result = dict(seed=20261116, independent_datasets=45000, summaries=summaries,
                  by_center=by_center, revision="R2; post-outcome numerical amendment",
                  biological_validation=False)
    expected = json.loads((EVIDENCE / "numerical_ties_r2/synthetic_results.json").read_text())
    if summaries != expected["summaries"] or by_center != expected["by_center"]:
        raise AssertionError("Synthetic results differ from the archived R2 values")
    write_json(output / "synthetic_results.json", result)
    return dict(summary_rows_exactly_matched=len(summaries), center_rows_exactly_matched=len(by_center),
                independent_datasets=45000, candidate_family_assessments=135000)


def optical(output):
    """Replay archived derived images, not extraction from the original raw MAT files."""
    expected = json.loads((EVIDENCE / "input_audit.json").read_text())
    rows, maximum_error = [], 0.
    for cell in expected["cells"]:
        with np.load(EVIDENCE / f'input_cell{cell["cell"]:02d}.npz', allow_pickle=False) as z:
            shifts, center, axis = z["shifts"], z["centers"], z["axis"]
            points = (center[None, None, :] + shifts[:, None, :]
                      + np.arange(-5, 6)[None, :, None] * axis).reshape(-1, 2)
            ref = shifts.tolist().index(cell["reference_shift"])
            for original in cell["sensitivities"]:
                sigma = original["sigma_led_pixels"]
                bank = sample_led_images(z["images"], points, sigma).reshape(
                    len(shifts), 11, len(z["images"])).transpose(0, 2, 1)
                error = float(np.max(np.abs(bank - z[f"sigma_{sigma:g}"])))
                maximum_error = max(maximum_error, error)
                if error > 1e-12:
                    raise AssertionError("Archived sampled inputs differ")
                diff = bank - bank[ref]
                rms = np.sqrt(np.mean(diff**2, axis=(1, 2)))
                maxdiff = np.max(np.abs(diff), axis=(1, 2))
                counts = dict(exact_matches=int(np.sum(maxdiff <= 1e-12)),
                              rms_within_001=int(np.sum(rms <= .01)),
                              rms_within_005=int(np.sum(rms <= .05)))
                for key, value in counts.items():
                    if value != original[key]:
                        raise AssertionError(f"Optical count differs: cell {cell['cell']} {key}")
                rows.append(dict(cell=cell["cell"], sigma_led_pixels=sigma, **counts))
    result = dict(cells=6, cell_blur_comparisons=len(rows), sampled_input_max_error=maximum_error,
                  rows=rows, raw_extraction_repeated=False, neural_voltages_scored=False,
                  biological_validation=False)
    write_json(output / "optical_replay.json", result)
    return result
