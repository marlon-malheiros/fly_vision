# Temporal slowing/adaptation dissection V1

2026-11-03. Frozen component interventions on known development stimuli; no new parameter fitting.
**New numerical checks: 14/14. Nominated development variant: slowing_only. Biological validation: False.**

## Matched outcomes

| Assay | Variant | Coordinates outside existing joint band | Normalized RMSE |
|---|---|---:|---:|
| frequency | none | 7/7 | 0.661121 |
| frequency | slowing_only | 6/7 | 0.313121 |
| frequency | adaptation_only | 6/7 | 0.700675 |
| frequency | both | 4/7 | 0.398686 |
| contrast | none | 1/7 | 0.103664 |
| contrast | slowing_only | 1/7 | 0.103739 |
| contrast | adaptation_only | 1/7 | 0.103332 |
| contrast | both | 1/7 | 0.103293 |

The none/both responses and scores are read from the sealed preceding experiment and reproduce exactly. Only slowing_only and adaptation_only require new neural solves. A nomination means that the frozen relative development guards pass; it does not mean the whole physiological curve matches.

![Four-way matched comparison](../results/hs_temporal_components_v1/component_comparison.png)

## Preferred-direction frequency responses

All values are normalized by each model's own preferred1 Hz response. Solid figure lines are preferred direction; dashed lines are null direction.

| Hz | Recorded | None | Slowing only | Adaptation only | Both |
|---|---:|---:|---:|---:|---:|
| 0.5 | 1.068203 | 0.533678 | 0.637861 | 0.373051 | 0.455431 |
| 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 |
| 2.5 | 0.676028 | 1.764421 | 1.199220 | 2.072720 | 1.433708 |
| 15 | 0.076436 | 1.192886 | 0.232413 | 0.989119 | 0.094632 |

Removing adaptation changes the slow0.5 Hz ratio from0.455431 to0.637861 (recorded1.068203), while the fast15 Hz ratio changes from0.094632 to0.232413 (recorded0.076436). The two response properties must be assessed separately; an aggregate error cannot show that every frequency improved.

## Frozen mechanistic predictions

| Prediction | Supported in this model |
|---|---|
| slowing_reduces_PD15_error | True |
| removing_adaptation_improves_PD05 | True |
| adaptation_alone_worsens_PD05 | True |

These are causal effects of functional input-stage interventions within this model. They are not evidence that removing a particular biological neuron produces the same effects. No Mi1/Tm1 lesion, electrical-synapse reconstruction or new MaleCNS connectivity is simulated.

Raw and normalized factorial effects are saved for every primary condition: mean slowing effect, mean adaptation effect and both−slowing_only−adaptation_only+none interaction. Raw response units remain arbitrary. Own-reference normalization can create an apparent interaction, so the normalized interaction is not proof of a new neural nonlinearity.

## Development guards and remaining mismatches

| Guard | Slowing only | Adaptation only |
|---|---|---|
| numerical | True | True |
| zero_clipping | True | True |
| PD50_PD75_inside | True | True |
| contrast_violations | True | True |
| contrast_rmse | True | True |
| frequency_rmse | True | False |
| PD05_improves | True | False |

The selected slowing_only variant reduces frequency-panel RMSE by 21.46% relative to the previous combined stage and 52.64% relative to the gain-only baseline. Frequency violations remain 6/7; contrast violations remain 1/7. No claim of complete physiological compatibility follows from a better aggregate error.

Importantly, this nominee has **more frequency band violations (6/7) than the combined model (4/7)**. The nomination rule explicitly used aggregate frequency error plus contrast/numerical guards, not a frequency-violation-count improvement. The model is not uniformly better, and this selection does not establish improved biological validation.

PD50/full contrast: model 0.948082, recorded 0.913768. Full-contrast null/preferred: model -0.080326, recorded -0.330100.
Remaining frequency mismatches: PD 0.5, PD 2.5, PD 15, ND 0.5, ND 1, ND 15.
Remaining contrast mismatches: ND 1.

## Implementation, evidence and scope

Source checkpoint `c6087bb` and the [protocol](HS_TEMPORAL_COMPONENTS_PROTOCOL_V1.md) froze all cases, predictions, numerical tolerances and nomination rules before the new outcomes. All old parameters/results are retained. The source constants and their limits are documented in [the preceding study](HS_UPSTREAM_TEMPORAL_REPORT_V1.md). Nominal slowing constants are ON54/OFF44 ms; adaptation constants ON318/OFF296 ms. These are published response-fit proxies, not newly measured intrinsic membrane constants.

