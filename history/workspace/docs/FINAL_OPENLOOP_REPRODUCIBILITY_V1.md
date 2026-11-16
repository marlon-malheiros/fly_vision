# Final open-loop reproduction V1

This is a portable Linux CPU open-loop research pipeline. Use Python with NumPy, SciPy, Matplotlib, pytest and g++; the archived environment and build commands specify exact versions. All older graph/data directories are read-only scientific dependencies. Output directories are exclusive; stages refuse to overwrite evidence. Keep unrelated project work and old studies.

From the repository root, set `PYTHONPATH=src:scripts`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, and a writable `MPLCONFIGDIR`. The project Python is `<HOME>/Lab/mech_male_fly_cns/.venv/bin/python`.

Execution stages of `scripts/final_openloop_milestone_v1.py`, in dependency order: `prepare`, `pilot`, `pilot_review`, `training`, `calibration`, `numerics`, `fit`, `test`, `replay`. `prepare` requires a new study version/output root for a complete rerun: the existing V1 output must never be overwritten. Source review correction R2 and its new before-pilot manifest preserve the initial evidence. Training/calibration/numerics use the frozen R2 source inventory. `fit` locks pooled-speed coefficients before any final test images. Then run `scripts/analyze_final_openloop_v1.py` and `scripts/review_final_openloop_v1.py`. No step selects a new graph, gain, threshold or decoder family from results.

Every scientific episode saves all observable neural rates, raw image-reference scores, source-group epoch currents and image/source/full-state hashes. The world/trajectory recipes regenerate images deterministically. One known-room pilot and four preselected final cases retain lossless full movies, all source drives and complete state checkpoints. The full 27-case numerical subset retains hidden states for all refinements. Check each receipt before using files. Model masks and IDs are in `ablation_ledger.json` and `graph_metadata_*.npz`.

A label-free neural decision example, after the study runs:

```bash
PYTHONPATH=src python scripts/replay_final_openloop_v1.py \
  results/final_openloop_milestone_v1/test/z24_v5.5_y-2/observations.npz \
  --output <TEMP>/final-openloop-decisions.jsonl
```

This replay reads only observation times and current/past bilateral DNp15 rates, graph identities and frozen readout coefficients. It receives no speed, yaw, onset or scene labels. The simulator separately uses those quantities to generate the input and score the decisions. The external linear monitor is not an anatomical motor circuit. The legacy hybrid comparator separately receives known constant speed and lacks stationary calibration. None of these scripts controls a fly or robot, establishes real-time host latency, or demonstrates physiological validity.

For the entire retinal-image-to-decision path, without trajectory labels:

```bash
PYTHONPATH=src python scripts/image_to_turn_final_openloop_v1.py \
  results/final_openloop_milestone_v1/replay/z24_v5.5_y-2/retina_xor.zlib \
  results/final_openloop_milestone_v1/replay/z24_v5.5_y-2/retina_metadata.npz \
  --output <TEMP>/final-openloop-image-decisions.jsonl
```

This interface requires the frozen binocular pixel calibration and chronological 200-Hz luminance frames. It regenerates source drives, runs the intact LPi graph from zero, and emits 100-Hz causal decisions. Batch execution replays recorded frames; equivalent chronological decisions do not establish real-time wall-clock processing. Full retinal/source hashes printed by this command must match the sealed episode summary. For a fresh complete execution, use a separate version/output root and retain the V1 scientific parameters, rather than deleting the preserved release.
