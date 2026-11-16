# Data provenance

The replay uses six small **derived stimulus-image banks**, totaling less than
1 MiB compressed. These are under `results/alignment_assessment_pilot_v1/`.
They contain the distinct images, trial-to-image indices, nominal centres,
canonical axes, 289 shifts and sampled input arrays for three assumed blur scales.
The `sigma_*` arrays are reference outputs; replay recomputes them from `images`.
Their use is governed by the separate [attribution and data terms](../NOTICE.md).

Original source: [Janelia Figshare, Gruntman_2017_Data.zip, version 1](https://doi.org/10.25378/janelia.5576101.v1),
file ID 9691765 (2,839,269,706 bytes). Metadata is preserved in
`figshare_article_5576101.json`. No raw archive is downloaded automatically.

The source extraction used MATLAB `protocolStruct.stim[*].matCell`, retaining
static non-background frames (codes 3 and 7), recoding contrast as `(f-3)/4`
and deduplicating images byte-for-byte. For an image height H, the source grid
centre becomes `[gridCenter[0]-1, H-gridCenter[1]]` in the movie convention.
The inherited canonical axes and reference shifts are included in the banks
and archived audit; they are assumed metadata, not refitted here.

This export cannot repeat the raw extraction, verify the entire author archive,
or independently re-establish earlier fits, axes, selected aliases or trial-duration
condition counts. The archived audit's 1,640-trial/328-condition totals are historical
results, not new raw checks by the portable command. Optical replay only checks
the image banks and 18 cell/blur comparisons. Consult the original paper and
archive for the original two-dimensional receptive-field mapping.

Synthetic data are generated locally using the frozen seed 20261116, three filter
families, 25 centres, 11 calibration bars, 25 test patches, three repeats, three
known noise scales and 200 draws per setting. No neural recordings are simulated.
