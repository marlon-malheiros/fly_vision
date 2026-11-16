# H2 metadata/source extraction: reproduction V1

The raw 3.1-GB `edgeDataAndTable.mat` and spreadsheet remain at their original
verified locations under `data/raw/validation_sources_v1/zhao2025/`. Raw SHA-256:
`12d67bf1fd73d0fe1389e0168311f17c7b26b69fddaaaf4f3e411fc1a7ba0f26`.
No model parameters or raw-source files are edited.

From the project root, use the existing Python 3.12/h5py environment:

```bash
PYTHONPATH=src:scripts data/derived/postfix_test_env_v1/bin/python -m unittest discover -s tests -p 'test_h2*.py' -v
PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 data/derived/postfix_test_env_v1/bin/python scripts/reproduce_h2_trial_metadata_v1.py --output <TEMP>/h2_reproduction_unique_directory
```

The output directory must not exist. The wrapper executes final metadata V4,
independent metadata reviewer V2, source-only spike extraction V1 and its
independent sparse-event reviewer V1 in sequence. Every stage must exit zero.
It uses the original admitted source paths; no network download is necessary.
The schema/name-lookup failures V1–V3 remain preserved but are not the final
pipeline. Dependencies are Python, NumPy and h5py, with recorded versions in
the metadata provenance. No MATLAB execution, MCOS object code, pandas,
openpyxl or physiological parameter fitting is required.

Plotting is separate because the existing h5py interpreter lacks matplotlib.
The existing simulation interpreter has matplotlib; no package was installed
or modified. To regenerate figures/summaries into the new replay directory:

```bash
PYTHONPATH=src:scripts MPLCONFIGDIR=<TEMP>/mpl_h2_reproduction OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 <HOME>/Lab/mech_male_fly_cns/.venv/bin/python -c 'from pathlib import Path; import summarize_h2_trial_metadata_v2 as s; s.RUN=Path("<TEMP>/h2_reproduction_unique_directory"); s.main()'
```

Do not point plotting at a sealed study. Numerical outputs should match all
1,344 joins, 22,848 shared numeric elements, 4,000 aligned repeats, 4,032 raw
repeats/events and 84 curves. The independent count review checks all
conditions, sample boundaries and raw stop events, with 1e-9 arithmetic
agreement tolerance only; this is not a biological acceptance threshold.
Summary-sheet DSI agreement is descriptive and did not determine extraction
parameters or a new pass criterion.

The original execution and independent full-data reviews are preserved.
A fresh-namespace subset replay is also retained; a second complete end-to-end
replay has not been claimed. Code checkpoints and immutable evidence index
are listed in the report/completion record. The live progress report and
AGENTS.md are intentionally outside the immutable index.
