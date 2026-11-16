# Stationary-flash calibration and motion transfer: V1 with numerical R2/R3

2026-11-06. Admission freeze `3d67fed`; scientific freeze `44df452`;
warm-start correction `e8a949d`; recorded-duration correction `90ff3b6`.

**The flash repeat-prediction criterion passes; the motion-transfer criterion
does not.** Flash-derived position/timing/gain improves the previously failing
motion cell5 but worsens cell4. Neither the primary nor its diagnostics meets
the frozen motion uncertainty rule. The final numerical checks pass. This
completes the proposed experiment, not full biological validation or small-turn
qualification.

The result narrows the problem: this fixed source model can predict withheld
stationary repetitions under limited registration calibration, but that
calibration does not reliably transfer across stimulus classes in all cells.
No graph, cable conductance, synaptic time constant or neural connection was
tuned; no moving response selected the new parameters.

## Data, splits and biological provenance

Three stationary-flash MAT members were selected before flash-response scoring,
covering the complete preceding motion-comparison cohort: original cells3,4,5,
dates20160427/20160428/20160502. Sources are the
[Gruntman2018 public experiment](https://doi.org/10.25378/janelia.5576101),
interpreted using the author's stimulus/extraction scripts and
[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5967973/).
Only the three required ZIP members were downloaded by verified HTTP ranges;
size, CRC32 and SHA256 receipts pass. Raw files total189,559,908bytes, retained
once. No2.84GB archive,1.16GB aggregate MAT or new movie archive was acquired.

| Cell | Flash positions × durations | Trials | Fit repetitions | Repeat-test repetitions |
| --- | ---: | ---: | ---: | ---: |
| 3 | 11 × 4 | 220 | First3 per condition | Last2 per condition |
| 4 | 17 × 4 | 340 | First3 per condition | Last2 per condition |
| 5 | 13 × 4 | 260 | First3 per condition | Last2 per condition |

All820 trials/164 conditions remain included. Chronology is native recording
start time:492 trials calibrate the model registration;328 test repetitions.
There is no response-based animal, trial or condition replacement.

The existing moving responses for these cells were already inspected. Their
later two repetitions at PD/ND×four dwell times yield48 motion trials/24 means.
The motion test is retrospective stimulus transfer, not a new animal cohort.
The original author population cable parameters were also fitted using this
experiment's stationary-flash cohort. Thus even the project-withheld flash
repetitions are not proven independent of the original author parameter fit.
R2/R3 additionally use flash repetitions already inspected in V1. These limits
prevent a claim of fresh external biological validation.

## Frozen model and calibration

The full published cable stays at344 sections,235 dendritic sections,99E/55I
sites, seed300 and its12 original parameters. MaleCNS, the original frontend,
all earlier models/results and the four C2/C3 holdout animals remain unchanged.
No electrical conductance, absent pathway or artificial neural logic is added.

Actual32×96 images define stimulus patterns; recorded frame events and native
20kHz electrical timestamps define timing. Use channel3×10mV, integer-microsecond
half-open2ms bins, baseline[-250,−50)ms and flash score[0,duration+350ms).
Physical LED pitch is2.25deg. Grey3/bright7 map to native source inputs0/1.

Metadata reveals diagonal stationary series in cells4 and5 relative to the
previously fixed canonical motion axis. An unused single-bin draft was therefore
retained and replaced before scientific freezing. Actual images are sampled at
all eleven source positions for each registration, without treating centroid
projection as the input bin. All patterns happen to be exactly one-hot or empty:
44 native pulse patterns plus four empty cases. This is a verified property of
these images; no spatial voltage superposition is used. The source RF/temporal
shape remains fixed and is tested rather than freely reconstructed.

For each cell evaluate the predeclared5×51 grid: offsets−2..2 LED pitches and
causal delays0..100ms in2ms steps. For each pair fit one nonnegative common
voltage gain, minimizing mean MSE over the first three flash repetitions,
equally weighted by condition. All765 fit cases per numerical version are saved.
No RF width, E/I strength, cable time constant, lag sign, axis or per-condition
gain is searched. Bounds are modeling allowances, not measured physiological
ranges. No final selection is on a boundary.

Final R3 flash-only registrations:

| Cell | Offset along canonical axis | Effective input delay | Voltage gain |
| --- | ---: | ---: | ---: |
| 3 | 0 pixels / 0deg | 30ms | 1.37036263 |
| 4 | −1 pixel / −2.25deg | 20ms | 0.78175283 |
| 5 | +1 pixel / +2.25deg | 40ms | 0.67833070 |

The delay can absorb measurement/stimulus/model timing differences; it is not
an identified synaptic conduction delay. The scalar is observation calibration,
not a measured conductance or voltage-to-release relation. Canonical-axis,
one-dimensional source support and transverse integration remain assumptions.

Candidates are fixed: **flash-calibrated primary**(offset/delay/gain), diagnostic
with the same learned offset/delay and physical-voltage gain1, and the unchanged
cable baseline. No diagnostic is promoted after its score is inspected.

## Numerical failures and corrected forward predictions

All earlier versions are preserved, including stopped motion decisions.

1. **Metadata serialization:** strict JSON rejected source `intFrames=NaN` after
   image/time audit, before amplitude processing. The partial stream is retained;
   a [separate metadata wrapper](T4_FLASH_METADATA_CORRECTION_R2.md) writes
   missing metadata as null. Source data and scientific rules are unchanged.
2. **V1 cold-template mismatch:** initial source Vm−65mV was inconsistent with
   image runs after300ms grey prehistory, whose baseline is~−64.989882mV. The
   source's finite SEClamp resistance floor on future-active sites produces
   this small initialization offset. All4 comparisons fail the0.005mV guard
   (maximum0.010629mV), so V1 motion stops. Flash prediction already passes;
   this is not a numerical change devised to rescue a failed flash score.
3. **R2 warm-start repair:** regenerate the44 nonzero templates with identical
   grey prehistory and baseline subtraction, preserving source physiology.
   Two checks still fail(max0.008670mV). Actual pulse lengths differ slightly
   from nominal: control durations20036/160016/19998/160056us. R2 motion stops.
4. **R3 recorded-duration refinement:** derive min/nominal/max pulse lengths
   from timestamps only; simulate132 warm source anchors, plus four exact
   empty cases. Predict each trial by interpolation between its bracketing
   duration anchors, averaging the correct three-fit or two-test repetitions.
   This interpolates one forward model versus input duration, not different
   spatial sources. No extrapolation, response-fitted interpolation, threshold
   relaxation or new neural parameter. Record1ms, integrate0.1ms; actual motion
   runs retain the complete recorded event stream.

The [warm-start protocol](T4_FLASH_TRANSFER_WARM_START_R2.md) and
[timing protocol](T4_FLASH_TRANSFER_EXACT_TIMING_R3.md) were frozen before their
new numerical outcomes. R3 timing anchors in microseconds are:

| Nominal | Minimum | Nominal anchor | Maximum |
| --- | ---: | ---: | ---: |
| 20ms | 19933 | 20000 | 20085 |
| 40ms | 39910 | 40000 | 40152 |
| 80ms | 79903 | 80000 | 80112 |
| 160ms | 159919 | 160000 | 160105 |

All8 independent midpoint checks pass(max2.88927e-5mV), all4 actual-image
template checks pass(max0.000239054mV), and all4 motion0.1→0.05ms solver checks
pass(max0.00286565mV). Every threshold remains0.005mV. Five focused numerical/
software tests pass. Numerical consistency is separate from physiological fit.

## Stationary repeat-prediction result

Reference predictions are zero and a spatially blind calibration waveform,
averaged across positions separately at each dwell/cell. Conditions then cells
receive equal weight. Skill is `1−MSE/reference_MSE`. Require positive pooled
skills, positive zero skill in every cell and positive5th percentile of the
joint minimum skill over all27 cell-bootstrap resamples. This is a restricted
prediction rule, not physiological equivalence.

| R3 stationary candidate | RMSE, mV | Zero skill | Spatial-blind skill | Joint lower bound | Rule |
| --- | ---: | ---: | ---: | ---: | --- |
| **Flash-calibrated primary** | **2.410351** | **+0.660275** | **+0.536222** | **+0.392049** | **Pass** |
| Registered, physical gain1 | 2.491994 | +0.636871 | +0.504272 | +0.384357 | Pass |
| Unchanged cable | 2.833532 | +0.530513 | +0.359077 | +0.148777 | Pass |

Primary spatial-blind skills in cells3/4/5 are+0.676383/+0.390102/+0.397857.
The baseline also passes: this is evidence of predictive stationary response
structure under the source assumptions, not proof that the new calibration
alone creates that computation. It improves the restricted benchmark.

[Flash decision](../results/t4_flash_transfer_v1/recorded_timing_r3/flash_decision.json),
[flash maps](../results/t4_flash_transfer_v1/figures/flash_maps_r3.png).
For diagonal series the plotted axis is only projection; full images enter
predictions. Differences in the measured multi-lobed RF structure remain visible.

## Motion-transfer result without refitting

The primary registration/gain remains fixed from stationary flashes. Motion
references, response windows, bootstrap rule and signed observations are the
same as the preceding full-cable study.

| R3 motion candidate | RMSE, mV | Zero skill | Direction-blind skill | Joint lower bound | Rule |
| --- | ---: | ---: | ---: | ---: | --- |
| **Flash-calibrated primary** | **4.925398** | **+0.658928** | **−0.017603** | **−0.268560** | **Fail** |
| Registered, physical gain1 | 4.480536 | +0.717757 | +0.157915 | −0.087888 | Fail |
| Unchanged cable | 5.044183 | +0.642278 | −0.067278 | −0.285436 | Fail |

| Cell | Previous direction-blind skill | Flash-calibrated motion skill | Registered physical diagnostic |
| --- | ---: | ---: | ---: |
| 3 | +0.073112 | +0.109589 | +0.406199 |
| 4 | +0.172545 | **−0.440254** | −0.312223 |
| 5 | −0.459093 | **+0.310042** | +0.418917 |

Cell5 MSE decreases34.379103→16.256772mV², while cell4 worsens
20.797303→36.199423mV². We retain both. The primary remains1.76% worse than the
direction-blind reference overall. The physical-gain diagnostic beats that
reference on average, but its frozen uncertainty guard fails. Selecting it
after observing this difference would not establish the primary claim.

The unchanged160ms-ND inhibition masks remain0/3, so inhibitory qualification
is unavailable. The joint primary flash-to-motion waveform criterion is false.
No new walking, yaw threshold, downstream HS/H2/bIPS/DNp15 or closed-loop result
is established. No held-out moving cohort/C2C3 animal was opened.

[Motion decision](../results/t4_flash_transfer_v1/recorded_timing_r3/motion_decision.json),
[motion waveforms](../results/t4_flash_transfer_v1/figures/motion_transfer_r3.png),
[564 complete condition-output rows](../results/t4_flash_transfer_v1/condition_metrics_r3.csv).
PNG/PDF figures, individual traces, all fit grids and bootstrap arrays remain.

## Independent audit, storage and reproduction

Each V1/R2/R3 review independently reconstructs all820 native flash traces,
the chronological split, actual-pixel mappings,765 weighted-regression grid
cases, minima and flash statistics. R3 additionally verifies recorded-duration
mixtures and24 motion means. Max R3 native-bin error5.68e-14mV, fit-grid
error1.42e-14 and readout/reference error4.26e-14mV; metric/bootstrap error
7.11e-15. A final check independently recomputes all12 versioned parity tests,
four solver comparisons, masks, joint criterion and unchanged prior artifacts.
[R3 review](../results/t4_flash_transfer_v1/recorded_timing_r3/independent_review.json),
[final checks](../results/t4_flash_transfer_v1/final_bookkeeping_review.json).

All466 indexed preceding cable artifacts rehash unchanged. No retired movie
archive was rebuilt. A plot-helper list/array error and overlapping colorbar
were corrected before sealing; initial scripts/figures and the valid initial
CSV are preserved/verified. They did not change scientific results.

There are248 new NEURON solves,45.013101 child CPU seconds, peak worker
RSS580,194,304bytes. These exclude acquisition, parent-process flash grid fits,
preprocessing, reviews and plotting; they are not total project CPU. Before
snapshots the study occupies224,704,850bytes, under256MiB, of which189,559,908
are the single raw copy. No new large movies or full-brain simulation.

Use the repository scientific Python with `PYTHONPATH=src:scripts`,
`PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`; simulator workers use
the pinned Python3.11/NEURON8.2.7/NumPy1.26.4 temporary environment. In a fresh
output location reproduce admission, then V1 stages `freeze bank fit flash_test
numerical motion`. Reproduce R2 `freeze bank fit numerical flash_test motion`.
For final R3 use `freeze bank midpoints fit numerical flash_test motion` in
`scripts/t4_flash_transfer_timing_r3.py`. V1/R2 motion stops are expected and
must be preserved. Run `review_t4_flash_transfer_v1.py` with no flag, `--warm`,
and `--recorded`, then plotting, final completion checks, post-writer seal and
separate-process verification. Original methods are imported unchanged by
the explicit versioned adapters; raw MAT source paths are read-only aliases.

## Supported next alternatives and undergraduate explanation

Registration, causal delay and a common amplitude factor are insufficient for
robust stimulus transfer in this model/sample. This does not prove that T4
modeling or biological validation is impossible, or uniquely identify a missing
synapse. Cell-specific RF shape, temporal dynamics and two-dimensional geometry
remain candidate explanations. A defensible next model would constrain the
published excitatory/inhibitory profiles and time constants using flashes,
rather than repeatedly adjusting motion scores. The diagonal flash/canonical
axis mismatch also warrants a geometry-identifiability audit before adding
parameter flexibility. Both need a new frozen version and suitable independent
stimulus/cohort validation. A published pretrained visual network remains a
broader comparison option, not automatically a valid MaleCNS replacement.

We want a neural model that explains how a fly notices a small turn while
walking. This round first showed stationary flashes to real recorded cells,
used some repetitions to calibrate where and when the model responds, and
checked the remaining repetitions. That limited test worked. We then asked
the same calibrated model to predict motion without further adjustment. It
improved the cell that previously failed, but made another cell worse. The
model therefore needs more than a location, timing and volume correction to
reliably explain all these responses. We gained a useful physiological test
and a clearer limitation; the complete walking circuit is still unvalidated.
