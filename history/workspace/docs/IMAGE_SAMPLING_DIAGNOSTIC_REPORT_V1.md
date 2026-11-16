# Controlled image-sampling diagnostic V1

Completed numerical study, 24 October 2026, America/Belem. Original intact circuit
and all decoder parameters preserved. [Protocol](IMAGE_SAMPLING_DIAGNOSTIC_PROTOCOL_V1.md).

**Result:** panorama interpolation changes the effective input smoothing and
propagates into neural responses and yaw scores. Finer panoramas approach the
direct-ray reference. At 0.25° and 0.125°, all categorical decisions match direct
rays in the two tested rooms, but the complete predeclared numerical-stability
gate still fails. Straight-walking false alarms remain even with direct rays.
Thus image sampling contributes to earlier result changes; correcting that
approximation alone does not establish reliable small-turn detection.

## What was held fixed

Completed 44 visual inputs through five image profiles: **220 full neural
trajectories**. Existing rooms s07 (box) and s12 (three obstacles) were selected
for structural coverage. Each received 5.5/11/16.5 mm/s forward motion crossed
with yaw 0, ±2, ±5 and ±20°/s, plus a stationary control. These rooms were already
inspected in earlier studies; they are not fresh validation environments.

Only panorama pitch changed: 1°, 0.5°, 0.25°, 0.125°, compared with direct rays
at the same receptor directions. The original 173×173 receptor grid per eye,
eye origins/poses, world textures, frontend, 5-ms image clock, 10-ms network
input/recording, 1-ms solver, MaleCNS graph and neural parameters were unchanged.
The fixed readouts still use known walking speed and the original 70-sample
window, 0.70–1.39 s. No decoder was retrained or cutoff adjusted.

Direct rays are a numerical reference for the same point-sampled synthetic world.
They remove panorama interpolation; they do not establish the real fly's optical
aperture, receptor-grid convergence, exposure response or temporal convergence.
All main conditions and stability criteria were hash-frozen before these new
outcomes. [Configuration](../configs/image_sampling_diagnostic_v1.json),
[before-main record](../results/image_sampling_diagnostic_v1/before_main.json),
[complete execution](../results/image_sampling_diagnostic_v1/execution_complete.json).

## Where the difference enters

An exact code-level audit shows that the receptor coordinates are integer angles.
For each dyadic panorama pitch, interpolation weights are 0.5 along each axis.
Every receptor therefore receives the average of four point samples at
azimuth/elevation offsets ±half the panorama pitch, with float32 output rounding.
Refining pitch shrinks this implicit interpolation footprint toward the direct
point sample. This is inherited sampler behavior, not a newly fitted filter or
evidence for a measured photoreceptor aperture.
[Eight eye/pitch checks](../results/image_sampling_diagnostic_v1/sampler_footprint_v1.json).

The controlled comparisons trace that input change through motion channels,
routed source drives, 14 output-cell responses and the fixed readouts. Maximum
errors across the 44 inputs, relative to direct rays, are:

| Panorama pitch | Retinal RMS error | Routed-input relative RMS | Largest cell mean error | Largest class-score error | Changed class decisions |
|---:|---:|---:|---:|---:|---:|
| 1° | 0.02330 | 21.26% | 27.83% | 8.415°/s | 10/168 |
| 0.5° | 0.01268 | 10.34% | 9.68% | 2.666°/s | 1/168 |
| 0.25° | 0.00775 | 7.08% | 3.53% | 0.786°/s | 0/168 |
| 0.125° | 0.00393 | 5.10% | 1.82% | 0.240°/s | 0/168 |

Retinal values are luminance units; source and neural activity remain uncalibrated
model units. Relative input errors use the frozen RMS floor of 1e−6; cell means
use a 1e−5 magnitude floor. The 168 decisions per profile are 42 moving-input
conditions × four neuron classes, not independent animals or trials. Each column
reports its own maximum and need not refer to the same input.
[All comparisons](../results/image_sampling_diagnostic_v1/analysis_v1/comparisons.csv),
[every cell](../results/image_sampling_diagnostic_v1/analysis_v1/cell_responses.csv).

![Errors across processing stages](../results/image_sampling_diagnostic_v1/presentation_v1/stages_against_direct.png)

The ±5° horizon band contains about 6.4% of receptor-grid points but accounts for
a median 69.9% of remaining squared image error at 0.125°. This localizes image
disagreement; it does not prove that horizon pixels alone cause the neural
differences. Full maps and frame/eye errors remain retained. The geometric
footprint and fixed-decoder sensitivity explanations were added after the
primary protocol freeze; neither changes the acceptance rules.

## What is stable, and what still fails

The complete frozen gate requires both finest panoramas to meet the stated
retinal, input, cell-mean, yaw-contrast, score and decision tolerances against
direct rays, plus score/decision agreement between those two panoramas.
The gate is **not met**. Among the 88 finest-profile/direct comparisons:

- All routed-input RMS and all cell-mean comparisons pass their 10% rules.
- The 0.125° retinal RMS passes 0.005 for all 44 inputs; 0.25° fails all 44.
- Six input/profile comparisons fail the 10% yaw-minus-straight contrast rule.
  All flagged cells are H2 at fast walking and ±20°/s. Some reference contrasts
  are near zero: one 0.125° discrepancy is 4.57×10⁻⁷ model units despite a large
  floored relative error. The largest flagged 0.125° absolute discrepancy is
  2.07×10⁻⁶ model units. No HS, bIPS or DNp15 contrast fails in these two profiles.
