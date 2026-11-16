# Biological failure localization V1

27 October 2026. Completed retrospective diagnostic study. **The existing
anatomy-expanded circuit recovers the expected bIPS selectivity in these
simulations. DNp15 responses and robust physiological transfer remain unresolved.**
No replacement model was selected or declared biologically validated.

The [previous biological benchmark](BIOLOGICAL_SELECTIVITY_BENCHMARK_REPORT_V1.md)
and its [walking-preparation supplement](BIOLOGICAL_WALKING_TRANSFER_REPORT_V1.md)
remain sealed, including their failed acceptance decisions. This report adds a
separate diagnosis; it does not revise those decisions. The useful change concerns
translation/rotation response contrasts at 45 degrees/s. It does not establish a
biological threshold for the original small-turn target of 2 degrees/s.

## Scope, separation and reproducibility

The [protocol](BIOLOGICAL_FAILURE_LOCALIZATION_PROTOCOL_V1.md), code, parameters,
interventions and analysis choices were hashed in the
[pre-diagnostic freeze](../results/biological_failure_localization_v1/before_diagnostics.json)
at source checkpoint `b8793c8`, before these new diagnostic outcomes. Existing
recording outcomes were already known. These are retrospective comparisons on
development data, even where an inherited assignment is called `test`.

We reused the first two fixed dot realizations from the parent primary display,
seeds 202610279100 and 202610279101. Four protocols per seed give eight identical
saved image-derived input sequences: bilateral yaw, bilateral opposed-hemifield
motion used as a translation cue, and left/right unilateral motion. Each lasts
13 seconds with opposite motion epochs at 2–4 and 9–11 seconds. The translation
cue is a display stimulus; it does not recreate depth-dependent flow from a
walking fly in a 3D room. No new environmental generalization test was performed.

Six graph variants produce **48 full-network cases**. Two conditional references
using the previously reconstructed printed equations produce **16 more cases**.
The original 13,593-cell graph, retinal frontend, numerical parameters, 20-ms
global pole, 10-ms input clock and 1-ms production solver remain unchanged.
Every intact rate/final-state replay equals its parent arrays exactly. The
expanded graph is the existing 13,618-cell reconstruction; no new edge or
electrical conductance was invented in this study.

The comparison includes 234 previously inspected recording summaries from 83
sessions: 96 calibration, 124 inherited test and 14 walking-preparation traces.
Eight reporter/compartment/background cohorts remain separate. Both local
baseline standard deviations resolve for all 1,696 inherited usable trial/ROI/
protocol units; paired normalization removes no additional usable unit. Invalid
and padded units retain their previous exclusions. All outputs, inputs, graph
identities and source provenance are retained in the
[parent-input ledger](../results/biological_failure_localization_v1/parent_inputs.json).

## Circuit comparisons

The primary transfer comparison keeps the previous observation filter and gain.
Magnitude selectivity is `(abs(T) - abs(Y))/(abs(T) + abs(Y))`, where T and Y are
second-minus-first motion-epoch response contrasts, averaged within each fly.
Positive values indicate larger translational direction contrast; negative
values indicate larger rotational contrast. This does not simply compare mean
activity during any translation with mean activity during any rotation.

The recorded primary bIPS/sytGC7f/axon/native mean is **+0.15599**, with a
descriptive 95% fly-bootstrap interval **[+0.00140, +0.34375]**, n=4. The recorded
DNp15/GC6f/dendrite/WT mean is **−0.26170**, interval **[−0.72346, +0.25357]**, n=5.
The latter does not resolve a population preference. Bootstrap intervals use
5,000 draws; their draw order differs from the sealed parent, whose intervals
remain unchanged. Shared point estimates reproduce the parent.
The changed model estimates relative to the parent reflect this predeclared
two-seed subset instead of its four primary seeds; neural parameters did not change.

