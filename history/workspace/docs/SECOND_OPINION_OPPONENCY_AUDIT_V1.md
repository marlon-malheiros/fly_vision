# Second-opinion audit: statistics, motion opponency and LPi coverage

27 October 2026. Retrospective assessment of the user's external critique.
**The feedback changes the recommended next step: prioritize a source-constrained
horizontal LPi/opponency reconstruction audit on development data.** The critique's
statistics and response-polarity observations are useful. Its claim of an exact,
uniquely established biophysical cause and its LPi3–4/4–3 mapping are too strong.
No neural simulation, model alteration, parameter fit or new validation was
performed in this audit. Earlier sealed reports remain intact.

## Confirmed statistical correction

The previous full-waveform mean was numerically correct but incomplete as a
description of the five primary DNp15 test flies. For expanded-intact, inherited
observation transfer, all four protocols, 1–13 s:

| Fly | Fixed skill | Zero-response MSE | Model MSE |
|---|---:|---:|---:|
| 240119 / 1 | +0.37384 | 1.33989 | 0.83899 |
| 240205 / 1 | +0.49610 | 2.95887 | 1.49097 |
| 240212 / 2 | +0.34441 | 10.19048 | 6.68073 |
| 240214 / 1 | +0.34686 | 1.36666 | 0.89262 |
| 240221 / 1 | −2.84770 | 0.22068 | 0.84912 |

Four of five values are positive. Mean skill is −0.25730; median is **+0.34686**.
The ratio of equal-fly mean errors, `1 - sum(model MSE)/sum(zero MSE)`, is
**+0.33117**. This statistic differs from the mean of per-fly ratios: it gives
greater influence to flies with larger recorded signal energy. Neither statistic
replaces the predeclared primary mean retrospectively.

The low-response fly's model MSE is similar to two responsive flies, but its
small denominator makes its skill strongly negative. Removing it would give
+0.39030, shown as a leave-one-out sensitivity result rather than a new primary
cohort. No predeclared exclusion rule rejected that animal. A valid quiet animal
is also a real prediction challenge; its response cannot simply be discarded as
an artifact. All five leave-one-out analyses are retained.

The secondary DNp15/GC7f calibration cohort shows the analogous sensitivity:
skills +0.53433, +0.68776, +0.56130 and −10.85971; mean −2.26908, median +0.54781,
ratio of equal-fly mean errors +0.50564. Cohorts remain separate. The previous
report should have highlighted these distributions and the contrast between
typical-animal performance and population-mean performance.

[All per-fly errors and sensitivity summaries](../results/second_opinion_opponency_audit_v1/per_fly_sensitivity.json).

## Confirmed polarity problem; cause remains a hypothesis

The saved traces support the critique's main response-pattern observation. In
the four responsive primary test flies, preferred-yaw epoch cosines are about
**0.964–0.982**. Three right-soma flies have negative observed mean activity in
the other yaw epoch, whereas the model predicts approximately +0.394; their
null-epoch cosines are −0.533 to −0.725. The responsive left-soma fly has a
near-zero/negative first yaw epoch, versus a positive prediction near +0.447.
The first translation epoch is also overpredicted, with near-zero/negative
recorded means versus model means around +1.03 to +1.12 in these four flies.

This localizes a directional/polarity mismatch more specifically than a generic
failure to reproduce temporal dynamics. A high preferred-direction cosine is
shape agreement, not amplitude agreement or full physiological validation.
The primary DNp15 observation mapping is rectified before filtering, so negative
recorded deviations cannot by themselves identify the sign of the underlying
model voltage. Recorded baseline noise and calcium nonlinearities remain relevant.

Missing opposing-motion inhibition is therefore a well-motivated leading
mechanistic hypothesis. The existing equations already allow negative states
and inhibitory feedback; nonnegative retinal drive alone does not prove a
mathematical inability to hyperpolarize under every possible input. Nor have
the current arrays experimentally identified LPi loss as the unique biological
cause. A controlled reconstruction is needed to test whether those recorded
connections remove the extra positive responses while preserving preferred
responses and other conditions.

The claim that every neuron has |x|<0.03 is false even at the saved checkpoints:
maxima include T4/T5 0.13929, HS 0.04029 and H2 0.03167. The downstream circuit is
nevertheless close to the linear region of tanh in these cases. Small activity
does not imply weak recurrent interaction; feedback strength also depends on
the weights and network dynamics.

## Current accounting and anatomical asymmetry

The quoted same-side weight sums are reproduced: uLPTCrn→bIPS L −0.15804,
R −0.28261; H2rn→bIPS L −0.20163, R −0.16848. Counts are eight left and nine
right uLPTCrn-family candidates. These asymmetries contribute plausible context
for different responses; weight sums are not effective gains or proof that no
other interaction matters. Both male family assignments remain qualified
connectomic homologies, including the uLPTCrn candidates.

In the critique's seed-1, bIPS-L yaw example, H2rn silencing changes the rate
contrast by +0.00182023. The direct H2rn current change is +0.00193238 (106.16%
of that rate change), uLPTCrn current change −0.00011930 (−6.55%), with much
smaller HS/H2/bIPS current changes. Across all eight bIPS seed/side/yaw-or-
translation comparisons, the direct-current fraction is **105.8–127.3%** and
the uLPTCrn term opposes it by **6.2–28.1%**. Direct current is the dominant
accounted term in these saved cases.

