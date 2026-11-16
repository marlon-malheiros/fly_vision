# T4c indicator comparison: restricted prediction criterion passes

2026-11-05. **The frozen rectified-linear mapping predicts the reserved calcium
population curve better than zero and a direction-independent reference.**
This is a restricted static measurement result, not biological validation of
our image-driven T4 frontend or MaleCNS circuit. It also fails to reproduce
negative calcium responses in four directions.

The [protocol](T4_OBSERVATION_TRANSFER_PROTOCOL_V1.md) and methods were frozen
at `09af160` before response transformation. Earlier work had inspected the
paper's qualitative rectification claim, source code and clocks, but not these
quantitative responses, gains or heldout scores. There was no model/observer
selection after test results. The squared map remains a diagnostic and cannot
replace the primary because of a preferred result.

## Data, independent split and measurement

The new source-admission study recovered Ammer2023 T4c axon-terminal data at
`db1f8089b697d1b19da1394ef94450bbec24f32b`. Use13 voltage-indicator and11 calcium
session files, grouped conservatively into9 and10 recording dates. Their
individual animal identities are not independently verified. Voltage and calcium
were measured in different cohorts; no cellwise pairing is claimed.

| Cohort | Development | Heldout |
|---|---|---|
| Voltage indicator | 9 sessions /6 dates | 4 sessions /3 dates |
| Calcium indicator | 8 sessions /7 dates | 3 sessions /3 dates |

The [split](../results/t4_observation_transfer_v1/partitions.json) was determined
only from salted date-label hashes. A date never crosses a partition. Sessions
are averaged within a date and dates weighted equally. All source sessions
remain included; none was excluded because of response sign or magnitude.

The shared processed clock has200 samples,79.36ms apart. Use the first eight
directions0,45,...,315deg; the ninth360deg row is an exact first-row copy in
all24 sessions and is not a ninth independent condition. Remove each session's
pre-motion[-1,0)s mean, then measure voltage-indicator[0,5)s and calcium[0,6)s.
These are defined averages for a5s dot-motion assay, not pointwise voltage/calcium
waveforms. Source-summary endpoint conventions are separately reproduced.

The voltage files are sign-corrected minus-ΔF/F ArcLight responses; calcium is
ΔF/F. Neither voltage-indicator units nor a fitted gain are millivolts. T4c is
the vertical-motion subtype. The gain must not be transferred into horizontal
T4a/b, MaleCNS state, synaptic weights or transmitter release.

## Frozen fits and heldout results

Primary `Ca = g × max(V_indicator,0)`; diagnostic
`Ca = g × max(V_indicator,0)^2`. Each has one development-only nonnegative
least-squares gain, zero intercept and no sign/angle/time adjustment. Gains were
serialized in the [calibration lock](../results/t4_observation_transfer_v1/calibration_lock.json)
before any heldout trace transformation.

| Quantity | Rectified linear, primary | Squared diagnostic |
|---|---:|---:|
| Frozen development gain | 32.507544 | 1037.498741 |
| Heldout RMSE, calcium ΔF/F units | 0.459288 | 0.477654 |
| Heldout skill versus zero | 0.730495 | 0.708510 |
| Heldout skill versus development scalar mean | 0.627874 | 0.597518 |
| 5th percentile of joint minimum bootstrap skills | 0.051865 | −0.730684 |
| Restricted frozen criterion | Pass | Fail |

Skill is `1−MSE/MSE_reference`, not classification accuracy. The primary reduces
mean-squared error by73.05% relative to zero and62.79% relative to the
direction-independent development reference. Those percentages describe the
heldout population curve, not the fraction of individual neurons predicted
correctly.

There are three heldout dates in each unpaired cohort. Enumerate all27
three-date resamples per cohort independently, giving729 joint resampled
comparisons per fixed map. Keep the gain frozen. The predeclared criterion
requires positive skills against both references and a positive5th percentile
of their joint minimum. The linear lower value0.051865 only narrowly exceeds
zero. With three date groups, this empirical-bootstrap screen cannot establish
precise population coverage or physiological equivalence.

