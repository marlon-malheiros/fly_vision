# Continuous yaw mechanisms: prospective protocol V1

24 October 2026. Separately versioned open-loop study following the authorized
second-opinion plan revision. Preserve all previous sealed evidence, graphs,
parameters and original classification criteria. No closed-loop control,
fabricated electrical conductance or circuit fit for classification is allowed.

## Questions and fixed conditions

Measure how raw bilateral neural responses change with small yaw, how forward
walking creates a baseline difference, and which effects are attributable to
controlled image/routing/network manipulations. Hypotheses of saturation,
perfect common-mode rejection, nonlinear adaptation and a uniquely identified
error source are not assumed true. Existing room outcomes are known; controlled
follow-ups are diagnostic, not fresh validation.

Use unchanged point receptors on the 173×173 grid in each eye and **direct
rays**, without panorama interpolation or a new optical aperture. The functional
frontend and MaleCNS equations/parameters remain frozen. This defines a discrete
synthetic optical input; it does not establish biological optics or receptor-grid
convergence. Images are every 5 ms; source/recording every 10 ms; RK4 every 1 ms.
Episodes remain 2 s, with prescribed motion from 0.5 to 1.5 s. Eye baseline
remains 0.3 mm and poses use the existing exact SE(2) integration.

Core inputs: two known rooms s07/s12 × five world conditions × speeds
0/5.5/11/16.5 mm/s × yaw 0/±1/±2/±5°/s = **280 inputs**. Both intact and
bilaterally bIPS-silenced original graphs receive each identical saved drive:
**560 original-network trajectories**. Save every binocular movie, all source
drives, 10-ms neural trajectories/final states, pooled motion channels, fixed
field/depth/flow checkpoints, input/output hashes and intervention ledgers.

The five worlds are:

- A: original geometry and texture.
- M: exact reflection of A through y=0, including surface material indexing,
  world texture wavevectors, camera poses, eye positions and yaw sign.
- G: symmetric geometry, original/asymmetric texture prescription.
- T: original geometry, symmetric texture prescription.
- S: symmetric geometry and symmetric texture.

Symmetric geometry is the original sphere set union its reflection (duplicates
removed by exact identity); enclosing boxes are already symmetric. New sphere
copies retain their original material index. For symmetric textures, paired
y-walls share the original positive-y wall material. Every material's luminance
is averaged with its y-reflected field using all eight original Fourier modes
(16 terms), with no contrast renormalization. This necessarily changes local
contrast; retain image means/RMS contrasts and do not attribute every effect
uniquely to symmetry. Reflection of A instead permutes y-wall material indices
and reflects wavevectors without averaging. Empty s07 geometry gives exact A/G
and T/S duplicate controls. All prescriptions are fixed before neural outcomes.

## Circuit/input controls

The original intact and bIPS-output silencing definitions are unchanged; do not
renormalize lesions. On 36 core inputs (two rooms × A/S × three nonzero speeds
× yaw 0/±2), additionally replay four expanded graph copies: inherited normalized
intact and dual-new-family silenced; and a separately saved counterfactual with
the entire original 203,861-entry old-cell block restored exactly, intact and
dual-new-family silenced. Added-cell connections retain their recorded expanded
weights (fixed coupling one), and global parameters are unchanged. This is a
synthetic normalization control, not a new physiological reconstruction. The
restored/muted old-cell output must reproduce the original intact trajectory
within 1e-10. No coupling sweep or best-performing graph selection is allowed.

Use 26 bounded, channel-aware source probes: common horizontal FtoB amplitude
c=0.01/0.05/0.10 crossed with (dc,d)=(0,0),(±0.001,0),(0,±0.001),(0,±0.002),
plus c=0 with d=0/±0.001/±0.002. For local signed horizontal inputs
u_L=c+dc+d and u_R=c+dc-d, supply max(u,0) to ON/OFF H-positive channels and
max(-u,0) to H-negative channels; vertical input is zero. Use the same 0.5–1.5-s
epoch, source IDs and clocks. These are normalized circuit probes, not a mapping
from real velocity to T4/T5 firing. Run original intact/bIPS-silenced and the four
expanded/control copies: **156 probe trajectories**. Derivative denominators
use the actual float32 input amplitudes, not idealized unrounded values.

## Frozen continuous analysis

Primary response is the original window [0.70,1.40), indices [70,140), with
separate left/right class means and q=left-minus-right. Retain signed outputs.
Also retain the full time series and fixed early [0.55,0.70), late [1.20,1.40)
and decay [1.60,1.90) summaries. Do not select windows by favorable results.

- Yaw finite-difference gains: [q(+h)-q(-h)]/(2h), for h=1/2/5°/s at each
  room/world/speed; retain all three estimates rather than asserting linearity.
