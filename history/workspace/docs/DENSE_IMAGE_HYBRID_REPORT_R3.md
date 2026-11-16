# Dense image / frozen-neural hybrid report R3

Completed 2026-10-30. **A frozen external hybrid passes the prespecified small-yaw detection and straight-walking alarm criteria in 60 previously untouched simulated rooms.** This completes the bounded engineering detection milestone. The physiological and native-circuit questions remain unresolved.

## Goal and the concrete change

Detect a small yaw onset during forward walking, including the fastest speed, without frequent false alarms during straight walking. The user explicitly authorized a clearly labeled hybrid. Preserve the functional T4/T5 frontend, the 13,624-cell LPi-expanded MaleCNS graph, all neural parameters and every previous result. Only the external image-motion branch changes in R3; the readouts were already fitted in V1 and are unchanged here.

The neural branch receives the original full 1-degree binocular movie, passes it through the frozen frontend/circuit and computes causal bilateral activity features. The external engineering branch measures dense local motion from a separate 0.5-degree binocular crop of the identical scene/trajectory. A geometric projection removes forward-translation flow without knowing speed or depth; a confidence-weighted median and 100-ms mean produce image yaw. This bypasses the old image branch's channel clipping/routing and uses finer images. These combined changes are not an isolated causal test of clipping alone.

The fusion requires both branches to agree in sign and uses their smaller absolute support; alarm when the magnitude exceeds the unchanged cutoff 1. Inference receives observed neural activity, images and timestamps, never true yaw, speed, onset, depth, pose, scene identity or a same-room control. The image model assumes body-forward translation, yaw-only rotation and stationary surroundings. It is an engineered sensor computation, with additional spatial information beyond the neural frontend.

Selected candidate: `dense_hybrid/full_dnp_change`. Priority was fixed before the final test; it was the first candidate passing all six empirical conditions independently in 36 separated known rooms and 24 new development rooms, plus all 81 numerical comparisons. [Protocol](DENSE_IMAGE_HYBRID_PROTOCOL_R3.md), [selection](../results/dense_image_hybrid_r3/selection.json), [before-test freeze](../results/dense_image_hybrid_r3/before_test.json), [execution freeze](../results/dense_image_hybrid_r3/execution_before_test.json).

## Final untouched-room experiment

Sixty new seed-disjoint rooms, balanced for clutter and complete-scene mirror orientation, each supply 16 conditions: three speeds × yaw 0/±2/±5 degrees/s, plus stationary. Thus 960 final physical-motion episodes feed all 20 fixed readouts/controls. Rooms come from the existing textured box/sphere family; these are new instances rather than new environmental families. All neural states run continuously. Walking starts at 0.5 s and yaw at 1 s; the primary endpoint is 1.19 s. At 2 degrees/s the fly has turned only 0.38 degrees by that endpoint.

The unchanged requirements are ≥80% detected, correct raw direction and joint detection/direction, ≥80% for each sign, ≤10% straight endpoint alarms and ≤10% straight rooms ever alarming in [1,3), ≤10% stationary alarms and zero stationary neural activity. Missing required output fails. The 60-room integer requirements are ≥96/120 joint turns, ≥48/60 for each sign and ≤6/60 straight or stationary alarms, independently at each speed and both magnitudes.

| Speed mm/s | Correct ±2 turns | Negative yaw | Positive yaw | Correct ±5 turns | Straight endpoint alarms | Straight any alarms | Neural-only any alarms |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5.5 | 120/120 | 60/60 | 60/60 | 120/120 | 0/60 | 0/60 | 0/60 |
| 11 | 120/120 | 60/60 | 60/60 | 120/120 | 0/60 | 0/60 | 2/60 |
| 16.5 | 115/120 | 58/60 | 57/60 | 120/120 | 0/60 | 0/60 | 30/60 |

All six primary empirical gates pass. Stationary any alarms: 0/60; all observable cells, full final states and saved checkpoints are exactly zero in every stationary case. [Full-state stationary audit](../results/dense_image_hybrid_r3/analysis/stationary_full_state_audit.json), [every condition/control](../results/dense_image_hybrid_r3/analysis/test_curves.csv), [all 19,200 episode predictions](../results/dense_image_hybrid_r3/analysis/test_episodes.csv), [descriptive intervals](../results/dense_image_hybrid_r3/analysis/descriptive_intervals.json).

![Final sensitivity and full-episode alarms](../results/dense_image_hybrid_r3/figures/final_detection_and_alarms.png)

Neural-only and selected-hybrid turn-success curves coincide. Dense-image-only and selected-hybrid alarm curves coincide at zero; the table and complete CSV retain their separate counts.

