# Image-sampling diagnostic V1

Prepared 2026-10-24, America/Belem, before the new direct-ray/full-movie outcomes.
Existing sampling failures have already been inspected. This is a targeted
follow-up on known rooms, not blind biological or new-environment validation.

## Fixed question and conditions

Determine how much the panorama-to-retina sampling step changes motion signals,
HS/H2/bIPS/DNp15 responses and the already calibrated yaw decisions. Preserve the
original intact circuit, receptor grid, physical motion, frontend, neural solver,
decoder coefficients and cutoffs. Use existing synthetic rooms s07 (box only)
and s12 (three spheres), selected for structural coverage rather than favorable
responses. Their original test membership is preserved; no fitting is performed.

Each room receives 5.5, 11 and 16.5 mm/s crossed with yaw 0, ±2, ±5 and ±20°/s,
plus a stationary observer: 22 inputs per room, 44 total. Run five image profiles
for each: 1°, 0.5°, 0.25°, 0.125° panorama pitch and direct rays at the unchanged
173×173 receptor coordinates in each eye. There are 220 neural trajectories.
Movement remains 0.5–1.5 s in a two-second episode, eye baseline 0.3 mm, frontend
5 ms, graph input/recording 10 ms and RK4 1 ms. Preserve source ordering and the
70-sample response window, indices 70–139 (0.70–1.39 s).

Direct rays use the same analytic world texture, poses, eye origins, float32
luminance and frozen renderer. They remove panorama interpolation. They are a
numerical reference for this point-sampled synthetic scene, not measured fly
optics, exposure integration or a spatial-convergence test of the receptor grid.
Neither temporal steps nor optical apertures are changed. No expanded graph,
lesion, neural noise, gain adjustment, classifier refit or motor control is added.

## Trace and comparison

Retain complete retinal movies for both eyes at every frame, all routed source
drives, pooled eight-channel motion traces, five motion-field/delay checkpoints,
all 14 output-cell trajectories, final full-network state and hashes. Full retinal
storage is about 21 GB; reserve at least 10 GB before starting a new profile.
Run at most three independent inputs concurrently with single-thread BLAS.
Direct profiles run first within each input; profile order is not a timing test.

Compare each panorama profile with direct rays and adjacent spatial profiles.
Record retinal RMS/max errors over all frames, eye-specific spatial maps and
the fraction of squared error in fixed elevation regions (<−5°, ±5°, >5°).
These regions are descriptive diagnostics, not causal interventions or selected
exclusions. Trace errors through pooled motion, routed input RMS, per-cell mean
responses, yaw-minus-straight contrasts, bilateral asymmetry and frozen scores.
Preserve all borderline cutoff cases and sign/detection changes.

## Engineering stability criteria and finite stopping rule

The following are numerical engineering checks, not biological acceptance rules.
For **both** finest panoramas (0.25° and 0.125°) against direct rays, require:

- Whole-movie retinal RMS error ≤0.005 luminance units.
- Routed-input RMS error ≤10% of direct-input RMS, with floor 1e−6.
- Every 14-cell response-window mean difference ≤10%, using reference magnitude
  floor 1e−5; every nonzero-yaw minus matched-straight contrast difference ≤10%,
  using reference contrast floor 1e−7. These inherit prior change-flag conventions.
- Every fixed class-score difference ≤0.1°/s, and identical categorical decisions.
  The score tolerance is 5% of the smallest tested yaw; it is not a measured
  sensory threshold. Also require these score/decision checks between the two
  finest panorama profiles.

Report each component separately and the conjunction across all planned cases.
Zero stationary source and output responses must hold to 1e−10. Do not discard
a case that fails a criterion or extend the resolution grid until it passes.
Stop after all 220 trajectories and the declared independent checks, reporting
any unmet gate. A failed gate still completes the diagnostic with a limitation.
This restricted yaw grid and two-room sample cannot re-estimate the original
80% detection/80% direction/10% false-alarm threshold across all larger magnitudes;
report diagnostic counts only, preserving the original detector and its rules.

## Validation, provenance and reporting

Before freezing main execution, verify selected original source/graph/decoder
files against predecessor indexes. A preflight must reproduce the known s01,
16.5 mm/s, +20°/s legacy drive and retinal checkpoints exactly, and original
output trajectories within 1e−10. Check selected direct luminances against the
independent NumPy raycaster (≤1e−7). No main condition enters this preflight.

Independently recalculate retained image errors, scores, decisions and stability
flags; replay a fixed direct case with the original Python neural equations and
check ≤1e−10; replay one direct movie through the original offline frontend and
check drive ≤1e−7. These checks validate implementations, not physiology.
Freeze source/configuration/analysis hashes before main execution. Preserve
failures and incomplete output without overwriting. Append progress, provide
figures, complete tables and a concise report with an undergraduate explanation.
Save a dated progress snapshot before sealing this separate study.
