# Yaw false-alarm localization report V1

2026-10-30. **A supported model cause is sensitivity to scene-induced binocular motion imbalance. The detector is not repaired or newly validated.** This retrospective study preserves the [completed final test](FINAL_OPENLOOP_MILESTONE_REPORT_V1.md) and follows the [bounded protocol](YAW_FAILURE_AND_HS_BENCHMARK_PROTOCOL_V1.md).

## What we wanted and what changed

We wanted to explain why the model correctly detects small turns yet alarms during fast straight walking. We analyzed all 180 saved straight episodes, exactly replayed 18 representative source/circuit cases, and executed 12 bounded visual-input interventions. No graph, neuron parameter, fitted decoder, threshold or acceptance rule changed. This output is diagnosis using inspected rooms, not new held-out validation.

The fixed readout measures a recent change in each DNp15 side and combines them linearly. Its score can be written exactly as an intercept plus a common component and a left–right differential component. Removing only the common component leaves 36/60 high-speed false-alarm episodes; keeping only the common component produces none. At first alarms, the high-speed median absolute common contribution is 0.0112 versus 0.9398 for the differential contribution, plus the fixed -0.1090 intercept. These are external decoder units, not measured yaw velocity or membrane voltage. Algebraic removal is an attribution diagnostic, not a trained replacement detector.

In the representative replays, unequal T4/T5 drive projected through the recorded weights is visible before HS activity and HS chemical contributions to DNp15. Source/current correlations support the pathway trace; they alone are not causality. Independent matrix reconstruction matches every saved HS-to-DNp15 chemical contribution within 2.17e-19. The HS-labeled group here includes HST, as in the parent graph. It differs from the classical HSN/HSE/HSS trio used in the physiological benchmark. All currents retain arbitrary model units. The saved image-based geometric estimator is over its own threshold at only 2 of the 36 high-speed first neural alarms; physical yaw remains zero.

![Representative input-to-readout traces](../results/yaw_false_alarm_localization_v1/figures/representative_pathways.png)

## Why faster walking is harder in this test

Higher speed changes the temporal input and also covers more distance during the same two-second control window. Twenty-five of 36 high-speed first alarms occur beyond the farthest distance the slowest trials reach. However, restricting the saved traces to the shared 8.25–13.75 mm path interval still gives 11/60 high-speed alarms and zero at the lower speeds. The duration differs between speeds in this diagnostic, so it cannot replace the frozen reliability criterion or serve as an equally exposed population comparison. Both speed-dependent processing and path exposure matter; exposure alone does not explain the failure.

| Speed mm/s | Any alarm /60 over two seconds | Alarm /60 within common distance | Common-distance duration s | First alarms beyond that distance |
|---|---|---|---|---|
| 5.5 | 0 | 0 | 1.0 | 0 |
| 11.0 | 6 | 0 | 0.5 | 6 |
| 16.5 | 36 | 11 | 0.34 | 25 |


The six 11-mm/s failures all first alarm after 1.2 s; at 16.5 mm/s, ten rooms alarm in [1,1.2) and 31 in [1.2,3), with overlap. Median first-alarm time at the highest speed is 1.76 s and median total alarm duration is 0.125 s. The detector was fitted on one onset-relative endpoint, while straight-control alarms are scored across a longer interval and a changing scene. That is a generalization limitation, not a reason to remove later failures.

![All rooms and speeds](../results/yaw_false_alarm_localization_v1/figures/all_straight_scores_r2.png)

## Controlled visual interventions

The first three failing high-speed rooms in lexical order (z24, z25, z27) were selected before new interventions. Mirroring geometry/textures reverses much of the score waveform (correlations -0.767, -0.595, -0.948), but all three still alarm. The inherited symmetric-world control removes all three alarms. Its construction also changes local contrast and adds reflected geometry, so that result alone does not isolate symmetry.