The selected neural-only branch passes all final empirical gates: **False**. Dense image-only passes all final empirical gates: **True**. Image-only correctly detects all 120/120 ±2-degree/s cases at each speed, compared with 115/120 for the hybrid at the fastest speed; both have zero straight alarms. Thus this study demonstrates no added reliability benefit from the neural branch. The hybrid's intersections can remove neural alarms and also discard correct image detections; [paired branch comparisons](../results/dense_image_hybrid_r3/analysis/paired_branch_comparisons.csv) quantify both effects. This does not establish a bIPS advantage, native-circuit repair or biological causality.

The old-image hybrids also pass the empirical behavioral gates on this final finite cohort, although their predeclared numerical checks remain failed and they were not eligible for selection. At the fastest speed, the matched old-image hybrid gives 111/120 correct small turns and 2/60 any-alarm straight rooms, compared with 115/120 and 0/60 for R3. These observed differences are not a claim of statistical significance or uniquely necessary engineering design.

![Every final fast straight room](../results/dense_image_hybrid_r3/figures/all_fast_straight_rooms.png)

Solid curves are all rooms in fixed order; the dashed score boundary remains 1. A clean single endpoint does not substitute for the full two-second monitoring criterion.

![Predefined first-final-room trajectories](../results/dense_image_hybrid_r3/figures/predefined_timecourses.png)

These are the first final room's predetermined fast straight/negative/positive examples, not cases chosen for favorable outcomes. Vertical markers show the scored yaw-onset time and endpoint; they are not input to inference. Neural scores are calibrated engineering readout units, not measured membrane voltage.

## Failed repairs and why this result is different

[V1](CONTINUOUS_READOUT_REPAIR_REPORT_V1.md) trained on complete straight negatives; new-development fast DNp15 detected 47/48 small turns but produced 13/24 straight alarms. Its role-based hybrid detected 45/48 with zero straight alarms yet failed numerical refinement. [R2](CONTINUOUS_READOUT_REPAIR_REPORT_R2.md) added another 100 ms of averaging; the same hybrid fell to 26/48 fast small turns. Both failed revisions were sealed, and neither generated its planned final images. Their failures and criteria remain unchanged.

R3 changes the engineering image representation instead of increasing neural weights or relaxing a criterion. It retains the frozen neural decoder and gives the agreement rule a dense, finer-sampled rotation estimate. The result supports this engineering combination within the tested setting. It does not uniquely identify the biological source of the original neural ambiguity or isolate clipping from sampling/dense spatial pooling. No further tuning follows this final test.

## Numerical and software evidence

- All 81 required selected-hybrid refinement comparisons pass; largest score difference 0.133571 ≤0.2. Endpoint and any-alarm episode decisions are unchanged; individual callback differences total 0. Primary image sampling is 0.5 degrees at 200 Hz; refinements use 0.25 degrees and 400 Hz. Corresponding neural rates reuse the parent's original/spatial/temporal/solver profiles. These are 81 newly rendered image sequences and 108 combined profiles, not 108 new neural simulations. [Comparisons](../results/dense_image_hybrid_r3/analysis/numerical_comparisons.csv).
- A separate FIR/scalar implementation independently reproduces all 81 selected refinement comparisons and verdicts, with maximum discrepancy 1.38e-14 in their reported score differences. [Independent numerical audit](../results/dense_image_hybrid_r3/independent_numerics_v1/review.json).
- Independent crop/full luminance and compiled/NumPy renderer comparisons are exact; crop yaw differs by 1.78e-14 degrees/s. Eight hundred independent landmark checks differ by at most 9.87e-7 degrees/s. Synthetic ±2/±5 yaw and depth/eye-lever-arm cancellation checks pass. [Geometry](../results/dense_image_hybrid_r3/analysis/geometry_and_parity.json).
- One-copy neural execution equals the sealed eight-copy intact rates/final state bitwise. All five new weighted fits are independently reconstructed with augmented least squares, correct class/episode weighting and original feature samples. Maximum fit-score discrepancy is 1.40e-12. [Fit audit](../results/continuous_readout_repair_r2/analysis/independent_fits.json).
- Independent scalar arithmetic checks 2,810,880 finite scores across all 960 final cases and 20 methods; largest difference 8.88e-15. Selected label-free streaming/batch discrepancy is 8.88e-16. All final tables, primary gates and 2,000 room-bootstrap draws are reconstructed. [Audit](../results/dense_image_hybrid_r3/analysis/independent_final_audit.json).
- Scalar weighted medians are checked on every saved local-evidence frame: one per 100 ms, plus every output of the four retained final cases. Other frames retain yaw estimates and deterministic recipes/hashes. Four predeclared full end-to-end replays reproduce fine and neural retinal movies, source drives, rates and states exactly. These are subset replays, not a second 960-case sweep. [Median audit](../results/dense_image_hybrid_r3/analysis/test_median_audit.json).
- A separate predetermined retinal replay reproduces raw yaw estimates exactly; future-only image changes leave earlier outputs bitwise unchanged. Three malformed clock/image inputs are rejected, and the observation-only Linux CPU CLI matches batch scores/decisions. [Causality and replay review](../results/dense_image_hybrid_r3/additional_causal_validation_v1/review.json).

