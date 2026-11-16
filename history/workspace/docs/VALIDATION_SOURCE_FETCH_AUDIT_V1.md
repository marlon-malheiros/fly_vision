# Validation source fetch audit v1

**Status: REQUIRED PUBLIC RESPONSE DATA FETCHED; VALIDATION NOT YET RUN**

Audit date: 2026-09-30. This is a source and schema audit, not a neural-model score. It updates
`VALIDATED_FRONTEND_V1_EXECUTION_PLAN.md`. Source payloads and SHA-256
manifests are under `data/raw/validation_sources_v1/` and are ignored by Git.
The MaleCNS legacy project and all prior FlyVis results were left unchanged.
`configs/validation_source_lock_v1.json` pins the original 42 local payloads.
`configs/validation_public_source_addendum_v1.json` pins five newly found
GitHub files. All 47 local files are checked by
`scripts/verify_validation_source_lock_v1.py` using SHA-256 and, where
available, their Git blob IDs.

## T4/T5 functional data: Henning et al.

Source: [Zenodo record 5562205](https://zenodo.org/records/5562205),
`DATA.zip` (17,357,440,171 bytes). The server supports HTTP byte ranges.
Its ZIP64 index has 197 members. Four named processed members were fetched
by range and their uncompressed size and ZIP CRC checked:

| File | Useful content |
|---|---|
| `processed_Data_SIMA_CS5_sh_Edges.mat` | `T4T5_mb`, 114 recording entries; fly/recording name, T4/T5 layer counts, complex tuning vectors `Z`, maximal-response direction, masks. |
| `processed_Data_ROI_rf_Edges.mat` | `T4T5_mb_new`, 114 entries with matching layer/ROI counts, RF centers, and within-recording cell IDs. |
| `Turn_info_Edges.txt` | Per-recording screen orientation and depth. |
| `Snob_Cluster_Info_Edges.mat` | Authors' layer A/B subcluster analysis; preserve as context, not an automatic subtype remapping. |

The first two files jointly contain **3,537 finite nonzero tuning vectors**
across **14 flies**: T4 1,376 and T5 2,161. RF centers pair dimensionally
with all vectors; **3,112** centers are finite (T4 1,133; T5 1,979).
The remaining nonfinite RFs are source-defined missing values and must be
excluded from a spatial benchmark before model scoring. Recorded RF centers
use the authors' screen reconstruction; `Spatial_RFs_8DirEdge.m` states
horizontal/vertical/diagonal screen extents of 78°/53°/72° and an edge
speed of 20°/s. Its script uses an 80° edge and separates the T4 ON and T5
OFF halves. Screen-to-eye orientation still needs the per-recording turn
metadata and a checked physical-angle conversion.

These processed files contain PD vectors and RF locations. Four prespecified
raw recording members from distinct source flies were then fetched by HTTP
range and verified with ZIP CRC and SHA-256; see
`configs/validation_trial_fetch_v1.json` and the per-file `.source.json`
manifests. The 588,767,166 compressed bytes yielded 292 raw ROIs (183 T4,
109 T5), including 157 T4 and 98 T5 with finite processed RF centers.
These four flies form the primary trial-level test. The other processed
recordings extend spatial coverage but have no locally fetched per-trial
trajectory, so they cannot receive the same source-matched stimulus claim.

| Recording | Raw T4/T5 ROIs | Finite RF T4/T5 |
|---|---:|---:|
| `200729_Fly4_3_Image3` | 60 / 23 | 53 / 22 |
| `200804_Fly4_4_Image4` | 28 / 35 | 22 / 29 |
| `200805_Fly5_2_Image2` | 42 / 23 | 30 / 21 |
| `200814_Fly3_8_Image9` | 53 / 28 | 52 / 26 |

Every processed `CellID` for these four recordings points to a unique raw
ROI column with the matching T4/T5 and A/B/C/D layer assignment. All raw
`dSignal1_CA` traces are finite. Each file contains 16 edge epochs: **two
repeats of each of eight directions**. The stimulus string is identical in
all four: `DriftingEdge_LumDecLumInc_1period_20degPerSec_90deg_BlankRand_8Dirs_optimized`.
The `fstimpos1` trace records per-imaging-frame edge position and
`fstimpos2` records stimulus angle; labels 1–8 map exactly to 0°, 45°, ...,
315° in all four files. Frame rates range from 10.29 to 11.00 Hz. The MATLAB
7.3/HDF5 storage order transposes `Epochs`; each stored row is one trial. The
selected files passed the source-only schema admission for a trial-level
benchmark. Final eligibility, source-constrained edge reconstruction, and
angle registration still need to be checked before an N-FULL score.

A provisional source-only check using baseline-subtracted peaks in the T4
ON and T5 OFF halves found 155/157 finite-RF T4 and 96/98 finite-RF T5 ROIs
with split-repeat circular error at most 45° and an evoked peak above three
pre-epoch baseline SDs. All four flies contributed both families. This is
an acquisition sufficiency check, not the frozen eligibility decision:
the final active window, source angle convention, and noise rule must be
specified before model comparison. The reproducible calculation is in
`scripts/preflight_validation_trial_sources_v1.py`, with the captured output
in `VALIDATION_SOURCE_ONLY_PREFLIGHT_V1.json`. It gives no current reason to
download additional 100–180 MB recordings.

Each raw ROI also has an archived `AV_ROIS_resp` time-by-eight direction
matrix. Grouping raw `dSignal1_CA` repeats by `fstimval`, taking the source
T5 OFF or T4 ON half, and extracting peaks reproduces most archived curves:
across 292 ROIs, median correlation **0.998**, 10th percentile **0.988**,
minimum **0.674**. The low tail needs a documented source-only cause or
eligibility decision before model scoring. The now-available intact GitHub
analysis function also permits an exact check of the processed `Z` vectors:
all 292 are reproduced from archived curves with maximum absolute complex
difference **4.01 × 10⁻¹⁶**. These are data-pipeline checks, not FlyVis
validation scores.

The [paper's methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC8769539/)
specify full-contrast ON/OFF edges at 20°/s, a 9 × 9 cm screen spanning
about 80° × 55°, 100 Hz projection, and perspective correction onto a
virtual cylinder. The generator is described as custom C++/OpenGL.
The exact experiment-specific renderer version, stimulus definition file,
projection calibration, luminance calibration, and rendered frames are not
in the Zenodo archive or the inspected public study repository. The
recorded trajectory narrows the reconstruction problem but does not prove
pixel-for-pixel parity. Freeze a public-data-based family of edge
reconstructions and require neural scores to pass under every admitted
variant. If projection choices materially change the verdict, the
stimulus-dependent biological result is inconclusive.

All 15 small standalone files in [Zenodo record 5562205](https://zenodo.org/records/5562205)
were fetched and checked against deposited MD5 values, including
`subscripts.zip`, `Model.zip`, and the authors' edge processing and angle
conversion scripts. `MASTER_foldersummary_Miriam_sh.txt` was also extracted
from the large archive. The full 17.4 GB archive was not downloaded. Zenodo
record version 1 is CC BY 4.0. One file inside the deposited
`subscripts.zip`, `load_neuron_data10Hz_ks_CA_average_Edges_8Dir_mh.m`,
contains 8,869 zero bytes. Its CRC and the outer ZIP's deposited MD5 match,
so this is a Zenodo packaging defect, not a transfer error; Zenodo lists no
newer version. **Correction:** an intact 8,869-byte copy exists in the
[study's GitHub repository](https://github.com/silieslab/DS_tuning_Henning/blob/fd7a469fb5e40a5758a4d2d76fbd562d0e185b0d/subscripts/load_neuron_data10Hz_ks_CA_average_Edges_8Dir_mh.m).
It defines the eight-angle vector order as 90°, 45°, 0°, 315°, 270°, 225°,
180°, 135°, uses the first half for T5 and the second for T4, and gives the
processed `Z` formula. It is downloaded and hash-pinned in the public-source
addendum. The analysis-function gap is closed.

The GitHub repository also provides [one 100 Hz stimulus output log](https://github.com/silieslab/DS_tuning_Henning/blob/fd7a469fb5e40a5758a4d2d76fbd562d0e185b0d/Data/RawDataExample/200729_Fly4/Image4/_stimulus_output_2020_07_29_13_56_02.txt):
16,626 logged frames with time, epoch, edge position, and rotation. Its
first line names the source stimulus definition at
`C:\GitHub\2pstim-C-\stimuli\Miri\DriftingEdge_LumDecLumInc_1period_20degPerSec_90deg_BlankRand_8Dirs_optimized.txt`.
This is an example from Image4, not one of the four selected raw Image3/4/2/9
recordings, and its full stimulus definition is absent from the public
study repository. A [public base `2pstim` repository](https://github.com/ClandininLab/2pstim/tree/ea428fe1c37eaae7144e1e33145b1b5d8f9b9596)
contains C++/OpenGL display code and older edge examples. Its file tree
does not contain the named `2pstim-C-` variant or Miri stimulus file.
The base code is useful for reconstructing geometry; its equivalence to the
experiment-specific executable has not been established.

## Eye map and H2: Zhao et al.

Source: [authors' public repository](https://github.com/reiserlab/eyemap_T4)
at commit `99d2a43123db636cedb55af9ff31a59657e7d17e`. All fetched files
matched the Git blob IDs in the repository index; SHA-256 values are in
`zhao2025/source_manifest.json`.

- `eyemap.RData` contains an anatomical 778-row eye map and supporting
  medulla/lens point sets. These are from the authors' specimen/source,
  not MaleCNS body-ID coordinates.
- `T4_RF_pred.RData` contains two 778 × 12 predicted T4 RF arrays. It is
  anatomical/model-derived context, not a direct T4 functional recording.
- `H2_tuning_2023.rda` contains **78 finite edge-response summary rows**
  from seven H2 cells, six stimulus positions, and two contrasts. It
  includes spike/subthreshold PD and DSI summaries, but no per-trial
  16-direction response curves. One cell contributes only six rows; do not
  pretend all cells have identical coverage.
- The full [public H2 deposit v2](https://doi.org/10.25378/janelia.28462100.v2)
  was fetched. Its 2,631,587,183-byte ZIP matches deposited MD5
  `acc9e4b4eb23229e905d2ac2de644697`, and all four members passed ZIP CRC
  checks. The extracted MATLAB 7.3 `edgeDataAndTable.mat` is 3,106,787,136
  bytes. Its raw HDF5 structure contains seven cells, two protocols per cell,
  96 indexed stimuli per protocol, two or three repeats per stimulus, mean
  responses, repeated traces, and spike rasters. The `edgeTable` is a MATLAB
  MCOS table; its stimulus attributes and `newIndex` mapping still need a
  checked decoder before full 16-direction/time-course scoring. The source
  plotting script names the required columns. Full SHA-256 and member CRCs
  are in `zhao2025/h2_raw_source_manifest.json`. The deposit is CC BY 4.0.
  The v1 API lists the same ZIP size and MD5, so the fetched v2 raw payload
  is byte-identical by the deposited checksum.

## Decision for implementation

**The public response files needed for the planned bounded T4/T5 PD/RF and
eight-angle trial-level checks, plus H2 summary and raw response checks, are
now local and integrity-verified.** This is data admission, not a validation
pass. The remaining work is frozen source-only response extraction and
eligibility, physical angle and display-to-eye registration, a comparison of
the public `2pstim` base code with the example log, a declared
edge-reconstruction uncertainty grid, and a checked H2 MATLAB table decoder
if pursuing H2 full tuning. **No author contact is required for the bounded
edge benchmark.** Exact projector-frame reproduction remains outside its
claim. No private or exact
FlyVis-unit-to-MaleCNS-body-ID identity table is implied by these files.

The immediate next implementation task is a source-only extraction table
with fly, recording, layer, ROI ID, complex `Z`, source PD, RF center,
orientation metadata, trial responses, and a prespecified inclusion flag.
It must preserve the 425 nonfinite RF entries as explicit exclusions and
record all hashes. About 47 GB of disk remained free after acquisition.
