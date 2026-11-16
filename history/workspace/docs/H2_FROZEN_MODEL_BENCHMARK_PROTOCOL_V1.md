# Frozen-model H2 moving-edge comparison V1

25 October 2026. Execute the user-authorized comparison from the completed H2
trial study. This is an exploratory **approximate stimulus-family** benchmark,
not exact recording replay or physiological validation. All seven animals'
source summaries/curves were previously inspected. No neural or observation
parameter fit, new yaw experiment, ablation or controller is included.

## Fixed model and evidence

Use the original `results/fixed_neighbor_motion_v1` config, 13,579 source
identities/routes, graph and parameters; the unchanged StreamingFrontend and
StreamingCircuit equations/RK4 boundary convention. Left H2 is body 10019,
selected from graph labels and exclusive left T4/T5 afferents, never response
peaks. Preserve all fourteen wide-cell traces and final states. Biological
recordings are female; this is a male-connectome surrogate with assigned
retinotopy/cardinal channels and no electrical synapses.

The pinned author `Eyal_arena_2023` helper defines cylinder geometry and head
pitch. Its PD-vector displacement in display indices is (cos(theta),sin(theta))
with theta=-2*pi*relOrt/8; source polar-script comments specify upward/downward
and horizontal directions. `Fig_1.R` lines 205–206 explicitly reflect left
recording azimuth to the right-side anatomical plot. Our original body chart
has left azimuth negative, so convert author Cartesian coordinates with
(x,y,z)->(x,-y,z), supported by those conventions and checked geometrically.
No side/sign is chosen from neural agreement.

Use all 39 published cell/protocol/position combinations, 16 directions and
both polarities. Reuse model traces only where input pose/position/timing are
identical (cells 5 and 6 share two pose settings); preserve a complete
condition-to-trace manifest. Cell 7's other three positions lack head/arena
pose rows in the admitted files: mark unscored and do not infer their poses
from other animals. Report full-source missingness separately from the
39-position published-subset estimator.

## Renderer and explicit approximations

Implement the author's inch-based cylindrical surface, transforms and their
inverse ray-cylinder intersection. Use the unchanged 173x173 1-degree eye
lattice and original eye transforms. Radius/physical height come from the
helper, azimuth extent from 240 degrees. Intersect rays, then choose the
nearest LED index with floor(x+0.5). The circular window includes integer
indices at squared radius <=100 about the decoded center. Background is
0.49, edges are 0/1. Right eye is spatially constant zero (opaque-eye surrogate,
not calibrated retinal photometry); it must produce zero motion drive.

For direction theta, filled pixels satisfy dot(pixel-center,(cos theta,sin
theta)) <= -10.5 + floor(t/step) + edge_phase. Onset is model t=1 s. Display
steps are the recorded 0.04/0.08 s. At (fullFN-firstFN+1)*step after onset,
reset to background, consistent with the author's disappearance event but
not proof of exact pattern frames. Pixel origin, half-plane rasterization,
first-frame edge phase and event-clock offsets are approximations. Keep
edge_phase=0 primary. Sample the full movie at 5 ms and neural RK4 at 1 ms,
using every frontend frame as network input. Retain unique retinal keyframes
with a frame-index map, every delivered source sample and every wide-cell
trace, sufficient for lossless input replay. Retain a 0.1-s post-stimulus tail.
All reset states are zero neural activity and equilibrium frontend delay for
the initial constant images. The identically zero neural/source baseline
prefix is retained in arrays but repeated zero-RHS arithmetic can be skipped;
original-Python full-prefix replay independently checks this exact optimization. One model second is one stimulus second as an
explicit inherited time-scale assumption, not a calibrated membrane model.

## Fixed sensitivity and numerical controls

Do not expand variants based on agreement. At position (87,13) of cells
1,4,5,7, repeat all 16x2 conditions at edge_phase=-0.5 and +0.5 LED. At that
same position of cells 5 and 7, bracket the measured head-yaw magnitude with signed -2/+2 degree head
rotations, because the author helper ignores yaw and its sign is not independently
established here; report both, never select by agreement. These bounded
subsets do not establish uncertainty for all positions. Run one stationary
half-filled edge control per unique primary location, initialized at equilibrium.

For both polarities/directions relOrt=0,2,4,6 at (87,13) of cells 1 and 4
(16 cases), replay identical drives at 0.5-ms RK4 and rerender at 2.5-ms
frontend/input and 0.5-ms RK4. Numerical endpoint agreement tolerance is
5% of the reference magnitude plus 1e-7 model-rate units. Report failures;
never relax this criterion or silently replace primary runs. Numerical
instability/sampling sensitivity prevents a convergence claim; approximate
comparison results remain explicitly conditional. Independently check the
cylinder transform against the original R helper, inverse/forward ray
geometry (<1e-9 inch, <1e-8 display-pixel error), cardinal display motions,
right-eye zero drive and all stationary controls. Independently replay two
predetermined primary cases (cell 1, position 87,13, dark, relOrt 0 and 4)
through original Python FrozenGraph with rate agreement <=1e-10.

## Observation and comparison rules

Extract the identified H2 rate tanh(state). Model baseline is the pre-onset
mean; check its expected zero equilibrium. Integrate baseline-subtracted
model rate by linear-interpolated trapezoids over recording-relative
[0.001 s, protocol source-derived response_end], divided by that duration.
Compare this dimensionless rate curve with recorded baseline-subtracted
spikes/s only using PD/DSI and scale-free curve correlation. Positive-affine
shape correspondence is an explicit observation assumption; no absolute
firing-rate or calcium prediction is claimed and no gain is fitted.

Primary: average the signed bright/dark curves first, subtract the directional
minimum, compute the complex vector at theta=-2*pi*relOrt/8, and compare
atan2 phases with absolute circular error. Secondary: per-polarity PD, vector
DSI and Pearson direction-curve correlation. Define flat range <=1e-12 model
rate (or <=1e-12 spikes/s for recordings), or vector magnitude <=1e-12 times
weight sum, as undefined PD; retain every undefined/flat case and amplitude.
Report observed/defined coverage. If any primary published position has
undefined model PD, the complete primary estimator is not identifiable:
show available-case errors plus cell-weighted [0,180]-degree missing-error
bounds. Do not turn undefined predictions into zero-error or select locations
by agreement.

Each animal is equally weighted, then its available published positions
are equally weighted. Report cells individually and the previously specified
1–4/5–7 partitions; no training occurs and these are not fresh test animals.
Report all-source and published-subset coverage. The parameter-free reference
is body-horizontal back-to-front optic flow (increasing left-field azimuth),
projected into LED tangent coordinates using the local geometry Jacobian.
Also report fixed theta=0 LED-horizontal error, with no fitted sign.

Bootstrap 10,000 draws with seed 20261025: resample animals and aligned raster
repeat counts within each condition; recompute the source protocol pooled
baseline with original trial-column weighting, both-polarity PD and all
errors. Model traces stay fixed. Report 2.5/97.5 percentiles and missingness;
no retrospective biological pass/fail threshold. With seven animals, show
the individual results and do not imply precise biological generalization.
Freeze implementation/config/plans before model outcomes. Preserve failures,
all numerical evidence, figures, reproducible code and a separate report
ending with an undergraduate what/want/why explanation. Append live progress,
save its dated snapshot, checkpoint and seal independently of earlier studies.
