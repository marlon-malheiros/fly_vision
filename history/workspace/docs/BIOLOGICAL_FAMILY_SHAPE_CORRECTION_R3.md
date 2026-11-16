# DNp15 shape-audit execution correction R3

27 October 2026. Preserve the R2 shape-action failure: it requested an own-model
observation fit for DNp15/GC7f/native, although the protocol fits only the two
predeclared primary cohorts. It stopped before writing a shape diagnostic table.
The R2 metadata audit completed successfully and remains valid.

R3 keeps all DNp15 observations. The primary DNp15/GC6f/WT cohort receives both
inherited-transfer and its existing calibration-only mapping. The secondary
DNp15/GC7f/native cohort receives inherited transfer only, exactly as in the
preceding study's scoring routine. No missing model is invented, no extra fit is
performed, and no analysis criterion or mathematical formula changes.

Preserve V1, R2, their manifests and failures. Compile and hash R3 before producing
shape summaries; retain its separate source manifest. Use R2 for metadata and R3
for shape analysis when reproducing this study in a new output directory.
