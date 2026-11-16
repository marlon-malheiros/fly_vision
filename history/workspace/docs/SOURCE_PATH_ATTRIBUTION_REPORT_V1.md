# Where the small-turn signal is confused with forward-walking responses

26 October 2026. **The turn-dependent signal survives in the frozen model,
but the same horizontal source groups also transmit scene-dependent
straight-walking imbalances. At fast walking, variation of that imbalance
across rooms exceeds the typical±2°/s response.** This investigation
accounts for the recurrent model's responses; it does not repair detection
or identify a unique biological cause.

## What is new

The prior [continuous-response study](CONTINUOUS_YAW_MECHANISMS_REPORT_V1.md)
showed nonzero yaw gain and scene offsets. The [input audit](INPUT_MAPPING_AND_RESEARCH_AUDIT_REPORT_V1.md)
checked labels, sampling and population input means, explicitly without
decomposing recurrent neural outputs. Larger readouts had already failed
to improve generalization consistently. This study closes that specific
accounting gap rather than repeating those searches.

Reuse all704V2episodes,44rooms and allthree fixed input versions. Previous
outcomes are known; this is **retrospective mechanistic analysis**, not a
new held-out detection benchmark. Freeze the recipe and numerical gates at
checkpoint8e82d65before computing its new components. The sixteen groups
are the existing L/R×T4a–d/T5a–dbody-ID populations. Include every original
recurrent chemical connection and retain all neural parameters, source
positions, experimental labels and old acceptance criteria.
[Protocol](SOURCE_PATH_ATTRIBUTION_PROTOCOL_V1.md),
[pre-component identities](../results/source_path_attribution_v1/before_attributions.json).

## Method and checks

Construct a separate linear diagnostic about zero activity,
dx/dt=[−x+gWx+du]/τ, using the original chemical matrix and gains. Its
discrete adjoint computes the influence of each source drive sample on the
original[0.70,1.40)mean L/Rresponses in HS,H2,bIPSandDNp15. It preserves
the exact1-msRK4boundary convention and10-mssource clock, including the
initialization before motion. Summing source-weighted contributions gives
an approximate nonlinear response; the original model remains untouched.
No channel balancing, gain adjustment, new decoder or threshold search.

The kernel is201times×13,579sources×8outputs. Contracting it with the
retained real source drives yields all group contributions, including
indirect and recurrent paths. Linear contributions can have opposing
signs. They are not unique percentages of biological causality.

All704component tasks complete in57.7seconds, with zero execution failures.
Independent controls add80full forward trajectories in70.4seconds:
12linear replays and68strict nonlinear replays. The latter comprise four
known fast-walking cases intact and with each of sixteen source groups'
**external drive** set to zero. Their neurons and all recurrent synapses
remain. These are model input interventions, not biological cell lesions.

| Fixed check | Passed/total | Largest absolute discrepancy |
|---|---:|---:|
| L/Rclass mean versus original nonlinear output | 16,896/16,896 | 9.52×10⁻⁷model units |
| Bilateral difference versus original nonlinear output | 8,448/8,448 | 8.25×10⁻⁷model units |
| Original frozen decoder score | 7,920/7,920 | 0.00439°/s |
| Independent linear forward replay | 12/12 | 1.21×10⁻¹⁶model units |
| Strict nonlinear intact replay | 4/4 | 0 |
| Predicted versus actual input-omission effect | 768/768 | 1.76×10⁻⁷model units |

Primitive/omission endpoints use1%relative error with1e-5floor; bilateral
differences use5%with that floor. Decoder scores use0.02°/sabsolute error;
linear forward replays use1e-10. All tolerances were fixed before component
analysis. Original decisions remain authoritative, especially near cutoffs.
Fourteen toy input impulses independently match dense augmented-state
polynomial propagation within1.74×10⁻¹⁷against a1e-12gate.
[Every check](../results/source_path_attribution_v1/analysis/numerical_summary.json),
[all omission effects](../results/source_path_attribution_v1/analysis/input_omission_checks.json).

## Small-turn response versus scene-dependent baseline

Define q=L−R. For each room compare its straight value q0 with the odd
response[q(+2)−q(−2)]/2. The latter is the paired change associated with
2°/srotation; dividing it by2gives the local finite-difference yaw gain.
These same-room contrasts are descriptive analysis and are never supplied
to the detector as a test-time baseline correction.
The contrasts include image and curved-trajectory changes under prescribed
yaw; they are not isolated neuronal transfer functions.

The following original DNp15results use the24already-examined V2test rooms:

| Speed mm/s | Scene SD of straight q0 | Median absolute odd2°/sresponse | Ratio |
|---:|---:|---:|---:|
| 5.5 | 1.144×10⁻⁴ | 2.493×10⁻⁴ | 0.459 |
| 11 | 2.086×10⁻⁴ | 2.189×10⁻⁴ | 0.953 |
| 16.5 | 2.765×10⁻⁴ | 1.837×10⁻⁴ | 1.505 |

These are model-activity units and descriptive room variation, not
physiological noise, a signal-detectiond′, threshold or statistical
significance test. At fast walking the analogous ratios are1.435forHS,
1.324forH2and1.489forbIPS. This particular metric does not show improved
scene invariance at DNp15. It does not establish a unique stage where
information is destroyed or exclude a different neural representation.
[All versions/roles/speeds](../results/source_path_attribution_v1/analysis/output_summary.json),
[figure](../results/source_path_attribution_v1/presentation_v2/scene_offsets_and_turn_responses_v1.png).

