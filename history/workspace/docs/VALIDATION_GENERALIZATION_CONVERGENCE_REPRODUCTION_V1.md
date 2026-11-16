# Reproduce the numerical validation component — V1

The frozen numerical study is complete. These commands document its execution; do not rerun into existing output directories, overwrite evidence or modify files in the prospective manifest. The four predecessor studies remain sealed. Run from the project root with the recorded Python/NumPy/SciPy/C++ environment and the cached graph/data artifacts. The original experiment used four CPU workers and a separately recorded lossless-storage continuation; the main result directory also contains unfinished, separately identified hardware work.

The scientific conditions, copied graph identities, parameters, scene splits, clocks and acceptance criteria are in [the frozen configuration](../configs/validation_hardware_v1.json), [protocol](VALIDATION_HARDWARE_PROTOCOL_V1.md), [methods manifest](../results/validation_hardware_v1/prospective_manifest.json) and [storage amendment](VALIDATION_HARDWARE_STORAGE_AMENDMENT_V2.md). Every trial's receipt records its source-drive/time digests and output-file hash. Legacy convergence sources are inherited from Study A; other visual inputs are deterministically regenerated from their specified scene and profile. Full panoramas and full intermediate neural histories are not retained for every condition; full source drives can be regenerated, while retinal/drive checkpoints, all recorded wide-cell rates and full final states are retained.

Original execution order, already performed:

```sh
env PYTHONPATH=src python scripts/run_validation_hardware_v1.py setup
env PYTHONPATH=src python scripts/preflight_validation_hardware_v1.py
env PYTHONPATH=src python scripts/run_validation_hardware_v1.py freeze
env PYTHONPATH=src python scripts/run_validation_hardware_v1.py run --kind all
env PYTHONPATH=src python scripts/resume_validation_hardware_storage_v2.py freeze
env PYTHONPATH=src python scripts/resume_validation_hardware_storage_v2.py run
env PYTHONPATH=src python scripts/resume_validation_hardware_storage_v2.py review_orphans
env PYTHONPATH=src:scripts python scripts/analyze_validation_hardware_v1.py
```

The actual run's logs/receipts, rather than this abbreviated command list, describe the controlled storage interruption and corrected interpreter paths. Setup, freeze and analysis reject existing outputs; use an isolated workspace for a fresh end-to-end reproduction. No additional parameter calibration is required or permitted by this frozen study. Complete outputs: [simulation](../results/validation_hardware_v1/execution_all_complete.json), [analysis](../results/validation_hardware_v1/analysis_complete.json).

Review/replay/report commands executed after scoring:

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=src python scripts/review_validation_hardware_v1.py --destination results/validation_hardware_v1/analysis_review_v1_r2
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=src:scripts python scripts/check_validation_geometry_replay_v1.py --destination results/validation_hardware_v1/geometry_replay_review_v1
env MPLCONFIGDIR=<TEMP>/male_optic_matplotlib_validation OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=src:scripts python scripts/report_validation_science_v1.py --destination results/validation_hardware_v1/scientific_report_v1_r3
```

Each destination must be absent. For repeat review, choose a new directory; the reporting script uses the completed R2 arithmetic review as its input. The first failed review and plotting runs are retained separately. Their source snapshots document corrections, and the final scripts preserve the original scientific outputs and tolerances. Post-score adjacent-profile and paired-response diagnostics are labeled as such, with all values and deterministic bootstrap seeds saved.

The independent arithmetic review rechecks all 3,536 trial receipts, 2,950 predecessor index entries, splits, fits, predictions, thresholds and intervals. The separate original-Python replay checks eight regenerated source inputs and 32 neural trajectories; it does not independently reintegrate all 14,144 trajectories. A successful numerical check is not physiological validation. See the [technical report and undergraduate explanation](VALIDATION_GENERALIZATION_CONVERGENCE_REPORT_V1.md) for failed robustness criteria and unfinished hardware work.
