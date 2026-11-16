"""Independent scalar integration and squared-distance replay for the release."""
import json
import math

import numpy as np
from scipy.special import gammaincinv

from .reproduce import COUNTS, EVIDENCE, KINDS, write_json


def review(output):
    integration_max, checks = 0., 0
    for cell in range(3, 9):
        with np.load(EVIDENCE / f"input_cell{cell:02d}.npz", allow_pickle=False) as z:
            for sigma in (0., .5, 1.):
                bank = z[f"sigma_{sigma:g}"]
                for si in (0, 85, 144, 203, 288):
                    for native in (0, 5, 10):
                        point = z["centers"] + z["shifts"][si] + (native-5)*z["axis"]
                        frames = z["images"]
                        for fi in (0, len(frames)//2, len(frames)-1):
                            frame, terms = frames[fi], []
                            for y, x in zip(*np.nonzero(frame)):
                                weights = []
                                for pixel, pos in ((x, point[0]), (y, point[1])):
                                    if sigma:
                                        hi = (pixel+.5-pos)/(sigma*math.sqrt(2))
                                        lo = (pixel-.5-pos)/(sigma*math.sqrt(2))
                                        weights.append(.5*(math.erf(hi)-math.erf(lo)))
                                    else:
                                        d = abs(pixel-pos)
                                        weights.append(1. if d < .5-1e-10 else
                                                       .5 if abs(d-.5) <= 1e-10 else 0.)
                                terms.append(float(frame[y, x])*weights[0]*weights[1])
                            integration_max = max(integration_max,
                                abs(math.fsum(terms)-float(bank[si, fi, native])))
                            checks += 1
    if integration_max > 1e-12:
        raise AssertionError("Independent optical integration differs")
    with np.load(output / "synthetic_design.npz", allow_pickle=False) as z:
        cp, tp = z["calibration_predictions"], z["test_predictions"]
    source = json.loads((output / "synthetic_results.json").read_text())
    bykey = {(r["noise_sd"], r["generating_model"], r["assessed_model"]): r
             for r in source["summaries"]}
    cut_cal, cut_test = 2*gammaincinv(11/2, .975), 2*gammaincinv(25/2, .975)
    rng, n, count = np.random.default_rng(20261116), 200, 0
    for sigma in (.02, .05, .1):
        variance = sigma**2/3
        for truth in range(3):
            totals = [dict.fromkeys(COUNTS, 0) for _ in KINDS]
            for ti in range(25):
                y = cp[truth, ti] + rng.normal(0, math.sqrt(variance), (n, 11))
                v = tp[truth, ti] + rng.normal(0, math.sqrt(variance), (n, 25))
                for candidate in range(3):
                    # Different algebra from the primary broadcast-residual calculation.
                    c = (np.sum(y*y, axis=1)[:, None]
                         + np.sum(cp[candidate]**2, axis=1)[None, :]
                         - 2*y@cp[candidate].T)/variance
                    t = (np.sum(v*v, axis=1)[:, None]
                         + np.sum(tp[candidate]**2, axis=1)[None, :]
                         - 2*v@tp[candidate].T)/variance
                    keep, passed = c <= cut_cal, t <= cut_test
                    selected = np.argmax(c <= c.min(axis=1)[:, None]+1e-9, axis=1)
                    anypass = np.any(keep & passed, axis=1)
                    anyfail = np.any(keep & ~passed, axis=1)
                    row = totals[candidate]
                    row["single_reject"] += int(np.sum(~passed[np.arange(n), selected]))
                    row["set_reject"] += int(np.sum(~anypass))
                    row["set_support"] += int(np.sum(anypass & ~anyfail))
                    row["set_unresolved"] += int(np.sum(anypass & anyfail))
                    row["true_center_covered"] += int(keep[:, ti].sum())
                    row["compatible_total"] += int(keep.sum())
                    row["oracle_reject"] += int(np.sum(~passed[:, ti]))
                    row["n"] += n
                    count += n
            for candidate, row in enumerate(totals):
                expected = bykey[sigma, KINDS[truth], KINDS[candidate]]
                for key, value in row.items():
                    if value != expected[key]:
                        raise AssertionError((sigma, truth, candidate, key, value, expected[key]))
    result = dict(passed=True, scalar_image_samples_checked=checks,
                  scalar_image_max_error=integration_max,
                  independent_candidate_assessments=count, all_27_summary_counts_match=True,
                  scope="Numerical replay from derived image banks; no biological validation")
    write_json(output / "independent_review.json", result)
    return result
