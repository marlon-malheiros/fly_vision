# Reliability-weighted local-motion readout, V1

Frozen prospective engineering experiment, authorized 2026-10-26. Build on
[Sequential repairs V1](SEQUENTIAL_SMALL_TURN_REPAIRS_REPORT_V1.md). Preserve
every earlier source, frozen graph, parameter and indexed artifact.

## Question and single intervention

Does weighting ambiguous local image-motion estimates less strongly reduce
straight-walking false alarms without losing small-turn detection? This tests
an engineered spatial readout, not a biological T4/T5 or DNp15 repair.

Reproduce the existing matched local-velocity encoding: five centered images,
fourth-order spatial/temporal derivatives, fixed 5-degree LK window at 1-degree
pitch, the original determinant validity test, frozen standard-plaid conversion
coefficients, rectified duplicated ON/OFF channels, clipping, original T4/T5
locations and four-neighbor source-channel interpolation. Hold all of this fixed.

Primary comparison: `registered_uniform` versus `registered_confidence`. Both
calculate the same local yaw values and temporal mean. The old weights are
`te**2`; the new weights are `te**2 * det(M)/trace(M)**2`. Sample that confidence
bilinearly at the fixed common readout sites, before any median. Invalid LK
sites have zero confidence. No fitted exponent, floor, gain, threshold, site
selection, re-centering, or scene-specific straight partner. Confidence is an
extra image-derived conditioning cue, not measured neural reliability or a
calibrated noise variance. It does not undo clipping/interpolation errors.

Secondary fixed diagnostics: uniform/confidence-weighted lattice readouts on
the same sparse sites, and the unchanged dense confidence-weighted image
reference. These cannot replace the primary method after outcomes are seen.
All methods see identical binocular retinal movies. Inference receives images,
camera geometry, source coordinates and frozen standard-stimulus coefficients;
no simulator speed, depth, surface, yaw, trajectory or intended motion labels.
The renderer and later scoring necessarily use those labels, separately.

## Development, freeze and fresh test

Use the previous four known training rooms and 16 known straight-calibration
rooms (112 episodes) for implementation parity and descriptive development
results only. Fit no parameters. Verify original source drives and both old
spatial readouts against their sealed responses, and the dense image readout
against its sealed output. The inspected z rooms are not fresh test data and
are not used to select a candidate. Save code/config/protocol/helper and parent
evidence hashes before development; verify them and freeze again before any
new test movie is generated. No outcome-driven changes after either freeze.

Generate 24 fresh room seeds 202610273000--202610273023, after checking against
all prior scene inventories. Keep the same room/texture generative family and
balanced empty/three-sphere conditions as the previous study. This is
within-family generalization, not natural-scene or physical deployment.
Each room has one stationary episode and the 15 speed/yaw combinations:
5.5/11/16.5 mm/s crossed with 0, -2, +2, -5, +5 deg/s (384 total episodes).
Both eyes retain the original 0.3-mm baseline and exact SE(2) trajectories.

Render the required memoryless-LK window only: images from 0.69 through 1.40 s,
at 5 ms. Estimates are at 0.70, 0.71, ..., 1.39 s. This exactly matches the
previous scoring window without recomputing unrelated neural ODE trajectories.
Retain all unique float32 retinal images, their times/index, source-channel
drives, local yaw values, confidence/geometric weights, scores and receipts.
The centered derivative still uses 10 ms of future images, and the episode
score averages 0.7 s; causality/latency is a separate future experiment.

## Unchanged acceptance and statistical analysis

Average the 70 frame estimates per episode. An undefined estimate is a
failure, never silently imputed/dropped. Detect when absolute score >1 deg/s;
direction is the raw score sign. At each speed, require >=80% detection,
>=80% raw sign accuracy, <=10% observed straight false alarms at +/-2 and
sustained at +/-5 deg/s. With 24 rooms this means >=39/48 detected turns,
>=39/48 raw correct signs, <=2/24 alarms. Raw sign includes undetected turns.
Also report joint correct-sign detections, RMSE, stationary and per-room
errors, but do not promote diagnostic metrics to new acceptance rules.

Primary success requires all speeds/magnitudes and the predefined numerical
controls to pass. Report behavioral and numerical gates separately. Neither
an unchanged uniform comparator passing nor a successful image reference
establishes an improvement by the new primary method. Report paired-room
differences with 10,000 fixed-seed bootstrap draws and Wilson 95% intervals for
observed rates; these are descriptive, not evidence of population FPR <=10%.
No multiplicity-selected winner or post-test retuning. Regardless of outcome,
complete the report and preserve failures. Close this particular fixed recipe
if it fails; further optical/frontend hypotheses require a new version.

## Numerical and independent checks

1. Reproduce archived development source drives and old readouts at their
   exact timestamps; compare at <=1e-12 (source arrays exactly when possible).
2. Re-evaluate three known f00 fast-walking cases (0, -2, +2 deg/s) on the
   archived 0.5-degree retinal grid and 2.5-ms image/5-ms readout clocks.
   Require each episode score within 0.2 deg/s of its primary value. Retain
   failures; three controls are not a uniform accuracy guarantee.
3. Check local tensor conditioning with analytic flat/edge/2D-texture inputs;
   verify the confidence [0,0.25] range and weight scale invariance. Independently
   recompute weighted medians/counts from saved site evidence.
4. Check pure-forward/yaw geometric cancellation with independently sampled
   depths, binocular lever arms and finite differences of world landmarks.
   Compare compiled rendering with independent NumPy rendering at predefined
   times for three fresh fast cases. Rendering truth never enters inference.
5. Re-run four predefined fresh episodes in a separate replay directory and
   compare retained arrays. Preserve any mismatch rather than overwrite.

There is no neural ODE change or solver in this engineering readout. Previous
neural solver gate failures remain documented in the parent study; do not
reinterpret them or claim physiological validation from this computation.

## Deliverables and reporting

Versioned source/config/protocol, complete fresh-room numerical evidence,
paired comparison figures, numerical review, reproducibility receipt and a
technical report including an undergraduate explanation of what we did,
what we want, and why. Append progress, snapshot it before sealing, index the
study artifacts and verify the index after all writers exit. Live AGENTS.md
and PROJECT_PROGRESS_REPORT.md stay outside immutable indexes.