- Forty-five input/profile comparisons exceed the 0.1°/s score tolerance.
  Thirty finest-adjacent comparisons also exceed it.
- All finest-profile/direct and finest-adjacent categorical decisions agree.
  All stationary source and neural responses are exactly zero.

At 0.125°, the ±2°/s score error is at most 0.0868°/s across all four classes
(0.0667°/s for DNp15), within the declared score tolerance. Larger ±5/±20°/s
conditions still contain failures. This encouraging subset result does not
replace the full predeclared gate or justify a new sensitivity threshold.
[Gate results](../results/image_sampling_diagnostic_v1/analysis_v1/complete.json),
[every score comparison](../results/image_sampling_diagnostic_v1/analysis_v1/score_comparisons.csv).

The unchanged readout can magnify small activity changes. For DNp15, its fixed
left/right feature coefficients give sufficient 0.1°/s score-error bounds when
each feature error is below approximately 2.74–3.05×10⁻⁶ model units. These are
conservative linear-readout bounds, not measured neural precision requirements.
Whether a decision changes also depends on distance to its existing cutoff.
[Explanatory coefficients and scope](../results/image_sampling_diagnostic_v1/decoder_explanation_v1/provenance.json).

## Does direct sampling solve detection?

No reliable detector is established by this diagnostic. With direct rays, the
fixed DNp15 readout has the following observed counts in the two known rooms:

| Forward speed | ±2°/s detected | Correct signs at ±2°/s | Straight false alarms |
|---:|---:|---:|---:|
| 5.5 mm/s | 3/4 | 4/4 | 1/2 |
| 11 mm/s | 1/4 | 3/4 | 1/2 |
| 16.5 mm/s | 1/4 | 3/4 | 1/2 |

These counts are diagnostic, not population false-alarm estimates. In s07 at
fast walking with +5°/s yaw, the legacy DNp15 score is 7.760 and the direct-ray
score is 10.458: it changes from nondetection to detection at the unchanged 8.892
cutoff. In s12 during fast straight walking, the score changes from 8.506 to
11.805: the same cutoff now produces a false alarm. Finer sampling therefore
does not uniformly improve classification.
[All diagnostic counts](../results/image_sampling_diagnostic_v1/analysis_v1/diagnostic_counts.csv).

![DNp15 scores in both rooms and all speeds](../results/image_sampling_diagnostic_v1/presentation_v1/dnp15_frozen_scores.png)

## Independent validation and preservation

Historical preflight reproduces the saved legacy source, retinal checkpoints
and neural trajectory exactly. The independent review verifies all 660 main
output-file hashes, all 308 full-retinal comparisons, 840 scores and 4,312 cell
comparisons. It independently reproduces the failed combined-gate classification.
A direct movie replayed through the existing offline frontend gives exact routed
drives and pooled channels. Original Python neural equations match the direct
case within 8.68×10⁻¹⁹ in rates and 8.14×10⁻²⁰ in final state. Independent NumPy
raycasting matches all 76,296 sampled direct retinal values exactly.

These checks establish scoped numerical reproducibility. They do not independently
reconstruct every frontend equation, validate real optics or establish physiological
agreement. Approximately 21.1 GB of raw binocular retinal movies are retained,
alongside all drives, motion checkpoints, outputs and source identities. All 220
main trajectories completed without execution failures. No further panorama
profile was added after the gate failed.
[Independent review](../results/image_sampling_diagnostic_v1/independent_review_v1/complete.json),
[reproduction guide](IMAGE_SAMPLING_DIAGNOSTIC_REPRODUCTION_V1.md).

The separate-namespace reproduction entry point passed preparation, historical
preflight and source freeze. It has not run a second full 220-trajectory sweep.
Earlier studies, model packages and unfinished V9 hardware evidence remain
preserved. This study provides no motor controller or physical deployment claim.

## Interpretation and next evidence priority

We have isolated an image-sampling contribution with the circuit held fixed:
interpolation changes input smoothing, changes motion drives and moves some
scores across fixed cutoffs. It is not sufficient to explain away all false
alarms, and this study does not establish which missing biological mechanism
or alternative readout would solve them. The old coarse threshold remains
resolution-dependent, as already reported in the broader study.

The next bounded step should explicitly fix the input's optical sampling rule
and qualify its numerical accuracy before recalibrating/testing a readout on
separate development and test environments. Direct rays provide a useful point-
sampling reference; a physical aperture/filter needs biological or camera evidence.
Any revised input representation or calibration belongs in a separate version,
with the original circuit and results retained. New finer grids, physiological
fits and circuit changes were not executed here.

## Undergraduate explanation: what we did, what we want and why

We want to understand why the model sometimes mistakes straight walking for a
turn. We showed the same frozen circuit the same movements, changing only how
the images were sampled. We found that the old image step also averages nearby
directions, and changing its resolution changes that averaging. Finer images
make the answers more consistent with our direct-ray reference, but false alarms
remain and some numerical checks still fail. This tells us that image sampling
is part of the problem, while more work is needed on the model and its readout.
We now have a clearer basis for choosing the visual input and comparing the
model fairly with recordings from real flies.
