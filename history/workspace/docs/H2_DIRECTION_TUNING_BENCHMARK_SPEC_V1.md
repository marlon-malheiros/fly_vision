# One H2 direction-tuning benchmark: specification V1

25 October 2026. This specifies a separate **stimulus-family comparison** to
real recordings. No neural score is produced in the trial-metadata study.
Original aggregate summaries have already been inspected: these seven animals
cannot be described as fresh external validation. Freeze any implementation,
uncertainty variants and analysis before opening model predictions.

## Question and observations

Does the frozen surrogate reproduce the local preferred direction of left H2
for bright/dark edges at the measured display locations? This tests a visual
response property needed for interpretable yaw work. It does not test walking,
small-turn detection, bIPS necessity or motor control.

Use the checked source index and all 16-direction signed spike-rate curves.
Retain the full-source set and flag the author's published-summary subset;
never remove a curve based on model agreement. Record every original protocol
ID and per-protocol step interval, including discrepancies from the Methods.
Compare only a biologically identified left-H2 output, with right-eye visual
input held at the documented background/occluded condition. Do not equate an
arbitrary neuron mean with the recorded intracellular observable.

Primary derived measurement: circular error of the PD vector, separately for
each cell, display protocol and position, first averaging **signed** bright
and dark curves at each direction, then subtracting the minimum across
directions and taking the vector sum. Use atan2 and explicitly retain flat or
undefined curves as missing/undefined, not zero-error. Secondary endpoints:
per-polarity PD, dimensionless min-shift vector DSI, and Pearson correlation of
signed direction curves after a separately specified observation transform.
Spikes/s, model rates and calcium/voltage are different observables. Do not
claim absolute firing-rate agreement without an independently calibrated
measurement model. A constant gain alone does not establish such a model.

## Stimulus and spatial frame

The paper specifies a cylindrical G4 display, approximately 240° azimuth,
50° elevation, about 1.25° per pixel, circular edge window of diameter 21
pixels, mid-intensity background, 16 directions and nominal 40-ms edge steps.
The decoded table retains radius 10, intensity, frame numbers, positions and
step-interval fields. The pinned author helper `Eyal_arena_2023` supplies an
inch-based arena geometry, arena/head pitch rotations, translations and the
projection into spherical eye coordinates; the summary spreadsheet supplies
per-recording angles. `proc_ephys.R` explicitly renames headAngPitch to
headAng. Preserve that transform including its sign conventions, rather than
rotating the predicted result until it agrees. Head yaw is measured but this
helper does not apply it; document that approximation and its uncertainty.

A renderer must implement rays intersecting the actual cylinder and its
rotations/translations, not directly paint a circular spherical-eye patch.
Reconstruct a documented stepwise edge family from the table. Verify each
orientation's sign from primary generator code or independently justified
arena conventions, not neural response peaks. Establish whether relOrt,
first/full/last frame numbers, and the step interval fully determine edge
frames; retain unresolved pixel rounding, pattern origin and timing rules.
If no exact pattern arrays/generator or photometric calibration are available,
label every simulation an approximate stimulus-family comparison. An image
reconstruction is not an exact replay merely because its speed is plausible.

## Separation, uncertainty and decision

No neural parameter fit is allowed for this first comparison. For any later
observation calibration, split by animal (cells 1–4 calibration, cells 5–7
locked test) before inspecting model predictions; never split directions or
repeats from the same animal across fitting and test. These are computational
held-out partitions of previously inspected animals, not new biological data.
Leave the frozen source-window counting rule fixed. Any tuning of the
observation model beyond calibration animals invalidates that test partition.

Report per-animal results and all curves; uncertainty uses an animal-level
bootstrap (10,000 draws, seed 20261025) with repeats resampled within
conditions. Preserve the source protocol baseline weighting when resampling.
With seven animals, show the individual values and avoid precision claims.
Freeze all rendering/head-pose variants from documented uncertainty ranges
before model scoring; no best-convention selection from agreement.

For the primary error report a cell-weighted mean absolute circular PD error,
with every cell equally weighted and its available published positions equally
weighted. Report full-source and published-subset results separately. Compare
with a position-independent horizontal-direction reference selected from the
**documented convention**, not fitted to these responses. No biological
pass/fail tolerance is justified by current evidence: report estimates and
uncertainty, not a retrospective acceptance threshold.

## Gates before a model comparison

1. All-row trial correspondence, repeat counts and clocks independently pass.
2. Source spike counting and frame-derived windows independently pass.
3. Demonstrate orientation sign, cylinder-to-eye projection and left-H2
   identity; distinguish an exact replay from an approximate edge family.
4. Specify the frozen model time-to-ms relationship, pre-stimulus adaptation,
   occlusion/background, spatial coverage and observation statistic. Any
   unsupported choice must be a declared approximation, with variants frozen
   before predictions; do not claim quantitative physiological validation.
5. Freeze model hash, rendering implementation, calibration/test ledger,
   observation mapping and all analyses before scoring.

A failed gate means complete and preserve the metadata/source task, name the
specific missing constraint, and do not invent a score. A supported approximate
family comparison can be a later exploratory study; it remains distinct from
recording-matched physiological validation and from yaw-threshold studies.

## Primary provenance

[Zhao et al. paper and Methods](https://www.nature.com/articles/s41586-025-09276-5),
[H2 raw deposit v2](https://doi.org/10.25378/janelia.28462100.v2),
[author transform at the pinned commit](https://github.com/reiserlab/eyemap_T4/blob/99d2a43123db636cedb55af9ff31a59657e7d17e/eyemap_func.R),
[processing script](https://github.com/reiserlab/eyemap_T4/blob/99d2a43123db636cedb55af9ff31a59657e7d17e/proc_ephys.R).
