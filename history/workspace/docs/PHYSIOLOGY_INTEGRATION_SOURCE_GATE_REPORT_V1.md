# Physiological frontend: source comparison and integration decision

Date: 9 October 2026. Decision: the published backup is better supported;
strict anatomical integration is still incomplete. No full-eye replacement,
downstream rerun, fitting or additional checkpoint search was performed.

The T4 comparison now has quantitative evidence from the published response
summary. The larger local anatomy source also supplies substantially more
input wiring than the selected downstream circuit. These checks resolve
specific uncertainties, but do not establish biological validation of the
complete proposed frontend.

## T4 comparison: all four speeds, both directions

The released README identifies the fixed source as the model in Figure 5b
and Supplementary Figure 6c. The paper identifies its motion reference as
pooled recordings: 31 trajectories from 16 cells. The archive's assignment
script identifies 17 cells and 18 eight-direction files, rather than a
single matching example. Selecting one recording would not reproduce the
paper's reference. Its methods also include additional trajectories along
the receptive-field axis. The recovered public directory and instructions
do not identify the entire published pooling calculation.

We therefore performed a precisely scoped alternative: recover every peak
point from Figure 5c's vector paths in the published PDF, calibrated by
its 10-mV ticks. Compare them with the already saved unchanged NEURON run,
using the paper's 0.995-quantile response definition during bar presentation.
No response-based scale, time adjustment, parameter change or threshold
selection was made. The extraction retains the original path attributes,
affine transforms and axis calibration.

| Bar dwell (ms) | Fixed code PD (mV) | Published recorded PD (mV) | Fixed code ND (mV) | Published recorded ND (mV) |
|---:|---:|---:|---:|---:|
| 20 | 14.009 | 13.899 | 9.480 | 9.621 |
| 40 | 17.368 | 18.915 | 8.237 | 8.153 |
| 80 | 19.080 | 19.637 | 6.772 | 7.059 |
| 160 | 19.262 | 18.855 | 8.439 | 6.842 |

Across all eight peaks, fixed-code agreement with the paper's plotted
**simulation** has RMSE **0.043807 mV** and maximum absolute error
**0.069472 mV**. The plotted line's half-width corresponds to about
0.142 mV; these small discrepancies are below that figure precision.
This is useful reproduction evidence, rather than an exact waveform oracle.

Against the plotted **recorded means**, peak RMSE is **0.831981 mV** and
maximum absolute error is **1.596360 mV**. The model is direction selective
at every speed. Its `(PD-ND)/PD` values are 0.3233, 0.5258, 0.6451 and
0.5619; the corresponding ratios derived from recorded mean peaks are
0.3078, 0.5690, 0.6405 and 0.6371. These ratios are not a distribution of
individual-cell DSI, and are not the grating DSI used in previous audits.

