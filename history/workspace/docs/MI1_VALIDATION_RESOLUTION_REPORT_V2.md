# Mi1 validation resolution V2 and full-circuit evidence audit

2026-11-05. **A restricted Mi1 calcium-prediction test now passes. Full biological
validation of the MaleCNS walking/yaw model is not complete. There is no evidence
that biologically grounded small-turn detection is impossible.** The finite
alternatives are executed and closed, not left as another proposal.

## What changed scientifically

The V1 zero gains were real for its all-ROI, sustained-response candidates. They
did not establish that every Mi1 model or the selected positive-response cohort
was unmodellable. V2 tested six fixed dynamics and independent repetition-based
qualification. An existing source-supported adaptive Mi1 proxy was selected using
only development animals and later passed the predeclared reserved-animal rule.
This changes the evidence from "no new component agreement" to "limited positive
temporal-component evidence." It does not repair or certify the whole circuit.

## Audit findings

All40 V1 indexed files, prior C2/C3 sources and the prior factorial study rehash
unchanged. All113 V1 development ROI epochs and five zero gains reproduce.
Native and interpolated traces correlate at least0.999298; all development
fluorescence means are positive. Thus normalization by a negative mean or an
interpolation sign inversion does not explain the sign mixture. Quality fields
are all zero; driver and compartment labels do not resolve the opposite signs.
No independent anatomical rule was found in these files to discard inverted ROIs.
The old unsigned-difference helper limitation is retained; V2 casts to float.

The source plot selects Q>0.5 positively stimulus-correlated ROIs, while V1's
primary included all ROIs. They target different cohorts. V1's13s averages also
overlap across10s cycles: that was faithful to the source averaging, not a V1
train/test leak, but would be invalid for independent repetition qualification.
V2 uses98 samples (0–9.7s) from separate complete cycles, with a whole skipped
cycle between early qualification and late scoring. Sources and outcomes:
[audit](../results/mi1_validation_resolution_v2/V1_audit.json),
[metadata](../results/mi1_validation_resolution_v2/development_metadata_audit.csv).

## Prospective design, candidate choice and measurement assumptions

[Protocol](MI1_VALIDATION_RESOLUTION_PROTOCOL_V2.md) and methods were frozen at
commit `f716145` before new scores and all reserved responses. V1 development
results and paper-level qualitative findings were already known; V2 is not a
preregistered V1 analysis. The original six-control/four-C2 development and
three-plus-three reserved animal split remains unchanged.

An early-only functional localizer computes each ROI's Q against stimulus;
Q>0.5 qualifies it. Its F0 uses only early samples. Predictions use that same
early normalization; no late baseline, sign or latency fitting. There are5–8
early and5–8 late cycles per ROI across the full cohort, separated by a guard.
The mean early response also predicts late responses as an explicit
repeatability reference, not a neural model or a mathematically defined ceiling.

For each of six fixed dynamics, one nonnegative amplitude is calibrated from
early control development animal means. Leave-one-development-animal-out
late-response MSE chooses `adapted54` before test responses are processed. Five
control development flies have locally qualified ROIs; one does not. Both
candidate choice and all18 gains are hash-locked. Reserved early masks/F0/cycle
plans are then separately locked before processing any late fluorescence.
No test result changes coefficients, selection thresholds or acceptance rules.

