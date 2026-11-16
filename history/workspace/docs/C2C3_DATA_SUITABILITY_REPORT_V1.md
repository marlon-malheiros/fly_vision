# C2/C3 physiological-data suitability audit V1

2026-11-05. **Useful new data are available for a small Mi1 calcium-response benchmark.
The audit does not justify a new full-circuit reconstruction yet.** No neural
simulation, parameter fit, response-curve comparison or biological validation
was performed. The earlier72-model study remains sealed and unchanged.

The [protocol](C2C3_DATA_SUITABILITY_PROTOCOL_V1.md) and acquisition code were
frozen at `f7643d5` before retrieving new MAT files. Identity/split code and four
passing tests were versioned at `418d846` before the complete metadata review.
Qualitative paper findings and public source code were already known. Quantitative
responses have been loaded only as containers to examine structure; no response
amplitudes, genotype effects, model errors or selection correlations were scored.

## What was acquired and checked

Twenty pinned source/data files: eight T4/T5 ON/OFF direction files, two Mi1
flash files and ten small source/helper/license files. Initial retrieval was
41,645,727bytes; two justified preprocessing helpers added4,076bytes. Every
source file matches its pinned Git blob and SHA256 receipt. The complete output
is about44MiB, with no raw movies or full repository clone.

Source: [Henning et al.](https://doi.org/10.7554/eLife.108529.3) and
[authors' repository](https://github.com/silieslab/C2C3_feedback_Henning/tree/745c6114b72a61dabc9389a1f024dbe22f679edf).
The paper describes a100Hz display, an approximately80×55deg field, full-contrast
5deg bars moving at20deg/s, and GCaMP6f imaging. These article-level specifications
are distinct from per-recording stimulus logs. They do not reproduce our375deg/s
15Hz grating condition or establish2deg/s yaw sensitivity. The recordings are
from female flies; transfer to MaleCNS would be a comparison across sexes.

## Biological units and preserved holdout

The direction files contain64 animal/session records across ON/OFF. After
conservatively grouping shared date/Fly names, there are34 naming-based groups.
Suffixes such as `_1` and `_2` have unresolved meaning; they remain separate
session labels but share a partition to prevent possible animal leakage.
These labels do not establish34 independently verified biological preparations.

| Direction-file condition | ON records | OFF records | Same-position strict name matches | Conservative animal-name groups |
|---|---:|---:|---:|---:|
| Control | 11 | 11 | 11 | 11 |
| C2 silenced | 8 | 8 | 8 | 8 |
| C3 silenced | 6 | 6 | 2 | 7 |
| C2/C3 silenced | 7 | 7 | 0 | 8 |

Thus ON/OFF array positions cannot be treated as paired animals in every group.
The source figure's explicit seven-of-eleven control selection is documented;
all11 controls remain inventoried. None was discarded for this audit. The
[identity crosswalk](../results/c2c3_data_suitability_v1/ON_OFF_crosswalk.json)
keeps strict labels, possible name matches and unmatched records separate.

The Mi1 files provide177 distinct fly/cell records:99 from9 control flies and78
from7 C2-silenced flies. Numeric flyIDs map one-to-one to their source names;
there are no duplicate fly/cell pairs. Source labels indicate the Mi1 C2 condition
uses shibire/water-bath preparations, while the T4/T5 direction cohort uses Kir.
They are separate perturbation datasets and cannot silently share one efficacy parameter.

A deterministic whole-animal SHA256 split reserves19 of50 total naming-based
groups, leaving31 for development. It uses identities only. The more securely
identified Mi1 cohort has6 control and4 silenced development flies, plus3+3
reserved test flies. All records from an animal remain together. No held-out
response curve has been scored; the partition is feasible but does not guarantee
statistical power or a successful validation.
[Partition](../results/c2c3_data_suitability_v1/animal_partitions.csv).

## Stimuli, clocks and observation model

Mi1 has explicit native timestamps, binary stimulus traces, stimulus codes and
10Hz resampled clocks. Logged cycles span9.9–10.1s. Native sampling intervals
range0.0421–0.0809s in controls and0.0510–0.0607s with C2 silenced; a nominal
frame rate must not replace these clocks. The source stimulus name is
`LocalCircle_5sec_220deg_0degAz_0degEl_Sequential_LumDec_LumInc`; the exact
projection geometry remains distinct from that label and the article description.

The Mi1 helper computes `idSignal1 / mean(idSignal1) - 1` using the whole trace,
aligns on falling stimulus transitions, uses an epoch window1.3 times the mean
cycle length and averages repetitions. The source plot applies a response/stimulus
correlation threshold and displays an ROI-weighted mean. A future benchmark must
predeclare those choices, retain an all-ROI sensitivity analysis and use animal-level
outcomes for independent testing. Calcium is not membrane voltage, and the data
alone do not identify a unique calcium-to-voltage or voltage-to-release transform.

The T4/T5 direction files preserve per-ROI native arrays, interpolated per-fly
arrays, named layers, ROI masks and precomputed vectors. All512 subtype/record
counts agree with their declared ROI counts. However, original trial-wise
stimulus sequences, native time axes, display logs and the generator are absent
from these processed files. Fifty interpolated samples do not by themselves
verify their time origin or the coordinate order of all eight directions.
Conditional relative-tuning comparisons may be feasible; exact image-to-recording
waveform validation is not currently supported.

## Processing hazards found before a response comparison

The pinned source code needs independent checking before reuse. In the pooled
T4 vector-length branch, the `Average=true` path reads OFF-derived T4 values while
layer-specific T4 summaries read ON. The relative-response helper appends temporary
subtype arrays outside the branches that initialize them, allowing empty subtypes
to reuse stale values or fail. The dummy compass-angle list contains130deg, but
its dummy vector uses only the first angle; that does not establish an error in
stored vectors. These are static source-code findings, not a numerical correction
to the paper or evidence that its biological conclusions are false.
[Exact source locations](../results/c2c3_data_suitability_v1/processing_code_audit.json).

## Decision and next action

**GO for a separately frozen Mi1 calcium-component benchmark.** Start with the
logged flash stimuli, an explicit observation model and the10 development flies;
define scoring and freeze the candidate before using the6 reserved animals.
Compare the response timing/shape to a baseline and report failures. This offers
new physiological evidence without another whole-network sweep.

**Conditional only for T4/T5 relative-direction benchmarking.** First reconcile
the source processing, direction convention and animal identities. Treat ON/OFF
as separate cohorts when identities cannot be confirmed. Do not treat every ROI
as an independent fly or silently apply the seven-control subset.

**NO-GO for exact end-to-end validation or C2/C3 integration now.** The acquired
files do not identify electrical conductances, synaptic strengths, coupling or
the full neural/indicator dynamics. Adding feedback in front of already measured
intact-circuit kernels may double-count those dynamics. No new connections or
physiological parameters were invented, and no new model was installed.

## Reproducibility and limits

The independent checker re-parses all241 metadata rows, reconstructs all50
partitions, verifies zero animal-group leakage and checks512 ROI counts. Four
focused identity/split tests pass. Source acquisitions, schema descriptions and
all audit tables are retained. Initial schema work used0.47 CPU s, the metadata
review used0.32 CPU s; download, startup and independent-review resources are
recorded separately. No costly neural rerun was performed. The audit does not
prove biological validity, neural degeneracy, a small-turn improvement or
publication acceptance.

To reproduce in a clean output workspace with the pinned prior source manifest:
run `c2c3_data_suitability_v1.py prepare`, `acquire`, `inspect`, then
`review_c2c3_data_suitability_v1.py prepare`, `supplement`, `review` and this
completion script. Run the four tests with `PYTHONPATH=src`. Producers refuse to
overwrite existing evidence. See the two freeze manifests, source receipts and
[independent review](../results/c2c3_data_suitability_v1/independent_review.json).
Final sealing is performed in a separate process after this writer exits.

For an undergraduate: we found new recordings with enough information to test
one earlier stage of the visual circuit properly. We also found pitfalls that
would make a careless comparison misleading. This gives us a concrete, small
next experiment; it does not mean the whole small-turn model is fixed.
