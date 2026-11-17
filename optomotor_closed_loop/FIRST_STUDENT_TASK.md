# First student task: gain, delay and the disturbance/drift tradeoff

Assignment prepared 16 November 2026. This is a proposed new study, **not an experiment already executed**. Reproduce the supplied R2 baseline first, then freeze this study's exact protocol before new outcomes.

## Why this is the first task

The baseline motor conversion is calibrated with target_loop_gain=2. In an ideal linear steady-state velocity-feedback model, with disturbance d and loop gain G,

`residual yaw / disturbance = 1 / (1 + G)`

The expected reduction is therefore `G / (1 + G)`: **66.7% at G=2**. R2's measured 66.4% RMS reduction is close to that value. The idealized calculation ignores transient dynamics, nonlinear motion detection, saturation and scene differences; it does not predict every measured trajectory. It does show why the current compensation number should not be treated as a biological circuit ceiling.

Stronger feedback may reduce residual turning, but sensor/neural/motor delays can cause oscillation or overshoot. It may also worsen unwanted turning from translation-related signal biases. The student should characterize this tradeoff before changing neuronal weights or adding circuit components.

## Question

With R2 anatomy and neural dynamics fixed, can a fair, bounded choice of feedback strength improve disturbance rejection while keeping straight-travel errors and transient behavior acceptable? Does the neural circuit differ from conventional visual control under matched tuning opportunities and added delay?

## Fixed scope

- Put new code, protocol and configuration under studies/gain_delay_v1. Leave the R2 model, calibration, inputs and result files unchanged. Use composition or a separately versioned runner for new settings.
- Keep the random-square display, circuit topology, neurotransmitter assumptions, normalization, 20-ms central time constant and camera/motor assumptions fixed except for the explicitly tested added delay.
- Candidate target loop gains: **1, 2, 3, 4, 6**.
- Additional image-observation delays: **0 and 20 ms**. These are added to the existing frontend/neural/motor dynamics, not replacements for their time constants. Model the added delay causally using past image observations and preserve timestamps.
- Controllers: intact neural and conventional visual controller. Include a no-controller reference. Both controllers receive the same gain candidates, calibration data, scenes and selection rule. Do not select parameters separately for each test pattern.
- Do not refit neural weights, change the descending readout, use simulator truth during inference, or retune a failed test outcome.

## Splits and execution budget

Proposed unused seed namespaces, to be checked against all prior project seeds before use:

- Motor-conversion calibration: **1501-1504**.
- Development/setting selection: **2501-2504**.
- Final held-out test: **9501-9506**.

Document and hash any necessary seed correction before generating outcomes. Calibration may use known imposed rotations. Development patterns choose one gain per controller under the common selection rule; final test patterns choose nothing. Retain results at G=2 as the existing-operating-point comparator.

Use translation speeds 0, 0.04 and 0.08 m/s, disturbances 0 and +/-20 degrees/s, and the R2 disturbance schedule. The 5-gain x 2-delay x 2-controller x 4-development-pattern x 3-speed x 3-disturbance grid contains **720 development episodes**, before the small calibration/no-controller bank. Testing two controllers at both the selected and G=2 operating points, two delays and six patterns requires up to **432 held-out episodes**, plus **54 no-controller references**; deduplicate an identical selected/G=2 setting rather than rerunning it. Preserve all cases and define deduplication before execution.

At the measured R2 speed, this workload is expected to take roughly **10-15 minutes of simulation on the original CPU**, plus setup, tests and analysis. This is an estimate, not a deadline. Measure a small development-only timing pilot, then report the updated cost estimate before the full grid. Do not use final test outcomes for timing admission or selection.

## Outcomes and selection rule

Preserve the R2 primary metric: yaw RMS over the full disturbance epoch relative to its paired no-controller reference. Also report steady-epoch RMS, median and worst straight-travel yaw RMS, peak post-disturbance counter-turn, command saturation fraction, recovery time and oscillation amplitude.

Provisional **new-study engineering target**: at least **80% median disturbance RMS reduction**, separately for both signs, with median straight-travel RMS <=**0.5 degrees/s** and no straight-travel case above **2 degrees/s**. These are design targets, not measured fly thresholds or changes to the original R2 pass rule. Keep the selected half-step RMS-change limit at **5%**.

Before execution, define the exact transient/stability measurements. A concrete starting definition is: recovery time after disturbance offset is the first time |yaw| remains <=1 degree/s for 0.2 seconds, with non-recovery right-censored at episode end. For sustained oscillation, report peak-to-peak yaw in the final second and compare it with the immediately preceding second; add a longer predeclared episode if five seconds cannot establish stability. Specify acceptance limits and timing before looking at new outcomes.

Use a common development selection rule: reject settings that violate the predeclared drift, saturation or stability guards at either tested added delay; among remaining candidates, maximize the smaller of the two disturbance-direction median reductions, pooling declared development conditions; break exact ties toward lower gain. If no setting qualifies, report that outcome and the complete tradeoff instead of relaxing limits.

Evaluate each controller's selected setting once on the final test patterns, alongside G=2 and no-controller references. A setting chosen to meet 80% on development data does not count as success unless it meets the predeclared final criteria. The current six R2 test patterns are already inspected and must not serve as this study's blind test.

## Deliverables

1. A dated protocol/configuration/source lock made before new outcomes, with seed freshness and resource admission.
2. Automated checks for causal delay, identical disturbance/no-controller kinematics, fixed neural weights, calibration/test separation and refusal to overwrite old evidence.
3. A complete per-case table, calibration/selection receipt, final results and numerical refinements.
4. A plot of disturbance rejection versus unwanted straight turning, labeled by gain/controller/delay; show every candidate rather than only the winner.
5. A plain-language conclusion: what improvement occurred, what it cost, whether conventional control remains as good/better, and whether the next limitation appears to be control tuning, sensory bias or missing circuit evidence. Do not infer a unique biological cause from this experiment alone.
6. Append completed work and failures to the repository-root progress report. Make a reviewable pull request before broadening the study.

After this one bounded control-characterization study, proceed to the anatomical boundary audit in STUDENT_HANDOFF.md. A better engineering number alone does not establish a biological mechanism or restore missing bIPS/DNp15 inputs.

## Copyable AI prompt

```text
Our first student study is FIRST_STUDENT_TASK.md in optomotor_closed_loop. Read the repository and local AGENTS.md files, STUDENT_HANDOFF.md, that assignment, and the R2 result appraisal. Reproduce the baseline first if there is no matching local receipt.

Implement a new studies/gain_delay_v1 study with R2 neural weights, anatomy and dynamics unchanged. Test only the five declared gains and two added observation delays, with identical tuning opportunities for the neural and conventional controllers. Use separate calibration, development and untouched final-test seed namespaces. Keep simulator truth out of inference. Freeze exact metrics, stability limits, selection, resource budget and source hashes before new outcomes. Measure a development-only timing pilot and report the full estimated runtime before executing the grid.

Keep all candidate/failure results, retain G=2 and no-controller comparators, run the causal-delay and numerical checks, and evaluate the selected settings once on the final patterns. Report rejection/drift/transient tradeoffs and whether the provisional 80% target was met. Do not change reference files, neuron weights, test criteria or seeds after outcomes. Stop after this study and deliver a reproducible report, plots, progress entry and reviewable diff; do not launch another tuning search on the final test set.
```