These are differences between two full trajectories, not separate direct-edge
and indirect-edge interventions. Currents and output-rate contrasts are also
not algebraically identical: the example has a residual about −7.01×10⁻⁶ due
to dynamical/state-to-rate terms. Thus the critique's decomposition is a useful
approximate accounting, not an exact causal mediation or path-isolated result.
Still, it makes another broad pathway-simulation sweep a lower priority. The
existing currents should have been examined before recommending that sweep.

[All current accounting](../results/second_opinion_opponency_audit_v1/h2rn_current_accounting.json),
[weight sums](../results/second_opinion_opponency_audit_v1/group_weight_sums.csv),
[saved-state bounds](../results/second_opinion_opponency_audit_v1/checkpoint_state_limits.json).

## LPi correction and new connectomic evidence

LPi3–4 and LPi4–3 in the cited experiments are the upward/downward, T4/T5c/d
and VS motion-opponent circuit. They cannot be substituted by name for horizontal
HS/H2 inhibitory partners. Horizontal LPi types and cross-dataset naming require
a separate audit. [Ammer et al. (2023)](https://www.nature.com/articles/s41593-023-01443-z),
[Matsliah et al. (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11446827/).

The raw MaleCNS annotation table has **755 LPi-labelled cells; none is selected
in the current expanded graph**. Its existing omitted-pathway ledger contains
strong horizontal candidate inputs. We then scanned the original **151,856,684
connection rows** for the six MaleCNS LPi12/LPi21 cells, retaining 159,854 incident
edges. All 21 relevant incoming edges represented in the earlier sealed ledger
match the raw counts exactly.

| Raw MaleCNS connection | Synapse count |
|---|---:|
| T4a → LPi12 | 53,256 |
| T5a → LPi12 | 54,541 |
| LPi12 → H2 | 4,279 |
| T4b → LPi21 | 55,493 |
| T5b → LPi21 | 63,041 |
| LPi21 → model HS population, including HST | 7,837 |

The four LPi12 and two LPi21 candidates have **GABA consensus predictions**,
with per-cell prediction confidence approximately 0.895–0.906. The blanket
description of the relevant horizontal LPi cells as glutamatergic is therefore
inappropriate for these MaleCNS annotations. Predictions are not receptor or
conductance measurements. Other LPi types, feedback partners and off-subtype
inputs also exist; the table is not a complete reconstruction.

MaleCNS `LPi12`/`LPi21` codes must not be confused with newer FlyWire numbering
such as `LPi14` or `LPi15`. Anatomical identity and subtype correspondence should
be documented explicitly. Strong counts make an evidence-based reconstruction
feasible to investigate; they do not establish its dynamics, sign at every
target, effective strength or success on the present response mismatch.

[Raw candidate edges](../results/second_opinion_opponency_audit_v1/raw_LPi12_LPi21_edges.csv),
[type-level counts](../results/second_opinion_opponency_audit_v1/raw_LPi_type_summary.csv),
[cell identity/NT ledger](../results/second_opinion_opponency_audit_v1/LPi_identities.json),
[raw-count cross-check](../results/second_opinion_opponency_audit_v1/raw_LPi_scan_review.json).

## Revised recommendation and alternatives

1. Complete the retrospective current/statistical correction using existing
   outputs; this audit does so without new simulations. Retain all animals and
   the old primary results, while presenting mean, median, pooled-error ratio,
   per-fly errors and leave-one-out sensitivity together.
2. Prioritize a separately versioned horizontal LPi/opponency reconstruction
   using verified MaleCNS identities and chemical edges. Freeze inputs, candidate
   membership, inherited-parameter assumptions and success/failure criteria before
   new outcomes. Include an added-LPi-silent control to separate normalization
   changes from transmitted inhibition. Test both preferred and null responses,
   both sides, and bIPS/DNp15 together on known development data. Do not tune a
   missing conductance or adopt a gain solely to obtain the expected response.
3. Then freeze the candidate circuits and external analysis before extracting or
   scoring independent quantitative targets. Suver et al. has already been read
   for qualitative findings in this project; calling the entire source untouched
   or fully blind would be inaccurate. Independent animals can still provide
   external evidence, with the inspection history and any uninspected numeric
   targets stated honestly. Include unchanged baselines in the external comparison.

If the anatomy or physiological constraints cannot support reconstruction,
the alternative is a clearly labeled functional opponency diagnostic followed
by an independently constrained measurement/physiology comparison. A direct-edge
cut study remains available for a narrow causal question inside the model, but
is not the most useful next broad experiment. No reconstruction or success claim
has been made by this feedback audit.

In undergraduate terms: the feedback points to a plausible missing response to
opposite-direction motion, and we found real candidate wiring for it. We should
test that wiring before doing more score optimization. The model also works
better for most recorded flies than the negative average alone suggested, while
its failure on the quiet fly still counts. These are reasons to revise the
next experiment and improve reporting, not reasons to declare the model fixed.