The initial independent landmark auditor used a forward difference that failed its fixed tolerance. Its source/failure is retained; a symmetric central difference passes the unchanged tolerance. No inference or gate changed. [Failure](../results/dense_image_hybrid_r3/failures/geometry_audit_v1/failure.json). All simulation execution failures, if any, remain in each revision's failure directory and stage logs; the [sequence receipt](../results/dense_image_hybrid_r3/sequence_complete.json) records the completed execution. Numerical reproducibility is distinct from physiological validity.

## What remains unresolved

The reliable result is an external hybrid for yaw onset in noiseless synthetic scenes. It does not establish sustained-turn tracking, sensitivity below 2 degrees/s, arbitrary onsets/speeds, lateral translation, gait/head motion, roll/pitch, moving objects, camera noise, real-time deadlines or physical deployment. Visual output measures net yaw, without determining whether the fly intended to turn. This is open-loop work; no locomotion controller was added. Independent rooms provide only 60 environmental units: signs and speeds share rooms. Cluster-bootstrap intervals and Wilson alarm intervals are descriptive; passing observed counts does not guarantee a population false-alarm rate ≤10% or formal significance after multiple development revisions.

No new physiological dataset is scored here. The [existing independent HS constraint](HS_VOLTAGE_BENCHMARK_REPORT_V1.md) remains broad and cannot select the circuit; the earlier calcium comparisons, missing electrical coupling, anatomical/registration uncertainty and observation-model limitations remain. Neural-only false alarms and lack of a robust demonstrated bIPS benefit remain scientific findings. This milestone does not complete biological validation or the broader PhD assignment.

Two useful experimental follow-ups are now concrete. First, record bilateral HS/H2 and DNp15 responses to matched straight versus small-yaw optic flow while varying scene depth and texture asymmetry: the frozen model predicts texture-dependent straight-walking signals that can mimic turns. If recordings remain robust where this model fails, that identifies a missing biological computation rather than a need to tune its decoder. Second, compare those responses with and without experimentally justified bIPS perturbation using identical stimuli; the earlier computational lesions do not establish a reliable bIPS benefit. Both are testable hypotheses requiring real recordings and a matched measurement model, not biological findings established by the hybrid.

## Reproduction and evidence preservation

Use a separate Linux workspace with the original parent data and no existing V1/R2/R3 result directories. Use the [recorded Python/NumPy environment](../results/continuous_readout_repair_v1/environment.json), `PYTHONPATH=src:scripts`, one BLAS/OMP thread and a writable Matplotlib cache. Keep the parent's compiled renderer/circuit libraries and their source/parameter hashes. Tests: `tests/test_continuous_readout_repair_v1.py`, `tests/test_continuous_readout_monitor_r2.py`, `tests/test_dense_causal_yaw_r3.py`.

V1 driver: `prepare`, `cache`, `fit`, `known`, `numerical`, then `development`. Before inspecting the new development outcomes, freeze R2 (`prepare`, `known`, `numerical`) and R3 (`prepare`); run R3 `known` and `numerics`. Run the R3 independent `geometry` audit and the V1/R2 independent `fits` audit. The coordinator `scripts/execute_dense_image_sequence_r3.py` waits for upstream receipts, completes development/selection, freezes final execution, runs test/replay and independent audits without retuning. Every writer refuses existing outputs; old results must remain intact.

For label-free CPU replay, run `scripts/replay_dense_hybrid_r3.py` with any final `observations.npz` and a new `--output` JSONL path. It accepts no speed, event or yaw arguments. Raw-image estimation is implemented by [DenseCausalYaw](../src/male_optic_frontend/dense_causal_yaw_r3.py); the [study driver](../scripts/dense_image_hybrid_r3.py) runs the complete rendering → frontend/circuit → fusion path. This is portable software evidence, with physical-camera deployment unverified.

Git method checkpoints are ab39b50 (V1), 301fc21 (R2), 2ed027c (R3) and 3067f56 (auxiliary checks/coordinator). Completion archives include exact source/report copies and a dated progress snapshot; live AGENTS.md and progress remain outside immutable indexes. V1/R2 and all parent sealed outputs are preserved.

## Undergraduate explanation: what we did, what we want, and why

We want the simulated fly to notice a slow accidental turn while walking, without confusing fast straight walking with turning. Teaching the readout more straight walks and averaging longer did not solve both problems. We then kept the brain model unchanged and combined it with a separate, finer image-motion measurement. That hybrid passed our accuracy and false-alarm targets in 60 new virtual rooms. The image-only version also passed and missed fewer turns, so we have not shown that adding the brain model helps. We now have a working engineering reference for these simulations; explaining how a real fly's neural circuit achieves reliable detection remains the biological research goal.
