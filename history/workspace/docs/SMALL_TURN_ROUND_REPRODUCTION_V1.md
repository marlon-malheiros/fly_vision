# Small-turn round reproduction

1 November 2026. Producers require fresh output paths; reproduce in a separate
workspace with earlier studies/input data available. Never execute a producer over
sealed outputs. Use the same tested isolated runtime as
[the previous investigation](NEURAL_MODEL_OPTIONS_REPRODUCTION_V1.md): CPython
3.11.16, FlyVis1.2.0 and Torch2.13.0+cu130 executing on CPU. Most new computations
use NumPy; Torch fits/inference are CPU-only. The four original models and their
parameters remain fixed. New readers are task-trained artificial readouts.

Prefix each stage with:

```bash
PYTHONDONTWRITEBYTECODE=1 <HOME>/.local/bin/python3.11 \
  scripts/run_neural_completion_runtime_v1.py SCRIPT STAGE
```

Exact execution sequence:

1. `small_turn_round_v1.py prepare`; `review_small_turn_round_v1.py source`.
2. `small_turn_round_v1.py existing_fit`.
3. `small_turn_operating_points_v1.py freeze` before any calibration scores.
4. `small_turn_round_v1.py reduced_train` and `reduced_calibration`; these input
   generation stages are independent and may run concurrently, with four workers
   each. Calibration is not scored until the fit is frozen.
5. `small_turn_round_v1.py existing_calibrate`. This original V1 stage saves its
   complete predictions/scores, then reproduces the retained NumPy-scalar JSON
   export failure. `run_small_turn_round_serialization_r2.py recover` preserves
   the partial file and completes its summary without repeating inference.
6. `small_turn_temporal_followup_v1.py freeze`, then `evaluate`, before reduced
   fits exist. This is the separately declared post-failure temporal development.
7. `run_small_turn_round_serialization_r2.py reduced_fit`, then
   `reduced_calibrate`. Run the dependent reviewer only after this export finishes.
8. R2 runner `decide`, then `operating_evaluate`; `finish_small_turn_round_v1.py
   select`, `diagnose`, `figures`. No candidate qualifies, so no new-room stage runs.
9. R2 runner `arithmetic`; `audit_small_turn_round_v1.py replay`, `curves`,
   `decisions` in separate independent processes.
10. `numerics_small_turn_round_v1.py prepare`, `run`, `analyze`; execute
    `review_small_turn_numerics_v1.py` with no stage argument, after analysis.

Run `audit_small_turn_constant_features_v1.py` without a stage argument for the
descriptive post-outcome audit `constant_feature_audit.json`:
count scale-floor features in each fit and check reduced calibration extrema;
no inactive feature is found in a reduced fit. It is not a fitted correction.
All original scientific sources are verified against `before_execution.json`.
Supplementary operating/temporal/numerical sources have separate pre-outcome
freezes. The serializer-only R2 correction remains separate, with its failed
partial export retained under failures. Reports and independent reviews do not
change the failed behavioral/numerical criteria.

Focused tests:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src \
  <HOME>/Lab/mech_male_fly_cns/.venv/bin/python -m pytest -q \
  tests/test_small_turn_round_v1.py tests/test_small_turn_temporal_followup_v1.py
```

All nine pass. The fresh literal-source replay reproduces an entire walking
input hash and both circuit copies' three feature vectors. This is a subset
replay, not a second complete 748-run execution. Current source/report versions,
original frozen methods, failures, numerical evidence and a dated progress copy
are sealed with an artifact index. Live progress and AGENTS are excluded; the
post-exit integrity receipt is outside its own index. Numerical integrity is not
physiological validation. No new matched-recording benchmark was executed.

Final packaging also preserves every pre-outcome source under its full relative
path after verifying the original digest. This repairs the initial flat archive's
driver/module basename collision while preserving its original files and the
pre-outcome Git version. `seal_small_turn_round_v1.py seal` runs after the final
source/report checkpoint; `verify` runs in a separate process after sealing.