Slowing only propagates h'=(u-h)/lp and d'=(h-d)/delay, initialized h=d=u. Adaptation only propagates g'=(u-g)/hp and d'=(u-g-d)/delay, initialized g=u,d=0. Matrix exponentials advance the states under the previous held image. Adaptation's direct current u-g may read the current frame causally. The existing detector delay30 ms, gain sigma0.121902687872575, spatial mapping, LPi graph, neural parameters and decoder remain unchanged. No sign/gain fitting.

The22 image cases are identical to the previous study:16 primary and6 refinements. Four frequencies0.5/1/2.5/15 Hz, two motion directions, phase zero; five contrasts at1 Hz with frequency1 reused as full contrast. Fixed60 Hz/four-bit grating, methods85 field and2/2/1 static/moving/static seconds. Primary image/source steps1.25/2.5 ms, refined0.625/1.25 ms, solver0.25 ms, half-solver controls0.125 ms and inherited absolute1 ms forcing ramp.

The readout remains right HSN/HSE/HSS equal-mean atanh(rate), [2,4) minus[1,2). All seven frequency and seven contrast coordinates keep the existing descriptive joint bands. The candidate’s source responses, cell overlap, stimulus registration and voltage-proxy limitations remain. This panel has no fresh animals, phase average, full frequency bank or new walking test. Upstream dynamics are homogeneous functional proxies rather than a reconstructed full-eye circuit. Full-contrast opposite-direction suppression and any remaining timing mismatches must not be hidden by a relative nomination.

Three focused tests pass: independent ODE propagation, analytic frequency-response checks, and causal prefix/reset/stationary behavior. New time/solver checks pass14/14; old reference checks reused14/14. The old checks were not newly simulated. Largest new normalized discrepancy=0.0309919. No tolerance relaxation or new spatial-convergence claim.

Independent log1p arithmetic verifies88 endpoints (maximum difference3.47e-18); comparison and numerical decisions are separately reconstructed. One none/both full replay verifies images, sources, rates, final states and checkpoints bitwise for both models. All22 new retinal hashes match their old cases. Reference arrays are linked through old receipts instead of duplicated in new neural archives. Zero pre-motion output; clipping totals{'slowing_only': 0, 'adaptation_only': 0}.

CPU2834.66s below4800; peak worker RSS1,457,614,848 bytes below2 GiB. No movies, permanent source-drive archive, source ZIP duplicate or previous-result overwrite. Both unsuccessful interventions and unfavorable responses remain preserved.

Evidence: [decision/predictions](../results/hs_temporal_components_v1/decision.json), [all comparisons](../results/hs_temporal_components_v1/comparisons.json), [raw/normalized factorial effects](../results/hs_temporal_components_v1/factorial_effects.json), [all response summaries](../results/hs_temporal_components_v1/model_responses.csv), [new numerical checks](../results/hs_temporal_components_v1/numerical_checks.json), [reused checks](../results/hs_temporal_components_v1/reused_numerical_checks.json), [arithmetic review](../results/hs_temporal_components_v1/independent_arithmetic_review.json), [execution/resources](../results/hs_temporal_components_v1/simulations_complete.json).

## Reproduction and next alternatives

Use the scientific environment recorded in environment.json and `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1`. In an isolated tree with all indexed source/dependency paths, run `scripts/hs_temporal_components_v1.py prepare`, `run`, `analyze`. Existing output directories intentionally reject writes; old sealed results are required as read-only dependencies, not bulk movies. `seal` saves exact sources/report/progress before indexing; `audit` rehashes after writer exit and writes one exclusive receipt. Full22-case repetition is not claimed: the two specified exact reference replays were executed. The companion report generator is presentation-only.

This finite round ends without another parameter sweep or walking simulation. If a component qualifies, preserve it as a development comparator and first address the explicitly remaining response mismatch using source-supported branch-specific dynamics or downstream opponency. An alternative is obtaining more closely matched physiological recordings/stimulus metadata before another revision. Freeze a distinct unused measurement before claiming independent validation. No source time constant or neural connection is invented merely to improve yaw classification.

## Undergraduate explanation

We want a model that notices small turns and responds like real fly neurons. Last time, adding slowing and adaptation together helped fast motion but weakened slow motion. Here we switched each part off separately while keeping everything else fixed. That tells us which component causes each effect in our simulation, and whether a simpler version deserves further testing. It still does not prove how the real fly works or transfer the old small-turn success automatically to the new input stage.
