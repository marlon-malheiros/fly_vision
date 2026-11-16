# Reproduction scope

The portable program is a release adaptation. `alignment_assessment/core.py` is
byte-identical to the pilot's frozen original numerical helper. The separate
`corrected.py` preserves the R2 1e-9 chi-square tie tolerance. The driver uses the
same seed and observation-generation order. The source-to-export hashes and
adaptations are recorded in `../export_provenance.json`.

The archive includes the original synthetic output and failed review, corrected
output and successful review. R1 single-fit counts depended on floating-point
near ties and are **not** the current baseline. The R2 amendment occurred after
initial outcomes; it is not an independently prespecified study.

The command checks:

1. SHA256 values for the selected shipped files.
2. All 18 cell/blur optical count rows and all recomputed bank values (tolerance
   1e-12 contrast), starting from included derived images.
3. Exact equality of all 27 R2 summary rows and 225 centre rows, including wrong
   families and unresolved cases, using all 45,000 generated datasets.
4. A separate squared-distance implementation and inverse-gamma thresholds for
   135,000 family assessments, plus literal scalar integration at 810 image samples.

The full original study index is **not** included as this export's inventory:
its missing historical dependencies would make a full availability claim misleading.
Its hash and the original post-exit receipt are preserved in the provenance file.
This export's own `release_manifest.json` describes only files actually shipped.
Live AGENTS and progress files are deliberately outside that inventory; the dated
release-validation snapshot is inside it.

No new raw neural response comparison, biological validation, independent-animal
test or complete author-archive integrity audit is performed. Blur is an assumed
sensitivity, not measured optics; it could overlap with filtering already present
in an effective model. The original experiment's broader RF mapping must not be
treated as missing merely because selected bar stimuli were ambiguous here.

## Optional manuscript build

The shipped PDF is the exact previously reviewed ten-page draft. Markdown and
bibliography are unchanged; only the LaTeX figure paths were made relative.
With TeX Live and the packages named in the preamble, run from
`manuscripts/alignment_assessment_pilot_v1/`:

```bash
mkdir -p ../../generated/manuscript
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../../generated/manuscript manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../../generated/manuscript manuscript.tex
```

The output bytes may differ with timestamps, TeX and fonts. The reference PDF
has not been replaced. The selected figure assets are included, but regeneration
of the publication layout is not part of the numerical replay or CI.

## Validation limits

Local validation uses a relocated copy and the installed scientific dependencies.
This environment cannot resolve external package hosts, so a fresh dependency
download and a hosted GitHub Actions execution have not been verified locally.
The workflow is prepared for the recorded Python minor version. Other Python or
library versions are not certified by this release.
