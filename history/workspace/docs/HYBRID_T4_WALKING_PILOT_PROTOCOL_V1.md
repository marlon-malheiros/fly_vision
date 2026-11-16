# Hybrid T4 walking pilot V1

13 November 2026. Prospective **technical pilot**, using previously inspected
development data only. No held-out claim, new biological validation, or
population-level walking qualification follows. All details below are fixed
before the hybrid outputs.

Use the saved binocular retina frames and functional source drives for the
existing `f00` room, speed 11 mm/s, straight walking and yaw -2/+2 deg/s,
including the original 0.5 s walking and 1.0 s yaw onsets. All three are
previously inspected development cases. Verify each retained image/source file
against its pre-existing receipt, and independently replay the functional
frontend from the same saved images within `1e-7` normalized drive. Confirm
all three image and functional source prefixes are identical through yaw onset.

Select the four T4a/b source cells (one of each per eye) already fixed by the
previous [eye-control mapping](../results/t4_eye_bridge_controls_v1/mapping.json).
Their population-inventory centers and axes are anatomical approximations;
do not insert the recording-specific calibrated cell delays or alias choices.
Convert each cell's eleven native 2.25-degree points and nine transverse
samples from world to the eye chart, sample the *same* saved retinal pixels at
5 ms with bilinear interpolation, and apply the existing ON contrast rule.
Require all selected sampling points to be inside the saved retinal chart.
Hold the first walking image for 3 seconds to initialize each full T4 cable;
this is a declared initialization choice, different from the functional
frontend's own initialization. Run each cell/condition at 0.1 and 0.05 ms and
require every max voltage difference <= 0.005 mV. Do not fit a gain, geometry,
direction or voltage trace to walking outputs.

At the 10 ms network clock, replace only those four exact T4 IDs with
`max(V_mV+65,0)/65`; reject out-of-range drives. Every other T4 and T5 source
remains bit-identical to the original functional source. Run the same frozen
LPi graph and the explicit held-input solver for both versions; retain the
same parameters, start state and 10 ms observation clock. Also evaluate the
existing fixed raw-local artificial decoder and its fixed cutoff on both
versions, without refitting. Its previous validation does not transfer to
this changed model or solver; scores on one known scene are descriptive only.
Compare selected source traces, downstream rates and decoder scores, including
the original and hybrid result at 1.19 s. Do not infer detection ability or
biological validity from three outcomes or the sign of a single score.

Run a 0.5 ms graph refinement against the 1 ms result for both straight-case
models, with `1e-8` absolute wide-rate guard, plus an independent graph
reference check on a predetermined case. Check causal prefix equality across
the three conditions for each version. Stop on a failed guard, preserve the
failure and do not tune the model or claim a pass.

Use one NEURON worker, at most 300 scientific child CPU seconds, 20 GiB free
reserve and a 32 MiB retained-output budget; the three existing retina archives
total about 155 MiB read-only and are not copied or regenerated. Avoid saving
full network states or generated movies. Hash exact inputs and methods before
scientific outcomes; retain numerical and independent verification, a dated
progress snapshot, report and sealed evidence.
