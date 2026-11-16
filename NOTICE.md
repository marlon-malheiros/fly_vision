# Attribution and license scope

The root MIT license covers original code in `alignment_assessment/`, `tests/`,
`scripts/`, the workflow, and original release documentation. It does not alter
third-party rights or grant a license to the manuscript draft.

## Third-party recording source and derived stimulus extracts

Source archive: **Michael Reiser (2017), Gruntman_2017_Data.zip, version 1**,
[Janelia Figshare, doi:10.25378/janelia.5576101.v1](https://doi.org/10.25378/janelia.5576101.v1).
Associated paper: Eyal Gruntman, Sandro Romani and Michael B. Reiser (2018),
[Simple integration of fast excitation and offset, delayed inhibition computes
directional selectivity in Drosophila](https://doi.org/10.1038/s41593-017-0046-4).

The archived Figshare metadata declares
[Creative Commons Attribution–NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)
([legal text](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en)).
The exact metadata receipt is included as `data/figshare_article_5576101.json`.
This receipt was inspected during release preparation; a new API metadata request
could not be completed because this environment could not resolve the hostname.

The following selected files contain extracts or transformations of those source
stimuli and are distributed retaining that attribution and noncommercial scope:

- `results/alignment_assessment_pilot_v1/input_cell03.npz` through `input_cell08.npz`;
- `results/alignment_assessment_pilot_v1/input_audit.json`;
- `results/alignment_assessment_pilot_v1/figures/optical_sampling_sensitivity.png`
  and `.pdf`.

Changes from the source: deduplicated static flash frames; contrast recoding
`(image_code - 3) / 4`; zero-based movie coordinates; inherited receptive-field
centres/axes; subpixel sampling and assumed Gaussian convolution. No source neural
voltage traces or source MATLAB implementation are included. Attribution in this
repository does not imply endorsement by the original authors.

The source dataset's CC BY-NC terms are separate from any license on the paper.
Commercial use of these extracts is not authorized by the MIT code license.
Scientific result tables and synthetic outputs are provided as research evidence;
no additional rights over third-party material are asserted.

## Draft manuscript

Files in `manuscripts/` and `output/pdf/`, including figures embedded in the
draft, are included for reading and scientific review. No additional manuscript
reuse license is granted by this release. Investigators must confirm authorship,
affiliations, funding and declarations before any submission.

Python dependencies retain their own licenses and are not vendored here.
