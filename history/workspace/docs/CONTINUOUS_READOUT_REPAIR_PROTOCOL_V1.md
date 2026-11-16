# Continuous readout repair V1

2026-10-30. User authorizes iteration until a workable result and explicitly permits a clearly labeled neural/image hybrid. Preserve all parent circuits, frontend parameters, physiology results and sealed failures. This study changes external readout fitting/fusion only. No closed-loop control, biological-validation claim or invented connection/conductance.

## Scope and pass criteria

Detect yaw onset during constant 5.5, 11 and 16.5 mm/s simulated walking. Yaw is 0, ±2 and ±5 degrees/s. Walking begins at 0.5 s and yaw at 1 s. Neural and frontend states run continuously. The current/past-input monitor receives no true speed, yaw, onset label, scene ID, depth or matched control. Tested ability is onset detection, not sustained yaw estimation, movement intention, physical deployment or physiological validity.

Retain the existing criteria at every speed and both magnitudes: ≥80% detected, ≥80% raw-direction correct, ≥80% jointly detected/correct, ≥80% joint success for each signed direction, ≤10% straight endpoint alarms and ≤10% straight episodes with any alarm in [1,3) s. Stationary any-alarms must be ≤10%, with zero raw neural equilibrium. The primary endpoint remains 1.19 s (190 ms after onset). Integer boundaries use ceiling for successes and floor for alarms; undefined required outputs fail. Do not lower a requirement or remove a speed after results.

## Development and exposure

Every z00–z83 parent room is inspected development data now; none is fresh validation. Fit on z00–z47 and select on z48–z83, keeping room identities separate. Use only 0/±2/±5 episodes. A matched endpoint-training control uses the same rooms, features, targets and class weights as the first repair. The repair uses every 100-Hz straight/stationary sample in [1,3), instead of only sample 119. Turn positives use sample 119; there is no unsupported sustained-yaw labeling. Each negative episode has equal total weight regardless of its 200 correlated samples. Three direction classes (negative, zero, positive) have equal aggregate weight, with equal episodes within a class. Standardize from weighted training moments; multiply weights to the original episode count and keep ridge 0.001 and an unpenalized intercept. Fixed cutoff |score|>1; no threshold sweep.

Predeclared neural attempts, in increasing feature complexity: bilateral DNp15 change (2 features), bilateral DNp15 current mean plus change (4), HS/H2/bIPS/DNp15 group changes (8), and their means plus changes (16). Means use the current ten samples; change subtracts the ten samples 200 ms earlier. All four fits use identical training conditions and class weighting. The matched endpoint control and legacy frozen LPi DNp15 readout remain controls.

Allowed hybrid attempts require same-sign agreement between one neural score and the unchanged ten-sample causal image-yaw mean, with support sign(n)*min(|n|,|image|), otherwise zero. Both component cutoffs are 1. There is no supplied walking speed. Try the four repaired neural branches, then the matched endpoint control and legacy frozen pooled-speed LPi DNp15 branch. Image-only and neural-only results are retained. These are external engineering algorithms, not reconstructed biological readouts.

## Independent new development and final test

After methods freeze, generate 24 new development rooms and 60 final test rooms from guarded unused seeds beginning 202610301900. Each has three speeds × five yaw conditions plus stationary: 384 development and 960 final episodes. Same existing textured box/sphere family; alternate empty/cluttered rooms. Mirror complete room geometry/textures in a deterministic balanced pattern, so each split balances both clutter and lateral orientation. No response-driven scene replacement. Audit geometry/trajectory clearance before rendering. These are new instances, not natural-scene or new-family generalization.

Evaluate candidate priority on the known separated selection rooms and all 24 new development rooms; a workable development candidate must pass both. Prefer the simplest qualifying neural-only method, then the first qualifying hybrid in the declared order. If none qualifies, retain failures and add a separately frozen revision before another development attempt. No final images or responses may be inspected until one candidate, its coefficients, criteria and numerical checks are frozen. A failed final cohort becomes known development only in a new version; it must never be reused as a fresh final test.

Select a passing candidate before final execution; score all frozen controls on the identical final inputs without promoting a failed candidate using final outcomes. Final test requires ≥96/120 joint successes, ≥48/60 each direction and ≤6/60 alarms per required condition. Four preselected first-room conditions (stationary; slow -2; medium +2; fast straight) retain full lossless retinal movies and source/state evidence for deterministic replay. Every other case retains observable rates, reference, final/checkpoint states, recipes and image/source hashes; its movie is reproducible rather than all stored.

## Numerical and software validation

Use the existing known-room primary/spatial/temporal/solver profiles (27 conditions × four profiles) for candidate selection checks before final evaluation. Score differences must stay ≤0.2 in the candidate's score units at endpoints and across straight monitoring. Endpoint decisions and any-alarm episode outcomes must be unchanged. Retain individual callback differences as sensitivity; episode/endpoint rules are the declared numerical capability checks for this new study. Preserve the old study's stricter all-readout verdict unchanged. No coefficients or cutoffs are fitted on numerical-test outcomes.

Independently reconstruct weighted fits, window features, all scores/decisions/gates and room-bootstrap summaries. Verify label-free streaming/batch equality, future-prefix invariance, uniform clock checks, stationary behavior and four full deterministic replays. Numerical reproduction is separate from physiological validation. Record every failure/correction; archive source and dated progress before sealing and verify hashes after exit. The live progress and AGENTS.md remain outside immutable indexes.

## Stop and claim

A candidate passing the fresh final cohort and its declared numerical checks is a workable solution within these simulated conditions. If only a hybrid passes, explicitly retain neural-only failure and describe the image branch's contribution. No claim about native circuit repair, real flies, arbitrary onsets/speeds, noisy cameras or robotics follows. Stop tuning after the successful final test and report what worked, what failed, why and the remaining limits in undergraduate language.
