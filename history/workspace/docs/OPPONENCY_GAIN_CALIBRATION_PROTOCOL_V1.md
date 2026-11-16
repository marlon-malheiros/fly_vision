# Scale-only observation calibration after horizontal opponency, V1

2026-10-29. Authorized task: determine whether the remaining response mismatch
can be reduced by recalibrating the conversion from model activity to recording
units, without changing any circuit. This is a bounded development test, not
another neural parameter search. Preserve every earlier acceptance rule and
sealed artifact. The previous LPi advancement failure remains a historical result.

## Fixed data and models

Reuse all 32 sealed neural responses from horizontal_opponency_v1: expanded
control, recorded LPi, same-graph LPi silent, and artificial functional opponent
diagnostic; eight shared 45 degree/s dot inputs per copy. No new simulation.
This study is not a 3D walking or small-turn threshold experiment.

Primary cohorts only: bIPS/sytGC7f/axon/native and DNp15/GC6f/dendrite/WT.
There are four calibration animals per cohort (10 and 8 summaries respectively),
four bIPS test animals (16 summaries), and five DNp15 test animals (20 summaries).
Use the inherited split and all animals, including low-response DNp15 240221/1.
Audit disjoint full fly IDs AND date/animal IDs within each cohort, source
directories, metadata, hashes, sample clocks and finite support. Animal 240205/2
is calibration; 240205/1 is test. Same date is not the same animal.

All these test recordings have previously been inspected. Training separation
is enforceable; freshness is not recoverable. Do not call this prospective
biological validation. No independent physiological data are acquired/scored in
this scale-only experiment. External voltage comparison is the next distinct
evidence stage, with availability and prior inspection stated honestly.

## Only fitted quantity

For each variant and primary cohort, hold the inherited rectification and two
filter poles fixed. bIPS: signed, poles 0 and 0.4 s. DNp15: rectified, poles
0 and 0.4 s. Average model cells by role/soma side, then average the two seeds,
then apply the same causal observation filter and interpolate to recorded time.

Fit ONE nonnegative absolute gain g with zero offset using calibration animals,
bilateral stimuli only, all sampled times 1–13 s inclusive. Each animal has equal
total weight; its summaries split that weight equally. Minimize weighted mean
square error in the measured baseline-SD units. The solution is the positive
projection g=max(0,sum(w*mean(x*y))/sum(w*mean(x*x))). A zero denominator is a
recorded identifiability failure, not an arbitrarily chosen gain. Do not fit
per-side, per-stimulus, per-test-fly or per-epoch gains. No new filtering,
rectification, offset, neural gain, synaptic strength or decoder fit.

Fit the expanded control in exactly the same way. Retain original fixed-transfer
mapping as a comparator for every copy. Eight full-calibration gains result.
Also fit 32 calibration leave-one-fly-out gains (four animals omitted for each
model/cohort); record held-out calibration error and gain ranges before test
scoring. These assess calibration sensitivity; never select an omission or gain
using test outcomes. Freeze all coefficients and training-key lists in a separate
manifest before computing the new test metrics.

## Frozen summaries and decisions

Score original-transfer and scale-calibrated predictions on every retained
calibration/test trace, with full-window and motion-window MSE. Aggregate per-fly
errors before computing skill (1-model_MSE/zero_MSE). Report mean fly skill,
median fly skill, pooled ratio of equal-fly mean errors, every fly, leave-one-test-
fly-out summaries and bilateral/unilateral/all-protocol summaries separately.
Do not exclude quiet animals or replace the previous primary metric.

Report first/second motion means, errors, cosines, signed peak-window contrasts
and magnitude selectivity indices. A strictly positive scalar cannot change a
model trace's sign, normalized shape, null/preferred ratio or magnitude index;
verify this explicitly. A fitted zero gain is degenerate and fails mechanistic
retention. Raw neural suppression and asymmetry remain identical by construction.

Primary comparison: LPi scale-calibrated versus equally scale-calibrated expanded
control, not only LPi calibrated versus old control transfer. The amplitude-only
hypothesis receives limited support for a cohort only if median AND pooled
all-protocol test skills improve or tie versus both its own transfer mapping and
the recalibrated expanded control. Record each component separately. For the
LPi candidate overall, both cohorts must meet this rule with positive fitted
gains; otherwise report a residual cohort-wide scale mismatch/shape/heterogeneity
limitation. This rule is a development diagnostic, not biological acceptance.
Report each other candidate under the same rule without selecting a winner.

For each comparison, bootstrap paired animals 5,000 times for mean-, median-
and pooled-skill differences, fixed RNG seed in config, 2.5–97.5 percentiles.
These are descriptive small-sample intervals, not independent replication or
multiple-comparison significance claims. Evaluate test summaries under all
calibration leave-one-out gains as a labeled sensitivity analysis. Compare each
candidate with the expanded-control fold omitting the same calibration animal;
also retain its unchanged transfer comparator. Do not adopt an omission or use
these repeated scores to optimize the fit.

## Verification, alternatives and archiving

Compile and unit-test new estimator before fitting. Verify parent seals and
strict split before freezing source/protocol/config/input hashes in Git.
Independently reimplement prediction averaging, the causal filter recurrence,
weighted projection, LOFO fits, errors, all aggregations, paired bootstraps,
per-motion metrics and invariant indices using different arithmetic. Reproduce
all original-transfer primary waveform metrics exactly within 1e-10 tolerance.
No new solver-convergence claim is required: there are zero new neural solves;
preserve parent numerical checks and verify unchanged arrays/hashes after exit.

If scale-only transfer improves fairly and robustly, freeze the resulting
observation mapping for independent physiological evidence. If it fails, do not
add more observation parameters to force the known test scores: seek matched
stimuli/independent voltage or horizontal LPi dynamics/receptor constraints.
New small-yaw simulations remain a functional generalization alternative with
the candidate explicitly unvalidated. No closed-loop locomotion.

Provide code, full numerical tables and predictions, figures, report with plain-
language explanation and explicit alternatives, dated progress, exact source
copies and progress snapshot, immutable index and independent post-exit receipt.