## Which sources carry the contributions?

In the original fast-walking DNp15decomposition, the large contributions
come from the currently assigned horizontal subtype-agroups: L/R T4aand
T5a. All sixteen were tested and are retained. Their mean straight
contributions are respectively+4.943,+5.417,−5.554,−5.942in10⁻⁴model
units. Their mean odd2°/scontributions are+0.420,+0.446,+0.473,+0.496in
the same units. They therefore transmit both the large opposing
straight-walking components and a turn-dependent component.

Across all left-eye source groups the mean straight contribution is
+1.059×10⁻³; across right-eye groups it is−1.171×10⁻³. Their cancellation
leaves approximately−1.123×10⁻⁴. Scene variation in this residual can be
comparable with the small turn signal. Adding standard deviations or
assigning causal percentages would ignore correlated, cancelling terms.

The predeclared a/bgroup aggregate has straight-scene SD2.738×10⁻⁴and
mean odd response1.850×10⁻⁴. The c/daggregate is much smaller:
7.190×10⁻⁶and3.140×10⁻⁶. This does not support a simple explanation
dominated by c/dinput contamination under these conditions. T4andT5both
contribute substantial yaw response (mean odd9.144×10⁻⁵and9.668×10⁻⁵),
so this is not an OFF-only bottleneck either. These are group-defined
input effects through the frozen recurrent circuit, not emitted T4/T5
firing rates or newly measured biological preferred directions.
[All sixteen group summaries](../results/source_path_attribution_v1/analysis/group_summary.json),
[predeclared aggregates](../results/source_path_attribution_v1/analysis/coarse_summary.json),
[complete group figure](../results/source_path_attribution_v1/presentation_v2/all_source_groups_dnp15_v1.png).

## Why the direction-field change did not fix this

Across all44known rooms, the T4-only field changes mean DNp15yaw gain by
−0.84/−0.90/−1.02%at the three speeds; the T4/T5transfer hypothesis gives
−1.97/−2.08/−2.28%. On the old24test rooms the fast offset-to-turn ratios
remain1.519and1.543, versus1.505originally. This accounts for a small
effect on the problematic balance, rather than a successful repair hidden
by the classifier. The source field can be anatomically motivated while
this projection remains insufficient.
[All field changes](../results/source_path_attribution_v1/analysis/field_changes.json),
[comparison](../results/source_path_attribution_v1/presentation_v2/direction_fields_and_offset_ratio_v1.png).

## Biological interpretation and next evidence

[Erginkaya et al.(2025)](https://www.nature.com/articles/s41593-025-01948-9)
report transformations in rotational/translational selectivity and effects
of inhibitory circuitry, including bIPS. Our scene-variation metric is not
their physiological discrimination index, and the stimuli/measurement
models differ. These results cannot be treated as a quantitative
contradiction or validation. Likewise, the position-dependent T4field of
[Zhao et al.(2025)](https://www.nature.com/articles/s41586-025-09276-5)
does not establish our cross-specimen registration, T5transfer or single-node
rate-equation assumptions.

The specific supported model finding is **shared source pathways for
scene offsets and yaw signals**, verified by predefined nonlinear input
interventions. It does not identify whether optics, functional T4/T5
encoding, spatial pooling, graph normalization, missing electrical
coupling or unmodeled uLPTCrns/H2rnsphysiology supplies the main biological
error. No contribution here licenses an invented connection or a fitted
reweighting chosen to improve yaw classification.

The next informative biological comparison is to quantify matched-stimulus
ON/OFFhorizontal motion responses and bilateral integration during forward
plus small-yaw stimulation, using independently calibrated measurements.
Model predictions to test are: both T4andT5drive influence DNp15baseline
and yaw gain; changing scene structure at fixed speed changes the
straight-walking bilateral residual; suppression of scene-dependent
translation must be assessed separately from amplification of yaw gain.
These hypotheses need physiological tests; they are not demonstrated fly
mechanisms or a new detector. No closed-loop control is introduced.

## Reproducibility, corrections and scope

Independent arithmetic review checks34,048rows, reconstructs all704output
means within2.17×10⁻¹⁸ and separately sums every kernel element on six
specified version/control combinations. A fresh source build reproduces
the full kernel, four main component cases and four forward controls
exactly. No second complete704+80execution is claimed.
[Independent review](../results/source_path_attribution_v1/independent_review.json),
[fresh-build replay](../results/source_path_attribution_reproduction_v1/complete.json),
[reproduction instructions](SOURCE_PATH_ATTRIBUTION_REPRODUCTION_V1.md).

The first figure layout placed a caption over panel titles. PresentationV2
moves it to a separate footer and preserves every initial figure and all
numerical values. Four final PNG/PDFpairs accompany the report. There were
no simulation execution failures or failed new approximation gates. Prior
small-turn detection failures remain unchanged; the original fast DNp15
readout still detects5/48±2°/s turns. This finite mechanistic study is
complete, while neural repair and biological validation remain open.

## Undergraduate explanation: what we did, what we want, and why

We want the brain model to recognize a small turn while walking forward.
We traced its responses back to the existing visual input groups. The
turn signal is still there, but forward walking also produces strong
responses that depend on what each eye sees. Small differences between
those large responses can resemble a turn. This helps explain the model's
mistakes and tells us what to measure next, without pretending that an
unsupported change to the circuit would be a biological fix.