- Straight offset q(0), yaw-minus-straight contrasts, even and odd components,
  and forward leakage q(0)/v for nonzero speed (explicit physical units).
- Yaw-equivalent offset q(0)/G_yaw(h=1) in °/s, and a dimensionless ratio
  |2°/s × G_yaw|/|q(0)|. Undefined divisions are null with a status, never a
  fitted epsilon. These are diagnostic scene biases, not stochastic noise SNR.
- Original/reflected parity: compare A(v,w) to M(v,-w) at images, pooled channels
  and neural class differences. q_even=(q_A+q_M)/2 and q_odd=(q_A-q_M)/2 are
  decompositions; neither uniquely labels an error physical or numerical.
- In S/straight cases, check aligned left/right retinal images and pooled
  fields before interpreting neural differences. The receptor coordinate
  transform makes eye exchange the local-grid reflection; do not silently flip
  a horizontal channel. Source targets have unequal counts/retinotopy and no
  invented homolog pairing; retain per-side/type counts and mean drives.
- For probes at each c>0, measure differential and common-input gains with
  matched ±0.001 perturbations, and differential gain at ±0.002. Inputs share
  normalized drive units, so 20 log10(|G_diff/G_common|) is dimensionless. Zero
  denominators remain explicitly undefined/zero-leakage rather than regularized.
- Retain activation operating points and local tanh slopes. Failing a scalar
  description does not prove divisive gain or nonlinear adaptation.

## Fresh-environment readout comparison

Generate 16 independent rooms with fixed seeds 2026102400–2026102415 before any
new neural outcome. First four are training, next four calibration, last eight
held-out. Each gets three walking speeds × yaw 0/±2/±5 = 15 conditions, **240
inputs and 480 original-network trajectories**, using the identical direct-ray
operator. These small scene counts cannot qualify population error rates.

Predetermine three nested readouts: two DNp15 means; all 14 cell means; and all
14 means plus within-window least-squares temporal slopes. Fit separate
known-speed ridge regressions, standardizing on training data only. Candidate
ridge penalties are 0.001/0.01/0.1/1 on mean squared training loss. Select one
penalty per feature family by equal-room calibration MSE averaged across all
three speeds; exact ties choose the larger penalty. Save all candidates,
calibration predictions and selected coefficients before opening held-out neural
arrays. Test every selected readout; select no winner using held-out results.

Report held-out yaw RMSE/MAE, raw sign accuracy, straight score offsets and
turn-vs-straight AUROC using |score| separately for magnitudes 2 and 5. AUROC is
over these sampled environments, not neural-trial or behavioral sensitivity.
Transfer the intact-trained readouts to bIPS silencing as a secondary comparison.
Retain original sealed DNp15 decoder scores/cutoffs as another secondary result;
do not declare a new detection threshold or replace the original failed gate.
No added circuit is selected or trained for classification in this study.

## Numerical/source checks and finite stopping rule

Preflight must reproduce historical A/s07/16.5/+2 direct-ray images/source drive
exactly and original rates within 1e-10. New variable-mode renderer is checked
against independent NumPy intersections/cosines in all ten worlds and three
poses (luminance tolerance 1e-7); verify reflected material mapping and eye-ray
coordinates. All source values must remain finite within [0,1]. These are
implementation prerequisites; preserve failures before any correction.

Fixed refinement inputs: s07/A/16.5/yaw±1 and s12/S/16.5/yaw0. Run each with
2.5-ms images, 5-ms source/recording and 0.5-ms solver. Also replay primary
source inputs with a 0.5-ms solver alone. Compare primary-window class means
with a 5% tolerance and 1e-5 denominator floor; compare s07 central yaw gain
with 5% and 1e-6 floor. Preserve failures and stop at these two resolutions;
do not refine until favorable. No universal retinal-grid convergence is claimed.

Independently review array arithmetic, mirror/symmetry/duplicate identities,
all file hashes and readout train/calibration/test separation. Check one visual
case and one probe with the original Python equations, including the restored
normalization control. Produce figures, complete tables, a concise report and
an undergraduate what/we-want/why explanation. Save progress throughout and a
dated progress copy before sealing the finite study. No failed scientific or
numerical criterion can be removed retrospectively.

## Physiological benchmark workstream

In parallel, audit the available primary stimulus generator, recording metadata,
fly identities and reporter/compartment information. Specify one canonical
horizontal-motion HS/H2/bIPS/DNp15 image-to-recording benchmark with exact
stimulus/side/measurement/calibration requirements. The old test flies and
diagnostic outcomes are already inspected. If exact images, mapping or fresh
validation data are unavailable, record that gate and execute only supported
audits; do not insert a generic calcium time constant or claim physiological
validation. Exact walking-agent source is not required for these diagnostics.
