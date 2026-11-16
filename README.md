# Alignment assessment pilot

Research code and an **initial manuscript**, prepared on 16 November 2026.
This is a focused export from the Fly Vision project, covering the completed
alignment-assessment pilot. It does not contain the full walking/optic-flow
system or the project's earlier research history.

The pilot asks whether uncertain placement of visual inputs changes a model
assessment. It combines a retrospective stimulus-image check for six previously
examined T4 cells with a separate simulation of three simple spatial filters.

**Main result:** wider assumed blur removes the exact input aliases on the tested
grid. In the simulation, retaining several plausible alignments reduces incorrect
rejections but often leaves the answer unresolved and retains wrong families.
This does **not** establish biological validation, neuronal degeneracy, improved
mechanism recovery, or publication novelty.

## Read first

- [Initial manuscript PDF](output/pdf/alignment_assessment_manuscript_v1.pdf)
- [Editable manuscript](manuscripts/alignment_assessment_pilot_v1/manuscript.md)
- [Detailed study report](docs/ALIGNMENT_ASSESSMENT_PILOT_REPORT_V1.md)
- [Numerical correction and original failure](docs/ALIGNMENT_ASSESSMENT_NUMERICAL_TIES_R2.md)
- [Data, attribution and license scope](NOTICE.md)
- [Reproduction scope and limitations](docs/REPRODUCIBILITY.md)

Authorship, affiliations and declarations in the manuscript remain for investigator
review before submission. This repository is a research draft, not a paper acceptance.

## Reproduce

Use Python 3.14. The recorded local environment was Python 3.14.10,
NumPy 2.4.6, SciPy 1.18.1 and pytest 9.1.1. Run from this repository's root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
python -m alignment_assessment verify
python -m alignment_assessment reproduce --output generated/replay
```

The package runs directly from the checkout; no editable installation is needed.
On Windows, activate with `.venv\Scripts\activate`.

The replay recomputes all sampled input banks from the included small image
extracts, matches 18 cell/blur result rows, reproduces all 27 corrected synthetic
summary rows and 225 centre rows, then independently checks 810 image samples
and 135,000 candidate-family assessments. A failed comparison exits nonzero.
Outputs go to a **new** directory; existing outputs are refused.

Estimated complete replay: under one minute, under 512 MiB RAM and under 8 MiB
new files on the tested machine, with a required 1 GiB free-space reserve.
There are no neural simulations, model downloads or movie generation in this command.

The included image extracts allow a derived-input replay. They do not replace
the original multi-gigabyte recording archive or reproduce the raw extraction
and earlier historical parity checks. See [data provenance](data/README.md).

## Repository contents

| Path | Purpose |
| --- | --- |
| `alignment_assessment/` | Original numerical helpers and portable R2 replay/review |
| `tests/` | Scalar integration, decision and numerical tie tests |
| `results/alignment_assessment_pilot_v1/` | Selected archived reference evidence, including R1 and R2 |
| `manuscripts/`, `output/pdf/` | Initial manuscript, bibliography and reviewed PDF |
| `docs/` | Protocol, correction, results and reproduction notes |
| `data/` | Source metadata and attribution; raw recordings are excluded |
| `release_manifest.json` | SHA256 inventory for this export |
| `export_provenance.json` | Source hashes and explicit export adaptations |

The live `AGENTS.md` and `docs/PROJECT_PROGRESS_REPORT.md` stay outside the
release checksum inventory. The dated release-validation snapshot is included.
The selected evidence is a curated export, not a full copy of the original
sealed study; its original index hash is recorded in the provenance file.

## License

[MIT](LICENSE) applies to original code and the original release documentation.
The third-party stimulus extracts retain **CC BY-NC 4.0** terms and attribution;
they are not relicensed as MIT. The research manuscript is a review draft with
no additional reuse license granted here. See [NOTICE.md](NOTICE.md) for the exact
file scopes and source links.
