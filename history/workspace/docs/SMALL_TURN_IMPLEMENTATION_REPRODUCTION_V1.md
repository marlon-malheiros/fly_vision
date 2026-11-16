# Reproducing the small-turn implementation studies

25 October 2026. Preserve sealed outputs. All writers require new paths;
do not rerun prepare, score, review, plot or seal stages against the
completed study directories. Fresh execution below builds from source,
writes to a new namespace and compares retained arrays with the archive.

## Dependencies and scope

Portable Linux CPU implementation, tested here with Python3.14.8,
NumPy2.5.3,SciPy1.18.1,matplotlib3.11.2,g++16.2.1,R4.6.1. No new packages
were installed. Six independent one-thread workers produced the primary
sweeps; no GPU, live camera, robot or closed-loop deployment was tested.
[Exact environment](../results/small_turn_implementation_environment_v1.json).
R is needed for the original source-array export, not the retained-CSV
replays below. Base R exported the original unsmoothed Zhao arrays without
new fitting; source arrays, CSV and assignment tables are retained.

The archive depends on original fixed-neighbor config/targets/graph,
unchanged old walking inputs reused in V2, source eye-map datasets and
local source modules. Their used files are indexed with hashes. A source
checkout alone does not include these large numerical datasets. Preserve
the corresponding results/data paths when moving the project.

## Fresh-build replays actually executed

From the repository root, select the project's existing Python:

```bash
export PYTHONPATH=src:scripts
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MPLCONFIGDIR=<TEMP>/small_turn_reproduction_mpl
PYTHON=<HOME>/Lab/mech_male_fly_cns/.venv/bin/python
```

Use new output names for each invocation (the following example paths
must not already exist):

```bash
"$PYTHON" scripts/reproduce_small_turn_implementation_v1.py neural --output results/my_neural_replay
"$PYTHON" scripts/reproduce_small_turn_implementation_v1.py image --output results/my_image_replay
"$PYTHON" scripts/reproduce_small_turn_implementation_v1.py target --output results/my_target_replay
```

Each command recompiles the renderer; neural replay also builds strict and
accelerated solvers. Four predetermined cases per study cover original
input reuse, fresh rooms, straight/±2/±5 motion and fine numerical clocks.
All retained retina/source/neural/reference arrays match exactly on this
host, and target replay also checks both policies' associated decisions.
Cross-platform floating-point identity has not been established.

Executed receipts:

- [Four neural cases](../results/small_turn_reproduction_neural_v1/complete.json)
- [Four V3 image/control cases](../results/small_turn_reproduction_image_v3/complete.json)
- [Four V4 target-decision cases](../results/small_turn_reproduction_target_v4/complete.json)

Append `--full` to replay every primary episode (704neural,432image,
384target) into another new directory. This option repeats **primary
execution only**, not every pilot/numerical control, decoder fitting,
scoring, independent review, figures or sealing. It has not been run as
a second full sweep; the completed originals and four-case replays are
the evidence claimed here.

## Analysis evidence and version history

V1 known pilots/H2 diagnostics were superseded before their main sweep.
V2 is the complete three-version neural comparison; all coarse image
spatial failures remain. V3 is the completed numerically stable image
study whose calibration alarm policy fails. V4 is the new fixed-target
policy tested prospectively on new rooms. Reports:

- [V2 neural comparison](GEOMETRY_GROUNDED_SMALL_YAW_REPORT_V2.md)
- [V3 failed policy](SMALL_YAW_IMAGE_REFERENCE_REPORT_V3.md)
- [V4 engineering milestone](SMALL_TURN_TARGET_DECISION_REPORT_V4.md)

Reviewers independently reconstruct retained endpoints/means,
coefficients/cutoffs where relevant, decisions, qualification gates,
thresholds and room-bootstrap evidence. Their completed PASS receipts are
in each study root. These reviewers write exclusive receipts and should
be adapted to a new review namespace before rerunning; do not overwrite
the originals. Authoritative JSON retains nested fields; six CSV files
provide flat convenience tables only.

Prospective checkpoints: c2df8dc(V1),78b705a(V2),8376261(readouts/control
implementation),b967430(V3),e483e5a(V3controls/test scheduling),c5c1ce8(V4).
Frozen per-study manifests record exact files before test generation.
Final completion receipts identify the completed source/report commit.

## Integrity and preserved limitations

Each study's `completion_v1/artifact_index.json` lists path,size andSHA256.
The sealer includes a dated progress copy and excludes liveAGENTS.md and
`docs/PROJECT_PROGRESS_REPORT.md`, its own index, post-exit review and
Python bytecode. Verify indexes after writers exit using the read-only
verifier, choosing a new output receipt path:

```bash
"$PYTHON" scripts/seal_small_turn_implementation_v1.py verify --output results/my_small_turn_integrity_review.json
```

This command rehashes the three existing indexes; it does not rerun the
simulations. Do not modify indexed files to make a review pass; record a
new version and correction instead.

Passing checks demonstrate numerical reproducibility of these finite
simulations. They do not establish biological validity, a repaired neural
detector, a threshold below2°/s, universal scene generalization or robotic
performance. The broad PhD objective remains open.
