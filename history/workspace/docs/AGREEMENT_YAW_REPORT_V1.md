# A working neural/image hybrid for simulated small-turn onset, V1

2026-10-27. Prospective policy checkpoint `1ad23e1`; online/execution checkpoint
`1490058`. All original frontend, graph, neural parameters and earlier evidence
are preserved. The successful output is an external engineering readout.

**The hybrid passes every frozen endpoint and repeated-alarm capability gate
on the new c-room test set.** It detects 48/48, 47/48 and 40/48 +/-2-degree/s
turns at 5.5/11/16.5 mm/s by the 200-ms simulated response deadline. Every
detected turn has the correct direction. Endpoint straight alarms are 0/24 at
each speed; any rolling straight alarm occurs in 0/24, 0/24 and 2/24 rooms.
All 144 +/-5 turns are detected and correctly signed. Neither component alone
passes all the endpoint/rolling gates on these identical inputs.

This is a working capability in the tested simulated conditions. It is not
physiological validation, a population reliability guarantee, physical deployment
or a repair of the native neural circuit. Fast small-turn sensitivity is 83.3%,
not perfect, and two fast straight rooms still produce rolling alarms.

## What changed and why

The preceding [neural change study](NEURAL_CHANGE_READOUT_REPORT_V1.md)
recovered usable turn information but produced excessive straight-walking
alarms. Its neural and image branches made different mistakes. Here keep both
branches exactly unchanged and require them to agree before accepting a turn:

* Neural branch: the frozen DNp15 own-history change fit for the known walking
  speed. It uses current bilateral 100-ms mean rates minus their means 200 ms
  earlier. Its original coefficients, centers, scales and cutoffs remain fixed.
* Image branch: the frozen backward-current registered confidence-weighted
  geometric yaw estimator, averaged for 100 ms with its fixed 1-degree/s cutoff.

For same-sign estimates n and i, support is sign(n) times
min(abs(n)/neural_cutoff, abs(i)/1 degree/s). Opposing/zero signs give zero
support; unavailable inputs stay unavailable. A turn requires abs(support)>1.
Support is dimensionless, not an estimated physical yaw velocity. Both branches
use the same retinal images and are correlated computations, not independent
sensors. No scene, imposed yaw, onset label, depth or future image enters this
rule. Known speed remains an experimental condition, as in the old readouts.
[Protocol](AGREEMENT_YAW_PROTOCOL_V1.md),
[policy configuration](../configs/agreement_yaw_v1.json),
[portable frozen model](../configs/agreement_yaw_model_v1.json),
[agreement code](../src/male_optic_frontend/agreement_yaw_v1.py).

At any callback an accepted hybrid alarm must also be an alarm of both
components in that direction. This explains how isolated component errors are
rejected without assuming statistical independence. Requiring both can also
lose true turns, so sensitivity and alarms must be evaluated together.

## Development selection, then independent testing

The already examined p and w rooms are explicitly known development data.
Before new development scores, freeze confirmation counts 1/2/3/5 successive
same-sign support samples. Select the smallest count passing every endpoint
and rolling criterion separately in both sets, every speed and both magnitudes.
No branch is retrained, no cutoff or gain is adjusted, and no new neural or
physiological parameter is fitted.

The rule selects count **1**, the only passing candidate. Additional confirmation
loses enough turns to fail one or more gates. At +/-2, p-room detections are
48/47/45 of 48, with zero endpoint/rolling alarms; w-room detections are
48/46/39, with zero endpoint alarms and rolling alarms 0/0/1 of 24.
These are development results, not fresh validation.
[All four candidate results](../results/agreement_yaw_v1/analysis/development_curves.csv),
[selection](../results/agreement_yaw_v1/selection.json),
[independent selection audit](../results/agreement_yaw_v1/development_review.json).

After selection and numerical checks are frozen, generate 24 new c rooms with
seeds 202610278000--202610278023, disjoint from 212 prior distinct seeds.
The same textured-room/clutter generator produces 12 empty and 12 three-sphere
rooms. Each has 15 moving conditions (three speeds crossed with 0,+/-2,+/-5)
and one stationary control: **384 episodes**. Walking begins at 0.5 s and yaw
at 1.0 s. Frontend and neural state run continuously with no event reset.
[Seed audit](../results/agreement_yaw_v1/seed_audit.json),
[plans](../results/agreement_yaw_v1/plans.json),
[pre-test identities](../results/agreement_yaw_v1/before_test.json).

Retain original 1-degree retinal sampling, 2-mm height, 0.3-mm stereo baseline,
5-ms images, 10-ms inputs and 1-ms solver. Turn trials stop at 1.25 s; straight/
stationary controls at 1.8 s. This horizon choice was declared before new scores
to preserve full evidence within disk capacity. It leaves all primary inputs
through 1.2 s unchanged in definition and retains the original 80 straight
monitoring callbacks from 1.00 through 1.79 s. No maintained-turn claim beyond
250 ms follows from this experiment.