To address that confound, a final predeclared control presents either the original left eye-chart movie to both eyes or the original right movie to both eyes. This preserves the chosen movie without averaging or rescaling contrast. All six such clamps remove alarms; the chosen eye's original source-cell drives remain bitwise unchanged. Retinal sampling and anatomical/readout asymmetries remain. This supports a contribution from binocular scene-input imbalance in these selected failures. The controls do not prove that every high-speed failure has one unique cause, nor identify missing electrical coupling as the cause.

| Room | Original peak | Mirrored peak | Symmetric-world peak | Both get L peak | Both get R peak |
|---|---|---|---|---|---|
| z24 | 1.5058 | 1.0093 | 0.3500 | 0.7282 | 0.5431 |
| z25 | 1.0804 | 1.7260 | 0.4845 | 0.6737 | 0.9135 |
| z27 | 1.4238 | 1.3136 | 0.3861 | 0.7489 | 0.4125 |


![Unchanged model under all visual controls](../results/yaw_false_alarm_localization_v1/figures/all_counterfactuals_r2.png)

The duplicated movies are artificial retinal clamps, not physically faithful new walking environments or a deployable remedy. They can remove genuine binocular information needed to detect rotation. No turn-detection success is claimed for them. Making a test scene symmetric is likewise not a solution for general navigation.

## Numerical audit, failures and limits

All 18 original image/source hashes and LPi rates reproduce exactly. Independent FIR convolution reconstructs all straight-episode decisions; source/current and mirror/symmetric renderer checks pass. The last six clamps have an additional source/decision audit. A post-outcome check of all full [1,3) windows in the nine already saved known-room straight numerical cases gives:

| Refinement | Known straight cases | Any-alarm episode changes | Sample decision changes | Max score difference |
|---|---|---|---|---|
| spatial | 9 | 0 | 0 | 0.209421 |
| temporal | 9 | 0 | 0 | 0.0405848 |
| solver | 9 | 0 | 0 | 3.0674e-09 |


These are existing known numerical rooms, not the three selected final failures. They do not override the original failed overall numerical gate or establish full physiological accuracy. See [base independent review](../results/yaw_false_alarm_localization_v1/independent_review.json), [additional review](../results/yaw_false_alarm_localization_v1/additional_review.json), [clamp review](../results/yaw_false_alarm_localization_v1/retinal_clamp/independent_review.json), [all diagnostics](../results/yaw_false_alarm_localization_v1/straight_episode_diagnostics.csv) and [source traces](../results/yaw_false_alarm_localization_v1/source_circuit_trace.csv).

The initial audit failed on a metadata label lookup; its original source and failure are retained and the corrected lookup reads labels from the full graph. No simulation or numerical response changed. Initial draft figures had an overlapping colorbar and limits set by samples outside the plotted window; readable R2 figures preserve the same values alongside those drafts. No exclusion, fit, gain search or unreported neural failure occurred.

## Plain-language conclusion and next decision

The model notices a change between its two sides, but an uneven scene can create that change even while walking straight. Faster walking makes this harder and exposes more of the scene. We traced this through the input, HS and DNp15 and checked it with controlled visual changes. We now have a supported explanation within the model, not just another failed benchmark. The reliable-detector goal remains open.

Recommended next engineering hypothesis: test a separately versioned readout or binocular computation designed to reject translation-induced scene imbalance, using distance-matched exposure and new asymmetric rooms. It must retain small-turn detection; deleting binocular information or increasing a threshold until alarms disappear is insufficient. Biological alternative: replay these same asymmetric and mirrored stimuli during bilateral HS/DNp15 recordings to test whether the predicted scene sensitivity occurs in real neurons. Missing coupling and the functional frontend remain hypotheses requiring evidence. No further intervention or tuning occurs in this study. [Physiological comparison](HS_VOLTAGE_BENCHMARK_REPORT_V1.md); [reproduction](YAW_HS_FOLLOWUP_REPRODUCIBILITY_V1.md).
