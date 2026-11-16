# Storage recovery choices — 2026-11-01

Prepared at the user's request to identify what can be discarded. **No file has
been deleted or consolidated.** This plan prioritizes space recovery without
losing unique scientific evidence. The [disk audit](STORAGE_AUDIT_2026-11-01.md)
contains the complete size breakdown.

## First choice: eliminate duplicate physical storage

Existing checksum indexes identify **406 duplicate groups**, with potential
recovery of **13,197,348,864 bytes (12.29 GiB)** among files at least 1 MiB.
The scan read 65 index files and examined 17,365 indexed large paths. No missing
files, conflicting indexed hashes or current size mismatches were found. This
is not a complete duplicate search: unindexed files and sub-MiB files were not
included. Current file bytes have not yet been freshly rehashed for all groups;
matching saved hashes identify candidates, not authorization to delete them.

[Concrete candidate plan](../results/storage_recovery_plan_2026-11-01/duplicate_candidates.json)
records the expected SHA-256, size, allocated blocks, current inode/device and
every path in each group. The earlier audit independently confirmed one large
movie pair with a fresh full-file hash comparison.

Recommended operation: verify every candidate's actual SHA-256, retain one
physical copy, and consolidate duplicate names with hard links on the same
filesystem. Preserve every expected path and file byte so original scientific
indexes can continue to pass. Only immutable sealed artifacts are eligible;
sharing writable working files would couple future edits. A later edit would
require first creating an independent copy. This is a storage change, not a
change to observations, model outputs or scientific conclusions.

This is the immediate recommendation because it can recover meaningful space
without an external disk or discarding unique evidence. It has not been applied.

## Larger recovery: retire or archive old retinal movies

The known retinal-movie filenames occupy **217.24 GiB** across the project.
They are the largest potential reduction. Full input movies are unnecessary
for many analyses that already use stored neural/source arrays and summaries,
but remain unique retained stimulus evidence and may be used by replay checks
or future frontend comparisons.

Prefer checksum-verified archival to another filesystem. If no external storage
is available, deleting selected older movies requires an explicit revision of
the user's preservation requirement, a path/hash deletion ledger, and a clear
statement that original artifact-availability checks will fail for those files.
Keep renderer versions, environment definitions, seeds, eye/trajectory settings,
source/neural results, numerical reviews and reports. Regeneration may be
possible but has a runtime cost; exact recreation was not established for every
movie by this storage audit. Do not present movie deletion as lossless.

The 217.24-GiB movie estimate overlaps the duplicate candidates; these savings
must not be added together as independent amounts.

## Keep

- Frozen model/connectome inputs, source code, parameters and split definitions.
- Raw physiological recordings and anatomical provenance.
- Neural/source responses, quantitative results, uncertainty estimates and gates.
- Reports, failure logs, correction history, receipts and integrity indexes.

Small Python/test caches are not a meaningful solution to a 305-GiB footprint.
Deleting the whole `results/` directory would destroy research evidence and is
not recommended. No new experiment should expand the footprint while this
storage problem is being resolved.
