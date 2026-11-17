# Research objective and evidence discipline

The main objective is a fly optomotor circuit constrained by MaleCNS anatomy, tested against physiology and perturbations, and eventually implemented in an embodied system. The alignment pilot in the repository root is a supporting study. Do not redirect the project toward an alignment-methods paper without a new user instruction.

Read STUDENT_HANDOFF.md, docs/RESULTS_APPRAISAL_R2.md, docs/PROTOCOL_V1.md and docs/NUMERICAL_CORRECTION_R2.md before scientific changes. Follow the repository-root AGENTS.md as well.

Preserve results/r2, results/calibration_r2, results/v1 and results/calibration_v1 as reference evidence. Preserve the failed V1 numerical gate. Use generated/ for replays and new versioned output directories for new studies. Baseline verification is read-only through tools/check_baseline.py; do not run the receipt-writing review script against sealed reference outputs. Retrieve the baseline Git revision when checking historical source locks after later code changes.

The current T4/T5 population drive is functional and clamped. The central network has 20 individually identified cells; it is not a complete neuronal visual pathway. PS321-to-bIPS correspondence remains qualified. Only about 10-13% of PS321 and 14-17% of DNp15 incoming synapses are retained. Do not infer biological absence of a bIPS effect from this reduced model. No biological-recording or physical-robot validation has been completed.

Maintain the image-only controller interface. Simulator pose, true yaw, scene identity and disturbance timing may be used for stimulus generation, evaluation and explicitly separated calibration; they must not enter controller inference. Calibration/test scene seeds must remain disjoint. Current test scenes are inspected evidence for any subsequent scientific change.

Before expensive work, specify one question, anatomical/physiological assumptions, model/version, training/calibration/test separation, endpoints, numerical checks and stopping criteria. Use recorded chemical pairs, not invented edges or electrical conductances. Keep normalization fixed when comparing silencing conditions. Report all comparator outcomes, including the conventional controller's slightly better performance.

Ordinary reproduction requires only shipped derived anatomy. Do not download raw recordings, the >1-GB connectome table or bulk movies unless reconstruction is specifically needed. Do not commit data/raw, environments, tokens, caches or generated replays. Preserve byte-exact scientific files according to .gitattributes.

Append completed changes, checks, failures and limitations to the repository-root docs/PROJECT_PROGRESS_REPORT.md. Separate implementation correctness, engineering performance, biological explanation and deployment evidence. Append dated snapshots before sealing a new study.