`adapted54` uses the existing nominal54ms low-pass and318ms high-pass constants
from the [previous source audit](HS_UPSTREAM_TEMPORAL_REPORT_V1.md), from
[Borst2025](https://doi.org/10.1007/s10827-025-00914-5), repository commit
`2e277fef43139230fafc598c93301bf7b27645dd`. It is a continuous-time functional
Mi1 proxy, half-wave rectified and observed through a fixed250ms calcium filter,
not a reconstructed conductance circuit or a bitwise reproduction of source
Euler plotting code. Its positive-cohort fitted amplitude is
2.97292808; temporal constants were not fitted here.

The other candidates are the existing Gonzalez-Suarez measured kernels with
paired200/250/300ms observation assumptions, the signed250ms branch and the54ms
low-pass baseline. Dataset/source commits remain those of
[V1](MI1_CALCIUM_BENCHMARK_REPORT_V1.md). Henning's source code/paper are available
at [the pinned repository](https://github.com/silieslab/C2C3_feedback_Henning/tree/745c6114b72a61dabc9389a1f024dbe22f679edf)
and [eLife](https://doi.org/10.7554/eLife.108529.3).

## Complete fixed-family comparison

Skill is1−MSE/zero-response MSE, pooled from equal-animal errors. It measures
prediction error reduction, not a biological-validity percentage. All columns
below use early-qualified positive ROIs, with distinct late scoring repetitions.

| Fixed dynamics | Development positive-cohort LOAO skill | Reserved control skill | Reserved C2 challenge skill |
|---|---:|---:|---:|
| measured250_rectified | -0.15981 | -0.09958 | 0.47497 |
| measured200_rectified | -0.15636 | -0.09885 | 0.47695 |
| measured300_rectified | -0.16293 | -0.09987 | 0.47251 |
| measured250_signed | -0.14554 | -0.09352 | 0.48336 |
| adapted54 | 0.37930 | 0.27432 | 0.46534 |
| lowpass54 | -0.17916 | -0.11025 | 0.44388 |

Selected-model control test skill is0.274319. It improves MSE by
34.64% relative to the separately calibrated low-pass baseline.
The two individual control skills are positive; the >=2-control-animal coverage
guard and all numerical guards pass. These are the frozen limited-component
criteria, not post-hoc relaxed rules. All qualified reserved outcomes:

- C2Sil / 200302_Fly1: 6 early-qualified ROIs; skill 0.50927, correlation 0.84240.
- C2Sil / 200302_Fly10: 7 early-qualified ROIs; skill 0.39370, correlation 0.65515.
- Control / 200218_Fly3: 7 early-qualified ROIs; skill 0.26765, correlation 0.58906.
- Control / 200219_Fly3: 1 early-qualified ROIs; skill 0.27803, correlation 0.78110.

Control200219_Fly1 has zero early-qualified ROIs; C2-silenced200219_Fly2 likewise.
They are retained in all-ROI diagnostics and explicitly counted as noncoverage,
not removed secretly or called biological failures. The qualifying control
sample is only two flies/eight ROIs, including one fly represented by one ROI.
No population-equivalence or robust generalization claim follows from this n.
Errors remain substantial: roughly72.6% of the zero-baseline squared energy
remains in the selected model's pooled control error.

## Alternatives, negative findings and measurement limitations

- The measured-kernel family has negative qualified-control test skill, about
  −0.094 to−0.100. Changing its200–300ms observation assumption or dropping
  rectification does not fix this independently scored control test.
- Using all ROIs with a separately development-calibrated adaptive proxy gives
  control skill0.185781 across all three test flies (all three individual skills
  positive). This is supportive secondary evidence, not the primary target.
- Flipping each ROI's observation polarity from its early Q does not solve the
  adaptive model: all-ROI polarity-diagnostic control skill−0.101108. A
  polarity-mapped low-pass gives+0.366015, but assumes response-derived sign
  reversals and is an observation diagnostic, not physiological reconstruction.
- The early-repeat template has all-ROI control skill0.936113 and C2 skill
  0.812322, showing that many recorded waveforms are reproducible. On qualified
  control subsets its skill falls to0.021086. Thus aggregate repeatability and
  stability of a small response-selected subset are different properties.
- Exploratory late-Q inspection, explicitly AFTER the test, finds6/7 selected
  ROIs remain Q>0.5 in control200218_Fly3 but0/1 in control200219_Fly3. That last
  ROI's late Q is−0.02358. No ROI is dropped or rule changed after this finding.
  Positive predictive skill therefore does not establish a stable sustained
  ON phenotype in every qualified fly. This materially limits the biological
  interpretation even though the frozen component rule passes.
- C2 positive-cohort challenge skill0.465337 uses an intact calibration. No C2
  efficacy, circuit lesion or differential perturbation mechanism was modeled;
  this agreement cannot validate C2 causality. The source uses shibire/water-bath,
  not the separate T4/T5 Kir manipulation.

These finite alternatives are complete. No additional post-test model tuning
followed. All six formerly reserved animals have now been used; their future
use must be labeled development/replication rather than fresh validation.

[All294 metric rows](../results/mi1_validation_resolution_v2/late_metrics.csv),
[all pooled scores](../results/mi1_validation_resolution_v2/late_summary.json),
[exploratory selection stability](../results/mi1_validation_resolution_v2/selection_stability_exploratory.json),
[time courses](../results/mi1_validation_resolution_v2/heldout_late_curves.png),
[candidate comparison](../results/mi1_validation_resolution_v2/candidate_comparison.png).

## Numerical verification, resources and failures

Three pre-execution tests cover unsigned inputs, repetition non-overlap and
invariance of localizer decisions to arbitrary late fluorescence changes.
Independent explicit-index reconstruction checks all177 retained ROI curves,
294 scalar error rows and18 calibrated gains. All96 representative
animal/candidate refinement and independent algorithm checks pass. Maximum
240/480Hz unscaled-prediction RMS change is
0.460566%, below2%. The adaptive cascade is
independently checked with explicit state recurrences. No analysis/runtime
exceptions occurred in this V2 execution. V1's reviewer failure remains preserved.
These numerical checks establish consistency, not biological validity.

Recorded scientific stages used4.196 CPU seconds, peak RSS181.7MiB.
Presentation cost is recorded separately after this writer exits. Budget180CPU s,
32MiB outputs,20GiB reserve; no raw recording copies or movies. Old reports and
model files remain unchanged. [Independent review](../results/mi1_validation_resolution_v2/independent_review.json)
and [decision](../results/mi1_validation_resolution_v2/decision.json).

## Full biological-validation evidence matrix

Different rows refer to different model versions and modalities; they cannot
be combined into a claim that one end-to-end model passed every benchmark.

| Target | Actual supported evidence | Remaining obstacle |
|---|---|---|
| Mi1 temporal component | This V2 restricted independent-repetition prediction passes; two qualified control test flies | Modest accuracy, unstable one-ROI phenotype, approximate calcium observer, no spatial/motion validation |
| T4/T5→HS temporal processing | Prior72-model search completed; no primary candidate passes all frozen guards; three confirmed finalists have wrong preferred15Hz sign | Existing candidate equations mismatch measured frequency responses; not repaired by solver refinement |
| HS contrast | Original LPi circuit has4/8 lower-contrast endpoints outside descriptive band; normalization later repairs one contrast ratio | Different versions retain unresolved response-shape/sign discrepancies; source LUT/subtype uncertainty |
| H2 | Original graph mean PD error16.72deg vs13.76deg geometric reference; median per-polarity shape correlation0.69 | Approximate stimulus replay, modality/pose limits; no current full-circuit held-out validation |
| bIPS | Recorded LPi index+0.15382 vs known observed+0.15599 | Full-waveform mean skill worsens+0.45738→+0.32544; inspected recordings, missing exact G3 patterns |
| DNp15 | Recorded LPi fixes mean null-yaw sign; known-data pooled waveform skill+0.27114 | Mixed amplitude/waveform errors; observation and exact stimulus unresolved; not fresh validation |
| Circuit anatomy | Supported chemical additions, explicit omissions and subtype provenance | Electrical conductances, compartment physiology, some family homologies and effective strengths remain unmeasured |
| Small walking turns | Frozen artificial neural readout passed its bounded fresh24-room2deg/s simulation benchmark | Its weights are not identified biological synapses; no recording-matched biological2deg/s threshold; new Mi1 proxy inherits none of this qualification |

Every source report/hash is recorded in
[cross-study evidence](../results/mi1_validation_resolution_v2/cross_study_evidence.json).
This is a synthesis of prior results, not a new rerun of whole-circuit physiology.

## Definitive conclusion within current scope

We cannot honestly certify the current whole MaleCNS walking model as biologically
validated using this evidence. There are direct unresolved physiological
mismatches in tested versions, and crucial untested mappings/conditions. The
current failed candidate family cannot acquire a validation pass from a new
decoder threshold or a successful Mi1 flash test. The evidence supports stopping
claims of full validation, rather than claiming simulation success proves biology.

It also does NOT support "biological validation cannot ever be done." A new
component has just shown limited predictive agreement, and much of the recorded
signal is repeatable. Additional well-constrained models and experiments remain
possible. A finite grid excludes that grid, not every possible neural circuit.

Uniform flashes cannot identify spatial motion circuitry: spatial-filter
differences summing to zero have exactly zero effect on uniform input, yet
different effects on spatially structured input. A saved mathematical
[counterexample](../results/mi1_validation_resolution_v2/uniform_flash_identifiability_example.json)
demonstrates this without modifying any biological graph. Similarly, uncertain
calcium coupling and chemical-only counts do not determine electrical
conductances. More identical flash simulations cannot resolve those missing
constraints. Published raw STRF/behavioral inputs are not all publicly supplied;
no raw-only analysis is reported as completed.

The concrete next milestones, if further work is commissioned, are: separately
integrate the supported adaptive branch with an explicit coupling model; test
that exact whole-model version on matched spatial/contrast/frequency assays;
obtain independently identified ROI/compartment and indicator calibration plus
matched downstream stimulus/recordings; then test fresh animals and independently
repeat the small-turn qualification. Missing electrical parameters must be
constrained or explicitly left untested. Do not invent connections to fill gaps.
This is a staged research program, not a guarantee that the present model can be
made fully valid by another finite parameter sweep.

## Reproduction and preservation

Scientific Python with `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1` and
`PYTHONPATH=src`. Run `scripts/mi1_validation_resolution_v2.py` stages in order:
`freeze`, `audit`, `development`, `localize`, `evaluate`, `review`; then run
`scripts/complete_mi1_validation_resolution_v2.py`; finally `seal` and `verify`
in separate processes after writers exit. Outputs are exclusive-write protected;
replay in a separately versioned output location. Old recordings/kernels are
referenced by checksum rather than copied. All177 ROI early/late curves,
candidate predictions, F0 values, Q values, partitions, cycle plans, gains,
development LOAO outcomes and locks are retained. Dated progress/method/report
copies enter the seal; live AGENTS/progress remain outside it.

## Undergraduate explanation

We want a fly neural model that notices gentle turns AND behaves like real
neurons. The previous comparison mixed signals that changed in opposite ways.
Here we chose responsive signals using early flashes, froze the model, and
tested later flashes in different flies. A published adaptation-based Mi1 proxy
performed better than silence and a simpler filter. That is real but limited
progress: one small component passed a modest prediction test. Other parts of
the full model still disagree with recordings or lack the measurements needed
for a fair test. We can reject a claim that the whole system is validated now;
we cannot conclude that building a validated system is impossible.
