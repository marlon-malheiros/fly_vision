# Corrected physiological diagnostics — V2

Completed 2026-10-21. Status: conditional computational diagnostics and independent data-handling review complete; full physiological validation remains unestablished.

## What changed and why

An independent geometry/image audit identified an interface error in the inherited physiological motion clamp: the two eyes were assigned incompatible local horizontal signs, and the signed clamp included negative sensory drives. This diagnostic bypasses the image frontend. Its correction therefore leaves all sealed walking studies, image-processing parameters, anatomical graphs and neural gains unchanged. Both geometry-corrected signed and nonnegative rectified proxies were specified before their network outcomes. Neither was selected by recording agreement.

[Geometry audit](FLOW_CLAMP_INTERFACE_AUDIT_V1.md), [correction protocol](PHYSIOLOGICAL_INTERFACE_CORRECTION_PROTOCOL_V2.md), [new-condition protocol](HELDOUT_SPEED_CONDITION_PROTOCOL_V1.md).

## Reused 13-second recording comparison

The comparison retains all 240 source traces, soma-specific population readouts, reporter/background cohorts, 35 calibration flies and 28 test flies. The test flies were already inspected in V1; this is a corrected reanalysis, not fresh validation. Each corrected proxy has 16 observation models fitted only on calibration recordings. These measurement filters and gains do not change neural parameters. All 760 test trace/model/mode scores were retained.

The table gives original-circuit equal-fly MSE divided by the measured zero-response reference MSE, with each proxy's separately calibrated observation model. Lower values indicate lower conditional prediction error. These ratios are descriptive outcomes, not a biological acceptance rule.

| Cohort | Test flies | Legacy signed | Corrected signed | Corrected rectified |
|---|---:|---:|---:|---:|
| DNp15 / GC6f / dendrite / WT | 5 | 0.907 | 0.648 | 0.686 |
| DNp15 / GC7f / dendrite / native | 1 | 0.870 | 0.703 | 0.630 |
| H2 / sytGC7f / axon / native | 2 | 0.993 | 0.605 | 0.659 |
| HS / GC7f / axon / native | 3 | 0.977 | 0.247 | 0.314 |
| HS / sytGC7f / axon / native | 3 | 0.816 | 0.454 | 0.545 |
| bIPS / GC6f / axon / WT | 9 | 0.850 | 0.480 | 0.573 |
| bIPS / GC7f / axon / native | 1 | 0.801 | 0.655 | 0.594 |
| bIPS / sytGC7f / axon / native | 4 | 0.309 | 0.381 | 0.525 |

Both corrected proxies reduce this original-circuit error in seven of eight cohorts. The bIPS/sytGC7f cohort becomes worse than its legacy comparison under both proxies. This mixed result is preserved. The geometry correction is justified by coordinate consistency independently of these errors.

Anatomical additions still do not give a consistent advantage: effects vary by cohort, proxy and whether the original observation model is transferred or the expanded model receives its own calibration. Large apparent improvements in native DNp15 and bIPS/GC7f each involve only one test fly. All modes and both circuits are available in the [complete comparison](../results/validation_hardware_v1/physiology_review_v2/thirteen_proxy_comparison.csv).

## New six-second speed condition

Audited 45 sessions from 34 flies: 20 calibration-partition flies and 14 test-partition flies. All were already present in the 13-second recording dataset, but these six-second responses had not been used to choose the observation parameters. Extracted all 360 traces with no rejected trace. The independent review retained a ledger of 86 unusable trial/ROI units; each accepted trace still meets the declared minimum valid-trial rule.

The unchanged 13-second observation fits predict 225 traces at nominal yaw speeds 5.625, 11.25, 22.5, 45 and 90 degrees/s. The other 135 traces at 180, 360 and 720 degrees/s remain measured but unmodeled because linear proxy scaling would exceed its inherited drive range. No clipping or gain retuning was used. The world-sign convention of the recorded CW/CCW flag remains unresolved, so both global sign hypotheses were retained, producing 3,600 score rows. Neither sign is selected from its error.

The table shows equal-fly RMSE in measured baseline-SD units for the original circuit with its own previously fitted observation model. Each sign column is a separate global hypothesis. The zero-response comparator uses the same recorded samples. These are six-second condition errors, not yaw-detection thresholds or false-positive rates.