| Variant | bIPS index | DNp15 index | bIPS bilateral skill | bIPS unilateral skill | DNp15 bilateral skill | DNp15 unilateral skill |
|---|---:|---:|---:|---:|---:|---:|
| Original | −0.15045 | −0.91159 | +0.52242 | −0.44872 | −1.23147 | −0.50540 |
| H2 → bIPS cut | +0.18278 | −0.96012 | +0.70253 | −0.09978 | −1.42969 | −0.58984 |
| HS → bIPS cut | +0.01417 | −0.61908 | +0.18886 | −0.19028 | −1.94383 | −0.78505 |
| bIPS → DNp15 cut | −0.15045 | −0.67366 | +0.52242 | −0.44872 | −2.20383 | −0.87584 |
| Existing expanded graph | **+0.16160** | −0.63536 | +0.47111 | **+0.38951** | −0.54931 | −0.12079 |
| Expanded, added families silent | −0.14948 | −0.80594 | +0.57381 | +0.34629 | −0.88950 | −0.27470 |
| Printed equations, all HS | +0.30340 | −0.82303 | +0.59007 | −0.66890 | −2.50419 | −1.79195 |
| Printed equations, classic HS | +0.29785 | −0.82182 | +0.58968 | −0.68392 | −2.43260 | −1.75755 |

Skill is the mean across flies of `1 - model MSE / zero-response MSE`, using the
unchanged full first-baseline-normalized waveform. Zero is the zero-response
predictor; negative values mean the model does worse. These descriptive means
are not newly declared acceptance tests. Predicted index variation across flies
comes from readout side, sampling clocks and measured normalization covariates,
not independently simulated neural noise or uncertainty about physiology.

![Circuit comparisons](../results/biological_failure_localization_v1/figures/circuit_comparison.png)

The expanded graph produces positive unfiltered bIPS indices on **both sides in
both seeds**, ranging **+0.09361 to +0.32938**. The original is negative in all
four, **−0.19232 to −0.03859**. The expanded graph with new families silent is
also negative in all four, **−0.18951 to −0.03670**. This sign change therefore
depends on activity transmitted through the added families within the specified
model, rather than solely on the expanded input-weight denominators. It does
not establish sufficiency or necessity of either family individually.

The graph contains 17 qualified uLPTCrn-family and eight H2rn-family candidates,
selected in the earlier [anatomical study](ANATOMICAL_STRENGTHENING_REPORT_V1.md)
using connectomic identities and transmitter annotations. Family homology remains
qualified. The earlier study records 80,833 omitted incident connections and
unavailable electrical conductances. Single scalar nodes with inherited common
dynamics cannot establish branch-specific inhibitory gating or measured firing
and calcium dynamics. This result does not repair those constraints.

## Mechanistic localization and controls

The lesions remove four positive H2→bIPS edges, 15 positive HS→bIPS edges, or
four negative bIPS→DNp15 edges. Each ledger retains its original source, target
and weight. No remaining edge is renormalized after a cut.

Removing H2→bIPS input reverses bIPS selectivity and improves its bilateral
waveform skill, but worsens DNp15 skill. H2 transmission is therefore one
determinant of the mismatch in this model, not a sufficient overall repair.
Removing HS→bIPS yields a slightly positive magnitude index but a **−1.0 signed
index**, revealing the wrong signed response. A favorable absolute-value index
alone would conceal that failure. The downstream cut leaves bIPS effectively
unchanged while altering DNp15, as expected for this pathway control.

The [current decomposition](../results/biological_failure_localization_v1/chemical_current_epochs.csv)
retains 1,344 summaries from complete selected-network states, including all
seven presynaptic roles. The added uLPTCrn/H2rn families contribute negative
chemical input to bIPS during the first yaw and translation epochs. These
terms disappear under the joint clamp. Their effects on contrasts include
feedback and upstream response changes; a current bar is not an effective
causal gain or a measured biological synaptic current.

![bIPS chemical inputs](../results/biological_failure_localization_v1/figures/bips_currents.png)

The [bilateral table](../results/biological_failure_localization_v1/bilateral_asymmetry.csv)
retains L, R and R−L for every full-network variant, seed, role, stimulus and
motion epoch. Anatomical additions change both bilateral balance and amplitude.
We do not equate reducing asymmetry during a particular motion epoch with
improved small-yaw detection. The previous anatomical study already found no
general small-yaw improvement under its frozen decoder criteria; that result
remains valid. This new cell-specific comparison asks a different question.

The printed-equation references recover a positive bIPS index with either HS
definition but fail primary DNp15 waveform transfer. They apply signed weights
from the publication's diagram to our intact HS/H2 trajectories. They are
conditional boundary comparisons, not recovered author simulator code, a new
anatomical graph or calibrated biological conductances. Their zero direct H2
coefficient cannot justify deleting an observed anatomical connection.

