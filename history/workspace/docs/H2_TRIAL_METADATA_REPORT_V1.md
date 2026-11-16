# H2 trial metadata and measured direction curves V1

25 October 2026. **Completed:** checked indexing and source-only reconstruction
of the already downloaded H2 recordings, plus one external comparison
specification. **Not established:** agreement of our neural model with these
recordings or a repair of small-yaw detection. Original model parameters,
MaleCNS graph, raw recordings and prior sealed results are unchanged.

## What was recovered

| Item | Result |
|---|---:|
| Recorded H2 cells / display protocols | 7 / 14 |
| Indexed conditions | 1,344 |
| Directions / positions per protocol / polarities | 16 / 3 / 2 |
| Raw repeats retained | 4,032 |
| Aligned analyzed repeats | 4,000 |
| Conditions with an explicit excluded raw repeat | 32 |
| Complete direction curves | 84 |
| Curves matching published summary keys | 78 |
| Additional curves retained and flagged | 6 |

The full index preserves cell, aligned and original protocol IDs, condition
index, relative direction, position, polarity, background, duration field,
mask and frame metadata, vector-valued fields and missing values. All global
rows match their local recording tables exactly: 22,848 shared numeric
elements checked, including NaNs, unique keys and complete coverage. Original
protocol numbers differ from aligned-array indices in several cells; joining
on them interchangeably would mislabel data.

[All conditions, clocks, source addresses and repeats](../results/h2_trial_metadata_v1/metadata/conditions.json),
[CSV metadata](../results/h2_trial_metadata_v1/metadata/metadata.csv),
[protocol inventory](../results/h2_trial_metadata_v1/metadata/protocols.json),
[independent metadata review](../results/h2_trial_metadata_v1/metadata_independent_review.json).

## Source physiology recovered without fitting our model

Reproduced the supplied MATLAB script's frame-derived response windows and
pooled −750 to −50 ms baseline. Retained signed baseline-subtracted firing
rates, all counts and indices. Window selection includes both first-sample-
strictly-after-boundary indices, matching the author. The response window
uses raw repeat 1 for each condition even when that repeat is source-listed
excluded; this behavior is disclosed and preserved. Aligned raster rows are
not asserted to have independently verified identities among original raw
trials.

Independent sparse-event counting agrees exactly for every condition and
window; derived rate arithmetic differs by at most **1.42e-14 spikes/s**.
It checks all 4,032 raw-repeat stop events, reading 69,237,473 aligned clock
samples and 79,949 nonzero raster entries. All 78 previously published
spike-vector DSI values are reproduced to roundoff: maximum difference
**3.33e-16**, median **5.55e-17**. This agreement was descriptive, not a
post hoc acceptance threshold or fitted objective. These are the same
recordings, not new independent animals.

Cell 4 lists `stimDur=0.08`, versus 0.04 elsewhere. Its frame-derived response
window is approximately **1.681 s**, versus **0.839 s** for the other cells.
Do not replace this difference with the paper's nominal 40-ms step interval.
All aligned clocks have approximately 0.05-ms spacing, consistent with the
reported 20-kHz sampling. Signed responses range from −9.467 to 41.439
spikes/s; 550 conditions are below baseline and remain retained. The six
curves absent from the summary sheet are cell 7, aligned protocol 2/original
protocol 3, at three positions for both polarities. The paper reports
excluding three positions from cell 7 because recording quality declined;
we retain and flag the raw-source curves.

[Every count, rate and frame event](../results/h2_trial_metadata_v1/source_curves/condition_endpoints.json),
[84 complete curves and summary joins](../results/h2_trial_metadata_v1/source_curves/direction_curves.json),
[all windows](../results/h2_trial_metadata_v1/source_curves/protocol_windows.json),
[independent count review](../results/h2_trial_metadata_v1/source_curves_independent_review.json),
[summary agreement](../results/h2_trial_metadata_v1/descriptive_summary_comparison.json).

[All measured curves, including omitted-summary curves](../results/h2_trial_metadata_v1/figures/all_direction_curves_v1.png)
and [analysis windows/baselines](../results/h2_trial_metadata_v1/figures/source_windows_v1.png)
are also supplied as PDF. These figures contain recorded responses only.
The min-shift used for vector DSI does not replace the signed response curves.
Our derived phase uses atan2; the source plot's atan(imag/real) loses quadrant
information. We do not select a convention from model-response agreement or
claim an unverified phase equivalence with the summary sheet.

## The single comparison now specified

