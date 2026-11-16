# Reproducing the bounded input-mapping audit

Run from the project root with the preserved previous-study inputs present.
The recipe is an offline Linux CPU replay. It uses Python, NumPy, SciPy and
Matplotlib; the optional existing-H2 schema check additionally needs h5py.
It does not rerun the 520-input neural study or invent new visual inputs.

The simulation interpreter used was
`<HOME>/Lab/mech_male_fly_cns/.venv/bin/python`.
For the H2 schema action, the existing
`data/derived/postfix_test_env_v1/bin/python` supplied h5py. Environment versions
are saved in the audit's completion evidence. No package was installed or
upgraded in either baseline environment.

```bash
export PYTHONPATH=src:scripts
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MPLCONFIGDIR=<TEMP>/mpl_input_mapping_v1

python scripts/reproduce_input_mapping_audit_v1.py prepare --destination results/input_mapping_replay_new
python scripts/reproduce_input_mapping_audit_v1.py audit --destination results/input_mapping_replay_new
python scripts/reproduce_input_mapping_audit_v1.py review --destination results/input_mapping_replay_new
python scripts/reproduce_input_mapping_audit_v1.py loader --destination results/input_mapping_replay_new
python scripts/reproduce_input_mapping_audit_v1.py plot --destination results/input_mapping_replay_new
# With h5py available:
python scripts/reproduce_input_mapping_audit_v1.py h2_resource --destination results/input_mapping_replay_new
```

Use the same new destination for all phases. Creation/writes are exclusive:
retain failures and use a new namespace instead of deleting old evidence.
Preparation verifies selected inputs against the previous study's index,
copies curated identity metadata and freezes sources before the new checks.
The wrapper explicitly sets each action's destination; no worker is spawned.

Source replay checks all eight known symmetric cases and independently samples
every target with RegularGridInterpolator. The separate reviewer checks stored
arithmetic and the virtual common-measure control. The loader action executes
only time-zero assembly fixtures and verifies that no ODE step occurred.
The H2 action verifies the existing source hashes and HDF5 top-level schema;
it does not decode trials or score physiological responses.

The authoritative execution has one complete audit plus independent checking.
A fresh-namespace preparation smoke is recorded separately; it is not a second
full replay. A passing numerical audit is not a biological validation result.
