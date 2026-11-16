# Family-specific circuit dissection and DNp15 audit V1

27 October 2026. Completed retrospective study. **Both added inhibitory families
contribute to the simulated bIPS preference. H2rn-family silencing has the larger
conditional effect, but side-dependent results prevent a single-family explanation.**
DNp15's mismatch has substantial amplitude and waveform components. Neither
biological validation nor improved small-turn detection is established.

## What was frozen and executed

The [protocol](BIOLOGICAL_FAMILY_DISSECTION_PROTOCOL_V1.md),
[configuration](../configs/biological_family_dissection_v1.json) and execution/
audit sources were frozen at checkpoint `ae9a38c` before new single-family
outcomes. The [manifest](../results/biological_family_dissection_v1/before_dissection.json)
records the exact sources and graph identities. Existing recordings and the
previous intact/joint-clamp outcomes were known; inherited `test` labels do not
make these new comparisons independent validation.

The same eight saved inputs comprise two dot realizations and four motion
protocols: yaw, translation cue, left motion and right motion. These are the
preceding 13-s, 45-degree/s display assays, not a new 3D walking or small-yaw
experiment. We executed 16 new single-family cases and reused 16 sealed controls
to complete a 2×2 design. Both families active, uLPTCrn-family silent, H2rn-family
silent and both silent all use the same expanded chemical graph, normalization,
frontend, numerical parameters and visual inputs. The masks silence 0, 17, 8
and 25 candidates respectively. No edge, conductance or neural parameter was
created or fitted. No remaining weight was renormalized after a clamp.

One new full expanded-intact replay matches every saved parent array bitwise.
All reused controls match their sealed parents. Sources, cell identities and
existing family-homology qualifications remain those of the
[anatomical reconstruction](ANATOMICAL_STRENGTHENING_REPORT_V1.md).

## Which family contributes?

Magnitude index is `(abs(T) - abs(Y))/(abs(T) + abs(Y))`, using second-minus-first
motion-epoch response contrasts. Positive values indicate a greater translational
direction contrast, rather than simply greater mean activity during translation.

| Circuit state | bIPS raw index L, seed 1 | R, seed 1 | L, seed 2 | R, seed 2 | Positive cases |
|---|---:|---:|---:|---:|---:|
| Both active | +0.32938 | +0.09361 | +0.32576 | +0.19305 | 4/4 |
| uLPTCrn-family silent | +0.22801 | −0.02212 | +0.22640 | +0.08503 | 3/4 |
| H2rn-family silent | +0.03516 | −0.09529 | +0.03289 | −0.05487 | 2/4 |
| Both silent | −0.03673 | −0.18951 | −0.03670 | −0.13494 | 0/4 |

The predeclared decision is **heterogeneous sign dependence**. Neither individual
clamp removes the positive sign everywhere; the joint clamp does. It would be
incorrect to call either family universally necessary for a positive sign here.

With its partner active, the H2rn family's conditional index effect is
**+0.18890 to +0.29421**, larger in all four cases than the uLPTCrn family's
**+0.09937 to +0.11573**. Both therefore support the intact index under these
conditions. The index interaction is +0.02151 to +0.02977. Raw yaw/translation
contrast interactions are also saved; a nonlinear index interaction alone does
not demonstrate physiological synergy. Silencing either family can change
upstream activity and recurrent feedback, not just its direct current to bIPS.

![Factorial responses](../results/biological_family_dissection_v1/figures/factorial_selectivity.png)

All [seed-level responses](../results/biological_family_dissection_v1/seed_indices.csv),
[48 factorial-effect rows](../results/biological_family_dissection_v1/factorial_effects.csv)
and [896 chemical-current summaries](../results/biological_family_dissection_v1/chemical_current_epochs.csv)
are retained. Effects are interventions within this qualified chemical graph,
not proof of biological causality or of correct candidate-family homology.

## Comparison with known recordings

The primary table transfers the original frozen observation filters/gains.
Recorded bIPS magnitude mean is +0.15599 in four known test flies. The model
means below account for each recording's side and clock. Recorded primary
DNp15/GC6f/WT mean is −0.26170 in five known test flies, with a broad interval
crossing zero in the inherited first-baseline comparison.

| Circuit state | bIPS index | DNp15 index | bIPS bilateral skill | bIPS unilateral skill | DNp15 bilateral skill | DNp15 unilateral skill |
|---|---:|---:|---:|---:|---:|---:|
| Both active | +0.16160 | −0.63536 | +0.47111 | +0.38951 | −0.54931 | −0.12079 |
| uLPTCrn-family silent | +0.04866 | −0.64621 | +0.56391 | +0.41245 | −0.55791 | −0.13553 |
| H2rn-family silent | −0.06204 | −0.80477 | +0.49304 | +0.34714 | −0.86747 | −0.25773 |
| Both silent | −0.14948 | −0.80594 | +0.57381 | +0.34629 | −0.88950 | −0.27470 |