The unchanged bar at both +/-2 and +/-5, every speed, is >=80% detections,
>=80% raw-sign accuracy including undetected turns and <=10% observed endpoint
straight alarms: >=39/48 detections/signs and <=2/24 alarms. This study also
requires <=2/24 any-alarm rooms during repeated straight monitoring. Undefined
walking outputs fail. None occurred in the scored intervals.

## Fresh primary result

| Speed (mm/s) | +/-2 detected with correct direction | Raw direction correct | Endpoint alarms | Any rolling alarm | All gates |
|---|---:|---:|---:|---:|---|
| 5.5 | 48/48 | 48/48 | 0/24 | 0/24 | Pass |
| 11 | 47/48 | 48/48 | 0/24 | 0/24 | Pass |
| 16.5 | 40/48 | 47/48 | 0/24 | 2/24 | Pass |

All 48/48 +/-5 cases at each speed are detected and correctly signed. Straight
controls are shared between magnitudes, not additional independent trials.
Across speeds, 135/144 small turns are accepted, all correctly signed. Pooling
does not replace the per-speed gates or make repeated rooms independent.
[All 18 curves](../results/agreement_yaw_v1/analysis/curves.csv),
[all 1,152 trial/method rows](../results/agreement_yaw_v1/analysis/predictions.json),
[conclusion](../results/agreement_yaw_v1/analysis/conclusion.json).

![Fresh hybrid versus its unchanged components](../results/agreement_yaw_v1/figures/fresh_agreement.png)

[PDF](../results/agreement_yaw_v1/figures/fresh_agreement.pdf).
Coincident plotted traces are disclosed by the exact counts below.

Values in each cell are ordered by 5.5 / 11 / 16.5 mm/s:

| Method | +/-2 detections, of 48 | Endpoint alarms, of 24 | Any rolling alarm, of 24 |
|---|---|---|---|
| Neural change only | 48 / 48 / 42 | 4 / 1 / 4 | 15 / 14 / 23 |
| Image estimate only | 48 / 47 / 46 | 0 / 2 / 2 | 1 / 2 / 5 |
| **Hybrid agreement** | **48 / 47 / 40** | **0 / 0 / 0** | **0 / 0 / 2** |

The hybrid reduces repeated alarms while sacrificing six fast detections
relative to the image branch and two relative to the neural branch. This
controlled software comparison supports an effect of the agreement rule, not
biological circuit causality. Repeated-alarm counts mean rooms with any alarm
during the fixed 80 decisions; they are not per-callback probabilities or
independent counts of 80 trials.

## Remaining mistakes are retained

The missed medium-speed turn is c17 +2 (support 0.22241). Fast misses are c03
-2, c04 +2, c08 -2, c09 +2, c10 -2, c13 +2, c15 +2 and c17 +2. Support for the
last is zero because the component signs disagree; this is the one raw-sign
failure, not an accepted wrong-direction alarm. All nine small-turn misses
remain in the denominator and exported evidence.

Fast straight c03 alarms from 1.28--1.36 s with support approximately
1.001--1.098. Fast straight c17 alarms from 1.00--1.05 s with support
-1.802-- -1.069. These residual alarms are not corrected or relabeled. The
near-threshold c03 event and missed c03 -2 support -0.97950 emphasize that the
passing counts are finite-sampling observations, not a numerical margin bound
for every new scene. Error inspection is descriptive and does not alter rules.

## Numerical reproducibility and implementation checks

Six targeted tests pass: component-agreement rejection, confirmation/future
prefix, explicit unavailable inputs, arbitrary IEEE-bit lossless image reversal,
online/batch equality and invalid timestamps. The full independent development
audit reconstructs 518,400 support samples and all 48 candidate curves, including
the selected rule (maximum arithmetic discrepancy 3.47e-14; no near-threshold
checks in that development reconstruction).

Two known complete/prefix cases reproduce all shared retinal/source/neural/
reference arrays exactly with the new storage/horizon adapters. The adapters
reuse the unchanged renderer/frontend/network implementation. Full movies use
lossless float32 temporal XOR, byte shuffling and deflate compression; no pixels
are discarded or quantized further. Every source/neural/reference array,
timestamp, final state and creation receipt is retained.
[Known-case parity](../results/agreement_yaw_v1/parity_review.json).

