# Physical-target small-turn decision V4

25 October 2026. Continue implementation after a new explicit failure,
preserving V1/V2/V3 and every original criterion/result. V2's frozen neural
variants remain unreliable at±2°/s. V3's finer-sampled reference algorithms
pass their fixed numerical checks and recover the signs of all48signed
±2°/s cases at each speed for three methods. However, their maximum-straight-
calibration decision policy produces3–8false alarms in24rooms and fails
the original10%false-alarm rule. Thus V3 does not qualify as a reliable
detector under its declared policy. Its accurate continuous yaw estimates
and failed alarm policy must not be conflated.

The next revision changes **only an engineering decision rule**, with no
neural, image-estimator, spatial-resolution or physiological parameter fit.
The requested minimum target is2°/s. Given a physical-unit yaw estimate,
choose the nearest of the three equal-cost hypotheses {straight=0,
left=−2,right=+2}; prefer straight on a tie. This algebraically fixes the
boundary at1°/s. It is derived from the assignment's specified target,
not searched over data or fitted to neural responses. Its equal-cost
assumption is an engineering operating-point choice, not fly physiology.

This is a new prospective policy motivated by the observed V3 failure;
it does not retroactively repair V3. Previously examined sets are
development evidence. Freeze V4 before new test generation. Use24new
rooms x16conditions=384episodes, seeds202610253000onward, IDs w00–w23,
disjoint from V2/V3. Keep all four original/median image algorithms,
0.5°samples, original crop/windows, prescribed trajectories and brightness/
geometry assumptions unchanged. Reuse V3 numerical evidence exactly with
hashes; do not claim a new complete convergence sweep. Fresh-build replay
a predetermined subset.

Primary detection uses the fixed physical target and requires no walking-
speed value or calibration sample at inference. The image estimator still
assumes body-forward translation and yaw-only rotation. It receives no
actual speed/yaw/depth/pose labels or same-room zero-yaw partner. The
scene generator necessarily uses prescribed motion; scoring alone uses
its truth labels. Preserve the continuous estimates as the measurement.

Also apply V3's original frozen, speed-specific calibration cutoffs to
the identical new estimates as a secondary policy, without refitting.
Report both policies and all methods. This distinguishes a failed alarm
operating point from absent small-turn information, and avoids hiding the
old policy when introducing a new one. The primary fixed decision boundary
is distinct from the unchanged reliability acceptance criteria:
≥80%detection,≥80%raw-sign accuracy,≤10%observed straight false alarms,
with qualification also at±5°/s. At each speed24straight cases and48turn
cases per magnitude remain. A grid qualification at2°/s is not an inferred
threshold below2°/s.

Independently verify the nearest-hypothesis decision against squared
distance comparisons (including ties/undefined inputs); reconstruct all
means, decisions, cutoffs, counts, gates and Wilson straight-room intervals.
Room-bootstrap both signs together,10000draws,seed202610253337; retain
indices/draws. Preserve undefined estimates and all failures. Frozen V3
numerical gates must pass for a method to support a capability claim.

A numerically qualified primary policy meeting the2°/s rule at all three
speeds is an implemented finite engineering milestone. It is not a repaired
MaleCNS neural detector, biological validation, proof that the original1°
neural input contains sufficient information, physical robot validation
or closed-loop control. The stronger geometric prior, finer image sampling,
noiseless scenes and finite same-family room generalization remain explicit.
Do not claim formal statistical significance from a sequence of exploratory
revisions or biological causality from classification.

Produce a separate report, complete numerical evidence, figures, portable
CPU reproduction instructions and beginner what/we want/why explanation.
Version code, append progress, preserve every failed predecessor, save dated
progress copies and seal with live progress/AGENTS.md excluded.
