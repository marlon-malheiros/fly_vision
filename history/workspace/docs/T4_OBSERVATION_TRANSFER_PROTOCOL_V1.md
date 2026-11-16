# Prospective T4c voltage-indicator to calcium population transfer V1

2026-11-05. This finite experiment addresses one newly supported part of the
user's goal: constrain a measurement comparison before neural changes. The
source-admission audit recovered pinned Ammer2023 T4c axon-terminal mean traces,
processed relative timestamps, source filename order and the published analysis.
Only metadata, clocks and code-cell source have been inspected. Notebook outputs,
response amplitudes and quantitative tuning/gains remain uninspected. Qualitative
paper statements about rectification are known. All old neural models, outcomes
and four reserved C2/C3 flies are preserved.

**Scope:** predict static calcium direction-response means from voltage-indicator
direction-response means in the same cell class and stimulus family, across
independent recording cohorts. There are13 voltage and11 calcium session files;
conservatively group sessions recorded on the same day (9 and10 date groups).
Dates/session labels do not independently verify fly identity. This is neither
simultaneous voltage/calcium calibration nor image-to-T4 model validation. T4c
is vertical; its fitted scale must not be injected into horizontal T4a/b,
MaleCNS neural states, mV, release or synaptic conductances.

## Fixed acquisition, split and measurement

Source: `gammer/Ammer_et_al_2023` at
`db1f8089b697d1b19da1394ef94450bbec24f32b`, Figure1/SplitT4c_ArcLight and
ExtendedDataFig2/Calcium_analysis/T4c_SplitT4c/Dot_motion. Use all source-listed
axon session files in literal notebook order. No response-based exclusion or
post-hoc correction of recording signs. Source ArcLight files use a depolarizing
positive, minus-dF/F convention, as shown by the author plotting label. Calcium
is dF/F; these are indicator units, not millivolts. Never execute the notebooks.

Before response transformation, hash source/date metadata and sort each cohort's
date groups by SHA256(config salt + '|' + date). First three groups are holdout,
all others development. Same date never crosses a split. Cohorts have disjoint
date labels; assert this. Retain source session labels and date uncertainty.
Only load development response arrays for calibration. Freeze fitted gains and
predictions contract before transforming any heldout file.

Use supplied200-sample relative clocks, dt0.07936s, and first eight directions
0,45,...,315deg. The ninth0/360-degree alias does not count twice; report whether
it is numerically copied. Subtract each session/direction's mean over[-1,0)s.
Average voltage-indicator response over[0,5)s and calcium over[0,6)s, matching
the paper's voltage-period / calcium-period-plus1s measurement conventions for
the5s dot stimulus. Actual projector frames, random-dot seeds and raw trial
triggers are unavailable here. Published source summary windows differ from
those primary windows; preserve and verify the original summary calculation
separately, without silently adopting its endpoint indexes.

Average sessions within each date, then dates equally; population curves are
unpaired across indicators. This avoids pretending to have13 paired cells or
treating repeat sessions as independent verified animals.

## Frozen candidate and decision

Primary static mapping: `Ca = g * max(V_indicator, 0)`, g>=0. Diagnostic fixed
mapping: `Ca = g * max(V_indicator, 0)^2`. For each, fit exactly one nonnegative
gain by least squares on the eight development population means. No intercept,
threshold, sign reversal, angle rotation, time shift, exponent search, calcium
time-constant fit or neural parameter fit. The linear map is primary; do not
select the diagnostic if it performs better after testing.

Compare frozen predictions on the independent heldout voltage/calcium population
means with zero and the development calcium scalar grand mean (direction-blind
reference). Define skill=1−MSE/MSE_reference; zero denominators are explicit
failures, not discarded animals. Report RMSE, all eight residuals and gain.

With three heldout dates in each cohort, enumerate all27 possible3-date bootstrap
resamples for each cohort independently:729 joint population comparisons. Keep
g frozen. For each joint resample, compute both skills and their minimum. The
restricted primary criterion requires positive development gain, positive mean
skills versus both references, and the5th percentile of the729 joint minimum
skills >0. This is a predeclared provisional predictive criterion, not a
physiological equivalence margin or proof that the indicators' relationship is
identified. Three date groups per cohort give limited uncertainty information;
eight directions are correlated conditions, not eight independent animals.

If both development gains are zero, stop before heldout transformation. Otherwise
execute the two fixed maps once and report all failures. Do not fit gains to the
test or reinterpret an empirical bootstrap interval as whole-circuit validation.
Even a passing restricted result cannot identify calcium kinetics, membrane mV
or a physiological transfer to our current image-driven neural circuit.

## Verification and resource limits

Three focused checks: known rectifying gain, exact bootstrap/reference behavior,
and split/equal-date weighting with a deliberate repeated-session imbalance.
Independent process reconstructs raw means and gains by scalar loops, predictions
and all729 bootstrap results without production fit/summary functions. Reconstruct
published source summary means from archived trace files and original endpoint
indexes to verify identity/column order; record discrepancies as failures.
All inputs must rehash before/after; previous studies' retained-file indexes
must remain unchanged. Preserve any implementation exception and correct in a
new version if needed. One worker,120CPU seconds,8MiB new output and20GiB reserve.
No model sweep, neural solve, images, movies, closed-loop control or new walking
claim. Save reports, figures, dated progress and method copies before sealing;
verify after the sealer exits.
