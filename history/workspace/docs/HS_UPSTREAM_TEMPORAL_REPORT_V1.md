# Fixed upstream temporal-filter experiment V1

2026-11-03. One fixed source-constrained candidate, tested against inspected development data.
**Development-improvement flag: True. Numerical checks: 14/14. Biological validation: False.**

## Result

| Assay | Frontend | Coordinates outside existing joint band | Normalized RMSE |
|---|---|---:|---:|
| frequency | baseline | 7/7 | 0.661121 |
| frequency | candidate | 4/7 | 0.398686 |
| contrast | baseline | 1/7 | 0.103664 |
| contrast | candidate | 1/7 | 0.103293 |

Candidate frequency-panel RMSE / matched baseline = **0.6030**. The prospective improvement requirement was <=0.75, together with every contrast/numerical/clipping guard. These are practical development criteria, not statistical equivalence or biological acceptance.

| Frozen guard | Passed |
|---|---|
| numerical | True |
| frequency_rmse | True |
| contrast_rmse | True |
| contrast_violations | True |
| PD50_PD75_inside | True |
| zero_clipping | True |

![Matched temporal and contrast curves](../results/hs_upstream_temporal_v1/temporal_candidate.png)

## Preferred-direction frequency shape

Each curve is normalized by its own primary PD1 Hz endpoint. Phase zero only; the same images and observation are used for both models. These means are not mV or animal-level confidence estimates.

| Hz | Recorded | Gain baseline | Temporal candidate |
|---|---:|---:|---:|
| 0.5 | 1.068203 | 0.533678 | 0.455431 |
| 1 | 1.000000 | 1.000000 | 1.000000 |
| 2.5 | 0.676028 | 1.764421 | 1.433708 |
| 15 | 0.076436 | 1.192886 | 0.094632 |

The frequency-panel RMSE reduction is 39.70%, with violations falling from 7 to 4 of seven. Preferred 15 Hz is now inside the retained descriptive band; preferred 0.5 Hz becomes worse, and preferred 2.5 Hz remains too large. The four remaining frequency violations are PD0.5, PD2.5, ND0.5 and ND1 Hz. Compatibility at a point is not independent biological validation.

The whole upstream-stage intervention has a demonstrated effect within this model. This round does not isolate which benefit comes from low-pass slowing versus high-pass adaptation, nor prove biological causality for Mi1/Tm1. Those require separate component interventions and physiological evidence.

At 50% contrast, recorded PD/full ratio is 0.913768, matched gain baseline 0.948111, candidate 0.947400. Full-contrast ND/PD is recorded -0.330100, baseline -0.080624, candidate -0.081713.

No additional candidate, gain adjustment or parameter fit followed these outcomes. Better aggregate error does not imply every condition improved. All signs, contrasts and negative outcomes remain in the complete response arrays and comparisons.

## What changed and why

The [pre-execution protocol](HS_UPSTREAM_TEMPORAL_PROTOCOL_V1.md) and source checkpoint `43af0b7` fixed the candidate, cases, guards and stopping rule before neural outcomes. Existing gain normalization, sigma=0.121902687872575, spatial footprint, graph, neural parameters, 30 ms detector delay and original successful detector are preserved.