No new physiological pass criterion was declared. This is a same-study,
figure-derived comparison; it supplies neither raw-trace reproduction,
uncertainty-based biological acceptance, nor independent held-out validation.
The model was originally fit to the study's flash responses, while motion
responses tested generalization within that study.
[T4 paper and public-data links](https://pmc.ncbi.nlm.nih.gov/articles/PMC5967973/).

![T4 published peak comparison](../results/physiology_integration_source_gate_v1/t4_published_peaks.png)

## What the local anatomy actually contains

The selected frozen downstream circuit still contains 13,593 cells, including
13,579 T4/T5 targets, and lacks the early Mi/Tm visual stages. It is unchanged.

The **larger structural export**, inspected separately in read-only mode,
contains **65,799 neurons, 1,967,771 edges and 1,771 columns**. Its verified
binary SHA-256 remains
`1a2db419a817a3bfa9572bb87b2d9264d47eb48992fda69a82cc861678cfa80f`.
We recovered **73,282 per-target/input-type offset records**, covering both
eyes and every T4/T5 subtype. Relevant input coverage is substantial:

| Target family | Input type | Targets with same-eye column-mapped input / family total |
|---|---|---:|
| T4 | Mi1 | 6,861 / 6,861 |
| T4 | Tm3 | 6,855 / 6,861 |
| T4 | Mi4 | 6,818 / 6,861 |
| T4 | Mi9 | 6,831 / 6,861 |
| T5 | Tm1 | 6,718 / 6,719 |
| T5 | Tm2 | 6,718 / 6,719 |
| T5 | Tm4 | 6,702 / 6,719 |
| T5 | Tm9 | 6,716 / 6,719 |

The larger export has 13,580 T4/T5 cells. One T5a has no column assignment;
it remains excluded from the selected 13,579-target experiment. This audit
does not assign it an invented coordinate.

T4 Mi4-minus-Mi9 and T5 Tm2-minus-Tm9 centroid vectors give orderly subtype
and bilateral structural proxies. However, the chart itself was calibrated
using T4a/c expectations. Their agreement cannot independently validate that
calibration. The T5 proxy does not identify the physiological inhibitory arm.
Hand-set time constants and neurotransmitter-to-sign conventions in the
structural export were **not** adopted as physiological parameters.

The filtered export deliberately omits CT1. We checked the original full
annotation and weight files instead: two traced CT1 cells, body IDs 10009
and 10157, are present. Streaming **151,856,684 raw edge rows** recovered
**13,537 CT1-to-T4/T5 edges**, contacting 6,824 of 6,861 T4 and 6,713 of
6,719 T5 targets, with **230,681 total synapses**. Thus CT1's absence from
the filtered graph is a selection effect, not absence from the biological
source.

The full weight table contains only `body_pre`, `body_post` and `weight`.
It supplies no local synapse/branch coordinates. A global CT1 body spans
many visual columns, so assigning its soma one visual coordinate cannot
recover each local inhibitory input. Contact existence is established;
the spatial physiological mapping is not.

The T5 source paper itself treats CT1 as a proposed inhibitory source,
rather than proving that the model's inhibitory Gaussian is CT1.
Its functional equations use a one-dimensional stimulus along the receptive
field and omit bar height. Extending them to two-dimensional random squares
therefore requires an explicit transverse receptive-field assumption.
[T5 primary paper](https://doi.org/10.7554/eLife.50706),
[input anatomy](https://doi.org/10.7554/eLife.40025).

## Integration gates and finite remaining work

| Gate | Current evidence | Decision |
|---|---|---|
| Fixed T4 executable model | Unchanged author source, four speeds and 44 flashes | Supported |
| T4 published motion comparison | All eight Figure 5c peaks, small source-simulation discrepancy | Supported at figure level; raw waveform gate unresolved |
| T5 equation correctness | Independent author equations across all 168 protocols | Supported; original archival compatibility failure remains recorded |
| Early-input wiring and bilateral coordinates | Larger export offsets plus recovered CT1 contacts | Partially established; functional inhibitory placement unresolved |
| Image sampling in native model units | Published bar protocols and one-dimensional axes available | Two-dimensional extension and transfer to each subtype need a frozen specification |
| Physiological voltage to frozen downstream drive | Output is mV; downstream input/state/rate are arbitrary model units | No experimentally calibrated conversion established |
| Full replacement rerun | Requires accepted mapping and coupling definitions above | Not executed |

These are different evidence levels, rather than a demand that every future
computational experiment prove all biological details. The professor explicitly
allows a fixed, predeclared exploratory value for a missing parameter. An
assumption-based extension can therefore be a legitimate **new computational
study**, if its wiring respects the anti-leakage rule and its scope is explicit.
It must not be presented as completing the stricter source-backed physiological
integration gate or as validating the biological circuit.

For a strict anatomical replacement, seek local CT1/input synapse positions,
not merely more edge counts. For an assumption-based physiological extension,
declare the spatial embedding and transverse sampling once, use the published
fixed dynamics, and freeze one common voltage normalization before any output.
For example, normalization by the published excitatory driving force provides
a dimensionless model quantity; whether it is a suitable input to the frozen
downstream circuit remains a separate coupling assumption. Do not copy a
FlyVis activity scale of 1.0 into mV units without such a declaration.

Additional physiological observations would be required to establish a
calibrated biological coupling or independently validate the complete hybrid.
The present results do not establish that new experiments are needed merely
to run a clearly labeled exploratory model. Public synapse-level resources
may supply missing anatomical information; their availability for this exact
mapping has not been established by the aggregate tables inspected here.

## Verification and reproducibility

Source acquisition used verified HTTP ranges and ZIP-member CRC checking:
62 authored instruction/code files, 262,240 transferred ZIP bytes, no bulk
raw-recording archive download. The primary T4 PDF/manuscript and T5 manuscript
were separately saved and hashed. New result scripts are isolated from the
previously sealed packages.

Independent review passed: eight code peaks recomputed through sorted-order
quantiles; vector-path arithmetic checked separately; all 104 anatomy summaries
recomputed; 64 fixed, evenly spaced per-target centroids checked; every recovered
CT1 pair checked against a second raw-table pass using Arrow filters.
The five focused T5 regression tests also passed in this turn.

All 1,585 historical ledger entries, the additional 741 comparison/backup
entries, 40 T5-investigation entries and 49 previous T4 output entries retain
their hashes. These 2,415 checks include overlapping files and are ledger
entries, not a claim of 2,415 distinct experiments. A separate artifact index
seals the new report, code and evidence.

Reproduce from the repository root (existing environments):

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/acquire_t4_matching_sources_v1.py
PYTHONDONTWRITEBYTECODE=1 <TEMP>/maleoptic-flyvis-r3-venv/bin/python scripts/audit_physiology_anatomy_v1.py
PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR=<TEMP>/maleoptic-weak-mpl <TEMP>/maleoptic-flyvis-r3-venv/bin/python scripts/compare_published_t4_peaks_v1.py
PYTHONDONTWRITEBYTECODE=1 <HOME>/Lab/mech_male_fly_cns/.venv/bin/python scripts/audit_ct1_full_source_v1.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src <HOME>/Lab/mech_male_fly_cns/.venv/bin/python scripts/review_physiology_source_gate_v1.py
```

Network access is required only for acquisition. These V1 producers have
fixed output paths: reproduce in a separate checkout/result revision to retain
the sealed evidence. The CT1 annotation evidence was obtained by reading the
four named annotation columns and selecting `type == CT1`; neither that read
nor execution under the existing legacy interpreter modifies the legacy source.
