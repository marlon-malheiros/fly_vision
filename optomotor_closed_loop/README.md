# Connectome-constrained optomotor closed loop

**Student: begin with [STUDENT_HANDOFF.md](STUDENT_HANDOFF.md)** for exact environment setup, read-only baseline verification, safe replay, next tasks and AI prompts. The repository entry point is [STUDENT_START_HERE.md](../STUDENT_START_HERE.md).

A new, bounded research prototype: a panoramic camera viewing a **random-square cylindrical display** drives functional ON/OFF motion inputs, measured MaleCNS chemical connectivity constrains a recurrent central circuit, and the descending output steers a virtual robot. The robot's action changes the next camera observation.

The target is a biologically testable optomotor circuit and eventual embodied implementation. The current R2 establishes an executable integration and evaluates synthetic engineering behavior. V1's textured-arena results and numerical FAIL remain in results/v1. [R2 discloses the subsequent temporal-integration correction and user-requested stimulus change](docs/NUMERICAL_CORRECTION_R2.md). Neural-recording validation and physical hardware tests remain separate work.

## Model

- Official **MaleCNS v1.0** data, acquired with source size and SHA256 checks.
- **20 individual central neurons:** bilateral HSN/HSE/HSS/HST/H2/PS321/DNp15 and six LPi12/LPi21 cells.
- **6,753 T4a/b and T5a/b inputs**, grouped into eight type/side functional motion-drive channels. All their measured connections into the selected central neurons are retained.
- Core-to-core recurrence retains measured asymmetry and synapse counts. Entire-brain incoming counts determine normalization; omitted partners have zero modeled drive.
- Presynaptic sign assumptions from predicted neurotransmitters, tanh signed deviations, and assumed 20-ms central dynamics.
- Motor command reads **DNp15 left minus right only**. It receives neither simulator pose nor true yaw. Motor sign/gain is calibrated in separate scenes before evaluation.

The clamped T4/T5 approximation cuts their recurrent dynamics and central feedback; cut feedback is explicitly exported. This is a reduced central-circuit model, not a complete fly visual pathway or a reproduction of the collaborator's omitted original engine. PS321 is used as the bIPS-associated candidate from the prior project; that identity remains a qualified correspondence.

## Run

From this directory, in a Python environment with the requirements installed:

```powershell
python -m pip install -r requirements-reproduce.txt
python tools/check_baseline.py
python -m unittest discover -s tests -v
python tools/replay_baseline.py --output generated/student_baseline_01
```

The supplied compact `data/derived` files allow offline model runs; the >1-GB raw release is unnecessary for ordinary replay. Experiments refuse existing output directories. The replay helper also compares every trajectory with the reference. To use the lower-level runner in a new directory:

```powershell
python scripts/run_experiment.py --stage all --calibration generated/manual_01/calibration/calibration.json --output generated/manual_01/results
```

Calibration sources and data are hashed and checked again before test execution. Calibration uses four scene seeds. Evaluation uses six different seeds, three translation speeds, +/-20 degrees/s disturbances, straight/static controls, and intact, bIPS-silent, H2-silent, no-controller and conventional visual-control conditions. See [the frozen protocol](docs/PROTOCOL_V1.md).

Primary outputs: `results/r2/report.md`, `summary.json`, `episodes.csv`, `traces.npz`, and `overview.png`. A failed engineering gate is retained and is not evidence that all biological optomotor circuits fail.

The completed R2 run passes its three engineering gates. It reduces disturbance RMS by a median 66.4%, with median straight-travel yaw RMS 0.20 degrees/s. The conventional visual controller reaches 67.2%; a circuit advantage is not established. Fourteen unit/integration checks and the separate arithmetic/source-integrity review pass. [Read the result appraisal](docs/RESULTS_APPRAISAL_R2.md) for the scientific limits and execution timing.

## Data reconstruction

`scripts/prepare_connectome.py --extract` requires PyArrow and NumPy and downloads approximately 1.1 GB once from the official public release. It scans connectivity in Arrow batches, emits compact source/core metadata and edge tables, and preserves central incoming/outgoing boundary counts. Reconstruction must be performed in a separate workspace because the script writes to data/derived. The original author's private .data_runtime environment is not included in GitHub and is not needed for ordinary replay. The normal model requires NumPy; the random-square renderer uses SciPy, and plotting uses Matplotlib.

The source dataset is [MaleCNS v1.0](https://male-cns.janelia.org/download/), licensed **CC BY 4.0**. Credit: FlyEM/HHMI Janelia, University of Cambridge, MRC Laboratory of Molecular Biology, Google Research, and collaborators. Derived anatomy retains this attribution. Synapse counts and transmitter predictions are not measured physiological efficacies.

The physiological/mechanistic reference is Erginkaya et al. (2025), [A competitive disinhibitory network for robust optic flow processing in Drosophila](https://doi.org/10.1038/s41593-025-01948-9). This prototype has not yet been compared quantitatively with those recordings or perturbation data.
