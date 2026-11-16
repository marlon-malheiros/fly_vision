# Small-turn round V1: fixed alternatives and stopping decisions

1 November 2026. Freeze executable sources, configuration, prior-input identities
and this protocol before fitting or producing responses. Prior reports remain
sealed. This is adaptive research after the earlier failed rounds; it is not an
independent replication of a prospectively fixed research program.

The primary target remains yaw +/-2 degrees/s during forward walking at
5.5/11/16.5 mm/s, scored at 1.19 s (yaw starts at 1.0 s). A candidate must attain
>=80% joint detection/correct direction, >=80% separately in each sign, and <=10%
straight/stationary episode alarms at every speed. Retain +/-5 controls. Secondary
1.49/1.99-s endpoints characterize a latency tradeoff and cannot pass the original
190-ms target. All readers are causal and receive neuronal activity only, without
true speed, pose, depth, scene, onset or same-room straight partners at inference.

## Existing circuit options

Reuse exact archived training and calibration observations; do not alter neural
parameters. MaleCNS uses all 24 p training and 16 w calibration rooms from the
previous population study. Native FlyVis uses its 12/6 rooms. These already
inspected rooms are development, even though train and calibration remain disjoint.
Fit only +/-2 turns and zero-yaw training trials; retain +/-5 solely for evaluation.
Negative callbacks cover [1,3) at 100 Hz; turns use the 1.19-s endpoint. Weight the
three sign classes equally and episodes equally within each class.

Execute four declared readers: (1) 45 individual downstream neural changes ->
three-class linear softmax; (2) spatial T4/T5 opponent ratios plus downstream
changes -> linear softmax; (3) spatial MaleCNS features -> nuisance-penalized ridge;
(4) full published-population features -> the same nuisance-penalized ridge.
For (2), rectify and combine T4/T5 ON/OFF rates, form horizontal and vertical opponent sums
divided by their local sum plus a floor of 0.1 times the training-only median
positive local energy. Use causal 100-ms level and 200-ms-lagged change of the
ratios, plus the existing downstream change. This changes observation only, not
the old frontend normalization already tested in earlier studies.

Softmax: standardized training-only features, float64 Adam, 600 steps, lr .003,
weight decay .001, seed 202611013000 plus fixed reader ordinal. Score P(+)-P(-).
Ridge: ordinary class-balanced mean squared error to sign(yaw), standardized
coefficient penalty .01, plus 10 times weighted squared zero-yaw predictions.
This predeclared hard-negative emphasis is not a neuronal parameter adjustment.

## Released reduced opponent circuit

Reproduce the released Ammer et al. 2023 Figure7a equations and fixed default
parameters. Source DOI: https://doi.gin.g-node.org/10.12751/g-node.7v3pe6/ .
The source is a vertical-motion T4/T5-LPi-VS model. Applying its motif along
horizontal image coordinates is an explicitly exploratory transfer, not an
anatomical horizontal HS/H2 reconstruction or newly measured physiology.
Do not label these output units HS, H2, bIPS or DNp15. No new electrical synapse,
conductance or anatomical connection is installed in MaleCNS.

Keep source temporal filters 50/250 ms, thresholds/DC, input offsets, gain .5 for
LPi->T4/T5 and gains 1 for the other source links, all neural taus 20 ms, and the
source 40/-20-mV conductance readout. Reproduce both intact and source-defined
feedback block (remove LPi->T4/T5 and reciprocal LPi links only). Use identical
images for these two model copies. First verify the implementation against literal
author functions; this is numerical reproduction, not a new recording comparison.

Render physically correct binocular movies using inherited eye centers and yaw/
translation poses, a regular 30x30 spherical retina at 6-degree centers, and 5x5
midpoint aperture integration. The retinal layout/horizontal motif transfer and
2.5-s first-image adaptation are declared modeling assumptions. Baseline subtraction
for the conductance output uses the final 100 adaptation samples; it never uses
future walking activity. Temporal step is
5 ms. Native 30x28 local drives pool into the source's 6x6 patches, including its
three-column final edge patch. Record the four recurrent neural populations and
the two global conductance outputs per eye, yielding 292 values. Use 100-ms level
and 200-ms-lagged change, 584 features. No image-flow estimator enters a reader.

Generate all 16 stationary/speed/yaw conditions in the same 24 p training and 16 w
calibration rooms. For each copy and each of the three declared latencies fit both
nuisance-penalized ridge and linear softmax, with the same fixed schedule as above.
These 12 reduced-model readers plus four existing-model readers are the complete
finite bank; report all of them. Fit each before scoring its calibration outputs.

## Decisions, controls and evidence

One cutoff per candidate is max(.5, maximum absolute zero-yaw calibration score)
over all monitoring callbacks. It uses no turn scores and no speed at inference.
Zero calibration alarms at this cutoff are true by construction. Inspect every
candidate's +/-2 and +/-5 outcome. No cutoff sweep or additional fitted repair is
authorized within V1. If none qualifies, preserve the fresh room reservation and
close this finite round. Failure does not prove absence of information or biological
impossibility. If any qualifies, select the earliest-latency qualifying candidate,
then highest worst-speed +/-2 correct rate, then protocol bank order on a tie;
freeze coefficients/cutoff before rendering 24 new seed-disjoint rooms. A later
candidate is only a separately labeled slower capability. Evaluate all 16 conditions.

Before a behavioral success claim, require all space/time/solver controls in known
f00/p00/p01 rooms, each speed by yaw0/+/-2: compare 9x9 aperture, 2.5-ms visual/neural
steps, and half neural steps with identical visual holds. Maximum score difference
<=.2 and unchanged endpoint and any-episode decisions are required in every case.
Keep failures. Verify literal-source recurrence/filter arithmetic, stationary and
causal-prefix behavior, training-only fits and prediction/count arithmetic using a
separate implementation. Pre-yaw turn/straight image prefixes must agree bitwise.
Record refinement outputs at equal physical state times, respecting the source
previous-input update convention. Neural response to a simple +/-2 canonical
stimulus is a functional control, not a physiological-validation claim.

Report the empirical signal/negative-score overlap, sign errors, latency effects
and training/calibration shift. A causal claim about the source feedback block is
limited to that model. Retain exact sources, failures and all outcomes. New output
budget is 240 MB, preserving old studies; stage reversible arrays in /tmp if needed.
Archive a dated progress snapshot before sealing and rehash in a separate process.

We want a neural system to notice a tiny turn while walking. This round tests a
published smaller circuit and readouts focused on tiny turns. We also ask whether
extra response time helps. Each failed option gives a specific stopping decision;
successful simulation alone cannot establish agreement with a real fly.
