# Reproducing the published-circuit boundary comparison

This is a conditional reconstruction of printed equations, not the authors'
agent software. See the [protocol](PUBLISHED_CIRCUIT_COMPARISON_PROTOCOL_V1.md)
and [report](PUBLISHED_CIRCUIT_COMPARISON_REPORT_V1.md).

Requirements: Linux CPU, Python ≥3.11, NumPy, SciPy, Matplotlib and the existing
frozen graph, source drives and strict compiled kernel. No GPU or physical
camera is required. This is a project replay, not a standalone export. The
preserved primary-source audit is reused; a replay makes no new claim about
remote repository updates. Primary evidence records the 24 October 2026 audit.

Set `PYTHONPATH=src:scripts`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1` and a
writable `MPLCONFIGDIR` (for example `<TEMP>/mpl_published_circuit_v1`). Use the
project's scientific Python environment; on the study host this was
`<HOME>/Lab/mech_male_fly_cns/.venv/bin/python`.

From the repository root, run each action in order, with the **same new** path:

```bash
python scripts/reproduce_published_circuit_comparison_v1.py prepare --destination results/published_circuit_replay_new
python scripts/reproduce_published_circuit_comparison_v1.py freeze --destination results/published_circuit_replay_new
python scripts/reproduce_published_circuit_comparison_v1.py run --destination results/published_circuit_replay_new
python scripts/reproduce_published_circuit_comparison_v1.py analyze --destination results/published_circuit_replay_new
python scripts/reproduce_published_circuit_comparison_v1.py review --destination results/published_circuit_replay_new
python scripts/reproduce_published_circuit_comparison_v1.py plot --destination results/published_circuit_replay_new
```

The preparation and exclusive output writes refuse existing result files.
Execution verifies all frozen input/source identities before and after work.
It repeats 88 original trajectories and 176 algebraic reference traces. The
review verifies every output hash, rational/closed-form reference equations,
summaries and original decoder arithmetic, and independently replays one
small-yaw input with the original Python solver in both intervention conditions.
Figures use the same recorded means; no decoder or physiology fit is performed.

The authoritative initial audit additionally used the read-only original
Erginkaya source cache and ZIP central directory. Those inventories, the public
code snapshot, article, parameter figure, supplement and download failures are
preserved under the study's `audit/` directory, so reproduction needs no new
23-GB Zenodo download or temporary audit directory. This inventory does not
assert that every archived MATLAB variable was exhaustively inspected.

Use this wrapper for alternate destinations: it explicitly sets each spawned
worker's directory. The frozen low-level driver's direct `run --destination ...`
option does not propagate that setting to spawned workers and is unsupported.
Its first reproduction attempt stopped safely at exclusive creation of an
existing authoritative directory; the failed namespace and wrapper are retained
in `results/published_circuit_reproduction_v1`.

The complete second execution in `results/published_circuit_reproduction_v1_r2`
is checked by the study's completion review. Refer to that evidence for the
actual numerical agreement; command availability alone is not validation.
