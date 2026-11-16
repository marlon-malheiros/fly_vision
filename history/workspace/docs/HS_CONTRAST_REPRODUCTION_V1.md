# Reproducing the HS contrast assay without changing sealed studies

The completed study preserves compact observations, both source interpretations, frozen criteria, code and source hashes. Full replay requires the retained upstream graph/source dependencies and the original scientific interpreter. It takes roughly an hour of aggregate observation CPU, not necessarily wall time. No movie archive is generated. The helper can share the 156-MB source ZIP by hard link on the same filesystem; simulation code only reads those dependencies.

Prepare a **new** destination; never rerun write stages in the original sealed result directory:

```bash
PYTHONDONTWRITEBYTECODE=1 <HOME>/Lab/mech_male_fly_cns/.venv/bin/python scripts/prepare_hs_contrast_reproduction_v1.py <TEMP>/hs_contrast_reproduction_v1
cd <TEMP>/hs_contrast_reproduction_v1
export PYTHONDONTWRITEBYTECODE=1
export OPENBLAS_NUM_THREADS=1
```

Run each stage with `<HOME>/Lab/mech_male_fly_cns/.venv/bin/python`:

```text
scripts/hs_contrast_validation_v1.py prepare
scripts/hs_contrast_validation_v1.py targets
```

Copy the staged public source-audit files before freezing R2 (these are scripts, one figure and access receipts, not simulated responses):

```bash
cp -a source_audit_for_r2 results/hs_contrast_validation_v1/source_audit
```

Continue with the same interpreter:

```text
scripts/hs_contrast_source_correction_r2.py freeze
scripts/hs_contrast_source_correction_r2.py targets
scripts/check_hs_contrast_interpretation_v1.py freeze
scripts/hs_contrast_validation_v1.py run
scripts/hs_contrast_validation_v1.py analyze
scripts/hs_contrast_source_correction_r2.py analyze
scripts/review_hs_contrast_validation_v1.py review
scripts/hs_contrast_source_correction_r2.py review
scripts/check_hs_contrast_interpretation_v1.py check
scripts/finish_hs_contrast_validation_v1.py plot
scripts/finish_hs_contrast_validation_v1.py report
scripts/finish_hs_contrast_validation_v1.py seal
scripts/review_hs_contrast_validation_v1.py audit
```

The prepare helper was checked for dependency integrity and imports; two complete source-to-neuron legacy cases were independently replayed during the original study. A second full 144-slot experiment is **not** claimed. Timing, absolute file locations and freeze timestamps may differ in a replay; physiological source values, formulas and neural output comparisons should reproduce. Reproduction is numerical verification, not a new biological dataset or new independent validation.

For the original completed study, run only the read-only audit stage. Old intentionally retired movies are not dependencies of this assay, and no bulk historical archive is regenerated.