Skill is mean per-fly `1 - model MSE / zero-response MSE`. Negative values mean
worse agreement than predicting zero response. H2rn-family removal worsens the
primary DNp15 comparison more than uLPTCrn removal under this mapping. No state
has positive primary DNp15 bilateral or unilateral mean skill in either declared
observation mode. Removing a family is not an overall physiological repair.

Secondary calibration preserves the original 56-candidate family and primary
cohorts: 448 candidates yield eight calibration-only models, hashed before
reused test scoring. No test data choose a model. All 234 known recording
summaries, three normalizations and both indices remain available. Eight
reporter/compartment/background cohorts stay separate.

Measurement dependence persists: bIPS unilateral skill is +0.38951 with both
families active under transfer, but −0.44730 under own calibration. Under the
uLPTCrn clamp those means are +0.41245 and −0.59717. A better waveform mean can
coexist with worse selectivity. All outcomes, including walking-preparation
transfer and secondary reporter cohorts, remain in the
[complete transfer results](../results/biological_family_dissection_v1/transfer_summary.json).

![Waveform comparisons](../results/biological_family_dissection_v1/figures/waveform_transfer.png)

## Why does DNp15 disagree?

The source audit independently reread 16 selected DNp15 sessions and checked
46 recording summaries. Soma, neurite and selected ROI labels match the inherited
plans; selected raw arrays and clocks match exactly. Source neuron labels are
DNp15 or the appropriate DNp15-RdlFlpStop-WT control. All selected compartments
are dendrites, and the imaging hemisphere matches the recorded soma side in
these sessions. Frame rates are approximately 13.02 or 13.47 Hz. **No supported
metadata/indexing correction was found.** This check does not establish that a
single whole-cell model state equals local dendritic calcium.

The primary expanded-intact DNp15/GC6f/WT test set has 20 trace summaries from
five flies. We tested a descriptive upper bound using each known trace: hold
the filtered model waveform fixed and find its best nonnegative scalar gain.
This oracle is computed separately per trace/window using the inspected outcome;
its gains were never adopted or labeled a calibrated model.

| Expanded-intact primary DNp15 window | Fixed-mapping skill | Per-trace gain-oracle skill |
|---|---:|---:|
| First motion epoch | −0.55623 | +0.57196 |
| Second motion epoch | −2.09853 | +0.51879 |
| First post-motion period | +0.06392 | +0.47277 |
| Second post-motion period | −0.54293 | +0.43903 |
| Full 1–13-s waveform, all four protocols | −0.25730 | +0.52964 |

The full-waveform mean includes bilateral and unilateral protocols together,
so it differs from the earlier bilateral-only −0.54931. The oracle reduces error
substantially, supporting an amplitude contribution. It still leaves a mean
**47.0% of the zero-response predictor's squared error**. Scalar gain therefore
cannot reproduce these observed waveforms exactly. Residuals can include noise,
stimulus mismatch, local calcium dynamics and neural-model error; this calculation
cannot uniquely assign their cause. There is no newly imposed acceptance cutoff.

The 20 full-trace oracle multipliers range from 0 to 4.461; one trace has
nonpositive model/data projection. A different gain for every known trace is
not a common physiological measurement model. The result supports testing
independent measurement constraints and waveform dynamics, rather than adopting
these oracle gains as a fix. All four circuit states have similar descriptive
full-waveform oracle skills, approximately +0.527 to +0.535 under transfer.

![DNp15 shape bound](../results/biological_family_dissection_v1/figures/dnp15_shape_ceiling.png)

