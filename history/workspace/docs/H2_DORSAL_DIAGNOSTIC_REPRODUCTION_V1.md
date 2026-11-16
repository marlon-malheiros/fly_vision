# Reproducing the upper-field H2 diagnostic V1

Use the existing local frozen inputs and original model, plus the versioned
code. No dependency or new physiological parameter was installed/fitted.
The simulation environment is Python 3.14.8 with NumPy 2.5.3 and SciPy 1.18.1;
the study's `environment.json` records actual versions and compiler.

From the project directory, a fresh-build four-case replay is:

```bash
PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  <HOME>/Lab/mech_male_fly_cns/.venv/bin/python \
  scripts/reproduce_h2_dorsal_diagnostic_v1.py \
  --output results/h2_dorsal_diagnostic_reproduction_new
```

Choose a new output name each time. The wrapper refuses an existing output
directory. It verifies frozen dependencies, compiles the unchanged strict
C++ kernel, and replays one edge-phase case, one head-yaw case, one
identical-input lesioned circuit, and one 80-ms-stimulus finer-resolution
case. Compare every retained retinal/source/network array where applicable,
including final states; agreement is exact, without a fitted tolerance.

Add `--full` to execute **all 832 tasks sequentially** (384 new stimulus
variants, 320 identical-input lesions, 128 numerical controls), rerun every
analysis JSON, and compare those analyses exactly with the completed study.
This option does not repeat the two independent Python solver replays,
independent review, figures, report or sealing. Only the four-case replay
was actually executed as a fresh-build reproduction here; no second full
832-task reproduction is claimed. Full replay may take substantially longer
than the original three-worker run. Model, input, numerical and biological
agreement are different assertions.

The original stage commands were `h2_dorsal_diagnostic_v1.py prepare`, `run`
and `analyze`, followed by `review_h2_dorsal_diagnostic_v1.py` and
`plot_h2_dorsal_diagnostic_v1.py`. Their default directory is the completed
study. **Do not rerun those default stage commands into sealed results.**
Use the reproduction wrapper to obtain a distinct namespace.

The final figure command is `plot_h2_dorsal_diagnostic_v2.py`, which preserves
the initial figure set and moves tuning legends outside the data. It used
`MPLCONFIGDIR=<TEMP>/h2_dorsal_matplotlib_v1` and the
same Python environment. It creates three PNG/PDF pairs from saved arrays.
They retain all locations/variants and use min–max scaling only to display
individual tuning-curve shapes; analysis always uses signed unscaled rates.

Necessary retained dependencies include the frozen model under
`results/fixed_neighbor_motion_v1`, H2 trial metadata/source curves under
`results/h2_trial_metadata_v1`, and saved primary inputs/network traces under
`results/h2_frozen_model_benchmark_v1`. The input manifest and immutable
indexes identify exact files with SHA-256 and sizes. These local data are
not all stored as Git blobs. The original raw 3.1-GB HDF5 file is needed for
raw-spike reconstruction in the prior study, not for this numerical replay.
No download or h5py is required for this diagnostic's replay.

The final report, completion receipt, immutable artifact index and independent
post-exit integrity check distinguish the completed finite diagnostic from
the still-unresolved goal of reliable small-yaw detection during walking.
