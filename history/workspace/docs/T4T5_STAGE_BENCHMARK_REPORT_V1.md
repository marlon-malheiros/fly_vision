# T4/T5 intermediate source-stage benchmark V1

2026-11-05. No candidate advanced; all four reserved control flies remain unscored.

This bounded study tests the representation injected into T4/T5, before the MaleCNS neural solve. It does not record simulated T4/T5 neural states or validate the complete circuit. No parameter was fitted, connection invented, old model changed, or old artifact overwritten.

## Frozen question and results

The [protocol](T4T5_STAGE_BENCHMARK_PROTOCOL_V1.md) and code were frozen before response scoring. The existing 7/4 development/holdout animal split was retained. The primary observer is positive fractional voltage squared with baseline subtraction; linear drive and grey backgrounds are sensitivity checks. These observers are assumptions rather than measured indicator calibration.

| Representation | D | In development band | Refinement checks | Advances |
|---|---:|---|---|---|
| measured_Mi1 | 1.000000 | False | False | False |
| adaptive_Mi1 | 1.000000 | False | False | False |
| Mi1_HP_removed | 1.000000 | False | False | False |
| T5_slowing_only | 1.000000 | False | False | False |

Development 95% simultaneous mean bands: T4: [0.504489, 0.774132], T5: [0.657520, 0.861018]. These are compatibility screens, not pre-established physiological equivalence margins. All animal and ROI values, zero-denominator counts, raw peaks and every observer/background outcome are retained.

## Numerical evidence and limits

Independent review passed: True. See the [review](../results/t4t5_stage_benchmark_v1/independent_review.json), [refinement checks](../results/t4t5_stage_benchmark_v1/refinement_checks.csv), [model metrics](../results/t4t5_stage_benchmark_v1/model_metrics.csv), [animal metrics](../results/t4t5_stage_benchmark_v1/development_animal_metrics.csv) and [decision](../results/t4t5_stage_benchmark_v1/decision.json). Source data and prior retained-file indexes were rehashed. Numerical agreement checks implementation, not biological validity.

The source paper describes eight-direction moving bars; this comparison uses its control A/B layers and preserves every inventoried development animal. Native time-series peaks were extracted directly, rather than from resampled fly means. Empty layers were not reused or invented. Preferred direction is response-selected, as in the source relative-tuning analysis. Because recordings select among eight directions while this horizontal source adapter tests two, agreement cannot validate absolute subtype direction, vertical tuning or its full tuning width. Signed fixed-template contrasts are separately archived.

Processed recordings lack original clocks, display logs, RF coordinates and trial-wise arrays. The reconstructed central 5-degree bar at20deg/s and100Hz is conditional on background, aperture and observation assumptions. A non-match cannot uniquely diagnose a missing neuron or synapse; a match cannot establish exact image-to-calcium validation. The experiment is not the prior15Hz grating failure and makes no new2deg/s walking claim. C2/C3 lesion cohorts were not used to invent circuit lesions.

## Reproduce

Use the project scientific Python environment with `PYTHONPATH=src`, `OPENBLAS_NUM_THREADS=1` and `MPLCONFIGDIR=<TEMP>/t4t5_stage_v1_mpl`. Run `scripts/t4t5_stage_benchmark_v1.py freeze`, `simulate`, `development`; then `scripts/review_t4t5_stage_benchmark_v1.py`; then `decide` and `report`. Existing output paths are exclusive; use a new version to rerun rather than overwrite. Run the three focused tests before freezing. Octave is required for independent ROI extraction. Seal only after all writers exit.

## Explanation for an undergraduate

We checked the motion detector before asking the whole network to steer. T4 handles bright motion and T5 dark motion. A useful detector should respond more to one direction than its opposite. We compared that difference with recordings, while keeping the old model unchanged. This helps locate a problem, but it does not prove the whole fly model is biological: the recorded stimulus and the conversion from model output to calcium are not known exactly. The next change must address an identified mismatch rather than merely improve a final turning score.

Sources: [Henning et al.](https://doi.org/10.7554/eLife.108529.3), [pinned author source](https://github.com/silieslab/C2C3_feedback_Henning/tree/745c6114b72a61dabc9389a1f024dbe22f679edf), [previous interface diagnosis](MI1_HS_INTERFACE_DIAGNOSTIC_V1.md).

## Completion notes before sealing

Use the [R2 loader entrypoint](T4T5_STAGE_BENCHMARK_LOADER_CORRECTION_R2.md)
for successful execution after the original V1 freeze. The generated reproduction
paragraph above describes stage order but omits that necessary label-field correction.
The table's numerical column is the frozen **global** guard: four of32 refinements
failed, although adaptive T4 and T5 passed their individual cases. No candidate
entered its primary biological compatibility band regardless of this guard.

The separately frozen [R3 numerical follow-up](T4T5_SAMPLING_DIAGNOSTIC_REPORT_R3.md)
corrects exact bar-edge quadrature, passes12/12 adjacent-grid checks and preserves
all six original primary T4 traces bitwise. It leaves D=1 and the original
primary stop unchanged. The linked report explains measurement uncertainty,
observation/background sensitivity and the next justified biological step.
