# Neural readout repair during established walking, V1

Prospective recipe, 2026-10-27. The preceding onset experiment is sealed.
Its fixed legacy readout failed, but raw activity was direction dependent and
scene offsets varied. These observations motivate this new hypothesis; they
are not new independent evidence for it. No change to the frozen HRC frontend,
MaleCNS graph, neural parameters, rendering, ODE or old studies is allowed.

## One intervention and controls

Primary candidate: a supervised, external **DNp15 temporal-change readout**.
At every available time, take each side's mean activity in the last 100 ms and
subtract its own mean 200 ms earlier. At the primary 1.2-s deadline this is
[1.10,1.20) minus [0.90,1.00). These are the same trial's past observations,
not a matched straight trial. The feature has no onset/yaw-label input, reset,
motion estimate or image-confidence cue. It is a causal fixed sliding stencil.
This is a turn-onset readout, not necessarily a sustained-rotation detector.

Control: fit the same decoder to absolute bilateral activity in [1.10,1.20).
It isolates task-matched calibration from temporal subtraction. Apply legacy
absolute readouts unchanged and retain the frozen engineering reference. HS,
H2 and bIPS readouts use the same recipes as fixed secondary outcomes.
No selection of the best role, feature, window, threshold or regularizer after
outcomes. Success of a secondary method cannot replace the primary candidate.

Use the existing standardization and signed ridge regression (penalty 0.001,
unpenalized intercept). Train coefficients on p00--p07 from the completed onset
study, all five yaw values and all speeds, with a separate fit for each speed
and role. Set each threshold to the maximum absolute predicted straight score
in p08--p23 (16 rooms), exactly the historical calibration rule. Those p rooms
are now known development data; they are never described as fresh validation.
Preserve fitted coefficients, thresholds, normal equations, all development
predictions and error counts. No physiological or neural parameter is fitted.
The experiment supplies the known speed, as in the original readouts.

## Fresh test and frozen targets

After fitting and freezing all readouts, generate images in 24 new seed-disjoint w rooms
(202610277000--202610277023), from the same balanced empty/three-sphere family.
Cross 5.5/11/16.5 mm/s with 0,+/-2,+/-5 degrees/s and include stationary controls:
384 episodes. Walk starts at 0.5 s; yaw starts at 1.0 s; run through 1.8 s.
No neural or frontend state reset. Reuse the exact simulation implementation
and physical/numerical parameters of the completed onset study. All decoders
and the engineering reference receive the same images/trajectories per trial.
Retain full retina, source, network and engineering arrays and receipts.

For each speed, at +/-2 and +/-5, keep >=80% detections, >=80% raw direction
accuracy including undetected turns, <=10% observed straight alarms. With
24 rooms, require >=39/48 detections and raw signs and <=2/24 alarms. Score
only samples before the common 1.2-s deadline. Report joint correct detections
and all undefined outputs as failures. Stationary neural trajectories are
checked directly, not assigned an arbitrary speed-specific classifier.

Report pre-event and late endpoint scores and any rolling straight alarm from
1.0 through 1.8 s as fixed diagnostics. The latter <=10% operational check is
reported separately and cannot be hidden by endpoint success. No sustained-yaw
claim follows from a transient change readout; no onset labels enter features.

## Numerical and independent checks

First test causal future-prefix invariance, exact sample windows, constant
offset cancellation and step response with synthetic inputs. Independently
reconstruct regression with an augmented least-squares system, calibration
maxima and scalar predictions. Check no room/seed crosses splits.

Use the three already sealed f00 fast yaw 0,-2,+2 controls: compare primary,
0.5-degree spatial sampling, and halved image/input time sampling using frozen
new coefficients. Keep the previous 0.2-degree/s score criterion. Preserve all
failures and do not tune around them. These controls and the preceding passing
solver-convergence check are finite-case numerical checks, not physiology.
Freeze again before any w-room image generation, even if controls fail.

Independently reconstruct fresh features with explicit time/cell scalar sums,
scores, counts and rolling decisions. Compare fixed fresh image samples with
the independent NumPy renderer and verify shared prefixes/full state through
yaw onset. Reproduce four fixed episodes exactly: w00 fast straight, w01 fast
-2, w02 slow +2, w03 medium +5. Inspect figures, preserve all failures, snapshot
progress, seal and verify after writers exit. Live progress and AGENTS.md stay
outside immutable indexes.

## Stop rule and interpretation

Execute this single frozen experiment and report its outcome. Do not add
nonlinear classifiers, further windows, new circuit wiring or a controller
in response to failure. If the readout works, it is an engineering decoding
repair of a frozen simulated representation, not a physiological mechanism or
proof of biological circuit sufficiency. If it fails, report that this specific
readout repair did not solve the target, without claiming no neural information.
Do not claim uniform convergence or biological validity from simulated scores.
