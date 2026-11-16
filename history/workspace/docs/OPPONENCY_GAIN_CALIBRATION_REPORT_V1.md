# Gain-only observation calibration after horizontal opponency, V1

2026-10-29. **A single calibration-only scale factor recovers much of the bIPS
waveform deficit, but does not consistently resolve DNp15.** No circuit,
frontend, stimulus, neural parameter, rectification or filter was changed.
The earlier LPi null-yaw mechanism improvement remains intact. No candidate
meets the new two-cohort amplitude-only diagnostic rule; previous sealed
advancement results are unchanged. This study is complete; biological validation
and small-turn detection remain unestablished.

## Question, split and frozen method

We asked whether the weaker responses after adding LPi were mainly a mismatch
between arbitrary model units and the units used by real recordings. We reused
the 32 sealed neural responses from [horizontal opponency V1](HORIZONTAL_OPPONENCY_REPORT_V1.md),
with no neural solves. The four copies are expanded control, recorded LPi,
LPi silent with identical enlarged normalization, and the explicitly artificial
functional subtraction diagnostic. Inputs remain two dot realizations and four
45 degree/s protocols, not new walking environments or small-yaw trials.

Primary bIPS/sytGC7f/axon/native uses four calibration animals and four test
animals; DNp15/GC6f/dendrite/WT uses four calibration and five test animals.
There are 18 calibration and 36 test summaries. The split audit finds no
overlapping animal IDs or source directories within either cohort. Same-date
DNp15 240205/2 and 240205/1 are distinct animals. All test recordings have been
previously inspected; strict training separation does not restore freshness.

We fitted one nonnegative, zero-offset gain per copy/cohort using only bilateral
calibration stimuli, equal total weight per animal, and the 1–13 s full window.
The original causal filters remain fixed: 0 and 0.4 s poles, signed for bIPS and
rectified for DNp15. The projection minimizes equal-animal mean squared error,
not mean per-fly skill. This distinction matters when response energies differ.
The expanded control was recalibrated identically. No per-side, per-stimulus,
per-test-animal, neural or time-constant adjustment was allowed.

Eight gains and 32 calibration leave-one-fly-out (LOFO) fits were frozen before
new test scoring. An independent filter/projection implementation reproduced
all 40 fits before test scoring. The methods Git freeze is
`0b7bbda`.
[Protocol](OPPONENCY_GAIN_CALIBRATION_PROTOCOL_V1.md),
[method freeze](../results/opponency_gain_calibration_v1/before_calibration.json),
[coefficient freeze](../results/opponency_gain_calibration_v1/before_test_scoring.json),
[split audit](../results/opponency_gain_calibration_v1/preflight_review.json).

## Coefficients and calibration sensitivity

| Copy | Cohort | Gain / inherited gain | Calibration LOFO range |
|---|---|---:|---:|
| Expanded control | bIPS | 2.89441 | 1.77664–3.52058 |
| Expanded control | DNp15 | 1.39454 | 0.87985–1.81027 |
| Recorded LPi | bIPS | 5.60988 | 3.49059–6.80744 |
| Recorded LPi | DNp15 | 2.46839 | 1.58949–3.23247 |
| LPi silent | bIPS | 4.60682 | 2.83493–5.60359 |
| LPi silent | DNp15 | 2.16612 | 1.37143–2.82149 |
| Functional diagnostic | bIPS | 4.61185 | 2.94004–5.54620 |
| Functional diagnostic | DNp15 | 2.24304 | 1.48884–2.94562 |

These are observation-unit multipliers, not synaptic conductances or measured
biological amplification. Each four-fly fit can move substantially when one
calibration animal is removed. Every omission is retained; none was selected
using test outcomes. [All coefficients](../results/opponency_gain_calibration_v1/observation_models.json),
[all training-only LOFO fits](../results/opponency_gain_calibration_v1/calibration_leave_one_fly_out.json).

## Known test recordings, all four protocols

Skill is 1 minus model MSE divided by zero-response MSE. Positive means better
than predicting zero under that observation mapping. Mean and median aggregate
per-fly skills; pooled skill divides equal-fly mean errors and therefore gives
larger-response animals more influence on the resulting ratio. It is not a
replacement primary metric or a measure of biological validation.

### bIPS/sytGC7f/axon/native: four test animals