One upstream bandpass proxy uses Mi1-like ON low/high-pass constants 54/318 ms and Tm1-like OFF constants 44/296 ms. They were extracted from author code at commit `2e277fef43139230fafc598c93301bf7b27645dd`, cross-checked against its separate simulation-library arrays, with explicit 10 ms source units. No constants were fit to the HS or walking results. [Borst (2025)](https://doi.org/10.1007/s10827-025-00914-5), [pinned author repository](https://github.com/axelborst/temporal_filtering/tree/2e277fef43139230fafc598c93301bf7b27645dd).

For held normalized image contrast u, the new states satisfy h'=(u-h)/tau_lp, g'=(h-g)/tau_hp, d'=(h-g-d)/tau_delay. The visual deviation h-g and delayed signal d enter the unchanged local motion computation. Exact state-transition propagation is causal, initialized at the stationary equilibrium h=g=u,d=0. Final T4/T5 drives remain rectified nonnegative, with clipping counted.

This is a functional hypothesis, not a reconstructed Mi1/Tm1 network or reproduction of the author's entire conductance model. Its four constants are published response-fit values, not newly measured intrinsic conductances. The author's figure filters use 10 ms Euler updates; this continuous-time experiment uses their nominal constants with exact propagation and does not claim bitwise reproduction of those plotted filters. The separate 50 ms calcium observation filter was not added as a neural stage. Uniform channel proxies, signed baseline deviations and retaining an extra detector delay are explicit modeling assumptions.

## What was tested

Twenty-two shared input cases: 16 primary (four frequencies, both directions; four additional lower contrasts, both directions) and six time refinements. Frequency1 supplies the full-contrast endpoints without duplicate simulation. Two exact cached-baseline replays and two half-solver checks are included in 40 new solves. Eight baseline cases are reused only after retinal/source hashes match.

Primary image/source sampling is 1.25/2.5 ms, refined 0.625/1.25 ms; solver 0.25 ms, with 0.125 ms solver controls and unchanged 1 ms forcing ramp. Stimulus: methods85 field, phase zero, 0.04 cycles/degree square grating, 60 Hz/four-bit display, two static/two moving/one static seconds. Both frontends receive identical binocular retinal frames.

Readout is the equal mean of right HSN/HSE/HSS atanh(rate), [2,4) minus [1,2). Individual subtypes and signed-rate summaries are retained. Frequency scoring takes seven coordinates from the pre-existing fifteen-coordinate joint recording band; contrast keeps seven prior coordinates. The band is not recomputed to favor this subset. All selected panel frequencies have 12 recording rows per direction. The panel-target JSON retains the full-bank observed_counts metadata; [coverage clarification](../results/hs_upstream_temporal_v1/panel_source_coverage_clarification.json) explicitly maps those counts to this panel without changing a score or decision. Recordings are already inspected, animal overlap is unverified, and exact projector registration/trial histories and physiological voltage conversion remain unavailable. No full frequency bank, phase average, fresh animals, walking or closed-loop control was tested.

## Numerical and provenance evidence

Fourteen frozen numerical comparisons pass 14/14; largest normalized change 0.0242122. Both dual five-percent endpoint criteria retain the model's own fixed primary PD reference. No failed tolerance was relaxed. The new candidate's spatial convergence is not established.

All three focused tests pass: exact propagation versus independent ODE integration, causal/reset/stationary behavior, and correct subset-band/direction mapping. Independent log1p endpoint arithmetic and separate scoring arithmetic review the results; the source constants agree across two author scripts. Two cached baseline cases reproduce images, drives, rates, final states and checkpoints bitwise. All pre-motion rates are <=1e-12. Recorded clipping entries: 0.

Observation/replay CPU 3133.74 s, cap4200; peak worker RSS 1,457,815,552 bytes, cap2 GiB. No movies, permanent full-source drive arrays, full repository clone or duplicate physiological ZIP. Source acquisition comprised two scripts totaling20,995 bytes. Initial browser403/captcha/API-access limitations are recorded in the acquisition receipt; pinned public raw sources were retrieved successfully. Old sealed outputs remain untouched.

Evidence: [decision and guards](../results/hs_upstream_temporal_v1/decision.json), [all comparisons](../results/hs_upstream_temporal_v1/comparisons.json), [all responses](../results/hs_upstream_temporal_v1/model_responses.csv), [numerical checks](../results/hs_upstream_temporal_v1/numerical_checks.json), [arithmetic review](../results/hs_upstream_temporal_v1/independent_arithmetic_review.json), [independent source cross-check](../results/hs_upstream_temporal_v1/independent_source_parameter_review.json), [resources](../results/hs_upstream_temporal_v1/simulations_complete.json).

## Reproduction and next alternatives

Scientific interpreter and package versions are in environment.json. In an isolated tree with the frozen source files and retained dependencies, run `scripts/hs_upstream_temporal_v1.py prepare`, `run`, `analyze`. The new result directory needs the two pinned source scripts and acquisition receipt before prepare; cases must not already exist. Existing sealed destinations reject writes. Use `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1`; no movie archive is required. A complete second 22-case replay is not claimed: the two specified exact full baseline replays were executed. This report is generated by the companion presentation-only script, which never changes decisions.

This round tests only the declared homogeneous upstream approximation. The immediate mechanistic alternative is a separately frozen component-ablation test: distinguish the contribution of low-pass slowing from high-pass adaptation without fitting new time constants. A more anatomical alternative is branch-specific transient/sustained upstream dynamics with a justified coupling map. Better matched temporal recordings and stimulus metadata are another route. Neither a new ablation nor a second candidate is silently executed after these outcomes. Keep all original failures, and pin separate unused measurements before claiming independent validation.

## Undergraduate explanation

We want a model that both notices small turns and responds like real fly neurons. This round added a fixed, source-inspired slowing and adaptation stage before motion detection. It substantially improved excessive responses to very fast motion while preserving the earlier contrast improvement. Slow-motion responses and opposite-direction suppression still need work. We now have a useful partial improvement and a more specific next question: which part of the new stage helps, and which part suppresses slow signals too much? This is development using known measurements; the revision still needs an independent biological test and its own small-turn check before inheriting either claim.
