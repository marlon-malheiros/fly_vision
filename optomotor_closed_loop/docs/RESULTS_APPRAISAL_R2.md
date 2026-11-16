# Appraisal of the random-square closed-loop prototype

16 November 2026.

Implemented and executed a new reduced optomotor model in this workspace. It is based on official MaleCNS v1.0 chemical connectivity, not the unavailable executable engine from the shared archive. A camera views random black and white squares on a gray virtual cylindrical display; ON/OFF correlation signals drive grouped T4/T5 sources; measured connections constrain a 20-neuron recurrent central network; bilateral DNp15 output controls a virtual robot. Robot steering changes its next camera observation.

## Stimulus

- 5-degree square width at the display center, nominal 15% area coverage; overlaps are possible.
- Equal counts of bright and dark squares on gray; luminance codes 1, 0, and 0.5.
- World-fixed coherent pattern on a cylindrical display, radius 0.9-1.4 m in virtual-robot coordinates.
- 360-degree azimuth, 60-degree elevation, 256x48 camera samples.
- Declared optical/antialiasing filters; no claim that these are measured fly optics or an exact published stimulus replay.
- Translation changes the optic-flow projection as well as body rotation. There is no hidden true-yaw or disturbance input to the controller.

## Results

Four scenes were used only for motor sign/gain calibration. Six different square patterns were evaluated across three forward speeds (0, 0.04, 0.08 m/s), +/-20-degree/s disturbances and straight/static controls. Five conditions produce 270 episodes. All comparisons retain intact motor calibration, topology and normalization; silencing clamps the specified neurons.

| Condition | Median yaw RMS reduction vs no controller | Median unwanted yaw during straight travel |
|---|---:|---:|
| Intact circuit | 66.38% | 0.197 degrees/s |
| PS321/bIPS-associated cells silent | 66.03% | 0.215 degrees/s |
| H2 silent | 55.22% | 0.212 degrees/s |
| Conventional camera-motion control | 67.24% | 0.088 degrees/s |
| No controller | 0% | 0 degrees/s |

The intact model improves all 36 disturbed cases. Its worst straight-travel RMS is 0.555 degrees/s. Both disturbance-direction medians improve and its median straight RMS remains below the predeclared 2-degree/s engineering guard. Six selected half-step checks change primary RMS by at most 0.0423%, within the unchanged 5% numerical limit.

All fourteen implementation checks pass. A separate arithmetic review reproduces every saved episode RMS with maximum discrepancy 1.78e-15 degrees/s, verifies the complete case grid and frozen sources, and checks no-controller physics. These are numerical checks performed within this project, not independent-laboratory replication.

The earlier textured-arena V1 remains a numerical FAIL. R2 followed that outcome and changed both temporal integration and the stimulus as disclosed in NUMERICAL_CORRECTION_R2.md. V1 results are not relabeled fresh or combined into a new acceptance rule. The readable V1 source copies normalize line endings; results/v1/source_bytes.json additionally preserves the exact original source bytes, verified against the original receipt.

## What the model supports

A real-connectivity-constrained descending pathway can be integrated into a functioning, image-driven feedback controller under this bounded synthetic setup. The prototype is now an executable basis for targeted biology and embodiment studies.

The conventional controller performs slightly better on the primary descriptive comparison. The experiment does not establish a useful advantage from the biological architecture. The small bIPS-associated lesion effect and larger H2 effect are properties of this reduced model and fixed motor calibration.

Biological interpretation is especially limited by circuit boundaries: only roughly 10-13% of PS321's and 14-17% of DNp15's incoming synapses are retained. Other partners have zero modeled activity. T4/T5 recurrence and 7,373 recorded central-to-source feedback pairs are cut by the functional clamped-input approximation. Transmitter signs, dynamics, sensory drive and motor conversion remain assumptions. PS321's correspondence to the experimentally identified bIPS class remains qualified. No physical fly detection threshold, biological necessity, or whole-pathway validation is claimed.

## Execution time

The completed R2 270-episode evaluation, including the selected numerical reruns, took **140.65 seconds (2 minutes 21 seconds)** on the current CPU environment. Calibration, data acquisition, implementation, unit tests, artifact review and conversational tool overhead are additional. Ordinary replay uses compact derived anatomy and does not download the 1.1-GB connectivity table again. Repeated test runtime is expected to be on the order of a few minutes on this machine, with system load and plotting affecting the total.

## Next evidence needed

1. Expand circuit coverage from recorded partners using an anatomical inclusion rule fixed before new outcomes, and restore selected measured recurrent feedback. Improve the PS321/DNp15 boundary before treating their ablation results as a biological explanation.
2. Build a matched-stimulus comparison with central-neuron physiology and perturbation data. Prior inspected recordings remain development evidence. Establish a distinct validation split or independent dataset.
3. Test noise, sensor/actuator delay, contrast, square size/density, wider yaw frequencies and continuous disturbances under separately declared conditions.
4. Add a physically calibrated camera and motor adapter for the intended robot and measure field performance. The current controller API already receives image observations only, but a real camera calibration and physical hardware test have not been performed.

For implementation and this first experiment, GPT-6.1 Sol Max is a reasonable setting. Ultra becomes useful when independent circuit, physiology and robotics work can be delegated in parallel. The reasoning setting does not substitute for missing physiological constraints or validation data.

See ../results/r2/report.md, ../results/r2/summary.json, ../results/r2/arithmetic_review.json and ../results/r2/overview.png.