| Copy | Mapping | Mean fly skill | Median fly skill | Pooled-error skill |
|---|---|---:|---:|---:|
| Expanded control | Original | +0.45738 | +0.49297 | +0.42556 |
| Expanded control | Gain calibrated | +0.51214 | +0.57823 | +0.54443 |
| Recorded LPi | Original | +0.32544 | +0.34536 | +0.30025 |
| Recorded LPi | Gain calibrated | +0.56804 | +0.63876 | +0.61951 |
| LPi silent | Original | +0.33880 | +0.36140 | +0.31213 |
| LPi silent | Gain calibrated | +0.53005 | +0.58994 | +0.56515 |
| Functional diagnostic | Original | +0.36961 | +0.39113 | +0.34590 |
| Functional diagnostic | Gain calibrated | +0.47258 | +0.53606 | +0.55205 |

Recorded LPi with gain calibration improves mean, median and pooled skill over
its own original mapping and over the equally recalibrated expanded control.
Its median/pooled point estimates pass this cohort's frozen diagnostic rule.
Three of four individual bIPS fly skills improve versus LPi's original mapping;
one worsens. The result is not a universal animal-level improvement.

### DNp15/GC6f/dendrite/WT: five test animals

| Copy | Mapping | Mean fly skill | Median fly skill | Pooled-error skill |
|---|---|---:|---:|---:|
| Expanded control | Original | -0.25730 | +0.34686 | +0.33117 |
| Expanded control | Gain calibrated | -0.87884 | +0.23618 | +0.33976 |
| Recorded LPi | Original | +0.09978 | +0.37853 | +0.27114 |
| Recorded LPi | Gain calibrated | -1.00259 | +0.34416 | +0.37541 |
| LPi silent | Original | +0.05253 | +0.36367 | +0.27251 |
| LPi silent | Gain calibrated | -0.92355 | +0.27709 | +0.34779 |
| Functional diagnostic | Original | +0.09060 | +0.45583 | +0.31604 |
| Functional diagnostic | Gain calibrated | -1.08138 | +0.39759 | +0.39752 |

For recorded LPi, pooled skill improves, including versus the recalibrated
expanded control. Median skill exceeds that control but declines relative to
LPi's own original mapping. Mean skill becomes more negative. Thus the complete
DNp15 amplitude-only rule fails. The same median-versus-own-transfer condition
fails for all four copies; further gain selection from these test results is
not justified.

| DNp15 animal | Original LPi gain | Calibrated LPi gain |
|---|---:|---:|
| 240119/1 | +0.41822 | +0.34416 |
| 240205/1 | +0.39208 | +0.65697 |
| 240212/2 | +0.22804 | +0.47241 |
| 240214/1 | +0.37853 | +0.21611 |
| 240221/1 | -0.91798 | -6.70261 |

The quiet animal remains in every primary result. Increasing the cohort-wide
gain makes its erroneous predicted response larger; its low zero-response
error also magnifies the negative skill ratio. Four of five DNp15 skills remain
positive. We did not exclude the quiet fly, adopt an animal-specific gain or
infer why it was quiet. Circuit/measurement mismatch, indicator/state variation
and individual differences remain possible explanations. A fit minimizing
calibration MSE need not improve test median or equal-fly mean skill.

## Paired uncertainty and decision

| LPi minus recalibrated expanded control | Median difference [interval] | Pooled difference [interval] |
|---|---:|---:|
| bIPS | +0.06053 [+0.00281, +0.11826] | +0.07507 [+0.00404, +0.11109] |
| DNp15 | +0.10798 [-0.88206, +0.10798] | +0.03565 [-0.05265, +0.08919] |

Intervals are paired-animal bootstrap 2.5–97.5 percentiles from 5,000 draws,
not fresh replication or multiple-comparison significance claims. They are
descriptive with only four or five animals. DNp15 intervals include zero;
its advantage over recalibrated control is uncertain. The LPi diagnostic rule
holds under 3/4 matched calibration-omission comparisons for bIPS and 1/4 for
DNp15. This sensitivity is additional evidence against declaring a stable
two-cohort amplitude-only repair. No omission coefficient is adopted.

[All aggregate/per-fly results](../results/opponency_gain_calibration_v1/summary.json),
[all paired intervals](../results/opponency_gain_calibration_v1/paired_bootstrap_comparisons.json),
[calibration sensitivity](../results/opponency_gain_calibration_v1/sensitivity_summary.json),
[frozen-rule decisions](../results/opponency_gain_calibration_v1/decision.json).

## What scaling can and cannot change

Positive scaling preserves trace signs, cosine shape, normalized ratios and
magnitude selectivity indices. It cannot change a network computation. All
144 test prediction identities and 108 selectivity rows were checked; 648
window cosines are invariant. LPi's existing raw null-yaw suppression and
bilateral responses are unchanged by construction. Its bIPS magnitude index
remains approximately +0.15382 versus observed +0.15599; DNp15 remains -0.64982
versus observed -0.26170. Scale calibration cannot repair that selectivity gap.
These are known-data indices, not detection accuracies or false-positive rates.

