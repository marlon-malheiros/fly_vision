# T4 matched-data admission: a useful observation test is available

2026-11-05. **We found enough public data to test a restricted T4 measurement
relationship and executed that test separately. Exact image-to-T4 biological
validation remains unsupported by these files.** No prior neural model or
recording split was changed. The four reserved C2/C3 control flies remain
unscored.

The [admission protocol](T4_MATCHED_DATA_PROTOCOL_V1.md) was committed at
`3dd6495` before new acquisition. It specifies identity, stimulus, time,
measurement and independent-partition requirements, a250MiB acquisition cap and
no bulk imaging/whole-archive downloads. This is source admission, not a new
neural validation score.

## Sources and what they actually support

| Source | Evidence verified | Remaining gap / decision |
|---|---|---|
| Ammer2023, T4c axon voltage and calcium | Pinned code and24 per-session mean-trace arrays;200-point relative clocks; eight directions plus exact plotting closure; source file order | Supports a static cross-cohort indicator-prediction test. Not simultaneous measurements, mV calibration, calcium kinetics or exact image replay. Vertical T4c does not establish horizontal T4a/b physiology. |
| Tanaka2023 Dryad | Dataset/version/file metadata, explicit T4a/b and T5a/b data description | README data routes returned403/401. Public/API ZIP-directory attempts failed before verified payload. Trial/stimulus metadata listed publicly are promising, but their contents were not admitted locally. No claim that the dataset is absent or corrupt. |
| Gruntman2018 T4 voltage | Public collection metadata matches the earlier local archive inventory; raw moving-bar and protocol files are listed | Direct voltage is a concrete alternative that avoids a calcium observer. Original pooled figure peaks are familiar; raw individual-waveform admission/identity/stimulus reconstruction is still needed for a new test. No bulk raw file was acquired in this round. |
| Existing Henning2022 local edges | Recorded per-imaging-frame edge positions/angles and repeated trials, documented in the earlier audit | Useful stimulus-timed development evidence. Previously inspected responses and uncertain experiment-specific projector generator prevent a claim of wholly blind, exact pixel replay. No repeat bulk download. |

Ammer source is pinned to
`db1f8089b697d1b19da1394ef94450bbec24f32b`. All source-code inspection used
notebook code-cell text or literal filename assignments; notebooks were never
executed and saved notebook outputs were not inspected. Numeric responses were
scored only after the separate observation-study freeze.

The13 voltage /11 calcium files form9/10 conservative recording-date groups.
The cohorts are unpaired and dates do not independently verify animal identities.
There is no date overlap across the cohorts. The shared supplied clock has200
samples, dt0.07936s, from−4.99968 to10.79296s; it is a processed relative clock,
not a raw per-trial display/trigger log.

The code's compiled voltage curve averages indexes63:145 (last sample6.42816s),
whereas calcium uses63:139 (last5.952s). The separate study preserves and checks
those source summaries but uses prospectively stated, paper-motivated primary
windows: voltage[0,5)s, calcium[0,6)s. This makes the measurement convention
explicit rather than treating unlike summaries as interchangeable. No claim that
this source-code distinction invalidates the paper.

## What was executed from this admission

The [separate observer protocol](T4_OBSERVATION_TRANSFER_PROTOCOL_V1.md), frozen
at `09af160`, fits one nonnegative gain on development data for a primary
rectified-linear map and a fixed squared diagnostic. Three date groups in each
indicator cohort are reserved until both gains are serialized. No neural
parameter, input image, gain into MaleCNS or connectivity is fitted. The
[completed observer report](T4_OBSERVATION_TRANSFER_REPORT_V1.md) gives the
positive restricted result and its important failures, including missed negative
calcium responses.

This is progress on the measurement part of the original task. It is not a
completed image-to-neuron benchmark. A voltage-indicator signal and a calcium
signal are different measurements, and their relationship need not be1:1.
However, an empirical cross-cohort gain cannot become a measured membrane
conductance or a justified calcium time constant.

## Acquisition failures, integrity and storage

The [acquisition summary](../results/t4_matched_source_admission_v1/acquisition_summary.json)
records45 successful small payloads totaling842,760bytes and7 failed ordinary
requests. Five failures were sandbox DNS restrictions; authorized network
retrieval succeeded for GIN/Figshare and Dryad metadata. Failed README requests
and both separate ZIP-index attempts are retained. ZIP-reader `BadZipFile`
errors captured no verified archive bytes; the reader did not preserve the
underlying I/O status. They cannot establish that Dryad serves a corrupt file.

A metadata-only probe used an unavailable private NumPy header helper; public
header functions then worked. Legacy Python2 NPY/header and notebook invalid
escape warnings are documented; source data were not rewritten. These technical
events did not consume a test response or change a scientific rule.

No13.8GB/17.4GB archive or raw imaging movie was downloaded. The new acquisition
is less than1MiB before evidence/method/progress copies. Each source file has a
URL/byte/SHA256 receipt. The [identity map](../results/t4_matched_source_admission_v1/ammer_recording_identity_map.json),
[metadata audit](../results/t4_matched_source_admission_v1/metadata_audit.json),
[decision](../results/t4_matched_source_admission_v1/admission_decision.json) and
[technical notes](../results/t4_matched_source_admission_v1/technical_notes.json)
preserve supported uses and unresolved gaps. Final seal receipts verify retained
files after writer exit; they are not biological evidence.

For an undergraduate: we found recordings that let us check one link in the
comparison between simulated electrical activity and measured calcium. That
helps make the next neural test fair. We still need a matched test of how images
produce the electrical response, and cannot declare the whole fly model valid.

Primary sources: [Ammer et al.](https://www.nature.com/articles/s41593-023-01443-z),
[pinned author data/code](https://gin.g-node.org/gammer/Ammer_et_al_2023/src/db1f8089b697d1b19da1394ef94450bbec24f32b),
[Tanaka data deposit](https://doi.org/10.5061/dryad.bcc2fqzjz),
[Gruntman T4 paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5967973/),
[earlier local-data audit](VALIDATION_SOURCE_FETCH_AUDIT_V1.md).
