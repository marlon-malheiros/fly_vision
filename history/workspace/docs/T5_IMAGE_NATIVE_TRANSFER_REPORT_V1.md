# T5 image-to-native transfer report, V1

Completed 12 October 2026 UTC (11 October local time).
Decision: **`NATIVE_AMPLITUDE_TRANSFER_COMPLETE`**, after separate numerical review.

## TLDR

The existing production frontend preserves the native T5 grating amplitude
benchmark when the image actually matches the native stimulus. All **64 primary
traces** preserve amplitude within the declared bounds and all **32 direction
pairs** pass. Maximum amplitude error is **0.2395%**,
DSI error **0.0006952**, and waveform maximum
error **0.036999 mV** at the existing 1°/5-ms
setting. Finer pixels reproduce all native waveforms within about 1e-12 mV.
The independent waveform solver and image checks pass, with one documented
audit-only integer-type correction. The published model's mean-response
limitation is unchanged. This is successful computational transfer under a
matched control, not population biological validation or neural degeneracy.

## Question and exact scope

The [previous physiological comparison](T5_MATCHED_GRATING_OBSERVATION_REPORT_V1.md)
found amplitude direction agreement for four pairs, but a mismatch in average
voltage between a fixed published T5 example and recordings. We tested whether
the image-input path can preserve that native amplitude result.

The experiment uses the same cell-7/iteration-52 parameters and eight grating
conditions. All eight previously selected T5 a–d/eye geometry templates are
retained; each receives a separate grating centered and aligned with its own
unchanged structural proxy axis. These templates are eight computational
placements of **one physiological model**, not eight independently recorded
neurons and not a shared full-eye scene. No T4, HS/H2, optimization or newly
collected physiological data is involved.

## Mapping and why the old image assay was different

The released author metadata uses a nine-column longitudinal aperture, dark
and background-level bars, discrete 40/160-ms phase steps and periods
320/1,280 ms. Our earlier image grating extended across the field, moved
continuously and used complementary black/white patterns; its 500-ms condition
also differs from the native 320-ms condition. These assays cannot be assumed
numerically equivalent.

