# Reproducing recurrent source-path attribution V1

26 October 2026. This is a retrospective mechanistic study of retained
frozen-model outputs, not a new held-out classification benchmark.
[Report](SOURCE_PATH_ATTRIBUTION_REPORT_V1.md),
[protocol](SOURCE_PATH_ATTRIBUTION_PROTOCOL_V1.md).

## Fresh-build subset replay

From the project root, use the existing Linux CPU environment:

```bash
export PYTHONPATH=src:scripts
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MPLCONFIGDIR=<TEMP>/source_attribution_mpl
PYTHON=<HOME>/Lab/mech_male_fly_cns/.venv/bin/python
"$PYTHON" scripts/reproduce_source_path_attribution_v1.py --output results/my_source_attribution_replay
```

The output must be a new path under the repository. The command builds
fresh strict nonlinear and diagnostic linear solvers, reruns preparation,
the14impulse checks and the full recurrent adjoint, then compares every
retained array with the completed archive. Four predetermined primary
cases span training/calibration/old-test rooms, speeds and signed yaw.
Four forward cases cover intact, two distinct input omissions and a linear
field-hypothesis replay. All arrays match exactly on this host.
[Executed receipt](../results/source_path_attribution_reproduction_v1/complete.json).
Cross-platform bitwise identity is untested. The source datasets, original
fixed model and retained V2source/network files are required; a code-only
checkout is insufficient.

Add`--full`with another new output path to repeat all704component cases
and80forward controls. It does not rerun the report, arithmetic review,
figures or sealing. That second full execution was not performed.

## Full execution and analysis into a fresh namespace

The component operations can also run separately. Use the same new path
for every command:

```bash
"$PYTHON" scripts/source_path_attribution_v1.py prepare --destination results/my_source_study
"$PYTHON" scripts/source_path_attribution_v1.py kernel --destination results/my_source_study
"$PYTHON" scripts/source_path_attribution_v1.py components --destination results/my_source_study
"$PYTHON" scripts/source_path_attribution_v1.py replays --destination results/my_source_study
"$PYTHON" scripts/analyze_source_path_attribution_v1.py --destination results/my_source_study
"$PYTHON" scripts/review_source_path_attribution_v1.py --destination results/my_source_study
```

All writers are exclusive; do not rerun stages into completed/sealed
directories. Plotting/presentation scripts default to the completed root
and must be adapted to a new namespace before regeneration. Original
figures and presentationV2are both retained. Five flat CSVtables accompany
the authoritative JSON; nested component lists stay inJSONandNPZ.

The adjoint's independent check uses small dense augmented-state RK4
polynomials, separate from the reverse implementation. Its twelve
full-graph controls use a generated copy whose activation is linear; the
strict nonlinear controls use the unchanged original solver source.
Original nonlinear responses, not linear reconstruction, remain the
authoritative prediction/classification evidence.

## Preserved boundaries

Source checkpoint8e82d65fixes the new component analysis after acknowledging
that the old visual outcomes are known. No new neural or decoder fit is
performed. Input omission zeroes only external drive; neurons and recurrent
connections remain. The original graph, frontend, biological assumptions,
classification criteria and sealed outcomes stay unchanged. Selected
known-control replay is not a physiological experiment or proof of broad
generalization.

Completion includes the report, full component arrays, all checks, forward
controls, exact subset replay, source identities and a dated progress copy.
The immutable index excludes liveAGENTS.md and project progress, itself,
active sealer stdout, post-exit review and Python bytecode. An outside
post-exit receipt records rehash verification. The environment is recorded
in[environment.json](../results/source_path_attribution_v1/environment.json).
