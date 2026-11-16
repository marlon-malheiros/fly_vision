# Neural options reproduction V1

1 November 2026. Producers use exclusive output files. Run a complete reproduction in a separate workspace with the original input data/results available read-only. Never rerun a producer into its sealed result directory.

The tested runtime is CPython 3.11.16 with native FlyVis 1.2.0, existing cached Torch 2.13.0+cu130 executing on CPU, and isolated restored dependencies under `<TEMP>/neural-completion-flyvis-v1`. The main project Python 3.14 interpreter does not contain these packages. No GPU is used. The recorded package inventory and native source hashes are in `results/neural_model_options_r2/before_execution.json`; its inventory includes visible duplicate distributions and is not a resolved dependency lock. `results/neural_model_options_r2/analysis/resolved_runtime.json` records the actual core module origins and versions. The original wheel and its PyPI digest are in `data/raw/neural_completion_options_v1`. The setup helper is `scripts/run_neural_completion_runtime_v1.py`. It reuses the old study's cached package paths without modifying them. Restoring a different CPU wheel or binary stack requires its own parity check; portability across all binary builds was not tested.

Restore the downloaded FlyVis wheel into the temporary target, install the recorded missing dependencies there, and retain access to the package paths recorded in `results/neural_population_readout_v1/runtime_r2/package_paths.json`. Copying the source workspace and symlinking prior input studies into its results directory permits separate output production. The original data/model files must remain available. The renderer is the preserved `results/final_openloop_milestone_v1/methods/renderer.so`.

Use this prefix for stages:

```bash
PYTHONDONTWRITEBYTECODE=1 <HOME>/.local/bin/python3.11 \
  scripts/run_neural_completion_runtime_v1.py SCRIPT STAGE
```

Run in this order in the separate workspace:

1. `neural_model_options_v1.py prepare`, then `canonical`.
2. `neural_model_walking_options_v1.py prepare`; `analyze_neural_model_flow_v1.py freeze`; then walking `run`, followed by flow `analyze`.
3. `neural_model_perspective_repair_v1.py prepare`, `run`, `analyze`.
4. `neural_model_numerics_v1.py prepare`, then `run`.
5. `published_population_yaw_v1.py prepare`, `observer`, `train`, `calibration`, `fit`, `calibrate`. Train and calibration **input generation** can run independently; calibration scoring follows the frozen fit.
6. `published_population_direction_repair_r3.py prepare`, `symmetry`, `fit`, `calibrate`.
7. `review_neural_model_options_v1.py freeze`, `active`, `scores`, `numerics`; `review_published_population_yaw_v1.py inference`, `replay`.
8. `report_neural_model_options_v1.py figures`, `biology`, `population`.

The population preparation explicitly permits reuse of the V1 **unrendered** test-seed reservation and rejects overlap with other prior inventories. A reproduction must include that recorded reservation or adapt only the workspace/bootstrap input arrangement in a documented revision. It must not reuse existing new-study outputs as inputs to conceal an incomplete reproduction. Restored package setup failures are not scientific model failures.

Focused tests in the project simulation interpreter:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  <HOME>/Lab/mech_male_fly_cns/.venv/bin/python \
  -m pytest -q tests/test_published_flow_probe_v1.py
```

All six pass. Replay checks establish canonical equality and a moving binocular image/final-state/feature reproduction. A second complete 384-condition study was not executed. Source code, configurations, all produced numerical artifacts, corrections, complete reports and dated progress copies accompany the completed studies. Immutable indexes exclude the live progress report and AGENTS.md; independent post-seal receipts remain outside their own indexes.

Packaging is separate from scientific execution. `seal_neural_model_options_v1.py provenance` uses the tested bootstrap; `prior` independently rehashes the two preceding neural studies. After committing source/report versions, `prepare --date 2026-11-01` archives exact sources and dated progress in each completed study; `seal` writes immutable indexes. Run `verify --study STUDY_DIRECTORY_NAME` in separate processes for the three completed studies. Do not run any packaging producer into an already completed directory. The main index also covers the raw source acquisition and preserved failed-attempt directories; the other indexes cover their own results and source snapshots.
