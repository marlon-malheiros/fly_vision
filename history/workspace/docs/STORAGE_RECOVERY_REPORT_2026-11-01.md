# Completed disk recovery — 2026-11-01

**Recovered approximately 12.84 GB (11.96 GiB). The filesystem now has about
13.02 GB (12.12 GiB) available**, compared with approximately 179 MB when the
recovery began. The user explicitly authorized discarding duplicates and
unnecessary files. No neural experiment, model fit or biological analysis ran.

[Final measured summary](../results/storage_recovery_2026-11-01/final_summary.json),
[final filesystem reading](../results/storage_recovery_2026-11-01/df_after.txt).
Available space can also vary with concurrent activity outside this process.

## What changed

| Operation | Completed scope | What was retained |
|---|---|---|
| Duplicate-block consolidation | 406 groups, 475 duplicate destination files | All 881 file paths, full contents and independent file identities |
| Transparent filesystem compression | 583 NPY-format retinal movies | Identical contents, names, sizes and inodes |
| Disposable cache removal | 347 files, approximately 6.4 MiB | Python source, tracked files and indexed scientific artifacts |
| Redundant download eviction | One 2.45-GiB H2 ZIP | All four extracted recording/script/README files, source manifest, checksums and download URL |

The project is on Btrfs. Its byte-range deduplication compares the ranges before
sharing their storage. Unlike hard links, this retains separate file identities
and independent later writes. A synthetic preflight tested identical-range
sharing, rejection of different data, unchanged hashes, separate inodes and
write independence. [Preflight receipt](../results/storage_recovery_2026-11-01/preflight.json).
The approach follows the [Btrfs deduplication documentation](https://btrfs.readthedocs.io/en/latest/Deduplication.html).

Compression was limited to files with no shared extents, checked immediately
before each operation. This avoids breaking deduplicated sharing during
defragmentation. Each file's full SHA-256 was checked before and after; no array
conversion, quantization, scientific parameter or file format changed. See the
[Btrfs filesystem command documentation](https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html)
and [compression receipt](../results/storage_recovery_2026-11-01/compression_r2.json).
All 583 eligible files were processed; the optional stop target of 20 GiB free
was not reached, so processing stopped at eligible-file exhaustion.

The H2 ZIP's full hash matched its original source manifest. Each of its four
extracted files was freshly hashed against that manifest, and ZIP member names,
sizes and CRCs were checked. The original recording file and MATLAB analysis
scripts remain present. The ZIP container was then deleted, with its original
hash and source URL retained in the [deletion ledger](../results/storage_recovery_2026-11-01/download_archive_removal.json).

**Availability exception:** `configs/validation_source_lock_v1.json` remains
unchanged and still lists the evicted ZIP. Any audit requiring that container
must reacquire it from the recorded URL and verify the locked SHA-256. This
does not require reacquiring the raw recordings for analysis; they remain
intact. The old source lock was not silently rewritten to conceal the eviction.

## Verification and accounting corrections

The recovery drivers freshly hashed every one of the 881 deduplication files
and 583 compression files before and after their respective operations. The
[post-operation review](../results/storage_recovery_2026-11-01/post_operation_review.json)
matches all 1,464 resulting hash records to the original scientific indexes,
confirms retained paths/sizes, verifies cache-removal exclusions, and verifies
that all **113 original index files remain byte-identical**. This review
crosschecks the operation journals; it is not an additional full-project data
rehash or a new scientific-validation result.

One pre-existing discrepancy was found: older indexes disagree about the hash
of `results/validation_hardware_v1/scientific_sealing_execution_v1.log`.
That log and both index versions were untouched by cleanup. The [separate
conflict record](../results/storage_recovery_2026-11-01/preexisting_log_index_conflict.json)
preserves the details. No claim of universal whole-project archive integrity
is made; this conflict is outside the changed data and cleanup scope.

The earlier **12.29-GiB duplicate estimate was a file-size/extent-counter
estimate**, not a measured amount of unique physical storage. The first actual
deduplication/cache pass increased available space by approximately **3.13 GiB**.
On this filesystem, shared extents and transparent compression mean ordinary
file-size/block counters do not establish independently reclaimable space.
The final synchronized filesystem before/after readings are the aggregate
recovery measure. Folder-size displays may still report large logical totals.

The first three-file compression pilot measured zero change through `st_blocks`.
Its original source/output and negative proceed flag are preserved. Compression
was active, but that counter was inadequate here. R2 used synchronized actual
filesystem availability, observing approximately 37.7 MB recovery for a separate
288-MB three-file pilot, with unchanged full hashes. The original pilot was not
overwritten. `compsize` physical-extent inspection lacked the required kernel
permission; no privileged workaround or filesystem-wide setting change was used.

Compression and ZIP cleanup overlapped, so the compression interval's free-space
delta includes ZIP removal. Do not add those phase deltas together or present
that interval as compression-only savings. The aggregate final before/after
measurement avoids double counting.

## Retained evidence and future use

Models, connectomes, physiological recording payloads, source/neural responses,
quantitative outcomes, failure logs, reports, split definitions and scientific
indexes were retained. No unique retinal movie was discarded. The operation
changes storage, not the conclusions of the small-turn studies or their
unfinished biological validation.

The exact recovery sources, journals and dated progress snapshot are archived
with this report. Live AGENTS and live progress remain outside the recovery
archive's index. Further large studies should estimate their complete footprint
and respect a workspace-wide free-space reserve before generating new movies.

In plain terms: we removed repeated storage and a redundant download package,
and stored existing images more efficiently. The research data still opens as
before, while approximately 13 GB of disk space is available again.
