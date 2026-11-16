# Frozen-model H2 comparison: reproduction V1

Use the existing Linux CPU Python environment; do not install packages or edit
the original model. Numerical dependencies are NumPy/SciPy and g++; the source
R geometry check also uses installed Rscript. Plotting uses matplotlib from
the existing simulation environment. The source admission remains separate.

```bash
PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 <HOME>/Lab/mech_male_fly_cns/.venv/bin/python -m unittest discover -s tests -p test_h2_edge_arena_v1.py -v
PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 <HOME>/Lab/mech_male_fly_cns/.venv/bin/python -m unittest discover -s tests -p test_h2_benchmark_statistics_v1.py -v
```

The main controller phases were `prepare`, original-R geometry review V3,
`freeze`, then `run`. Preparation is deliberately not rerunnable over an
existing namespace. Never point it at the sealed result directory. The
recorded source freeze and prospective git checkpoint identify the exact
implementation. All 1,473 planned main/sensitivity/static cases retain
lossless retinal keyframes and index maps, delivered source arrays, 14 wide
cell traces, final states and hash receipts. Primary source conditions reuse
traces only where declared stimulus inputs are identical.

After the main run, `validate_h2_frozen_model_benchmark_v1.py` executes the 32
fixed numerical checks and two full-prefix original-Python replays;
`analyze_h2_frozen_model_benchmark_v1.py` calculates observations/metrics and
all 10,000 bootstrap draws; `review_h2_frozen_model_benchmark_v1.py` checks
those results independently. Numerical failures are reportable evidence and
never cause post hoc tolerance changes or replacement of primary arrays.
Plotting is a post-analysis presentation step, with frozen metrics unchanged.

The separately versioned reproduction wrapper supports a new output directory
and a fresh-build bounded smoke. A full replay is available explicitly and
uses the same recorded plans/source inputs; no second complete run is claimed.
See `scripts/reproduce_h2_frozen_model_benchmark_v1.py --help` for options.
The original raw H2 data need not be decoded again: the sealed metadata/source
outputs and their primary provenance are unchanged dependencies of this study.

The live progress report and AGENTS.md remain outside immutable indexes. The
study includes a dated progress snapshot. Byte-identical reproduction and
independent numerical agreement are distinct from physiological validation.

Use a **new directory inside the project workspace** for receipt paths:

```bash
PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 <HOME>/Lab/mech_male_fly_cns/.venv/bin/python scripts/reproduce_h2_frozen_model_benchmark_v1.py --output results/h2_benchmark_new_smoke
```

Adding `--full` reconstructs and checks every main/sensitivity/static case.
That option is a full main-stage replay; it does not automatically rerun the
separately documented numerical controls, bootstrap, independent reviews or
presentation stages. Their preserved scripts and source freeze identify the
remaining calculations. The completed study ran all of them once; the bounded
fresh-build smoke is an additional replay, not a second complete study.