The [source methods](https://www.nature.com/articles/s41593-025-01948-9) distinguish
DNp15 dendritic imaging, reporter backgrounds and female imaging preparations.
They also describe their circuit model as a steady-state model, with calcium
convolution used for visualization. Our full-waveform test consequently asks
for temporal agreement beyond that published steady-state construction. Our
male connectome, approximate stimulus reconstruction and scalar observation
model retain separate transfer assumptions. These differences are limitations,
not explanations proven by the present diagnostics.

Independent DNHS1 electrophysiological observations are reported by
[Suver et al. (2016)](https://www.jneurosci.org/content/36/46/11768), providing a
possible comparison that does not depend only on calcium imaging. The
[institutional record](https://authors.library.caltech.edu/records/mqzzc-va989)
lists an article PDF; an exact raw-trial dataset and matched walking/small-yaw
assay were not identified in this bounded search. Published curves could support
a limited, explicitly digitized steady-state comparison, not raw-trial
validation. The known Erginkaya deposit remains inspected data. The renewed
search acquired no independent matched recordings or exact original G3 arrays.
See the [source-constraints ledger](../results/biological_family_dissection_v1/source_constraints_review.json).
This does not establish that such data are unavailable everywhere.

## Numerical checks, corrections and evidence

All 32 activity masks and unchanged weights were independently checked, with
32 independent Python RK4 checkpoint intervals and role-current decompositions.
Maximum neural arithmetic discrepancy is 2.78×10⁻¹⁷. Both new variants have
exact full 1-ms reference parity. Fixed-forcing half-step rate errors are at most
2.12×10⁻¹⁰ and saved full-state errors below 9.22×10⁻¹⁰, at unchanged 10⁻⁷
tolerance. No new retinal geometry or small-yaw convergence claim follows.

Independent review recomputes all 448 observation candidates, 1,208 waveform
comparisons, 3,828 fly indices and 834 bootstrap summaries. Maximum candidate-gain
discrepancy is 3.41×10⁻¹³. A separate filtered predictor and closed-form quadratic
projection reproduce all 2,072 DNp15 window diagnostics; maximum arithmetic
discrepancy is 2.92×10⁻¹¹. These checks establish numerical execution, not biology.

Two audit implementation failures are preserved. V1 repeated a Python keyword
and failed compilation before reading recordings; AST parsing had not caught it.
[R2](BIOLOGICAL_FAMILY_AUDIT_CORRECTION_R2.md) corrected the provenance-field name
and completed the metadata audit. Its shape action then requested a nonexistent
secondary-cohort own-calibration model. [R3](BIOLOGICAL_FAMILY_SHAPE_CORRECTION_R3.md)
retained inherited transfer for that cohort and both predeclared modes for the
primary cohort, without extra fitting. Both corrected versions were compiled
and hashed before their corresponding completed audit outputs. Original sources,
failures and manifests remain intact; scientific rules and neural parameters
were unchanged.

[Neural checks](../results/biological_family_dissection_v1/neural_review.json),
[solver checks](../results/biological_family_dissection_v1/numerical_review.json),
[measurement arithmetic](../results/biological_family_dissection_v1/measurement_review.json),
[bootstrap review](../results/biological_family_dissection_v1/aggregation_review.json),
[DNp15 metadata](../results/biological_family_dissection_v1/dnp15_metadata_audit.json),
[independent projection audit](../results/biological_family_dissection_v1/dnp15_shape_review.json).

## Decisions and alternatives

This study completes the authorized family dissection and DNp15 audit. We retain
the intact expansion as a candidate and the original circuit as its control;
no lesion is adopted as a repair. The frozen sign rule yields heterogeneous
dependence rather than a universal one-family mechanism. No fresh small-turn
experiment, physiological success criterion or motor controller was added.

| Next alternative | What it could establish | Main limitation |
|---|---|---|
| H2rn pathway-specific tests | Separate direct H2rn-family input to bIPS from feedback through H2/other selected cells | Remains a model mechanism; qualified identities and chemical-only dynamics persist |
| Independent DNHS1 electrophysiological benchmark | Test steady-state directional tuning outside the repeatedly inspected calcium dataset | Raw trials were not located; published-curve digitization requires explicit uncertainty and a narrower claim |
| Independent reporter/compartment calibration | Test whether one justified measurement model transfers across animals and stimuli | Requires suitable new measurements; current oracle gains cannot supply this evidence |
| Fresh small-yaw environments | Test functional utility of a justified frozen candidate | Existing anatomy walking tests did not establish a general gain; biological agreement is not yet secured |

**Recommendation:** prioritize the independent DNHS1 physiological comparison
for the biological-validation goal, starting with a bounded source/curve audit
and freezing a steady-state target before simulation. If the usable target is
too weak, the immediate computational alternative is the H2rn pathway-specific
test. Avoid another broad gain or decoder search on the same recordings. A
published-curve comparison would still not establish biological small-turn
thresholds, which need matched lower-speed measurements.

## Reproduction and undergraduate explanation

Use `PYTHONPATH=src:scripts`, one BLAS/OpenMP thread and the recorded Python
environment. In a new versioned output directory, run the main driver's `setup`,
reviewer's `preflight`, main `freeze`, `parity`, `run`, `fit`, `score`; run R2
`metadata` and R3 `shape` with their additional frozen manifests. Run reviewer
`neural`, `numerics`, `measurements`, `aggregates`, and finisher `characterize`,
`shape_review`, `figures`, followed by visual/export review, `seal` and a separate
`postseal` process. Do not run fixed-path producers over the completed archive.
V1's failing audit is intentionally preserved, so compilation checks should
distinguish that archived failure from the runnable R2/R3 audit versions.

We wanted to understand why extra inhibitory neurons helped bIPS and why DNp15
still looked different from real recordings. We switched the two added groups
off one at a time while keeping everything else fixed. Both helped, with a
larger effect from the H2rn candidates in these tests; their effects also differed
between the left and right sides.

We found no simple labeling mistake in the DNp15 recordings. Changing the size
of the simulated signal helps, but it does not reproduce the full recorded
response. This gives us more specific questions instead of a general request
to keep tuning. The next goal should be to challenge the circuit with independent
physiological evidence, with a pathway-specific simulation as the practical
alternative. Reliable biological detection of tiny turns remains a longer-term
goal; these larger-motion tests identify what still needs support.
