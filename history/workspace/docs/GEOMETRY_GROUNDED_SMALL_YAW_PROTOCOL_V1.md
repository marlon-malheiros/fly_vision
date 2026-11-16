# Geometry-grounded small-yaw study V1

25 October 2026. User authorizes continued implementation toward a material
change in small-turn detection. Preserve all sealed models and reports.
This study must measure actual ±2°/s walking detection, rather than stop at
another H2-only diagnostic. Prior errors, data and old test rooms are known.
No old test room becomes fresh held-out evidence.

## Interventions and evidence

Keep the original MaleCNS graph, source coordinates/identities, time constants,
chemical weights, gains and optical raster. Add two independent frontend
versions, leaving the functional baseline unchanged:

* `t4_field`: replace only the T4 cardinal direction vectors with the deposited
  unsmoothed 778-location `RF_lens_T4_pred` field from Zhao et al. (2025).
* `t4t5_field_hypothesis`: apply that same field also to matching T5 subtypes.
  This T5 transfer is explicitly an additional modeling hypothesis, not a
  measured T5 constraint. Never promote it to the evidence status of T4.

The native negative-y eye is mapped to project left coordinates; right is
its y-reflection. This follows author coordinate conventions and the central
T4b back-to-front direction, without choosing signs from response agreement.
At each original source location select the nearest published spherical
direction, parallel-transport its tangent PD to the source ray, convert to
the original eye chart, and normalize its two chart coefficients. Record
every nearest distance, especially peripheral extrapolation. Do not claim
specimen-specific registration between female published anatomy and MaleCNS.
The paper's supplied a/c estimates include its antiparallel assumptions.

Project the original signed horizontal/vertical HRC fields at each bilinear
vertex onto these fixed coefficients; rectify before the original spatial
interpolation. T4/T5 polarity, delay, pooling, sampling and drive bounds stay
unchanged. A cardinal-coefficient control must reproduce the original drive
exactly. This vector projection is a geometry-informed surrogate operation,
not reconstruction of upstream synaptic physiology or detector conductances.

As separate engineering positive controls, implement two image-only yaw
estimators: local Lucas–Kanade flow followed by geometric removal of forward
translation; and direct brightness-constancy fitting with unknown local-plane
inverse depths eliminated by a subspace projection. Both know only that
translation is body-forward and rotation is yaw. Neither receives simulator
depth, surfaces, velocity labels, pose trajectories, model outputs or pairing
with the same room's zero-yaw test condition. Translation speed and local
depth remain unknown nuisance quantities. Fit no yaw gain or bias. These
controls cannot establish a new neural mechanism, bIPS causality or a
biological detector. Success distinguishes available retinal information
from success of the modeled circuit.

Both estimators use fourth-order centered spatial and temporal derivatives,
fixed eye support h=[-60,60), elevation=[-48,48), the original 1° images and
5-ms frame spacing. LK uses a fixed ±2° box window and samples every 4°;
the subspace model uses fixed 8° blocks and eliminates three independent
inverse-depth plane coefficients per block. SVD rank decisions use machine
precision. Record undefined estimates; never replace them with correct
answers. Centered derivatives imply 10-ms future-frame latency in this
offline experiment and do not implement closed-loop control.

## Conditions, separation and scoring

Use three speeds 5.5/11/16.5 mm/s and yaw 0/±2/±5°/s, plus stationary control:
16 conditions per room. Prescribed poses/eyes/rendering remain the previous
exact SE(2), 0.3-mm binocular separation, 2-s episode, movement [0.5,1.5).
Primary frontend/input/RK4 clocks are 5/10/1 ms. Retain lossless retinal inputs,
every delivered source array, fourteen-cell output traces/final states and
both image-reference time series. Reuse previously saved retinal/source/
baseline traces only when inputs are identical and hash-verified.

Four known development rooms f00–f03 supply training. Four known calibration
rooms f04–f07 plus twelve newly seeded calibration rooms supply cutoffs.
Twenty-four independently seeded, unused rooms supply held-out tests. This
is 44 rooms ×16 conditions =704 episodes. New worlds use the existing
independent-world construction recipe and seeds starting at 202610251000;
room IDs, geometry, textures and split are frozen before new outcomes. New
held-out inputs and predictions are not generated until the fitted readouts
and cutoffs are saved and hashed. No selection on held-out scores.