The result supports an observation-amplitude contribution to bIPS's earlier
waveform deficit. It does not establish that the biological circuit is correct,
that all remaining DNp15 error is a faulty computation, or that a particular
missing connection is responsible. A single shared observation gain is not a
complete repair under this protocol; it does not rule out all possible
measurement models. Enlarging the model after each known test failure would
need new constraints and a new protocol.

## Verification and preserved evidence

Four estimator tests pass: equal-animal weighting, nonnegative projection,
rejection of test data during fitting and rejection of zero prediction energy.
Independent arithmetic reproduces all 40 fits, all 432 full-trace metrics,
1,296 window metrics, 576 calibration-omission sensitivity trace metrics,
80 aggregate rows, 96 sensitivity aggregate rows and 16 paired-bootstrap
comparisons. The original 216 primary transfer metrics are reproduced from
the sealed parent. Fit maximum absolute arithmetic difference is below 1e-12;
score/window difference is below 2e-13; index difference is below 5e-16, under
the frozen 1e-10 absolute/relative tolerance.

There are zero new neural solves and no new solver-convergence claim. Parent
arrays, models and original frontend/graph/parameter freezes are hash-checked.
Three PNG/PDF pairs were checked and PNGs visually reviewed. No analysis action
or scientific criterion was revised after the new gains/test results. All
failures, if any, remain in the evidence directory; no neural experiment was
rerun to improve a score.

[Independent fit review](../results/opponency_gain_calibration_v1/fit_review.json),
[prediction and parent-parity review](../results/opponency_gain_calibration_v1/score_review.json),
[summary/bootstrap review](../results/opponency_gain_calibration_v1/summary_review.json),
[invariance review](../results/opponency_gain_calibration_v1/invariance_review.json),
[complete evidence directory](../results/opponency_gain_calibration_v1).

## Next decision and alternatives

Recommended next: seek a separately frozen independent voltage benchmark for
HS/H2 or DNp15, emphasizing preferred/null and rotation/translation ratios that
do not depend on a freely chosen scale. Audit whether published stimuli and
quantitative recordings or digitizable curves support a matched comparison;
state prior qualitative inspection, target uncertainty and unavailable data.
No such independent voltage dataset was scored in this study.

If usable independent recordings exist, freeze the candidate, matching stimuli,
measurement mapping and analysis before numeric target scoring. If raw traces
are unavailable but suitable figures exist, digitization with declared uncertainty
is an alternative. If neither supports comparison, document that limitation
and seek measured horizontal LPi/HS/H2 dynamics or receptor constraints instead
of another score-driven gain sweep. Missing electrical coupling, incomplete
surrounding circuitry, qualified uLPTCrn/H2rn identities and reporter/compartment/
behavioral-state variation remain unresolved. A new small-yaw walking experiment
is a separate functional generalization option with the LPi circuit explicitly
unvalidated; it cannot substitute for physiological evidence. No closed loop.

## Reproduction and undergraduate explanation

Code: [driver](../scripts/opponency_gain_calibration_v1.py),
[estimator](../src/male_optic_frontend/observation_gain_v1.py),
[analysis](../scripts/analyze_opponency_gain_calibration_v1.py),
[independent reviewer](../scripts/review_opponency_gain_calibration_v1.py),
[report/archive utility](../scripts/finish_opponency_gain_calibration_v1.py).
Use the existing sibling Python environment, `PYTHONPATH=src:scripts`,
`OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`. In a fresh versioned destination,
execute setup, estimator tests, preflight, freeze/Git checkpoint, fit, fit review,
score, summarize/invariants/figures, independent score/summary/invariant reviews,
report/review, source/progress checkpoint, seal, and postseal in a separate
process. Existing destinations intentionally refuse overwriting. All fit keys,
neural input hashes, saved predictions, masks/clocks and exact source snapshots
are preserved. The live progress report stays outside immutable indexing.

**What we wanted:** determine whether the remaining disagreement was mainly a
response-size problem, while preserving the circuit's new ability to suppress
the wrong turn direction. **What we did:** fitted one shared conversion factor
from separate calibration flies and tested it without changing neurons.
**What we learned:** this helps bIPS, but increasing DNp15's response helps some
animals and hurts others. A single volume adjustment does not solve the whole
problem. **Why it matters:** we can retain the LPi mechanism improvement and
stop treating response scaling as a complete solution. The next useful test
should bring independent physiological evidence, rather than more adjustment
to the same recordings.