Test whether frozen **left-H2 local preferred directions** match measured
moving-edge directions across display positions. Primary statistic is
cell-weighted circular PD error; secondary statistics include DSI and curve
shape. The [benchmark specification](H2_DIRECTION_TUNING_BENCHMARK_SPEC_V1.md)
and [machine-readable gates](../results/h2_trial_metadata_v1/benchmark_specification_v1.json)
define stimuli, observables, source exclusions, uncertainty and separation.

Primary Methods establish left-brain recordings, an occluded right eye,
a cylindrical display, measured head orientation and a rotated arena.
Retrieved the pinned author's cylinder-to-eye helper and verified its Git
blob identity. These constrain an approximate renderer. Exact trial pattern
arrays, photometry and all pixel-generation conventions remain unestablished
in the admitted files. The model's eye coordinates, time-to-ms mapping,
adaptation and spike observation statistic still require a separate freeze.
A documented approximate stimulus-family comparison can proceed without a
private handoff; it must not be called exact recording replay.

No model prediction was scored or parameter fitted. If a later observation
calibration is needed, the proposed animal split is cells 1–4 for calibration
and 5–7 for testing, frozen before predictions. All animals' aggregate
summaries were inspected earlier, so this is a computational held-out split,
not fresh biological validation. The female recordings versus male
connectome and the functional surrogate's imposed input routing remain
biological limitations. H2 tuning alone cannot validate bIPS, DNp15, walking
thresholds or motor control.

## Failures, checks and preservation

V1 extraction incorrectly required raw trials to have the aligned mean's
length; preserved its failure and corrected separate clock inventory in V2.
V2 was interrupted after profiling excessive HDF5 reference-name searches;
V3 records stable raw-hash-bound addresses and explicit trial routes. V3
exposed retained raw repeats versus exclusion-filtered rasters; V4 checks
raw count minus explicit exclusions against declared/aligned repeats.
Original exact metadata criteria never changed. Earlier overbroad schema
listing and a parameter-group inspection error are retained in exploration
notes. A synthetic exception-class assertion was corrected, preserving its
failed log. Plotting initially failed because the h5py interpreter lacks
matplotlib; plotting V2 reads exported JSON using the existing matplotlib
interpreter. No dependency was installed or baseline environment changed.

All amended frozen sources are retained or recovered byte-for-byte with
matching prior hashes. Seven synthetic tests pass; independent full-data
metadata/count reviews pass; eight conditions replay exactly in a fresh
namespace. No second full end-to-end replay is claimed. Visual review passes
for both figure pairs. [Protocols and amendments](H2_TRIAL_METADATA_PROTOCOL_V1.md),
[clock correction](H2_TRIAL_METADATA_SCHEMA_CORRECTION_V2.md),
[addressing correction](H2_TRIAL_METADATA_REFERENCE_ADDENDUM_V3.md),
[exclusion correction](H2_TRIAL_METADATA_EXCLUSIONS_ADDENDUM_V4.md),
[source counting freeze](H2_SOURCE_CURVE_EXTRACTION_PROTOCOL_V1.md),
[reproduction commands](H2_TRIAL_METADATA_REPRODUCTION_V1.md).

This task closes an unfinished external-data step rather than repeating a
mapping audit or another yaw sweep. Reopen prior input-mapping hypotheses
only with a concrete counterexample or relevant new evidence. This study
supports usable H2 measurements and numerical reproducibility, **not
physiological validation of the model**, a new detection threshold or a
biological causal mechanism. Completion/index records in
[the study directory](../results/h2_trial_metadata_v1) identify the source
checkpoint, dated progress snapshot and immutable artifacts.

## Primary sources

[Zhao et al. (2025), paper and Methods](https://www.nature.com/articles/s41586-025-09276-5),
[raw H2 deposit v2](https://doi.org/10.25378/janelia.28462100.v2),
[pinned author transform](https://github.com/reiserlab/eyemap_T4/blob/99d2a43123db636cedb55af9ff31a59657e7d17e/eyemap_func.R),
[processing script](https://github.com/reiserlab/eyemap_T4/blob/99d2a43123db636cedb55af9ff31a59657e7d17e/proc_ephys.R).
Public retrieval URLs/hashes and original source hashes are retained in
[the retrieval record](../results/h2_trial_metadata_v1/source_snapshot/retrieval.json)
and [provenance](../results/h2_trial_metadata_v1/metadata/provenance.json).

## Undergraduate explanation: what we did, what we want, and why

We turned existing recordings into checked response curves showing how a
real H2 neuron reacts to motion in different directions. We want to present
comparable moving edges to our model and see whether its H2 neuron prefers
the same directions. This gives us a biological reference before changing
the circuit or asking it to detect tiny turns during walking. The recordings
are now usable; whether our model matches them is the next unanswered question.
