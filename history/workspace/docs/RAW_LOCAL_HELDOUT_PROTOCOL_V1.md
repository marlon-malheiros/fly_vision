# Frozen raw-local neural decoder: reserved-room test V1 — 2026-11-02

This conditional test may prepare only after the unchanged raw-local candidate
passes full calibration AND all 81 spatial/temporal/solver comparisons in
`results/raw_local_qualification_v1`. It does not access reserved room metadata
or outcomes until those gates pass. That control was nominated retrospectively
after the negative local-normalization pilot; the new room responses, unlike
development/calibration, must remain uninspected until this model/test freeze.

Use all 24 already-reserved st00–st23 environments from the completed small-turn
round, without selecting rooms by geometry or response. Verify reserved world
and scene hashes against their sealed index and confirm no existing st neural
or image outputs, no prior non-reservation seed overlap and no earlier outcomes.
If freshness or physical eye clearance fails, record the issue and stop; do not
silently replace rooms. Their generator is the existing A/M textured 3D room
family with specified optional spheres, not an unfamiliar real-world domain.

Freeze this protocol, config, execution/feature/observer/renderer source and
binary identities, actual room files, geometry/seed audit, all 384 conditions,
the exact pilot raw model, training floor, neuron map, and full-calibration
cutoff before rendering. No new training, threshold choice, sign adjustment,
time window or feature selection. The true speed, scene, yaw, depth, onset
clock and image-motion estimator are absent from readout inference.

For each room: one stationary control and all combinations of forward speed
5.5/11/16.5 mm/s and yaw 0,+/-2,+/-5 deg/s. Forward walking is ongoing before
yaw onset at one second. Use the unchanged 1-degree binocular renderer/frontend,
200-Hz image/100-Hz source clocks, frozen 1-ms solver with its 1-ms forcing
ramp, and 100-Hz actual neural rates. Store compact raw features/scores and
source/image digests; do not retain movies or full neural timecourses.

Positive endpoint is callback 119 (190 ms after yaw onset). Straight/static
controls monitor ALL callbacks 100..299. Apply the single fixed cutoff to every
condition. At BOTH magnitudes and EACH speed require >=39/48 joint detections
AND >=20/24 in EACH direction; require <=2/24 straight episode alarms per speed
and <=2/24 static alarms. Report raw signs as well as thresholded detections.
Both direction requirements together imply at least 40/48, so a 39/48 result
cannot pass the directional gates. No thresholds or exclusion criteria change
after inspecting test responses. A failure ends this candidate's qualification;
do not select another candidate on the same test rooms.

Verify identical pre-onset rate/feature/score prefixes for matching trajectories.
Replay the four config-listed cases with identical input/feature/score digests
after testing; save comparison receipts without overwriting primary outputs.
Independently recompute all 384 scores/endpoints/episode peaks/gates using stored
features and literal window checks on one preselected end-to-end replay.
This checks reproducibility/arithmetic, not physiology or an independent model
fit. Frozen source/model/map/cutoff hashes must remain unchanged.

Budget: four one-thread CPU workers, no GPU, <=3,600 aggregate new observation
CPU seconds including replay, <=1 GiB peak worker RSS, <=256 MiB persistent study
output, >=20 GiB free disk. Measured primary-profile costs suggest <=3,200 CPU
seconds for 384 tests plus four replays and <=60 MiB compact data/metadata plus
<=40 MiB reports/archive. Complete in-flight jobs after a detected limit, record
any overrun and stop; never relax the limit or claim a complete test from a subset.

A finite benchmark pass would support neural-only decoding in these noiseless
simulations, with an explicitly task-trained artificial readout. Report errors
and room-level sample sizes; observed count gates do not prove population
false-alarm probability <=10%. It would not establish a physiological small-yaw
threshold, a biological HS/H2/bIPS/DNp15 computation, realistic sensor noise,
robot performance, or closed-loop control. No such claims are acceptance items.
Preserve failures and all prior sealed evidence. Keep dated progress snapshots
inside completion archives and live AGENTS/progress outside their indices.
