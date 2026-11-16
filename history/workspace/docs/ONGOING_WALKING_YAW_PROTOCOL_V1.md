# Small yaw onset during established forward walking, V1

Prospective open-loop experiment, authorized 2026-10-27. One question: do the
unchanged MaleCNS circuit/readouts detect a small yaw onset after forward walking
is established, compared with the fixed successful engineering reference?
Preserve all previous sealed code, graph, parameters and evidence.

## Fixed experiment

Start from equilibrium at t=0. Forward walking begins at 0.5 s, yaw at 1.0 s;
continue through 1.8 s with exact piecewise SE(2) integration. Forward body speed
is unchanged at the yaw event. Render both eyes from their separated centers
and headings; preserve the original 1-degree retinal grid, 2-mm height and
0.3-mm stereo baseline. The frontend, original network and engineering detector
run throughout the entire sequence, with no event reset or access to yaw/onset
labels. A prescribed perturbation is not an inference of movement intention.

Test 24 fresh seed-disjoint rooms in the previous scene family, balanced empty/
three-sphere geometry. Cross 5.5/11/16.5 mm/s with 0, +/-2, +/-5 degrees/s and
include a stationary episode per room (384 fresh episodes). +/-2 is the primary
small-turn question; +/-5 retains the prior sustained-capability control.
Generate seeds 202610275000--202610275023 only after a global scene-seed audit.

The **primary decision deadline is 200 ms after yaw onset**. Both systems use
the same response interval [1.10,1.20): ten samples at 100 Hz, through 1.19 s.
No image after 1.20 s enters those decisions. The reference is the frozen
backward_current 100-ms confidence-weighted registered readout, with cutoff
1 degree/s; no window, gain or other candidate is selected. Record [0.90,1.00)
pre-event responses and [1.10,1.80) 700-ms late responses as diagnostics.

## Frozen neural scoring and interpretation

Use the original functional HRC surrogate and intact original MaleCNS graph.
Read HS/H2/bIPS/DNp15 left/right mean rates from the saved trajectories. Apply
the 12 existing MaleCNS_original role/speed decoders and thresholds from
`sequential_small_turn_repairs_v1/calibration/route1_decoders.json`, unchanged.
The DNp15 readout is the primary neural capability measure; other groups are
predeclared secondary measures. There is no decoder training or new lesion.
The experiment supplies its known speed condition to the already speed-specific
readouts; this is not a speed-independent neural decoder.

Those legacy readouts were calibrated on longer, simultaneous-onset episodes.
Their frozen application to a short response window is an explicit transfer
test. Failure does not prove that no yaw information exists in the neural
population. Report both decoded behavior and raw bilateral trajectories.
Within-room comparisons with straight trajectories and opposite yaw signs
are descriptive response contrasts only; they are never inputs to inference
or a new baseline-subtracting classifier. Identify response changes without
calling a modeled lesion or response difference proof of biological causality.
Stationary controls check raw neural equilibrium and zero reference motion;
the speed-specific neural classifiers have no stationary calibration and are
explicitly unscored there, rather than assigned an arbitrary walking speed.

At each speed/magnitude retain >=80% detection, >=80% raw-sign accuracy,
<=10% observed straight alarms: >=39/48 detections, >=39/48 signs, <=2/24
alarms. Undefined outputs fail. Report joint correct-sign detections, pre-event
scores, late scores and all mistakes. Do not change the fixed cutoffs or
promote a diagnostic response contrast into the primary detector.

## Pre-outcome freeze and controls

Freeze all recipes, source/configuration identities, copied legacy readouts,
analysis rules and seeds before new simulation. Use 16 known f00 conditions
(15 moving and stationary) for software/numerical checks, not tuning. Three
separate simultaneous-onset f00 fast controls at yaw 0,-2,+2, stopping at
1.4 s, reproduce the old source/network and causal engineering traces.
Freeze the completed checks again before generating fresh-room images;
preserve failures and continue the fixed comparison without retuning.

Verify independent piecewise trajectory derivatives and position/heading
continuity at the yaw event, plus agreement with the old trajectory when
both onsets coincide. Verify all within-room image/source/neural/reference
prefixes are identical through yaw onset. Compare selected raw retinal frames
with independent NumPy rendering.

On the three f00 fast yaw 0,-2,+2 conditions, render a 0.5-degree retinal
control with physical frontend neighbor/pooling radii retained (2/6 steps),
and a halved-image/input-time control. Record decoded endpoint changes against
0.2 degree/s for each method. No failure is waived or used to retune. These
three controls do not establish a uniform numerical bound across all rooms.

Check neural solver refinement separately on identical source drives, keeping
the historical physical 1-ms input-transition ramp fixed while comparing
1-ms and 0.5-ms RK4. Compare the independent Python integration with primary
compiled output at <=1e-10 model-rate units. Halving the solver must not also
halve the physical ramp. Sampling and solver checks are separate gates.

Independently reconstruct endpoint features, decoder arithmetic/counts, all
descriptive response contrasts and predefined full-episode replay subsets.
Retain source drives, network trajectories/final states, complete unique
retinal images and engineering local evidence/timestamps for every case.

## Completion boundary

Produce numerical results, figures and a concise report including an
undergraduate explanation of what we did, what we want and why. Answer the
fixed question whether it is positive, negative or limited by transfer or
numerical issues. No speed optimization, threshold tuning, physiological
reconstruction, bIPS intervention or closed-loop controller is included.
Append dated progress, snapshot it before sealing and verify the immutable
index after writers exit. Keep live AGENTS.md and progress outside indexes.