## Measurement, repeatability and data audit

We evaluated every predeclared combination of three normalization methods and
two indices. Local baseline centering changes the primary recorded bIPS index
from +0.15599 to +0.12362; local z-scoring gives +0.11516. The original model
remains negative: −0.15045, −0.15050 and −0.09105 respectively. The author-style
signed convention gives the same bIPS means here. These processing alternatives
therefore do not reverse the original mismatch.

DNp15 depends more strongly on measurement choice. Its recorded local-z
magnitude index is −0.42918, interval [−0.78877, −0.06960], whereas the local-z
source-signed mean is −0.26205, interval [−0.87213, +0.41172]. One cannot use the
first result as validation of the author's signed computation. Our local-z
analysis uses original saved clocks and within-fly aggregation; it is an
explicit approximation, not an exact rerun of author resampling/session pooling.
Predictions use measured baseline-SD ratios instead of invented neural noise.

For the original circuit we also computed all **1,344 observation-envelope
cases**: 56 filter/rectification candidates × four roles × two sides × three
display hypotheses. For bIPS L, none of 168 cases has a positive magnitude
index, range −0.09394 to −0.03056. For bIPS R, **8/168 are positive**, full range
−0.17684 to +0.69063. Thus some filters can reverse the right-side index; a
universal claim that calcium filtering can never change the sign would be
incorrect. No candidate was selected by agreement with test outcomes, and this
bounded envelope does not test all possible reporter physics.

Odd/even **compacted accepted-repetition slots** give a repeatability check,
not original chronological trial halves. Each half needs two distinct valid
repetitions. Three of four primary bIPS test flies qualify: magnitude-index sign
agreement is 3/3, correlation 0.988 and mean absolute difference 0.0415. Four of
five primary DNp15 flies qualify: sign agreement is 2/4, correlation 0.851 and
mean absolute difference 0.3623. Small samples and missing halves prevent a
population reliability claim. Poorer DNp15 repeatability limits precise model
comparison; it does not explain every waveform mismatch.

![Measurement diagnostics](../results/biological_failure_localization_v1/figures/measurement_diagnostics.png)

The initial source audit made a **false-alarm indexing assumption**: it treated
F_All repetition slots as original chronological trial positions and found 479
finite slots among 966 supposed excluded-slot checks. Independent exact
matching resolves this: **2,343/2,343 nonempty selected source trial/ROI traces
match an original accepted trial, zero match an excluded trial, and no mapping
is unresolved across 83 sessions**. The source has compacted accepted
repetitions before padding. Both the initial audit and its
[V2 correction](../results/biological_failure_localization_v1/trial_mapping_review_v2.json)
are preserved. No recordings were deleted again or reprocessed on this basis.

Author soma metadata remains the primary side mapping. The opposite-side
counterfactual makes the original signed index +1.0 for both primary cohorts,
while magnitude indices remain negative (bIPS −0.04129, DNp15 −0.92299).
This illustrates how a side reversal can manufacture an attractive signed
result. It supplies no anatomical justification for that reversal, which was
not adopted. Soma, local compartment and visual display registration remain
distinct anatomical questions.

The public source search and sampled supplementary video did not recover exact
G3 trial pattern arrays or a verified modified generator. Sampled titles show
roll, bilateral front-to-back, sideslip and combined fore-aft/sideslip examples.
They do not verify the unilateral recording protocol's stationary-versus-black
mask. The [movie-scope ledger](../results/biological_failure_localization_v1/stimulus_movie_review.json)
preserves this negative finding. Approximate input reconstruction remains an
alternative explanation for disagreement.

## Waveform transfer and retained negative findings

Secondary fits evaluated **896 candidates**, 56 per variant/cohort, yielding
16 observation models. Only inherited calibration flies' bilateral traces
entered each fit. All models were
[hashed before reused test scoring](../results/biological_failure_localization_v1/before_reused_test_scoring.json).
No neural parameter was fitted. Because test responses were already known,
these fits diagnose sensitivity; they are not fresh validation after model choice.

