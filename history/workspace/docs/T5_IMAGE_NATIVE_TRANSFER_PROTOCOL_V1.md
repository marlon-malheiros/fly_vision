# T5 image-to-native transfer protocol, V1

## Scope and prior knowledge

Test whether the existing production image sampler preserves the fixed T5
model's native grating amplitude direction, without fitting circuit parameters.
Prior native observation comparisons already establish the model's amplitude
direction classification in all four pairs and its mean-response limitation.
This is a computational transfer test, not additional biological validation.
Use all eight published grating conditions and all eight previously selected T5
geometry templates (a–d × two eyes). These placements share one recorded-cell
model; they are not independent physiological cells. No T4 or HS/H2 execution.

## Spatial mapping frozen before new responses

Keep the production sampler `physiological_population.sample_population`, native
positions -13..13, inherited 2.25° pitch, nine transverse points -9..9°, and the
unchanged geometry centers and Tm2-minus-Tm9 structural proxy axes. The pitch is
an inherited central-display approximation; diagonal/peripheral geometry and
physiological preferred axes are not validated. Each condition is an RF-centered
grating aligned with that template's own proxy axis, not one common world movie.

For each author phase, render longitudinal columns -4..4 as half-open stripes
centered at native column ×2.25°, each 2.25° wide. Published `PosD_mg` identifies
dark stripes (luminance 0); all other pixels have background luminance 0.5.
Bars are constant transverse to the proxy axis over the local raster. The
longitudinal stimulus aperture is [-10.125,10.125)°; no infinite-field extension
is used in the matched case. This is an explicit embedding of the author's
one-dimensional input metadata, not a reconstruction of LED-display curvature
or unknown transverse stimulus edges.

Primary raster: the existing population pixel pitch **1°**, anchored at global
pixel centers 0.5° + integer multiples of pitch, within approximately ±40° of
each geometry center. Half/quarter pixel variants have pitches 0.5°/0.25° with
the same anchor and cover all sampled points. Use decreasing elevation as in
production movies. No response-dependent alignment or geometry correction.

Save a nine-image dictionary (background plus eight phases), and sample it using
the unchanged production sampler. Explicitly remove only that function's extra
duplicate adaptation hold to recover the nine spatial contrast arrays. Assemble
time sequences by looking up those sampled arrays. This is equivalent to
sampling a full repeated movie because the sampler acts independently on each
frame. Verify that equivalence with actual short movies for all eight placements.
Only pixel-derived numeric contrast enters the neural simulator.

## Native timing and all cases

Native time -100 ms maps to simulator 0; onset 25 ms maps to 125 ms. The author
phase advances every 40 or 160 ms, for three eight-step cycles plus the original
extra final hold. Initial neutral contrast and zero filter states match the
native model. Primary frames are 5 ms; the onset and every native transition
land exactly on this grid. Retain actual fractional observation clocks, append
simulator zero only to satisfy the fixed forward API, and remove that added
sample from comparison output. Convert absolute model Vm to author-relative mV
by adding 65. Use the unchanged `t5_voltage` numerical routine.

Execute 64 primary traces, 64 half-frame (2.5-ms) traces, 64 half-pixel traces and
64 quarter-pixel traces. Add eight native reference replays. For the pre-existing
T5a_R template, execute eight full-field controls (periodic stripe extension,
same timing) and eight late-frame controls (matched aperture, all events 5 ms
late). Total: **280 trajectories**, with 272 image-driven cases and eight native
references. These controls must be retained even when amplitude direction still
passes; a stimulus difference need not reverse direction.

## Measurements and decisions

Reuse the previous frozen matched-observation baseline [-100,0) ms and cycles
2–3, on identical recorded clocks. Report robust half-quantile amplitude, signed
mean and secondary fundamental-harmonic amplitude, all four paired DSIs and
their fixed 0.065-mV/0.065-mV/0.1 criteria. Include direct sampled-input errors,
waveform maximum error/RMSE, and observed/model discrepancies. No new scores
may redefine preferred direction, select cells/phases or replace the window.

Primary amplitude transfer passes only if every primary trace has relative
robust-amplitude error <=5% (denominator floor 0.065 mV), every primary pair
has |image DSI−native DSI|<=0.02, and expected-direction classification passes
in all 32 pairs. Require the same amplitude criteria in all three refinement
variants, plus primary-to-half-frame amplitude/DSI agreement by those bounds.
These inherited engineering bounds are not physiological uncertainty estimates.
Report how close values are to thresholds and quantitative waveform errors.

Strict numerical identity is separately flagged when sampled contrasts agree
within 1e-7 and waveform maximum error <=1e-8 mV. Passing amplitude transfer does
not imply strict identity or full waveform accuracy. Mean/harmonic diagnostics
do not change the amplitude decision. Keep the previous native mean limitation.

Negative-control mismatch detection requires each control's input maximum error
>0.1 and waveform maximum error >1e-4 mV. It does not require amplitude failure.
Numerical/alignment/sampler audit failure gives `TECHNICAL_COMPARISON_INVALID`;
otherwise decision is `NATIVE_AMPLITUDE_TRANSFER_COMPLETE` when the primary and
refinement conditions pass, or `NATIVE_AMPLITUDE_TRANSFER_INCOMPLETE` otherwise.
Finer resolution success must not relabel a failed 1° primary comparison.

## Verification and evidence

Meaningful tests cover finite-aperture versus tiled input, phase/onset/extra-hold
boundaries, latency, translated/rotated geometry, dark/background contrast and
phase-dictionary/full-movie equivalence. Review saved raster pixels with separate
stripe-interval logic, all spatial samples with SciPy interpolation, and all 280
waveforms with independent augmented-matrix-exponential propagation. Check all
eight native replays against the saved matched reference and author RHS. Review
amplitude/mean arithmetic with independent sorted quantiles/sums, preserving
primary failures and diagnostic metrics. Check predecessor indexes and all
10,105 indexed entries before and after work (counts overlap). Save full case
tables, input/output arrays, protocol/hash manifest, figures and report/TLDR.
Append ongoing progress, record local Git checkpoints and seal artifacts with a
dated snapshot of the live report; exclude live files from the immutable index.
