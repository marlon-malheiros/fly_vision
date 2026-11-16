# Project disk audit — 2026-11-01

The project occupies **304.98 GiB (about 327.5 GB)**. Approximately **298.47 GiB
is in `results/`**, 6.46 GiB in `data/`, and 0.031 GiB in `.git`. This is accumulated
simulation output, not source code or Git history. The filesystem had about
173 MiB available at the initial check and 204 MiB at the inventory snapshot;
both readings indicate virtually no remaining space. Available space can change
with activity outside this audit.

[Machine-readable inventory](../results/storage_audit_2026-11-01/inventory.json)
records actual allocated bytes, per-study totals, filename/extension totals,
file counts, a duplicate example and filesystem availability. Values below use
GiB = 1,073,741,824 bytes. Directory totals use `du`; filename categories use
unique regular-file device/inode pairs and exclude directory metadata.

## What uses the space

| Stored artifact | Allocated GiB | Files |
|---|---:|---:|
| Compressed retinal movies, `retina.npz` | 140.98 | 3,518 |
| Uncompressed retinal movies, `retina.npy` | 67.07 | 747 |
| Losslessly encoded retinal movies, `retina_xor.zlib` | 8.80 | 403 |
| Dense retinal movies, `dense_retina_xor.zlib` | 0.40 | 8 |
| Frontend/source arrays, `source.npz` | 30.58 | 6,982 |
| Population observations, `observations.npz` | 3.86 | 7,136 |
| References, `reference.npz` | 3.81 | 1,191 |
| Network outputs, `network.npz` | 1.36 | 6,519 |

These retinal-movie filenames alone account for **217.24 GiB**, about **73% of
results storage**. They exclude additional movies embedded in older differently
named archives, so this is not an exhaustive classification of image storage.
Some older source archives also contain full retinal images and channel fields.
Compression is already used for much of the data; simply recommending ZIP does
not address all of this footprint.

| Largest study directory | Allocated GiB |
|---|---:|
| `continuous_yaw_mechanisms_v1` | 52.61 |
| `geometry_grounded_small_yaw_v2` | 32.03 |
| `ongoing_walking_yaw_v1` | 23.18 |
| `image_sampling_diagnostic_v1` | 22.35 |
| `sequential_small_turn_repairs_v1` | 21.61 |
| `small_yaw_image_reference_v3` | 21.36 |
| `neural_change_readout_v1` | 21.25 |
| `small_turn_target_decision_v4` | 17.94 |
| `causal_short_window_yaw_v1` | 15.19 |

## Why it accumulated

Successive investigations retained full binocular retinal movies, frontend
drives, numerical refinements, multiple environments, and versioned outputs.
For example, [the continuous-yaw runner](../scripts/run_continuous_yaw_mechanisms_v1.py)
writes a complete float32 `retina.npy` for each visual condition/profile,
alongside source and network arrays. Some reuse paths copy arrays into a new
study directory, as in [the geometry-grounded runner](../scripts/geometry_grounded_small_yaw_v2.py).
Individual study storage guards and later lossless-compression amendments
did not prevent the cumulative workspace from approaching the disk limit.

One concrete copied movie was checked end to end:

- `results/small_yaw_image_reference_v3/controls/s07_v16.5_y-2_spatial/retina.npz`
- `results/small_turn_reproduction_image_v3/controls/s07_v16.5_y-2_spatial/retina.npz`

They have distinct inodes and identical full-file SHA-256 hashes. Each consumes
approximately 202 MiB. This proves that some duplicate bytes exist; no full
duplicate search was performed, and a project-wide recoverable duplicate total
has not been established.

The most recent bilateral energy pilot's complete sealed package is only
**1,504,168 bytes**. It did not create the hundreds of GiB. The storage issue is
accumulation across earlier investigations. Retaining scientific evidence was
intentional; keeping all bulky evidence on the main working disk without an
effective overall capacity policy was poor storage management and should have
been raised earlier.

## What is safe to do next

No existing artifact was deleted, recompressed, moved or rewritten. No new
simulation was run, and no scientific result was reanalysed. This audit creates
only this report, a small inventory and a progress entry.

The first recovery option is **archive completed bulky studies to another disk**,
verify their files against the existing hashes, and retain a clear archive/path
manifest with reports and code locally. A move to another directory on the same
filesystem will not recover disk capacity. Existing sealed indexes and downstream
path references must remain intelligible and reproducible after any migration.

A second option is a separately approved deduplication/storage migration that
preserves every indexed file's bytes and expected references. Exact duplicates
must be verified; matching filenames do not establish identical content. Do not
delete movie/source arrays merely because they can potentially be regenerated.

Before new large experiments, use a project-wide storage budget and minimum-free-
space check, estimate complete-run size from a pilot, reuse existing inputs by
reference, and prospectively decide which newly generated movies need permanent
retention. These are proposed storage changes, not changes made during this audit.

This is an operational audit. It adds no neural-capability or biological-validation
evidence and does not alter any prior scientific conclusion.