The expanded circuit's bIPS unilateral skill is +0.38951 under the inherited
mapping, but **−0.44730 after its own calibration**. Its walking-preparation
bilateral skill changes from **+0.20911 to −4.10424** between those mappings.
Own-calibration gain is approximately 1,464 versus 514 in the original circuit;
that amplitude change helps explain why reduced raw responses can appear to
transfer well under the old mapping. The joint-silent expansion also improves
some unilateral waveform means despite keeping the wrong selectivity sign.
Consequently waveform improvements cannot all be assigned to recurrent activity.
Normalization and observation calibration contribute separately.

Every tested variant has negative mean bilateral and unilateral skill in the
**primary DNp15/GC6f/WT** cohort under both observation modes. Improvements in
the expanded graph do not make it adequate. Other cohorts are retained: the
single DNp15/GC7f fly has positive bilateral skill (+0.45322 original, +0.60594
expanded), and expanded unilateral skill +0.34642. One animal cannot replace
the primary cohort or establish generality. HS and H2 controls show modest
changes and remaining unilateral mismatches; different reporter cohorts are
not pooled to hide these differences.

![All primary transfer comparisons](../results/biological_failure_localization_v1/figures/waveform_transfer.png)

The four walking-preparation animals remain already inspected data; no verified
continuous walking, speed or 2-degree/s turn labels are available. Their local-z
bIPS mean is +0.09290 with a broad interval [−0.17670, +0.36042]. Neither a new
biological detection threshold nor behavioral-state correction follows.

## Numerical and independent checks

| Check | Result |
|---|---|
| Eight intact full rate/final-state replays | Bitwise identical to sealed parent |
| Independently rebuilt lesion masks and activation vectors | All 48 cases pass; no post-cut renormalization |
| Independent Python RK4 checkpoint intervals | 48 pass; maximum discrepancy 2.78×10⁻¹⁷ |
| Independent role-current decomposition | 672 checks at saved checkpoints pass |
| Printed-reference algebraic elimination | All 16 cases pass, tolerance 10⁻¹² |
| Raw recording baseline/epoch arithmetic | 234 traces pass; maximum epoch difference 2.84×10⁻¹⁴ |
| All 896 observation candidates | Maximum gain discrepancy 9.10×10⁻¹³ |
| Every predicted epoch and waveform error | Pass; maximum waveform-MSE discrepancy 4.55×10⁻¹³ |
| Independent fly indices and bootstrap intervals | 6,756 indices and 1,464 summaries pass |
| Independent transfer mean reconstruction | All variants, modes and groups pass |
| Expanded solver refinement with fixed forcing | Exact 1-ms reference parity; half/quarter-step rate errors ≤2.28×10⁻¹⁰ |

The expanded refinement keeps the inherited **1-ms input ramp fixed** at all
solver steps; maximum saved full-state error is below 9.78×10⁻¹⁰ at unchanged
10⁻⁷ tolerance. This respects the parent's numerical-control correction rather
than comparing different forcing waveforms. No retinal/front-end trajectory
was changed; current geometry/sampling checks are inherited from the parent.
This study adds no new small-yaw geometry or temporal-resolution validation.
Numerical reproducibility establishes correct execution of these equations,
not their physiological truth.

Evidence: [neural review](../results/biological_failure_localization_v1/neural_review.json),
[reference review](../results/biological_failure_localization_v1/reference_review.json),
[expanded convergence](../results/biological_failure_localization_v1/expanded_numerical_review.json),
[measurement review](../results/biological_failure_localization_v1/measurement_review.json),
[aggregation review](../results/biological_failure_localization_v1/aggregation_review.json),
[transfer review](../results/biological_failure_localization_v1/transfer_review.json).

## Interpretation, remaining questions and experimental tests