![Heldout static measurement comparison](../results/t4_observation_transfer_v1/heldout_transfer.png)

The [decision](../results/t4_observation_transfer_v1/decision.json),
[eight-direction predictions and residuals](../results/t4_observation_transfer_v1/heldout_predictions.csv)
and all729 draws for each map retain both results. No gain was revised after
seeing the squared diagnostic's failure.

## What still fails and what cannot be inferred

The heldout calcium means at180/225/270/315deg are−0.1651/−0.4083/−0.2573/−0.1481.
The primary predicts+0.0828/0/+0.1895/+0.5501. Both rectified maps are
nonnegative and cannot reproduce these negative baseline-relative responses.
This [post-outcome descriptive polarity check](../results/t4_observation_transfer_v1/polarity_diagnostic_exploratory.json)
does not add or retroactively change a frozen pass rule. It shows why a global
positive skill must not be described as complete waveform or sign validation.
The sign values alone do not establish the biological source of inhibition or
rule out measurement variability.

The measurements are from different animals and may differ in tuning, baseline,
indicator kinetics and averaging. Thus the fit does not identify a unique
calcium-from-voltage transformation. It tests population predictability under
one shared stimulus family. It gives no membrane-mV calibration, independently
measured calcium time constant, absolute fluorescence baseline, frame-exact
random-dot reconstruction or validated image-to-neural dynamics.

The current frontend still outputs a modeled, bounded neural drive, which is a
different quantity from ArcLight fluorescence. Multiplying it by32.507544 would
be an unjustified transfer. No original model, graph, parameter or acceptance
criterion was changed. The old conditional bar failures remain failures; this
positive component result does not erase them, validate the complete circuit,
or newly establish2deg/s walking reliability. The four reserved C2/C3 flies were
not consumed.

## Independent numerical checks and reproducibility

Three focused tests pass. A separate scalar-loop reviewer independently
reconstructs192 matched-window session/direction means,216 original-author
summary endpoints, both gains, all1,458 joint bootstrap cases and the decision
bounds. Maximum source-summary discrepancy4.45e-16; maximum extraction/skill
discrepancy4.00e-15. All24 plotting closures are exactly reproduced. All121 files
in the two immediately preceding study indexes rehash unchanged. These checks
establish numerical consistency, not physiological validity.

Use the scientific Python environment with `PYTHONPATH=src` and
`OPENBLAS_NUM_THREADS=1`. Run `scripts/t4_observation_transfer_v1.py freeze`,
then `calibrate`, then `test`; run
`scripts/review_t4_observation_transfer_v1.py` and the `figure` stage in separate
processes. Use a temporary `MPLCONFIGDIR`. Existing outputs use exclusive
creation; reproduce in a new version/path rather than overwrite. Source URLs,
receipts and literal session order are retained by the
[admission study](T4_MATCHED_DATA_REPORT_V1.md). Figures/reports/methods/progress
copies are sealed after all writers exit, with a later verification process.
No neural solve, generated retinal movie or parameter sweep was needed.

## What we wanted, what we did, and why

We want a fly neural model that detects gentle turns and behaves like real
neurons. Before comparing its activity with calcium recordings, we need to
understand how electrical activity and calcium signals relate. We found a
separate dataset, learned one simple rule from development recordings and
tested it on reserved recording dates. It predicted the broad response pattern
better than simple references, but still missed negative responses.

This is a useful piece of evidence about measurement, not the completed fly
model. The next neural milestone needs a stimulus-matched dynamics test. One
concrete alternative is the documented Gruntman T4 voltage dataset, which avoids
calcium conversion; its raw individual protocol/identity mapping must first be
admitted. A baseline-aware calcium hypothesis is another possibility, but its
resting fluorescence/voltage constraints are missing and these T4c test dates
are now inspected development evidence for future revisions. Do not add a fitted
offset to make the already inspected negative responses pass.

Primary source: [Ammer et al.2023](https://www.nature.com/articles/s41593-023-01443-z)
and [pinned data/code](https://gin.g-node.org/gammer/Ammer_et_al_2023/src/db1f8089b697d1b19da1394ef94450bbec24f32b).
