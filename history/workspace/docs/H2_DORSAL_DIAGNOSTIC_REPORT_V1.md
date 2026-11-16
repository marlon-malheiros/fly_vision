# H2 upper-field discrepancy diagnostic V1

25 October 2026. **The upper-field mismatch survives the tested stimulus,
numerical and direct HS/bIPS-input controls.** Removing the four direct
HS/bIPS chemical afferents into H2 changes preferred direction by at most
**0.0293°**. Sparse support in the assigned source map is a concrete next
candidate to investigate; this study does not establish a unique cause or
fix reliable small-yaw detection.

## Scope and frozen methods

Build directly on the sealed [frozen-model H2 benchmark
V2](H2_FROZEN_MODEL_BENCHMARK_REPORT_V2.md) and [raw-trial
reconstruction](H2_TRIAL_METADATA_REPORT_V1.md). The physiology is from
[Zhao et al. (2025)](https://www.nature.com/articles/s41586-025-09276-5),
[H2 deposit v2](https://doi.org/10.25378/janelia.28462100.v2). No new biological
recordings were obtained. These are approximate moving-edge stimulus
comparisons, not exact replay of the original pattern arrays.

Retrospective localization uses all 39 published recording locations. The
new controlled follow-up includes every available upper-patch (87,36)
recording from cells 1–6, including cell 3 with its smaller error. Each is
paired with the same protocol's lower patch (87,21). Cell 7's upper patch
remains unscored because its pose metadata are unavailable. Selection of
the upper field was informed by previous outcomes and is exploratory.

The [protocol](H2_DORSAL_DIAGNOSTIC_PROTOCOL_V1.md), code, inputs, lesion and
analysis rules were frozen before new outcomes at Git checkpoint
`9f78675`. [Pre-outcome hashes](../results/h2_dorsal_diagnostic_v1/before_new_outcomes.json),
[complete plans/mappings](../results/h2_dorsal_diagnostic_v1/plans.json).
Preserve the original frontend, renderer, 13,579 source identities/routes,
MaleCNS graph and numerical parameters. Analyze left H2 body 10019 with
the previous baseline-subtracted mean dimensionless rate, source-derived
observation windows, bright/dark average and circular vector PD. No parameter
fit, decoder, artificial noise, new neuron, connection or controller.

Completed **832 tasks** in **843.6 seconds**, with zero execution failures:
384 unique upper-patch stimulus variants, 320 identical-input lesion
replays and 128 numerical controls. Twelve recording positions map to 320
distinct primary inputs because cells 5 and 6 share poses. Each generated
movie retains retinal keyframes/index maps, delivered sources, all fourteen
wide-cell traces and final states. Lesion receipts identify the exact reused
source file by SHA-256. [Execution](../results/h2_dorsal_diagnostic_v1/execution.json).

## Where the existing discrepancy is largest

These patch means are descriptive averages of the available locations,
nested within animals. They are not independent population tests and differ
from the preceding benchmark's equally weighted seven-animal overall
estimator, which remains unchanged at 16.72°.

| Display patch | Recordings | Mean model PD error | Mean horizontal-reference error | Median model tuning amplitude |
|---|---:|---:|---:|---:|
| (29,13) | 7 | 8.14° | 7.12° | 2.65e-4 |
| (58,28) | 6 | 13.47° | 9.86° | 2.84e-4 |
| (87,13) | 7 | 9.14° | 7.49° | 1.01e-4 |
| (87,21) | 6 | 15.47° | 16.25° | 4.57e-5 |
| (87,29) | 7 | 18.41° | 15.28° | 7.55e-5 |
| **(87,36)** | **6** | **40.05°** | **30.15°** | **2.46e-5** |

The simple horizontal reference also disagrees substantially in the upper
field. The discrepancy therefore includes measured directional variation
that this reference misses, as well as the model's additional deviation.
Neither quantity alone identifies an incorrect connection or registration.
[All patch results](../results/h2_dorsal_diagnostic_v1/analysis/retrospective_patch_summary.json).

## Stimulus uncertainty does not remove the large errors

At the upper patch, repeat every direction/polarity with edge placement
shifted by ±0.5 LED. Repeat signed head orientation ±2° only for cell 5,
whose source metadata report that yaw magnitude. **This is static pose
uncertainty, not a ±2°/s walking-rotation detection experiment.** Cell 6
shares cell 5's primary input but does not inherit its biological yaw bound.

| Cell | Original error | −0.5 LED error | +0.5 LED error |
|---|---:|---:|---:|
| 1 | 42.36° | 43.24° | 42.60° |
| 2 | 66.14° | 63.67° | 63.02° |
| 3 | 6.69° | 4.86° | 5.28° |
| 4 | 28.85° | 27.73° | 25.68° |
| 5 | 30.71° | 29.85° | 29.23° |
| 6 | 65.54° | 64.68° | 64.06° |

Phase shifts change absolute errors by −3.17 to +0.88°. Cell 5's −2°/+2°
head-yaw cases give errors 28.35°/24.02°, changes −2.36°/−6.69°. Report both;
neither is selected as a corrected input. These limited variants do not
span unknown original patterns, photometry, eye geometry or all pose errors.
No preferred direction becomes undefined.
[Full curves and changes](../results/h2_dorsal_diagnostic_v1/analysis/sensitivity_metrics.json).

## Direct HS/bIPS afferents have little effect in this model

In separate circuit instances remove only four incoming chemical weights to
left H2: two HS and two bIPS afferents. Leave every neuron and all other
connections unchanged, including feedback into T4/T5. The original model is
never altered. [Exact original weights and identities](../results/h2_dorsal_diagnostic_v1/lesion_definition.json).

Across all twelve upper/lower recording positions, preferred-direction
shifts range from 0.00534° to **0.02928°**. Tuning-amplitude ratios
(lesioned/original) range from **0.999986 to 1.000136**, changes smaller than
0.014%. All predictions remain defined. The tested direct chemical afferents
therefore cannot account for the tens-of-degrees mismatch in this frozen
model. This joint removal does not isolate the two cell groups individually,
exclude indirect recurrent effects or measure bIPS's contribution to DNp15
yaw detection. [All lesion results](../results/h2_dorsal_diagnostic_v1/analysis/lesion_metrics.json).

## Source-chart support is a candidate, not an established defect

Transform the originally assigned source coordinates into each display
window without changing them. Of H2's 1,560 direct T4/T5 afferents, only
**1–3 assigned source centers** fall inside the upper patch before spatial
pooling; median 1. The paired lower patch contains 5–7, median 6. All 317
LED centers in each of these windows lie within the inherited model eye
grid, so there is no missing-center coverage in this check. Sparse afferent
support accompanies the weak upper-field responses.

This marker excludes pooling spillover, uses an imposed retinal coordinate
chart and does not count the full biological receptive field. It cannot
prove the sparse coverage is wrong, explain the error causally, or justify
adding connections. Previous mapping audits established consistency with
the curated mapping; they did not independently validate that mapping's
physiology. [All 39 support measurements](../results/h2_dorsal_diagnostic_v1/analysis/support_metrics.json).

## Numerical verification

For upper-patch cells 2 and 4, every direction/polarity was checked with
half-size RK4 steps on identical inputs and with finer frontend/input
sampling plus half-size RK4 steps. **128/128 endpoints pass** the unchanged
5% of primary absolute endpoint +1e-7 tolerance. Maximum discrepancy divided
by tolerance is 0.7355. All four full-curve phase diagnostics pass the fixed
1° gate:

| Cell | Same-drive RK4 refinement PD shift | Frontend/input + RK4 refinement PD shift |
|---|---:|---:|
| 2 | 0.00376° | 0.00298° |
| 4 | 0.00557° | 0.00443° |

These selected primary curves are stable under the tested refinements;
this does not establish convergence for every stimulus variant or an exact
biophysical time constant. [Endpoint checks](../results/h2_dorsal_diagnostic_v1/analysis/numerical_metrics.json),
[full-curve checks](../results/h2_dorsal_diagnostic_v1/analysis/numerical_phase_checks.json).

An independent arithmetic implementation checks 960 mapped endpoints,
including shared-input recording mappings: maximum discrepancy 1.69e-20
model-rate units. Independent phases/errors agree within 2.84e-14°.
All 320 source receipts verify. Independent connectivity selection confirms
exactly four changed edges. Two full-prefix original-Python lesioned-graph
replays agree with production traces/final states within 8.67e-19, against
the frozen 1e-10 criterion. [Independent review](../results/h2_dorsal_diagnostic_v1/independent_review.json).

A fresh strict-C++ source build exactly reproduces every retained array in
four predetermined phase, head-pose, lesion and finer-resolution cases.
A second full 832-task replay was not performed. [Fresh-build evidence](../results/h2_dorsal_diagnostic_reproduction_v1/complete.json),
[reproduction instructions](H2_DORSAL_DIAGNOSTIC_REPRODUCTION_V1.md).

## Interpretation, limitations and next evidence

The measured discrepancy survives a new spatially targeted test, not another
generic yaw sweep or source-label audit. Within this finite scope, neither
the four direct HS/bIPS chemical afferents, half-LED placement changes nor
tested time-step refinements explain the large errors. Static head-yaw
uncertainty matters by several degrees in one animal but leaves substantial
error. The sparse upper-field source chart is a supported observation; its
causal importance remains a hypothesis.

The next bounded target is **independent support for the imposed T4/T5
direction field and retinal registration**, using published visual-direction
maps and identified anatomical provenance. Compare any supported revision
in a new model version against this frozen baseline and the same stimulus
conditions. Reserve separate calibration and genuinely unseen validation
data; these already inspected animals are not new held-out validation.
No arbitrary coordinate/channel/weight adjustment is justified by this result.

The recordings are female and the connectome is male. Exact LED arrays,
photometry, individual retinal geometry, trial history and measurement-unit
calibration remain unavailable or approximate. Missing electrical synapses
and uLPTCrns/H2rns physiology are not repaired or invented here. This chemical
lesion does not test the full recurrent/electrical mechanisms discussed in
[Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9)
or [Pokusaeva et al. (2024)](https://doi.org/10.1038/s41467-024-53173-w).
Neither numerical reproducibility nor lesion effects establish biological
validity or biological causality. No new yaw threshold, DNp15 performance,
closed-loop behavior or robot deployment is claimed.

Initial preparation failed because the proposed (87,13) pair belonged to
another protocol. Corrected to metadata-supported (87,21) before freeze or
new predictions; preserve the [failure receipt](../results/h2_dorsal_diagnostic_preparation_failure_v1/failure.json).
Initial tuning legends obscured parts of curves; presentation V2 moves them
outside plots and preserves the initial figures and every numerical result.
No scientific criterion was changed. Live progress and AGENTS.md remain
outside immutable indexes; completion saves a dated progress copy.

[Final localization/support figure](../results/h2_dorsal_diagnostic_v1/presentation_v2/localization_and_support_v1.png),
[all upper-field tuning curves](../results/h2_dorsal_diagnostic_v1/presentation_v2/dorsal_tuning_v1.png),
[stimulus, lesion and numerical controls](../results/h2_dorsal_diagnostic_v1/presentation_v2/stimulus_lesion_numerical_v1.png).
Matching PDFs and complete numerical evidence are retained in the
[study directory](../results/h2_dorsal_diagnostic_v1).

## Undergraduate explanation: what we did, what we want, and why

We checked why our simulated H2 neuron prefers a different motion direction
from real H2 recordings in the upper visual field. Smaller numerical steps,
small changes in the displayed edge and removal of four direct circuit
connections leave the main mismatch. The model has very few assigned inputs
covering that region, which gives us a specific hypothesis to investigate.
We want visual responses grounded in biological measurements before asking
the network to detect tiny turns during walking. These tests narrow the
problem and help us decide what evidence to seek next; small-turn detection
is still unresolved.
