# Reproducing the continuous-yaw mechanisms study

This is a Linux CPU project replay using the preserved original/expanded graph
dependencies. It is not a physical camera benchmark or a standalone robot
package. Requirements: Python ≥3.11, NumPy, SciPy, Matplotlib and g++ with C++17.
The study host used `<HOME>/Lab/mech_male_fly_cns/.venv/bin/python`.

Set these variables before executing commands from the repository root:

```bash
export PYTHONPATH=src:scripts
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MPLCONFIGDIR=<TEMP>/mpl_continuous_yaw_v1
```

Use the wrapper below and one **new** directory for every action. Preparation
clones the fixed world/graph recipe, rebuilds the variable-mode renderer from
source and records the canonical configuration identity. It does not overwrite
the global configuration or use a temporary audit directory. Every spawned
simulation worker receives its destination explicitly. The existing frozen
graphs, strict neural kernel and historical preflight evidence remain required.

```bash
python scripts/reproduce_continuous_yaw_mechanisms_v1.py prepare --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py preflight --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py freeze --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py analysis_freeze --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py core --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py core_analysis --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py fresh --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py refine --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py probes --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py normalization --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py solver_half --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py control_analysis --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py fit --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py test --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py review --destination results/continuous_yaw_replay_new
python scripts/reproduce_continuous_yaw_mechanisms_v1.py plot --destination results/continuous_yaw_replay_new
```

Keep at least 75 GB free before a full batch. All 520 primary retinal movies,
three finer-time movies and source/neural outputs are retained. This can take
tens of minutes or longer depending on CPU and disk. Existing output creation
uses exclusive writes. A failed phase must be preserved and corrected in a new
version/namespace; do not delete evidence to make a rerun look successful.

The `fit` action reads training/calibration arrays only, writes all candidate
fits and freezes selected readouts before `test` opens held-out neural arrays.
The review independently recomputes neural summaries, input/geometry identities,
restored graph controls and ridge fits, and checks selected full trajectories
with the original Python neural equations. A passing review is numerical
evidence, not physiological validation.

The review also executes the fixed 12-trajectory supplementary half-step check
for the preserved-weight graph and other copies, using the same two existing
probe inputs. See the [validation addendum](CONTINUOUS_YAW_CONTROL_VALIDATION_ADDENDUM_V1.md).

The replay uses the V2 numerical reviewer. The first review's two-point
finite difference was inaccurate near vertical rays. V2 uses a fourth-order
stencil at the same time increment and unchanged tolerance. The original
review source and failed run are retained, with the
[correction](CONTINUOUS_YAW_VERIFICATION_CORRECTION_V2.md) recorded separately.
For optional descriptive tables after scoring, run
`python scripts/summarize_continuous_yaw_mechanisms_v1.py` on the authoritative
study only; these tables add no acceptance rules.

The authoritative source audit/benchmark specification is preserved separately
under `physiology_audit/`. It does not claim fresh recording validation. Reusing
its downloaded source snapshot makes no claim that remote repositories were
reaudited at replay time. See [physiological gates](CONTINUOUS_YAW_PHYSIOLOGY_BENCHMARK_V1.md).

Actual reproduction scope is recorded in the final report and completion review.
A fresh-namespace preparation/preflight/freeze smoke test is distinct from a
second full 520-input execution; neither should be inferred from the presence
of these commands alone. The original failed classification criteria remain
preserved. [Protocol](CONTINUOUS_YAW_MECHANISMS_PROTOCOL_V1.md).
