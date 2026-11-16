# T4 image-to-direct-voltage component test V1

2026-11-05. The user authorized another round. Actual32x96 LED patterns,
frame-event timestamps and20kHz raw electrical recordings are available in the
first prespecified Gruntman2018 file. Five cells were selected before voltage
scoring by published assignment/date; cells1–2 are development,3–5 test. Earlier
pooled figure values are familiar, but these individual waveforms and model
scores remain uninspected at freeze. All earlier circuits/results and four
unscored C2/C3 flies remain unchanged.

This is a **canonical PD-axis source-component test**. The modeled source drive
is not a simulated MaleCNS T4 membrane potential. Test its predictive content
after one development-only output gain; a signed internal-potential diagnostic
assesses information discarded by the adapter. No full graph solve or claim
of whole-circuit physiological validation.

## Admitted data and input geometry

Use the five cells/dates in
[source-admission protocol](T4_DIRECT_VOLTAGE_ADMISSION_PROTOCOL_V1.md), all four
dwell times20/40/80/160ms, all recorded repeats. Actual movie content and logged
positions supersede a newly invented grating or apparent-motion movie. Decode
voltage as native column3 times10 to mV; native timestamp ticks are microseconds,
as specified by the original author extraction function. Inspect only stimulus
and timing metadata before this freeze. Do not decode the opaque MATLAB table
when ordinary stimulus structures contain the necessary association.

Stored frame labels are0..N−1, with initial frame0 repeats and a terminal reset
to0. Keep all frame events in time order; reset selects the same stored grey
frame. The first non-grey frame defines onset. Grey level3 and white7 in the
3-bit movies map to luminance3/7 and1. Degree spacing is the recorded
`dpsFreq/generalFrequency` (2.25deg perLED), not a fitted spatial scale. Linear
LED luminance and local Cartesian angular geometry remain assumptions.

Movie rows have the opposite vertical convention from `gridCenter`: verify
the movie's motion-center centroid against `[gridCenter.x−1, nrows−gridCenter.y]`.
Use that source-defined center without response-based RF shifts. The initial
schema helper's mistaken terminal-index assertion was preserved and corrected
before any amplitude scoring; it did not change source data or acceptance.

For each cell, the first chronologically recorded repetition of each of the32
conditions is a **localizer**. Baseline-subtract it over[-250,−50)ms. Choose one
PD orientation from the eight by the mean99.5th-percentile response across all
four dwell times during motion plus50ms; break exact ties by smallest orientation.
The opposite orientation is PD+4 modulo8. This early-only calibration identifies
a canonical axis; it cannot validate anatomical subtype direction. Score only
the later two repetitions of those PD/ND conditions; no scored response may
choose the axis, RF center, gain, filter, temporal shift or exclusion.

Obtain physical axis from displacement of the actual movie's first/last bright
pixel centroids for the chosen PD, using image geometry rather than response
sign or a hand-selected angle. Sample along this axis through the recorded RF
center. Piecewise-constant LED pixels use symmetric half weights on exact
pixel boundaries. Normalize with the unchanged sigma and7x7 physical1deg
contrast-energy footprint in canonical coordinates. Apply the existing5.7deg
1D Gaussian, fixed measured250ms-deconvolved Mi9/Mi1/Tm3/Mi4/CT1 kernels,
5deg branch offsets and author relative conductances. The longitudinal Gaussian
and transport to each cell's canonical axis are existing-source modeling
assumptions; transverse RF physiology is not reconstructed. Outside-panel
computational padding is constant grey, not an expanded physical arena.

## Two fixed outputs and calibration

Primary: the existing delivered drive `max(V_branch,0)/60`, bounded0..1.
Diagnostic: signed pre-rectification `V_branch` from the exact same branches,
conductances and denominator. Preserve all neural parameters. Prove exact
agreement between the rectified diagnostic and the existing adapter on synthetic
signals. The diagnostic is not a newly measured voltage-to-release interface.

Subtract each modeled output's own pre-motion baseline. Fit one nonnegative
zero-intercept gain per output, on development cells1–2 only, equally weighting
cells and the eight PD/ND×dwell conditions. No neural or input parameter,
baseline offset, time lag, direction reversal or architecture search. Freeze
the two gains and numerical checks before opening any test-cell localizer or
scored voltage. Test cells may then use their predeclared early-only localizer.

Bin raw voltage into2ms intervals, preserving signed voltage changes. Predict at
bin centers using the recorded frame-event input. Mean the two scored repeats
within each condition before metrics; retain individual traces. Use motion
onset through nominal movie motion duration plus250ms. Compare with zero and a
direction-blind waveform reference, the mean of that cell's PD and ND **localizer**
traces at the same dwell. Source timing jitter stays in inputs, never fitted away.

## Frozen decisions and checks

Report each cell's mean squared error over its eight conditions, then weight
cells equally. Skill=1−MSE/MSE_reference. Enumerate all27 three-cell bootstrap
resamples with fixed gains. Require positive pooled skills against both
references, positive zero skill in every test cell, and5th percentile of the
joint minimum of both bootstrap skills >0. This is a restricted predictive
criterion, not a physiological equivalence margin.

Also test inhibition independently of dominant positive peaks. In each cell's
160ms-ND localizer, average with a20ms boxcar; identify runs of at least20ms
below−3 times the baseline2ms-bin SD. This mask is fixed from the localizer.
For masks whose later-repeat mean is negative, require the predicted mean there
to be negative. Require at least two confirmed test-cell masks to qualify this
inhibitory check. No mask may be selected or shifted from test predictions.
A restricted component passes only if the waveform, inhibition and numerical
guards pass. Report partial positives and all failures separately.

Three focused tests cover signed/rectified parity, pixel-boundary geometry and
binning/early-mask independence. Mandatory cell1 PD/ND20/160ms temporal and
spatial refinements are separate: ≤5% RMS difference relative to that output's
primary maximum absolute score-window response. Independently check native
timestamp/frame lookup, scalar voltage bin means, output gain, all test-cell
metrics and all27 bootstrap cases in a later process. Retained old studies
must rehash unchanged. No old movie archive regeneration.

One worker;1200 scientific CPU seconds,2GiB RSS target,320MiB total output cap,
20GiB disk reserve. Store compact scored/localizer/output traces, not source
filter fields or new movies; original source movies already reside in the raw
MAT files. If both development gains are zero or numerical guards fail, stop
before test-voltage scoring. Preserve exceptions and use explicit corrections.
Append dated project progress, archive progress/method copies, seal after writer
exit and verify in a separate process. No new walking/yaw qualification.