The publication supports investigating recurrent inhibition and H2-input gating,
including mechanisms beyond a simple GABA-receptor explanation. Our finding is
qualitative agreement with that broad direction; it neither identifies the same
cellular mechanism nor quantitatively reproduces the physiology.
[Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9),
[author analysis/data repository](https://github.com/ChiappeLab/Erginkaya_et_al_2025).

| Explanation examined | Supported conclusion or unresolved limit |
|---|---|
| Incorrect excluded-trial handling | Exact source matching finds no retained excluded trial in selected units |
| First-baseline drift or absolute-value formula alone | Does not reverse the original bIPS mismatch under declared alternatives |
| Observation filtering alone | Some R-side candidates reverse sign; none on L in the bounded family; no replacement selected |
| Excess effective H2 transmission to bIPS | Controlled removal changes the bIPS computation, but worsens DNp15 transfer |
| Existing recurrent-family chemical activity | Changes bIPS preference with normalization held fixed; joint effect only |
| Added-input normalization alone | Does not restore bIPS sign, but explains part of waveform/amplitude changes |
| Author printed central equations | Positive bIPS contrast possible from existing HS/H2 inputs; DNp15 transfer still fails |
| Soma/readout side reversal | Attractive signed counterfactual lacks independent anatomical support |
| Uniform reliable DNp15 target data | Small cohort, reporter differences and split-half variation limit that claim |
| Exact stimulus/compartment/reporter mapping | Still incomplete; plausible contributor to remaining disagreement |
| Missing electrical coupling or local gating | Not parameterized; no conductance invented |
| Reliable biological small-turn detection | Not established by this 45-degree/s diagnostic |

The next defensible biological comparison should keep the expanded chemical
circuit as a **candidate**, retain the original as its control, and freeze a
matched stimulus/compartment measurement specification before using independent
recordings. If no independent data exist, further reanalysis must stay labeled
development. Separating uLPTCrn-family and H2rn-family perturbations could resolve
their contributions; the current joint clamp does not do so. Exact stimulus
provenance, compartment mapping and behavioral-state measurements are more
informative than another search for a favorable decoder or gain.

Experimentally testable predictions are: (1) recurrent-family perturbations
should alter bIPS translation/rotation contrast beyond a uniform amplitude
scale; (2) selectively weakening effective H2 transmission may improve a bIPS
contrast while worsening a downstream response, so record both populations;
(3) reporter/compartment and walking state should be controlled when testing
amplitude transfer. These are model-generated hypotheses. A computational cut
does not reproduce all effects of a genetic or receptor manipulation and does
not prove a biological cause.

The finite diagnostic ladder is complete. No neural parameter search, adoption
of a lesion, new decoder optimization, hardware claim, motor-intention inference
or closed-loop controller was added. The previously working hybrid engineering
detector remains preserved and separate from biological validation.

## Reproduction and evidence

Use the repository Python dependencies and `PYTHONPATH=src:scripts`, with one
BLAS/OpenMP thread. For a new versioned output directory, execute the main
driver actions in order: `setup`, save the targeted pytest output to
`preflight_tests.log`, `freeze`, `audit`, `parity`, `run`, `envelope`, `fit`,
then `score`. Run reviewer actions `trial_mapping`, `neural`, `measurements`,
`aggregates`, `references`, `numerics`; finish with `characterize`, `figures`,
manual PNG/PDF review, `seal`, then a separate `postseal` process. Do not rerun
fixed-path producers over this completed directory. Set a new RUN/version and
freeze its recipe first; files are intentionally created exclusively.

[Execution/analysis driver](../scripts/biological_failure_localization_v1.py),
[independent reviewer](../scripts/review_biological_failure_localization_v1.py),
[characterization/figures/archive tools](../scripts/finish_biological_failure_localization_v1.py),
[all fly selectivities](../results/biological_failure_localization_v1/selectivity_summary.json),
[all waveform/transfer results](../results/biological_failure_localization_v1/transfer_summary.json),
[diagnostic conclusion](../results/biological_failure_localization_v1/diagnostic_conclusion.json).
The completed archive includes a dated progress snapshot and exact source/report
copies. Live progress and AGENTS.md remain outside its immutable index.

## Undergraduate explanation: what we wanted, did and learned

We want a model that detects small turns for reasons resembling the real fly's
brain. A detector can work on a computer without its simulated neurons behaving
like real neurons, so we compared the neural responses with published recordings.

The original model failed an important bIPS comparison. This time we checked the
data processing, several ways of measuring the responses, specific neural
pathways and an existing circuit containing additional inhibitory neurons. That
expanded circuit recovered the expected bIPS preference in these simulations.
Turning off the added neurons removed the improvement, giving us a concrete
mechanistic lead rather than only a better score.

The whole problem is not fixed: DNp15 still disagrees, some improvements depend
on how simulated activity is converted to the recorded signal, and these tests
do not demonstrate reliable biological detection of tiny turns. We now have a
more specific hypothesis to test, while preserving the working engineering
detector and every failed result. The purpose of this work is to identify what
the circuit needs, without making it look correct by adjusting it to known data.
