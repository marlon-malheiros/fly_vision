# H2 raw-repeat exclusions addendum V4

25 October 2026. The faster V3 failed before saving an extraction because it
required retained raw-repeat count to equal the aligned raster count. A full
schema-only inventory found 32 conditions with three retained raw repeats,
two raster rows and exactly one explicitly recorded `exclude` index. The
other conditions have three raster rows and no exclusions. Preserve V3 source
and failure log, plus the complete bounded exceptions inventory.

V4 requires valid unique in-range exclusion indices and exactly
`raw repeats minus explicit exclusions == numReps == raster rows`. Inventory
all raw repeats, including excluded ones, without deleting or recounting
spikes. All global/local equality and complete coverage rules remain fixed.
Per-raster-row spike counts will be labeled as aligned rows; correspondence
to particular original raw repeats is not asserted from ordering alone. The
author's response-window calculation explicitly uses raw repeat 1, even if
that repeat is listed excluded; reproduce that rule, disclose this limitation,
and preserve events from all raw repeats as an audit trail.

Source endpoint extraction has still not run. Its route implementation is
snapshotted before adding inventory of all raw repeats. Freeze V4 before
restarting metadata extraction. The synthetic window rejection test initially
caught the correct error from V1, but asserted the V2 subclass; correct the
test to their common ValueError superclass, retain the failed log and rerun.
No response criterion or model parameter changes.