For each network version, speed and class HS/H2/bIPS/DNp15, apply the existing
two-feature signed decoder to mean left/right rates over [0.70,1.40).
Use ridge=0.001, the existing fixed estimator; no new penalty search. Fit
coefficients/scaling on training rooms only. Set cutoff to the maximum
absolute straight-walking calibration score, separately by speed/version.
Score held-out signed ±2/±5 and straight walking. For image references use
their uncalibrated physical yaw estimates averaged over the same window;
only the same calibration cutoff is set. Fit no image-estimator gain/bias.

Use the original reliability gate: detection ≥80%, raw yaw-sign accuracy
≥80% (including nondetections in its denominator), observed straight false
alarms ≤10%, at the magnitude and every larger tested magnitude. This finite
grid contains 2 and 5°/s; it cannot refine thresholds below 2 or reproduce
the original larger-yaw grid. Preserve every count, estimate and undefined
case. Raw sign uses sign(score) for every turn, including those below the
detection cutoff; it is not sign(thresholded decision). Neural primary is
DNp15; other classes are secondary. Report paired
differences versus baseline on identical rooms, with room-resampling
intervals (10,000 draws, seed 202610251337); no biological population claim.

A material circuit improvement means satisfying the ±2 reliability gate at
all three speeds, or a ≥20-percentage-point fast-walking detection gain
with no worse false alarms/sign accuracy and passed numerical gates. An
image reference meeting the reliability gate across speeds is a material
engineering/information result, explicitly not a repaired MaleCNS circuit.
An H2-only improvement is insufficient to claim progress on yaw detection.

## Controls and numerical checks

Before main predictions, validate source parsing, tangent transport, cardinal
identity, baseline replay and analytical cancellation on synthetic optic
flow at independently generated depths/speeds/yaws. No synthetic truth may
enter an image estimator's actual input. Preserve software failures.

Twenty known pilot episodes: s07/s12 × three speeds ×yaw 0/±2, plus static.
They reuse inspected movies, are diagnostic only, and do not train/test the
new decoder. Independently assess the externally motivated field on all
bright/dark directions at upper patch (87,36) of H2 cells 2 and 4: 64 input
movies, with source-derived windows and the previously frozen observation
rule. These already inspected animals are not held-out physiology. Neither
pilot nor H2 comparison selects neural parameters or favorable variants.

For s07/s12 × speeds5.5/16.5 × yaw0/±2 (12 pilot inputs), rerun all models
with 2.5/5/0.5-ms clocks. Mean cell/class tolerance is 5% of the primary
magnitude with denominator floor1e-5. Reference yaw-estimate tolerance is
0.2°/s. Separately render the three s07 fast 0/±2 cases at 0.5° solely for
image-reference spatial refinement; keep neural source geometry unchanged.
Report all failed numerical gates without replacement of primary scores.
Independently replay two new source trajectories in the original Python
FrozenGraph with absolute rate/final-state tolerance1e-10. Fresh source-build
replay a finite predetermined subset and independently reconstruct scores,
cutoffs, gates, bootstrap effects and hashes. Numerical checks do not
constitute physiological validation.

## Persistence, reporting and limits

Freeze code/config/plans before predictions and separately freeze readouts
before test generation. If no material improvement occurs, identify a
specific violated prediction before a further separately versioned change;
do not tune on the inspected tests or endlessly reopen passed mapping audits.
Any continued version requires fresh held-out environments. Report failures
and improvements, all conditions and all three neural versions, including
the evidentially weaker T5 hypothesis.

Publish a separate technical report with figures, complete numerical tables,
reproduction instructions and an undergraduate what/we want/why explanation.
Append dated progress, save its dated copy, commit source and seal artifacts,
excluding live progress and AGENTS.md. No previous result is overwritten.
No missing electrical conductance, physiological calibration, motor-intention
signal, biological causal conclusion or closed-loop controller is introduced.
