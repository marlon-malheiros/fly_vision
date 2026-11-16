# Horizontal T4 integration pilot V1

2026-11-04. One fixed candidate; exploratory integration, not biological validation.
No candidate network outputs have yet been computed. Old physiological targets
and candidate source-mechanism results are already inspected development data.

## Feasibility and scientific boundary

The [preceding study](PHYSIOLOGICAL_BRANCH_VALIDATION_REPORT_V1.md) supplies an
independently reproduced Gonzalez-Suarez2022 T4 model, fixed measured kernels,
spatial spacing5deg/blur5.7deg, relative conductances and reversals. Its original
voltage is relative to rest, with maximum excitatory reversal+60mV and inhibitory
reversal-30mV. Because conductances are nonnegative, the voltage is a weighted
average of reversals and leak0. Therefore max(V,0)/60 is bounded[0,1].

Use this one common fractional driving-force conversion. It adds **no fitted
parameter**, threshold or condition-specific scale; it is nevertheless an
**unmeasured coupling assumption**, not a biological calibration. The earlier
full published frontend attempt already used driving-force normalization; this
principle is not presented as new. What differs here is the2022 measured,
input-specific, parallel-inhibition T4 mechanism and a deliberately narrow patch.
If a measured voltage-to-release coupling is required, feasibility is unresolved
and this pilot cannot satisfy that requirement. No tuning is authorized to fix it.

Replace only T4a/b (horizontal) inputs on both sides. T4c/d and all T5 sources
retain the frozen slowing-only functional frontend, gain and original routing.
This is a partial hybrid frontend. No T5 or vertical-T4 physiology is inferred
from the T4 source. No graph edge, neural parameter or decoder changes. The
legacy subtype-direction routing and eye chart remain explicit assumptions.

## Image and temporal specification

Use the same known methods85 vertical square-wave grating, 0.04cycles/deg,
four-bit luminance,60Hz display,5seconds with2s static/2s moving/1s static,
phase0, world az[-70,70] and el[-22.5,62.5]. Use the original binocular173x173
images for the unchanged functional channels and hash them against retained
old cases. No motion label enters the new neural equations.

The published T4 model is one-dimensional. This pilot is restricted to these
horizontal grating stimuli. Evaluate one horizontal profile for every in-field
elevation row and one for the uniform grey outside row; all such rows are
identical under this stimulus. There is no invented vertical receptive-field
width. Interpolate the resulting voltage fraction at old retinotopic cell
coordinates, with vertical weights equal to the original grid's bilinear field
mask. This row-wise lifting remains an exploratory2D embedding.

For horizontal support, render a full360deg eye-horizontal profile from the
same analytic display and eye transform (pitch1deg). The original173deg raster
alone is narrower than a5deg offset plus Gaussian support at edge cells; do not
wrap that narrow raster or fill unknown stimulus pixels arbitrarily. The display
is known across the panorama, so its additional samples can be generated from
the same stimulus. This changes receptive-field support, not the display or
physical stimulus. Anatomical eye coverage outside the old raster is unverified.
Use the author's full360deg Gaussian and periodic convolution. The source
coordinate5deg offsets follow the legacy local-eye positive/negative directions.
Refine horizontal sampling to0.5deg in one prespecified case.

Feed signed Weber-like contrast2L-1 into the published measured FIR filters,
with no fitted local gain. Use the retained already-deconvolved250ms kernels,
same Laguerre/PCHIP processing, support[0,1)s and the reference-grid amplitude
convention from the preceding study. Constant prehistory equals the actual
initial static image, hence each FIR begins in stationary equilibrium. This is
a declared initialization extension, not an added3s tunable warm-up. Use causal
convolution and no future padding. Retain the source's linear-nonlinear branches,
signs and conductance equation; couple rectified voltage/60, **not calcium**.

The new source may have static activity. Do not subtract it from source inputs
or demand the old zero-source condition. The network begins at its old zero
state and receives2s of static input before motion. Keep the original HS
observation: equal mean right HSN/HSE/HSS atanh(rate), [2,4) minus[1,2).
Record stationary drift and compare it against5% of the PD1Hz reference.

## Frozen finite cases and decisions

Eleven primary images: four frequencies times two directions, half-contrast
PD/ND at1Hz, and a stationary full-contrast pattern. Four fine image/source
cases: PD0.5/1/15Hz and half-contrast ND. Thus15 images. Primary/fine clocks
1.25/2.5ms and0.625/1.25ms; solver0.25ms; keep the absolute1ms source ramp.
Additional solves: half solver and horizontal0.5deg source sampling at primary
PD1Hz, plus one exact baseline PD1Hz replay. Eighteen solves total; only one
candidate and no sweep. Reuse retained baseline neural results elsewhere.

Before candidate outcomes, freeze continuation guards:

- all six numerical comparisons pass the inherited5% relative/reference gates:
  four joint image/source refinements, one horizontal sampling refinement and
  one solver refinement; no spatial convergence claim beyond the one test;
- old images and full baseline source arrays match hashes for every retained
  corresponding case; one neural baseline replay is bitwise; all non-T4a/b
  candidate source columns are bitwise identical to the baseline;
- all source drives finite[0,1], no clipping, positive candidate PD1Hz endpoint;
  stationary HS endpoint and largest baseline [1,2) HS drift each <=5% PD1Hz;
- frequency-panel RMSE <= the best of the four prior variants, AND violation
  count <= the best of those variants (different variants may set these bounds);
- absolute error of full-contrast ND1/PD1 against the retained contrast target
  is strictly smaller than every prior variant's error;
- half-contrast PD and ND ratios each remain within their existing retained
  contrast bands. Do not rebootstrap bands, refit a gain or select another phase.

All guards must pass for continuation. Guard failure means stop this candidate
without retuning or spending uninspected walking/recording data. Even passing
means only useful development integration, not biological validation. Preserve
all frequency/contrast outcomes, left/right group summaries and new source
range/static behavior. The stationary pattern has no calibrated turn-decoder
threshold, so its endpoint check is not a measured false-positive rate.

Budget:1800 total worker CPU s, one worker,3GiB worker peak RSS, estimated32MiB
and64MiB hard output cap,20GiB free reserve. Each case streams the original
retina; discard transient T4 and full-source arrays after solving. Retain compact
wide-neuron arrays, hashes, all endpoints and failures. No movies or full-eye
drive archive. Capture an execution receipt even when a case fails. Stop new
case submission if the budget/resource guard fails.

Before execution, preserve exact sources/protocol/config/tests and dependency
hashes, verify both immediately preceding retained studies, and commit the
freeze. At completion write a detailed report, dated live progress entry and
dated progress snapshot, then seal and independently rehash after writer exit.
Live progress and AGENTS stay outside the immutable index. Anatomical identities,
source physiology and the explicit coupling/embedding assumptions remain separate.
