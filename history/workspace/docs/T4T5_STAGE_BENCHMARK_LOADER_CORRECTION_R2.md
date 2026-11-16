# T4/T5 benchmark loader correction R2

2026-11-05. Original freeze `230bca2` is preserved. The first `simulate` command
stopped with `KeyError: listfilterList` before a stimulus case, model trace,
development score or heldout response transform was produced. The original
failure JSON is retained. This was a new-loader implementation error, not a
scientific failure of any candidate.

The archived MAT variable is `filterList` (12 named columns), not
`listfilterList`. The R2 entrypoint aliases that existing label array for the V1
runner without changing any stored numeric filter, old method file, criterion,
stimulus, observer or model parameter. It verifies both the original methods
manifest and an additional R2 manifest before dependent execution.

Use `scripts/t4t5_stage_benchmark_r2.py freeze` once, then its `simulate`,
`development`, `decide` and `report` commands in place of the V1 entrypoint.
The independent Octave/2D reviewer is unchanged. This correction is made before
response outcomes, and does not add candidates or loosen gates. Successful-stage
resource files do not include the failed process; the failure happened within
about0.5s wall time and its full process CPU was not logged.
