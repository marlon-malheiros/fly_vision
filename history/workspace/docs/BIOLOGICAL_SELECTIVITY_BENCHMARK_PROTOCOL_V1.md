# Image-to-recording selectivity benchmark V1

Specified 27 October 2026 before new images, network outcomes, observation fits
or unilateral-condition scores. Original frontend, graph and numerical parameters
remain frozen. This is a new, bounded stimulus-family comparison, not a repair
of prior experiments or an exact-replay physiological validation.

## Question and source evidence

Does the image-driven circuit reproduce the different translation/rotation
preferences of bIPS and DNp15? The [primary paper](https://www.nature.com/articles/s41593-025-01948-9)
documents these preferences and the visual display, protocol timing, dot count,
dot size, intensity levels and measured calcium reporters. The [author analysis](https://github.com/ChiappeLab/Erginkaya_et_al_2025)
identifies YawRightFlipped as bilateral front-to-back/back-to-front horizontal
motion. It is a horizontal translation cue, without the perspective and parallax
of 3D walking. Do not call it equivalent to the simulated walking environment.

The exact original G3 arrays, random-dot states and refresh are unavailable in
the audited sources. Use new random-dot ensembles, never optimize their seeds
or rendering assumptions for agreement. This relaxes the exact-replay gate only
for this explicitly approximate new benchmark; the previous gate remains open.

## Frozen reconstruction and uncertainty

Generate 500 uniform unit-sphere directions and 5-degree circular dots on black.
Rasterize a 0.25-degree spherical texture, average 4x4 subpixel samples per LED,
and quantize to 16 levels on a 32x96 display with 2.25-degree pixel pitch.
This is a declared implementation, not recovered author generation code.
Laminar yaw moves all azimuths together; translation moves the two hemifields
in opposite directions. Unilateral patterns move only the named display half,
leaving the other half's same initial dots stationary. Motion is 45 degrees/s,
from the 20-pixel/s labels and documented pixel pitch; use actual 13-s epochs.
The second epoch reverses displacement and returns to the initial pattern.

Primary registration assumes the display tilt compensates the head pitch,
placing its center at head elevation zero. Independently report an alternative
74-degree pitch registration, without selecting by recorded response. These are
discrete mapping hypotheses, not measured uncertainty bounds. A 50-Hz display
alternative tests the unknown refresh against the primary assumed 100 Hz.
Both are sampled by the unchanged 200-Hz frontend and 100-Hz network inputs.
Use four primary dot seeds and two fixed seeds in each alternative; retain all
outcomes. Black exterior, full contrast, dot occlusion, angular rasterization,
stationary opposite half and display/head mapping remain modeling assumptions.
No eye optics or absolute photometric calibration is inferred.

## Recordings and separation

Use all eight existing intact native/WT, reporter/compartment-specific cohorts
in the soma-matched metadata plan, preserving its whole-fly calibration/test
assignments and author ROI choices. Metadata-only eligibility additionally
requires one of the four exact configured pattern names. Separate sessions,
reporters, compartments and genetic backgrounds; pool sessions and ROIs within
fly before giving every fly equal weight. No inspected animal becomes fresh.
The raw speed-tuning metadata audit finds no YawRightFlipped trial among its
45 sessions. Previously scored pure-yaw speeds cannot provide a new paired
rotation/translation speed validation.

For each trial/ROI, use measured 1--2-s mean and sample SD, the prior 95% finite
coverage rule and at least two usable trials. Record exclusions. Baseline
normalization is not fitted neural noise. Retain per-trial/ROI arrays for audit.

Only calibration flies' bilateral yaw/translation traces can fit observation
parameters. Use the existing 56 signed/rectified one/two-stage filter candidates
with time constants 0, .05, .1, .2, .4, .8, 1.6 s and nonnegative gain/no offset.
Select the minimum equal-fly full-clock MSE over 1--13 s, with deterministic
candidate order for ties. This is a phenomenological fluorescence model, not
identified calcium kinetics or a fit of neural parameters. Fit only the primary
four-seed mean network; transfer it unchanged to every display alternative.
Save and hash fits before any test scoring. No alternative model is selected.

Unilateral stimuli are excluded from fitting for every animal. Their prediction
tests stimulus transfer on the inherited animal partition, not fresh animals;
the literature and earlier sources were already inspected. Preserve this
exposure explicitly. Exclude any cohort lacking calibration support, reporting
the exclusion rather than borrowing another reporter's fit.

## Metrics and prospective decisions

The primary scale-invariant index is
`(|T_second-T_first|-|Y_second-Y_first|) / (|T_second-T_first|+|Y_second-Y_first|)`.
Each epoch response is the last 500-ms mean. This magnitude-based index avoids
selecting a global CW convention; it is explicitly **not** the paper's signed
discrimination index. Undefined zero denominators stay undefined. Average
paired yaw/translation observations within fly. Model each paired fly using its
actual recorded clocks, soma-side population readout and cohort observation
model, then average exactly as for the measurements. Report both signed epoch
contrasts too; magnitude discards directional sign and cannot validate it.

Primary cohorts, fixed by reporter/compartment availability before outcomes:
bIPS/sytGC7f/axon/native (expected positive) and DNp15/GC6f/dendrite/WT
(expected negative). Other cohorts are secondary, never substitutes. With at
least three paired test flies, calculate equal-fly 95% percentile bootstrap CIs
using 5,000 resamples and the configured seed. A cohort supports the expected
property only if its measured CI excludes zero in the expected direction,
the primary model mean lies in that interval, and every declared rendering
profile retains the expected model sign. Any missing prerequisite is reported
as unsupported/inconclusive; record opposite predictions separately. Overall
support requires both primary cohorts. These are predeclared comparison rules,
not a universal definition of biological validity.

Report full-clock and motion-window MSE versus a measured zero-response
comparator and correlations. For unilateral transfer, aggregate per fly and
calculate `1 - model_MSE / zero_MSE`; support requires at least three test flies
and a fly-bootstrap lower 95% bound above zero. Neither a good full-clock score
nor filter calibration substitutes for the primary selectivity comparison.

## Numerical checks, preservation and stopping

Before main simulation: check uniform sphere geometry, pixel mapping, mirrored
flow and identical stationary prefixes; compare frontend drive with the existing
batch implementation; compare a fixed yaw case at 1-ms and 0.5-ms solver steps
(maximum wide-field error <=1e-7). Refine texture raster and LED quadrature in
the same known case, retaining differences (descriptive sampling sensitivity;
no post-hoc acceptance threshold). Audit recording normalization and selected
fits with independent scalar calculations. Bootstrap uncertainty describes
measured flies, not uncertainty of the neural parameters or registration.

Retain generated LED movies (lossless uint8), source drives, network responses,
raw normalized recording arrays, all fit candidates, failures and every test
metric. Preserve source identities, figures and numerical reviews. Save a dated
progress snapshot before sealing; leave the live progress/AGENTS files outside
the index. Stop after the declared comparison. No connection changes, decoder
optimization, lesion sweep or controller. A pass would support a limited
response property under stated assumptions; walking small-turn reliability and
the external hybrid decision rule remain biologically unvalidated.
