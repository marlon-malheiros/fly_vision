# One frozen negative-only calibration repair — 2026-11-02

The prior reserved-room test failed: +/-2 detections 48/48, 48/48, 46/48, but
fast straight alarms 5/24 exceed 2/24. Preserve that failure. Its post-hoc score
diagnostic shows an oracle feasible cutoff interval; that interval cannot choose
or validate a new cutoff. This last bounded follow-up of the current round uses
new negative-only calibration and a different untouched test population.

Exactly the same raw neural weights, input frontend, LPi graph, map, floor,
100-ms/200-ms causal history and 190-ms endpoint. No fit, sign change, feature
search, biological parameter change, image estimator or positive calibration
response is allowed. The new calibration design is informed by a previous test
failure; the new rt test outcomes must remain untouched until a cutoff freeze.

Before rendering, freeze the code/config, all seeds, worlds, geometry clearance,
input plans and model identities. Use the original A/M generator and dimensions/
sphere scheme. New calibration: 40 rc rooms, each with static and straight
walking at all three speeds (160 negative episodes, three seconds each).
New test: 24 rt rooms, same 384 zero/+/-2/+/-5/static conditions as the previous
test. Verify no seed overlap with existing scenes and no prior response outputs.
No outcome-based exclusion or replacement.

Choose the common cutoff using ONLY rc negative episode peaks over callbacks
100..299. For each speed/static group, take order k=ceil((n+1)*0.95) of n=40
sorted peaks, i.e. the 39th value/second largest, then take the maximum over four
groups. This fixed conservative 5% design target leaves headroom beneath the
unchanged 10% observed test-alarm allowance. It is not a claim of 95% biological
confidence or guaranteed conditional error. Do not choose a quantile, multiplier
or numerical cutoff using positives or the earlier oracle interval.

Freeze that cutoff. Then require preservation of all original w development
gates at this new cutoff (>=26/32 joint and >=13/16 per direction for both
magnitudes/all speeds, <=1/16 alarms), plus all 81 numerical decisions/score
gates. The neural scores are unchanged, so recompute the decision comparisons
from the preserved qualification features without rerunning numerics. If either
gate fails, stop before rt rendering; do not adjust the cutoff or quantile.

If gates pass, render/evaluate every rt condition once. Require >=39/48 joint
AND >=20/24 per direction for both yaw magnitudes at every speed, <=2/24 straight
episode alarms per speed and <=2/24 static alarms. One fixed cutoff. Verify
pre-onset rate/feature/score equality; replay the four preselected cases after
the complete test, and independently reproduce every score/peak/gate. Any test
failure ends this round: no additional recalibration, candidate, new test cohort
or encoder training. Do not turn the earlier failed test into a successful one.

Budget across new calibration, test and replays: <=6,000 observation CPU seconds,
four one-thread CPU workers, no GPU, <=1 GiB per-worker RSS, <=256 MiB outputs and
>=20 GiB free reserve. Estimate <=2,200 CPU seconds negative calibration and
<=3,000 test/replays; <=100 MiB compact output plus archive overhead. Preserve
in-flight overruns and stop; do not weaken scientific or resource rules. Stream
all images/full rates; retain compact features/scores and digests only.

This addresses an artificial decoder's false-alarm calibration. It changes no
neuron physiology and cannot establish a bIPS mechanism or biological validity.
Report all prior failures, the retrospective motivation, new calibration values,
fresh test counts, numerical evidence, costs and limitations separately.