The new renderer embeds the author's dark-position lists as 2.25°-wide stripes,
with background luminance 0.5 and dark luminance 0. Column centers -4..4 define
[-10.125,10.125)° longitudinal support. Stripes are constant transversely over
the raster. The inherited nine-point transverse averaging, native pitch,
geometry center and Tm2-minus-Tm9 axis are unchanged. They remain modeling
assumptions; this test does not validate the physiological axis, display
curvature or RF geometry. Central pixel pitch and dark/background grating
conventions are supported by the [original author paper](https://elifesciences.org/articles/50706)
and its [methods PDF](https://elifesciences.org/articles/50706.pdf); the exact
finite dark-column sets and timing come from our hashed author archive.

Primary images use the production 1° grid, with half-degree global pixel-center
anchor and 5-ms frames. The unchanged production `sample_population` function
samples real two-dimensional pixels. Nine saved phase images are reused by
frame index, avoiding repeated copies of identical images; eight separate
full-short-movie replays verify this cache is equivalent to temporal-frame
sampling. Its duplicated neutral adaptation hold is removed explicitly before
native times are applied. Native -100 ms maps to simulation zero, so the 25-ms
native onset is simulator 125 ms. All native events lie exactly on the 5-ms
grid. Recorded fractional clocks are preserved; no extra warmup is introduced.

Only sampled numeric contrasts enter `t5_voltage`; experiment directions do
not enter its dynamics. Author-relative Vm is obtained by adding 65 mV to
absolute model voltage. Primary readout and paired thresholds reuse the previous
frozen observation analysis: own [-100,0) baseline and complete cycles 2–3,
robust amplitude (q95−q05)/2, signed pair DSI, response/difference floors 0.065 mV
and |DSI|>=0.1. Mean and harmonic diagnostics are preserved. The transfer bounds
are 5% relative amplitude error and 0.02 absolute DSI error, inherited from prior
engineering checks, not physiological confidence intervals.

The [protocol](T5_IMAGE_NATIVE_TRANSFER_PROTOCOL_V1.md), code, thresholds and
input dependencies were frozen before new transfer responses. Historical native
scores were already known. Complete hashes and the starting Git checkpoint are
in [the prospective manifest](../results/t5_image_native_transfer_v1/prospective_manifest.json).

## All primary and refinement results

There are **280 trajectories**: 64 primary, 64 half-frame, 64 half-pixel, 64
quarter-pixel, 16 deliberate mismatch controls and eight native reference replays.
All complete. The primary remains 1°/5 ms regardless of refinement results.

| Setting | Amplitude preserved | Direction pairs preserved | Strict identity | Max amplitude error | Max DSI error | Max Vm error (mV) |
| --- | --- | --- | --- | --- | --- | --- |
| primary | 64/64 | 32/32 | 24/64 | 0.239505% | 0.000695183 | 0.0369987 |
| half_frame | 64/64 | 32/32 | 24/64 | 0.239505% | 0.000695183 | 0.0369987 |
| half_pixel | 64/64 | 32/32 | 64/64 | 3.00591e-12% | 1.82077e-14 | 9.9476e-13 |
| quarter_pixel | 64/64 | 32/32 | 64/64 | 3.00591e-12% | 1.82077e-14 | 9.9476e-13 |

The 1° primary sampled-input maximum discrepancy is 0.003530562 unit
contrast; 24/64 primary traces satisfy the separate strict identity criterion.
The small remaining raster interpolation error does not prevent amplitude
transfer: every trace and pair passes. The smallest primary amplitude DSI is
0.103366171, close to the project 0.1 floor, so threshold margins remain
visible in complete scores.

At 0.5° and 0.25° pixels, all 64 waveforms per variant satisfy strict identity;
these are numerical matches to the original native model, not an improvement
in fit to physiological recordings. Halving the frame interval changes relative
amplitude by at most 3.79359e-14, and
DSI by at most 2.05946e-14. Temporal sampling adds
essentially no error here because native phase events align with both frame
grids. This conclusion need not hold for continuously moving textures.

![All primary direction pairs](../results/t5_image_native_transfer_v1/amplitude_transfer_all_pairs.png)

![Matched raster and actual sampling points](../results/t5_image_native_transfer_v1/matched_pixel_mapping.png)

## Deliberate mismatch controls

For the pre-existing T5a_R geometry, extend the periodic grating outside the
native aperture or delay all events by one 5-ms frame. All 16 controls exceed
the predeclared input and waveform mismatch thresholds:

| Control | Cases detected | Vm error range (mV) |
| --- | --- | --- |
| full_field | 8/8 | 0.375443–2.987363 |
| late_frame | 8/8 | 1.812083–2.457876 |

Control detection does not require direction reversal or amplitude failure.
Different stimuli can retain similar direction preference. Direct input and
waveform comparisons make these discrepancies visible instead of declaring
every directional response equivalent.

![Every refinement and control](../results/t5_image_native_transfer_v1/transfer_refinements_and_controls.png)

## Numerical validation and the retained audit correction

**19 focused tests passed**, including translated/rotated geometry, finite
aperture versus tiling, event boundaries, the extra native hold, timing delay,
OFF contrast, full-movie/cache equivalence and prior numerical/readout checks.
All 25 raster dictionaries agree bitwise with separately implemented stripe
interval reconstruction. SciPy bilinear interpolation gives a maximum contrast
discrepancy of 0 from production
sampling. Full-movie/cache equivalence passes for all eight geometry templates.

All **280 waveforms** pass an independent augmented-matrix-exponential solver
for the four published filter equations. Maximum error is
**1.54898316396e-12 mV**, below
the frozen 1e-8-mV numerical tolerance. Independent sums, sorted quantile
interpolation and harmonic normal equations differ by at most
8.881784197e-15. Native reference replays
agree with the previous author-RHS-validated native outputs. The parameter
vector remains bitwise unchanged. This review is separate computational
implementation by this agent, not an external scientific reviewer.

The initial independent raster audit stopped on `uint8` position metadata plus
negative tile offsets (`OverflowError`). The original frozen script, inputs,
outputs and scores were retained. A separately hashed, post-score wrapper
converts only those metadata arrays to signed integers, verifies every value
is unchanged and reruns the same audit. This changes no simulation, readout,
criterion or scientific decision. See [the explicit amendment](T5_IMAGE_NATIVE_TRANSFER_REVIEW_AMENDMENT_V1.md),
[failure record](../results/t5_image_native_transfer_v1/review_failure_v1.txt) and
[corrected review](../results/t5_image_native_transfer_v1/independent_review.json).

Five predecessor indexes and all 10,105 indexed entries passed verification
before execution; final preservation is recorded at completion. The counts
overlap and are not independent scientific observations.

## What this resolves and what remains open

We now have a passing, fixed-parameter **image-to-native OFF-grating amplitude
benchmark** at the production resolution. The pixels-to-contrast-to-voltage
path can reproduce the intended native computation under this matched stimulus;
a full frontend rebuild is not supported by this result. Pixel refinement also
shows how to obtain strict numerical identity for this control.

Primary image mean criteria pass **0/32**; the native means remain
0/4 under the chosen strength criterion, with two native slow cases near the
cutoff. The earlier model/recording mean discrepancy therefore remains. The
image path successfully transferring the native model is a different claim
from the native model reproducing measured average voltage. The gray recording
traces below retain the observable biological mismatch.

![All eight native, image and recording traces](../results/t5_image_native_transfer_v1/image_native_recorded_waveforms.png)

This experiment does not explain random-texture sign reversals, establish
biological RF geometry or population validity, reproduce T4/HS/H2, or demonstrate
neural degeneracy. No parameter was adjusted to obtain the match. Its defensible
result is successful transfer for a precisely defined native control, with
technical correction and remaining scientific limitations preserved.

The next bounded scientific check should use the existing moving-bar recordings
as a second stimulus family: match their image and native schedules, retain the
appropriate native response measure and measured/model discrepancies, and keep
parameters fixed. This tests transfer beyond the deliberately matched grating
benchmark before population or degeneracy work. It is proposed, not executed
here; available archive observations suffice for that same-cell comparison,
while new-cell validation would require independently chosen cells and uncertainty.

## Evidence and development record

Complete values are in [trace metrics](../results/t5_image_native_transfer_v1/trace_metrics.csv),
[all paired scores](../results/t5_image_native_transfer_v1/pair_metrics.csv),
[analysis](../results/t5_image_native_transfer_v1/analysis.json),
[input hashes](../results/t5_image_native_transfer_v1/input_manifest.json), and
[technical review](../results/t5_image_native_transfer_v1/independent_review.json).
Every raster dictionary and input/output is retained in that study directory.
PNG and PDF figures are available alongside these tables.

Progress is continuously recorded in [the live report](PROJECT_PROGRESS_REPORT.md).
The study includes [a dated snapshot](../results/t5_image_native_transfer_v1/project_progress_snapshot.md),
[local Git checkpoints](../results/t5_image_native_transfer_v1/git_snapshots.json),
[completion record](../results/t5_image_native_transfer_v1/completion.json) and
[immutable artifact index](../results/t5_image_native_transfer_v1/artifact_index.json).
The live report and AGENTS.md remain appendable and are excluded from the seal.
All previous evidence remains preserved; records are local, not an off-device
backup. Reproduction uses `prepare`, `execute` and the corrected `review` wrapper
in the study scripts, in a fresh copy/output version; never overwrite sealed V1.
