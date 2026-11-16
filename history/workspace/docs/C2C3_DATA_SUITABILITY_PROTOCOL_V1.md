# C2/C3 physiological-data suitability audit V1

This is a bounded data audit, not another model sweep or biological-validation
claim. Preserve the completed72-model study, all frozen parameters and reports.
The source paper's qualitative findings and public Figure6 analysis code have
already been inspected. New numerical response curves have not been inspected.

## Scope frozen before acquiring new MAT files

Pin the existing authors' repository at
`745c6114b72a61dabc9389a1f024dbe22f679edf`. Retrieve all eight processed Figure6
ON/OFF direction-selectivity files, selected analysis helpers, README/LICENSE
and the two Figure4 Mi1 flash files. Their combined raw size is below45MiB.
No full repository clone, raw movie archive, behavioral archive or bulk images.
Retrieve additional small source scripts only when their dependency resolves a
specific metadata/measurement ambiguity. Record exact paths, hashes and reasons.

Inspect MAT variable names, field paths, dimensions, metadata, animal/session
identities, time axes, direction arrays and preprocessing definitions. Do not
inspect or plot per-direction response amplitudes, genotype effects or model
prediction errors. No fitting or neuronal simulation. Trial arrays may be
loaded to enumerate their structure; their response values remain unscored.
All source animals remain inventoried, including controls outside the authors'
explicit seven-fly display selection. Do not silently reproduce those exclusions.

## Decision checklist

1. Source identity/integrity and readability: every selected file is pinned,
   byte/hash verified, readable and its structure catalogued.
2. Biological units: find explicit fly IDs/session IDs, crosswalk ON/OFF and
   repeated ROIs, and check collisions across files/conditions. Array positions
   alone are not verified independent animals. Record whether genotype and
   neuronal-subtype assignments are explicit or inferred from source labels.
3. Stimuli: resolve angular directions, speed, bar width, contrast, timing,
   sampling, display field/refresh and coordinate convention. Separate
   file-level evidence from article descriptions and modeling assumptions.
   Missing exact generator/logs prevent an exact image-to-recording claim.
4. Measurement: trace background/baseline subtraction, trial averaging,
   interpolation, peak windows, normalization and ROI/fly aggregation. Identify
   missing processing steps and separate calcium from voltage/rate units.
5. Independent testing: if explicit identities support at least two animals per
   partition, reserve whole animals by a fixed SHA256 ordering within genotype.
   Allocate ceil(N/3), at least2, to holdout, leaving at least2 for development.
   This is a feasibility rule, not a statistical power guarantee. The same animal
   and all its ON/OFF/subtype/ROI records must share one partition. Unknown
   identities prevent a verified blind animal-level split. Do not compute
   response summaries or use reserved values for decisions in this audit.
6. Reconstruction constraints: identify whether the data constrain relative
   temporal/contrast/directional properties and whether actual connectivity,
   signs, conductances, coupling and kinetics are available. Synapse counts and
   observed silencing effects do not identify electrical or chemical conductance.
   Do not add feedback to intact measured kernels without resolving double counting.

Give separate go/no-go decisions for a descriptive source-data reproduction, a
conditional stimulus-matched component benchmark, exact end-to-end validation,
and integrating a new C2/C3 reconstruction. Unknowns are explicit; a usable
component benchmark does not imply a calibrated full circuit or small-turn result.

## Resources and evidence

One worker; <=600 scientific CPU seconds, <=2GiB RSS, estimated60MiB final data
and128MiB hard cap,20GiB free reserve. Store acquired originals once plus compact
JSON/CSV manifests; no duplicate response archives. Preserve failed probes and
corrections. Version the protocol/acquisition/audit sources before new MAT
inspection, append dated progress, save its dated copy before sealing, and
verify the final index after every writer has exited. Live AGENTS/progress stay
outside immutable indexes. No external contact is authorized or needed.
