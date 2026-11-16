# Larger cleanup: old generated movies deleted — 2026-11-01

**No, the current model and analysis do not require the entire former 300-GiB
workspace.** Much of that footprint was archived synthetic image sequences from
older experiments. The first cleanup prioritized retaining every indexed input
too strongly for the user's instruction to discard unused material.

Following that cleanup request and the user's challenge about retaining 300 GB,
the agent selected older generated movie caches for deletion while preserving
models, biological recordings, numerical evidence and representative examples.
This is a deliberate change to historical input retention, not a claim that all
old artifact-availability checks still pass.

## Completed larger cut

- Deleted **2,823 generated movie files** from seven completed older studies.
- Removed **159,674,482,886 bytes of nominal file content** (148.71 GiB).
- Increased measured available filesystem space by **149,603,348,480 bytes**,
  approximately **149.6 GB / 139.3 GiB**.
- Available space increased from approximately **13.0 GB to 162.6 GB**.
- Project file/block-counter footprint is now approximately **165.2 GB / 153.8
  GiB**, rather than approximately 327.5 GB / 305 GiB. This is not a declaration
  that all remaining archives are essential to the working model.

The actual before/after filesystem reading is the space-recovery measure;
nominal file totals do not account for compression/shared extents. Concurrent
activity outside the cleanup can also affect available space.

[Exact pre-deletion manifest](../results/legacy_movie_retirement_v2/before_retirement.json),
[per-file deletion ledger](../results/legacy_movie_retirement_v2/retirement.jsonl),
[operation result](../results/legacy_movie_retirement_v2/result.json).

## Scope and retained evidence

Deletion was limited to known generated movie filenames of at least 1 MiB,
inside an explicit older-study allowlist. Every deleted movie had separately
stored `source.npz` and `network.npz` files alongside it. Paths without that
supporting evidence were excluded, as were physiological/canonical H2 folders,
methods, source snapshots and presentations. Original foundational walking
archives and newer active study directories were not deletion targets.

All **5,646 associated source/neural files** remain with unchanged inode, size
and modification-time signatures. The operation did not write those files;
this is metadata-preservation checking, not a new full rehash of every array.
All models, connectomes, recordings, quantitative results, failed predictions,
reports, original receipts/indexes, world definitions, seeds and generation code
were retained. No biological recording or numerical-result array was deleted.

The plan explicitly retained **122 representative movies** across the twelve
considered study roots, plus all movies excluded by the guards. Representatives
were selected using speed, yaw, numerical profile and pathname, without
examining response quality. All original **113 index files** remain byte-identical.
The exact cleanup implementation is [the retirement driver](../scripts/retire_legacy_generated_movies_v2.py).

## Consequences for reproduction

**The deleted full movie files are no longer locally available.** This was
deletion, not migration to an external backup. Their original indexed hashes
and paths remain in the retirement ledger. The ledger uses recorded original
digests; the operation did not reread and rehash all 149 GiB before deleting it.

Historical full-index availability checks and pixel-by-pixel reviews requiring
those movies will report intentional missing files. They require regeneration
using the retained renderer, world/trajectory definitions, seeds and original
runtime information. Source-built recreation has been demonstrated for selected
older cases, not every retired movie, so universal bit-for-bit regeneration is
not claimed. Do not rewrite original indexes or silently skip missing inputs
and then claim a full original-archive integrity pass.

The historical source/neural response arrays and numerical summaries remain
available for analysis. The original reproduction guides, including
[continuous yaw](CONTINUOUS_YAW_MECHANISMS_REPRODUCTION_V1.md) and
[image sampling](IMAGE_SAMPLING_DIAGNOSTIC_REPRODUCTION_V1.md), remain preserved.
Do not automatically regenerate the whole movie archive during an integrity
check and fill the disk again.

## Current analysis verified after deletion

The latest neural readout uses cached `observations.npz` arrays rather than
these older saved movies. After deletion, its existing independent reviewer
was run with copied inputs and outputs redirected into this new retirement
audit directory. No sealed study output was overwritten and no model refit ran.

It reproduces **1,024 curves / 147,968 callback scores** within **2.11e-13**,
checks all 24 group gates, and passes **510 input/source hash checks**.
[Fresh analysis replay receipt](../results/legacy_movie_retirement_v2/active_readout_replay/independent_review.json).
This confirms continued saved-analysis reproducibility, not new physiological
validation or numerical solver qualification. The prior fast-walking result
remains 21/32 small turns; storage cleanup does not fix that scientific failure.

In simple terms: the neural model needs its circuit, parameters and relevant
inputs/results. It does not need every old rendered movie stored permanently.
We kept the research conclusions and numerical evidence, deleted a large older
movie archive, and documented the cost to exact historical image replay.