All six predefined f00 spatial/temporal checks pass. Maximum hybrid support
change is 0.16215 against its fixed 0.2 normalized-margin criterion; neural/image
component changes are at most 0.15157/0.15662 degrees/s against 0.2. Decisions
are unchanged. Temporal refinement retains the readout's physical 100-Hz clock
by sampling the finer trajectory at common arrival times. Independent scalar
sums reproduce these comparisons. The inherited fixed-forcing solver check
passes separately, at maximum rate difference 1.98e-11. These three known
conditions give no uniform numerical bound over all c rooms or timestamps.
[Numerics](../results/agreement_yaw_v1/numerical_review.json),
[independent numerical arithmetic](../results/agreement_yaw_v1/numerical_arithmetic_review.json).

All 384 fresh simulations execute with zero failures in 692.50 s. Four fixed
fresh replays reproduce all 84 retained arrays exactly and the compressed
retinal payload bytes exactly. Replay overlaps part of the sweep; wall-clock
duration is not a throughput benchmark. The online monitor matches all 48,960
moving-episode callback samples (maximum support error 1.78e-15). A separate
label-free replay CLI reproduces the fixed c01 fast -2 output from the portable
model, without reading trial summaries or imposed movement labels.
[Execution](../results/agreement_yaw_v1/held_out_complete.json),
[replays](../results/agreement_yaw_v1/reproduction_review.json),
[online parity](../results/agreement_yaw_v1/online_review.json),
[portable-model/CLI review](../results/agreement_yaw_v1/portable_model_review.json).

The independent fresh-data audit passes: 146,880 component/hybrid scores,
53,280 reference weighted medians, all 18 count curves, 24 stationary neural
zero checks, 288 shared image/source/network/reference prefixes including full
neural state through yaw onset, and 24 independent NumPy image checks. Maximum
scalar score discrepancy is 2.67e-14. The PNG figure was visually inspected;
the matching PDF header/export was verified. These are numerical checks,
separate from biological validation.
[Independent fresh audit](../results/agreement_yaw_v1/analysis_review.json),
[figure review](../results/agreement_yaw_v1/figures_review.json).

## Scope of the working solution

The solution is a causal software detector of small imposed yaw onset during
already established, constant-speed simulated walking. It provides a usable
output while preserving the neural circuit. The standalone neural readout
still fails its reliability target; the biological mechanism and anatomical
gaps are unresolved. This hybrid is not evidence that flies compute this rule.

The test contains 24 new instances of one visual scene family, reused across
conditions. Passing observed <=10% alarm incidence is not a population guarantee:
even 0/24 has a descriptive 95% Wilson upper bound around 13.8%. Only 0.8 s of
repeated straight monitoring is tested per episode. Longer operation, changing
walking speed, smooth/randomized yaw onset, gait, neural/camera noise and real
recordings need separate evidence. The simulation does not infer movement
intention. Physiological comparison requires matched stimuli and measurement
models; no physiological validation is claimed.

The 200-ms deadline is simulated signal time, using arrivals through 1.19 s.
End-to-end wall-clock real-time performance, camera transfer, physical deployment
and autonomous motor control are not validated here. The portable CPU monitor
is implemented and tested; it requires 30 input samples to become ready and
rejects irregular timestamps. See the [usage guide](HYBRID_YAW_MONITOR_V1.md),
[online class](../src/male_optic_frontend/hybrid_yaw_monitor_v1.py),
[label-free CLI](../scripts/monitor_hybrid_yaw_v1.py).

## Reproduction and archive

Use a separate workspace with the frozen parent datasets and no new study
output; set `PYTHONPATH=src:scripts`, BLAS/OMP threads to 1 and a writable
`MPLCONFIGDIR`. Run development driver `prepare`, `development`; independent
reviewer `development`; fresh runner `prepare`, `parity`, `numerics`,
`freeze_test`, `run`, `analyze`, `replay`; reviewer `review`; finisher
`numeric_review`, `model_review`. Inspect figures before sealing. All writes
are exclusive; prior reports/artifacts remain unchanged.
[Development driver](../scripts/agreement_yaw_v1.py),
[fresh runner](../scripts/run_agreement_yaw_v1.py),
[independent reviewer](../scripts/review_agreement_yaw_v1.py),
[sealer](../scripts/finish_agreement_yaw_v1.py),
[completion](../results/agreement_yaw_v1/completion_v1/completion.json),
[index](../results/agreement_yaw_v1/completion_v1/artifact_index.json),
[post-exit integrity](../results/agreement_yaw_postseal_v1.json).

## Simple explanation: what we did, what we want and why

We wanted a detector that notices small turns without constantly sounding
false alarms while the fly walks straight. We made the neural estimate and
the image-motion estimate check each other: accept a turn only when both agree.
This passed our targets in new simulated environments, including repeated
false-alarm checks. It still misses some fast-walking small turns and makes
two fast-room false alarms. We now have a working engineering component for
the virtual fly; understanding and validating the biological circuit remains
a separate research goal.
