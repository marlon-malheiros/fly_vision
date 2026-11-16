# Frozen-model H2 direction-tuning comparison V2

25 October 2026. Physiology: [Zhao et al. (2025)](https://www.nature.com/articles/s41586-025-09276-5),
[H2 deposit v2](https://doi.org/10.25378/janelia.28462100.v2).

**Completed:** an exploratory comparison of the original
frozen circuit with recorded H2 direction tuning, using an approximate moving-
edge stimulus family. Model parameters, graph and frontend are unchanged.
This does not establish physiological validation or a small-yaw repair.

## Main result

The frozen model has a cell-weighted mean absolute preferred-direction (PD) error of **16.72°**, with hierarchical-bootstrap 95% interval **[13.50, 23.61]°**, across all 39 published positions.

The body-horizontal reference gives **13.76°**, with interval
**[11.48, 19.93]°**. Descriptively, model mean error is 2.96° higher than the parameter-free body-horizontal reference. No biological pass/fail threshold was introduced.
The reference has no fitted parameter: back-to-front flow is horizontal in
the model body frame, projected into each arena's tangent coordinates. A
fixed LED-horizontal reference is also retained for every position.

| Cell | Defined / published positions | Model PD error (°) | Repeat-bootstrap interval (°) | Body-horizontal reference (°) |
|---|---:|---:|---:|---:|
| 1 | 6/6 | 16.05 | [13.31, 25.19] | 12.98 |
| 2 | 6/6 | 24.42 | [20.71, 28.29] | 17.89 |
| 3 | 6/6 | 13.27 | [8.56, 24.29] | 13.23 |
| 4 | 6/6 | 14.15 | [8.94, 28.13] | 12.64 |
| 5 | 6/6 | 12.21 | [9.04, 17.31] | 10.04 |
| 6 | 6/6 | 24.11 | [20.46, 31.91] | 19.15 |
| 7 | 3/3 | 12.86 | [5.24, 25.25] | 10.44 |

Cells are equally weighted, then their published positions are equally
weighted. Cell 7 has three published positions; the other animals have six.
Mean bright/dark signed curves are combined before the min-shift vector sum.
Source spikes/s and dimensionless model tanh rates are compared through PD,
DSI and shape only. Per-polarity shape correlations have median
0.69 over 78 defined curves.
There was no gain, time-scale, sign, neural parameter or decoder fitting.

[All position metrics](../results/h2_frozen_model_benchmark_v1/analysis/position_metrics.json),
[point summary and full-source missingness bounds](../results/h2_frozen_model_benchmark_v1/analysis/point_summary.json),
[bootstrap summary](../results/h2_frozen_model_benchmark_v1/analysis/bootstrap_summary.json),
[all paired-repeat/animal resampling evidence](../results/h2_frozen_model_benchmark_v1/analysis/bootstrap_draws.npz).

## Inputs and coverage

The 39 published recording locations supply 1,248 condition labels (16
directions, two polarities). Identical poses/positions/timings for cells 5/6
allow reuse, yielding 1,056 unique primary movies. The full source has 42
positions/1,344 conditions; 96 conditions at cell 7's other three locations
lack pose metadata and remain unscored. Full-source error bounds are
[15.80, 28.66]°. No pose or response is invented to fill them.

Use body 10019, the single anatomically labeled left H2, supported by 1,560
left T4/T5 afferent edges and zero right. The right eye has constant opaque-
eye luminance and exactly zero motion drive. The original 173×173 one-degree
retinal lattice and all 13,579 source identities/routes remain fixed. Model
traces from all fourteen wide cells are retained, but only the designated H2
output enters this benchmark. The new source-phase check finds that 77 of the
78 author-summary phases agree to arithmetic precision, while one differs by
180 degrees (cell 4, protocol 1, dark edge, position 87,29). That discrepancy
is consistent with the supplied plot's quadrant-ambiguous atan(imag/real)
rule. The frozen analysis uses atan2 of the full raw-response vector for
both observations and predictions; no curve is rotated to match a summary.
All 78 DSI values were reproduced in the preceding source study. These are
source-processing checks on known recordings, not model validation.
[Phase discrepancy evidence](../results/h2_frozen_model_benchmark_v1/analysis/phase_summary_diagnostic.json).

Moving half-planes are drawn on a circular nearest-LED patch, using table
intensities/background and the recorded 40-ms steps, or 80 ms for cell 4.
Model response integration uses the actual source-derived protocol windows.
First-frame rasterization/phase, exact pattern origin, LED photometry, optical
blur, exact display-clock offsets and the model-to-physiology time scale
remain assumptions. Each condition starts from equilibrium; original
trial-sequence/adaptation history is not reconstructed. This is **not exact recording replay**. Female recordings
versus a male connectome and the imposed cardinal-input surrogate remain
biological limitations.

[Condition-to-trace manifest](../results/h2_frozen_model_benchmark_v1/condition_manifest.json),
[poses/spatial coverage](../results/h2_frozen_model_benchmark_v1/positions.json),
[identity/count evidence](../results/h2_frozen_model_benchmark_v1/identity_and_counts.json),
[original-model identity check](../results/h2_frozen_model_benchmark_v1/original_model_reuse_verification.json).

## Sensitivity and numerical evidence

All 1,473 primary/sensitivity/stationary cases completed. The fixed extra
variants bracket edge phase by ±0.5 LED at position (87,13) of cells 1,4,5,7
and signed ±2-degree yaw at that position for cells 5/7; no favorable variant
is selected. Across these prespecified subset variants, changes in absolute PD error range from -1.16° to 2.51°. These are subset checks, not uncertainty bounds for every location. All 33 equilibrium stationary controls give
exactly zero source drive and neural response.

Identical-drive half-step RK4 checks meet the frozen numerical endpoint
criterion in **16/16** cases; combined finer frontend/input/solver
checks meet it in **16/16**. The criterion remains 5% of the primary
endpoint magnitude plus 1e-7 model-rate units. Original-Python full-prefix
replays meet their 1e-10 rate/final-state tolerance in
**2/2** cases.
Numerical review status is **PASS**. Failures, if any, are
retained and prevent a general convergence claim; no primary result or
criterion is silently replaced. Baseline rows retained as zero equilibrium
are checked by the independent full-prefix replay.

The independent observation/phase/input-integrity review is
**PASS**, with maximum observation error
3.25e-19 model-rate units. An additional
independent real-vector review verifies all 10,000 bootstrap draws, seed/
resample identities, condition baselines, position errors, animal weights,
missingness bounds and reported intervals: **PASS**. Numerical
reproducibility is distinct from biological validity.

[Sensitivity metrics](../results/h2_frozen_model_benchmark_v1/analysis/sensitivity_metrics.json),
[changes from primary](../results/h2_frozen_model_benchmark_v1/analysis/sensitivity_error_changes.json),
[numerical results including failures](../results/h2_frozen_model_benchmark_v1/numerical_review.json),
[independent review](../results/h2_frozen_model_benchmark_v1/independent_review.json),
[independent bootstrap review](../results/h2_frozen_model_benchmark_v1/bootstrap_statistics_independent_review.json).

[Final curve overlays](../results/h2_frozen_model_benchmark_v1/presentation_v2/all_tuning_curves_v1.png),
[quantitative comparison](../results/h2_frozen_model_benchmark_v1/presentation_v2/quantitative_comparison_v1.png),
[numerical controls and sensitivity](../results/h2_frozen_model_benchmark_v1/presentation_v2/controls_and_coverage_v1.png).

## Interpretation and limits

These results quantify local motion-direction agreement under explicitly
specified approximations. They do not prove a physiological circuit mechanism,
explain every disagreement, establish bIPS causality, validate DNp15 or show
reliable small-turn detection during walking. Missing electrical synapses,
uLPTCrns/H2rns and realistic upstream physiology were not invented. A response
difference can reflect the surrogate circuit, sampling, observation assumption
or stimulus approximation; this benchmark alone does not uniquely separate
those causes.

All seven animals' source summaries/curves were inspected before this study.
The comparison rules and code were frozen before new model predictions, at
source checkpoint `0910046ac7f93836799d01270da0938f454f73de`. No training occurred;
the earlier cells 1–4/5–7 partitions are descriptive here, not fresh validation.
Their model errors are 16.97° and
16.39°, versus reference errors
14.18° and
13.21°, respectively.
[Fixed-partition descriptive results](../results/h2_frozen_model_benchmark_v1/analysis/descriptive_partition_results.json).
The 10,000-draw animal/repeat bootstrap describes this small seven-animal
sample, not all flies or unknown environments. A defined deterministic PD
does not establish a detectable neural signal: amplitudes are retained and
no physiological noise model is added. Undefined PDs are preserved
as missing with explicit coverage/bounds; no post hoc biological pass/fail
threshold is applied.

This is a new external-measurement comparison, rather than another walking
sweep or repetition of the completed input-mapping audit. It supplies a
specific local-response discrepancy/agreement to investigate before choosing
any evidence-backed model change. No circuit repair, closed-loop locomotion
or physical deployment is claimed.

## Reproducibility and preserved failures

[Prospective protocol](H2_FROZEN_MODEL_BENCHMARK_PROTOCOL_V1.md),
[pre-prediction hashes](../results/h2_frozen_model_benchmark_v1/before_model_predictions.json),
[reproduction commands](H2_FROZEN_MODEL_BENCHMARK_REPRODUCTION_V1.md).
All retinal keyframes/time maps, delivered inputs, wide-cell rates/final
states, variants, count/phase summaries and bootstrap arrays are retained.
V2 corrects the initial generated report's erroneous wording that all 78
phase summaries were reproduced; the preserved numerical phase difference
was already 180 degrees and all primary metrics remain unchanged. V2 also
clarifies that the model error exceeds the reference, and final figure layout
moves amplitude labels above the data. Initial report and layouts are
preserved. [Correction record](../results/h2_frozen_model_benchmark_v1/report_correction_v2.json).

A fresh source-built subset replay supplements the full independent reviews;
a second complete experiment replay is not claimed. Live progress and
AGENTS.md are excluded from the immutable evidence index, with a dated
progress copy stored at completion.

Two pre-outcome geometry-verifier failures are preserved. The initial
rounding diagnosis was incomplete: sign conversion modified the reference
array through a NumPy view. V3 copies the array, keeps original R rounded
outputs, and checks unrounded geometry with unchanged strict tolerances.
The broad initial test glob also imported an old test requiring h5py in the
simulation interpreter; the two new modules pass seven tests when selected
explicitly. No dependency was installed and no neural outcome selected these
corrections. [Study evidence directory](../results/h2_frozen_model_benchmark_v1).

## Undergraduate explanation: what we did, what we want, and why

We showed moving edges to our unchanged model and compared its H2 direction
preferences with real recordings. Its average direction error is 16.72 degrees.
Zero-degree error would mean identical preferred directions; 90 degrees
would mean perpendicular directions. We want a circuit whose visual responses agree with measurements before
asking it to detect tiny turns while walking. This comparison gives us a
concrete biological reference and records where the model or stimulus
approximation still needs investigation; it does not yet fix small-turn detection.