| Test cohort | Flies | Zero response | Signed CW+ | Signed CW− | Rectified CW+ | Rectified CW− |
|---|---:|---:|---:|---:|---:|---:|
| DNp15 / GC6f / dendrite / WT | 2 | 2.165 | 1.874 | 2.165 | 1.435 | 2.100 |
| DNp15 / GC7f / dendrite / native | 1 | 9.616 | 7.639 | 9.616 | 7.486 | 9.487 |
| H2 / sytGC7f / axon / native | 1 | 8.026 | 6.398 | 8.026 | 6.561 | 7.631 |
| HS / sytGC7f / axon / native | 1 | 7.579 | 6.009 | 7.579 | 5.151 | 6.358 |
| bIPS / GC6f / axon / WT | 6 | 14.951 | 11.418 | 14.951 | 10.768 | 12.755 |
| bIPS / sytGC7f / axon / native | 3 | 5.094 | 5.649 | 5.094 | 3.210 | 3.605 |

HS/GC7f and bIPS/GC7f have no test-partition flies in this new condition. Several other test cohorts contain one fly. All calibration-partition condition errors are reported separately in the CSV, without treating those animals as a new test sample.

The speed curves expose failures obscured by one aggregate error: for example, the signed original-circuit DNp15/WT proxy exceeds the zero-response error at 90 degrees/s, and HS/sytGC7f also shows a high-speed mismatch under both corrected proxies. The expanded circuit does not resolve these failures consistently. Both global sign hypotheses and all supported speeds remain in the figures, including worse cases. A lower overall error than zero response is insufficient to validate speed tuning, direction selectivity or the entire visual circuit.

[All cohort/sign/circuit/mode errors and descriptive fly-bootstrap intervals](../results/validation_hardware_v1/physiology_review_v2/speed_cohort_overall_summary.csv), [per-speed comparisons](../results/validation_hardware_v1/physiology_review_v2/speed_cohort_velocity_summary.csv). The 10,000-resample percentile intervals were added after scoring for descriptive uncertainty, with seed 20261021; they do not replace prospective criteria. Single-fly intervals are unavailable and cross-animal population claims remain unsupported.

## Numerical review and evidence

An independent implementation recomputed all 360 raw recording traces using explicit trial/ROI indexing, checked all 32 selected calibration gains/losses and candidate minima, reconstructed all 760 corrected 13-second prediction/metric cases and all 3,600 six-second cases, and checked the existing fly-level aggregation. It imported none of the production normalization, filtering or scoring functions. Maximum observed numerical discrepancy was 2.85e-14, within the declared 1e-10 arithmetic tolerance. Four prospective manifests, covering 324 entries in total, still matched their hashes. This is numerical/data-handling reproducibility; it is not an independent reimplementation of the neural solver or biological validation.

[Independent review](../results/validation_hardware_v1/physiology_review_v2/independent_review.json), [unusable trial/ROI ledger](../results/validation_hardware_v1/physiology_review_v2/unusable_trial_roi_units.json), [review source](../scripts/review_corrected_physiology_v2.py).

Figures (PNG and PDF): [13-second proxy comparison](../results/validation_hardware_v1/physiology_review_v2/figures/thirteen_proxy_comparison.png), [signed speed condition](../results/validation_hardware_v1/physiology_review_v2/figures/speed_condition_coordinate_signed.png), [rectified speed condition](../results/validation_hardware_v1/physiology_review_v2/figures/speed_condition_coordinate_rectified.png). All three PNG figures were visually reviewed for labels, cohort coverage, preserved sign hypotheses and visible negative findings.

## Remaining gates

The simplified clamps do not reproduce image contrast, dot geometry, spatial/temporal frequency responses, adaptation or physiological T4/T5 amplitudes. Exact display frames/refresh and the world direction flag still need source evidence. A calibrated fluorescence filter does not identify a neuron's membrane voltage or prove that one population average explains an imaged neurite. These recordings concern immobilized visual stimulation, not matched forward walking. Missing electrical coupling and unresolved anatomical identities remain separate limitations. No new connection or conductance was invented.

The next physiological step is a source-supported image-to-recording comparison with matched stimuli and an explicit measurement model. If the required display and recording information is unavailable, preserve that limitation rather than adjusting signs or neural gains to improve the existing test scores. New independent animals are required before interpreting further model changes as fresh validation. Walking generalization/convergence and hardware timing have separate running analyses; these diagnostics do not decide their outcomes. Robot motor control remains deferred.

## Undergraduate explanation

We want to know whether the model processes visual motion in a way that resembles the fly, and eventually whether it can help a robot recognize unintended turns. We found that an old shortcut for supplying visual motion used inconsistent eye coordinates, corrected it using geometry, and compared both predetermined versions with real recordings. Many recording comparisons improved, but some became worse and several speed responses remain inaccurate. We also tested a new stimulus condition without refitting its response parameters. These checks help distinguish a software error from a missing biological mechanism; they do not yet show that the model is a validated fly brain or a working robot controller.
