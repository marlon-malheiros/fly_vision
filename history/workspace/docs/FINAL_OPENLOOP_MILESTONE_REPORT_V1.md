# Final open-loop milestone report V1

2026-10-30. Study started 2026-10-29. **Research package complete; neural capability failed; physiological validation not established.** This release closes the predeclared computation and its bounded source audit. It does not reinterpret a failed detector as success.

## Question and frozen study

Can a frozen LPi-strengthened MaleCNS chemical circuit, read through bilateral DNp15 activity, detect ±2 and ±5 deg/s yaw onset during forward walking at 5.5, 11 and 16.5 mm/s without excessive straight-walking alarms? Does bIPS improve this computation? The [plan](FINAL_OPENLOOP_MILESTONE_PLAN_V1.md), [execution protocol](FINAL_OPENLOOP_EXECUTION_PROTOCOL_V1.md), [wording correction](FINAL_OPENLOOP_EXECUTION_CORRECTION_R3.md), and machine-readable freezes distinguish prospective rules from inspected results. Neural parameters, original frontend and all parent results remain preserved. The R2 review added full-state retention and false-alarm intervals before fresh scientific inputs; R3 corrects grid-step units only.

The study executed **2,424 new binocular-image episodes**: 192 training, 192 calibration/audit and 2,040 untouched final tests in 84 seed-disjoint generated rooms. Twelve training rooms fitted fixed-recipe external linear decoders; twelve calibration rooms performed no selection or refitting. Sixty final rooms crossed three speeds with 0, ±2, ±5, ±10, ±20 and ±40 deg/s, plus stationary controls. Final images were first generated after coefficients froze. Room instances generalize within one prescribed textured box/sphere family; they do not establish natural-scene generality. Repeated signs, speeds and model copies share rooms and are not independent animals. Trajectories are constant-height body-forward kinematics, without a gait or head-motion model. No intrinsic neuronal, photon or camera noise was added; the reported variation is across rooms, not trial reliability in live flies. The zero stationary equilibrium is a synthetic implementation control.

Each image episode drove ten separately identified copies: original, expanded before LPi, LPi intact, LPi-silent normalization control, bIPS silent, all bIPS outputs cut, bIPS-to-DNp15 cut, HS silent, H2 silent and sham. All source-cell recurrent dynamics were preserved. Masks remove only recorded chemical edges and do not renormalize the graph. Silencing follows the inherited zero-output/drive mask rather than clamping hidden states. No electrical conductance was invented.

The primary readout is external: each side's 100-ms mean minus its own mean 200 ms earlier, followed by one training-only standardized ridge fit pooled across speeds. It receives no true speed, yaw, onset, depth, scene or counterfactual control. The fixed decision boundary is |score|>1 decoder-equivalent deg/s; these units are not calibrated physiological yaw velocity. The primary endpoint is 1.19 s, 190 ms after the imposed turn. Earlier transient correct decisions cannot rescue an incorrect endpoint. The prospective gate requires ≥96/120 joint successes, ≥48/60 each sign, ≥80% detection and raw direction, ≤6/60 endpoint and two-second any-alarm straight episodes at every primary speed/magnitude, and ≤6/60 stationary alarms. Observed counts are benchmark criteria, not population reliability guarantees.

## Primary outcome

The direct answer is **the empirical small-turn target was not met**. Count-level explanation: two-second straight alarms: 2/6 primary conditions above the required count boundary.

| Speed mm/s | Yaw magnitude deg/s | Joint /120 | Negative /60 | Positive /60 | Straight endpoint /60 | Straight any alarm /60 | Criterion |
|---|---|---|---|---|---|---|---|
| 5.5 | 2 | 120 | 60 | 60 | 0 | 0 | pass |
| 5.5 | 5 | 120 | 60 | 60 | 0 | 0 | pass |
| 11 | 2 | 116 | 59 | 57 | 0 | 6 | pass |
| 11 | 5 | 120 | 60 | 60 | 0 | 6 | pass |
| 16.5 | 2 | 108 | 55 | 53 | 2 | 36 | fail |
| 16.5 | 5 | 120 | 60 | 60 | 2 | 36 | fail |


The raw empirical detector verdict is **fail**. The numerical gate is **fail**. Combined neural capability is **FAILED**. Counts include both signs and every required speed; no favorable pooled average replaces a failed condition. Complete HS/H2/bIPS/DNp15 outputs, readiness, latencies, direction counts and 2–40 deg/s curves are in [test predictions](../results/final_openloop_milestone_v1/analysis/test_predictions.csv), [all curves](../results/final_openloop_milestone_v1/analysis/curves.csv) and [grid thresholds](../results/final_openloop_milestone_v1/analysis/grid_thresholds.json). A threshold is a smallest qualifying tested magnitude only when all larger grid points also qualify; no continuous or below-2-deg/s biological threshold is inferred.

![Detection curves](../results/final_openloop_milestone_v1/figures/detection_curves.png)

| Readout | Speed | Joint /120 at 2 deg/s | Any straight alarm /60 | Full gate |
|---|---|---|---|---|
| LPi_bIPS_silent/dnp15/fixed | 5.5 | 120 | 0 | True |
| LPi_bIPS_silent/dnp15/fixed | 11.0 | 116 | 1 | True |
| LPi_bIPS_silent/dnp15/fixed | 16.5 | 105 | 28 | False |
| LPi_bIPS_silent/dnp15/own | 5.5 | 120 | 0 | True |
| LPi_bIPS_silent/dnp15/own | 11.0 | 117 | 5 | True |
| LPi_bIPS_silent/dnp15/own | 16.5 | 109 | 33 | False |
| LPi_intact/dnp15/own | 5.5 | 120 | 0 | True |
| LPi_intact/dnp15/own | 11.0 | 116 | 6 | True |
| LPi_intact/dnp15/own | 16.5 | 108 | 36 | False |
| LPi_silent_same_normalization/dnp15/fixed | 5.5 | 120 | 0 | True |
| LPi_silent_same_normalization/dnp15/fixed | 11.0 | 116 | 1 | True |
| LPi_silent_same_normalization/dnp15/fixed | 16.5 | 109 | 28 | False |
| expanded_pre_LPi/dnp15/own | 5.5 | 120 | 0 | True |
| expanded_pre_LPi/dnp15/own | 11.0 | 116 | 10 | False |
| expanded_pre_LPi/dnp15/own | 16.5 | 106 | 42 | False |
| image_reference | 5.5 | 120 | 0 | True |
| image_reference | 11.0 | 119 | 4 | True |
| image_reference | 16.5 | 117 | 11 | False |
| legacy_known_speed_hybrid | 5.5 | 120 | 0 | False |
| legacy_known_speed_hybrid | 11.0 | 119 | 1 | False |
| legacy_known_speed_hybrid | 16.5 | 104 | 6 | False |
| original_frozen/dnp15/own | 5.5 | 120 | 0 | True |
| original_frozen/dnp15/own | 11.0 | 116 | 15 | False |
| original_frozen/dnp15/own | 16.5 | 104 | 45 | False |


The image reference is an engineering optic-flow estimate. The unchanged legacy hybrid additionally receives the known constant walking-speed condition and has no speed-zero calibration. Its walking-only criterion is reported separately; it cannot receive an invented stationary pass or count as neural success. All anatomical copies received fair train-only own readouts; primary LPi lesion effects use the unchanged intact decoder, with own refitting explicitly secondary.

![False alarms](../results/final_openloop_milestone_v1/figures/false_alarms.png)

## bIPS and circuit interpretation

With the unchanged intact readout, bIPS silence reduced joint detection with an entirely negative nominal 95% interval in 0/6 primary speed/magnitude conditions, increased it with an entirely positive interval in 0/6, and had an interval including zero in 6/6. These repeated-condition intervals are descriptive and are not adjusted for multiple comparisons. A robust bIPS-dependent small-turn solution was not demonstrated because the intact candidate did not meet the full empirical target.

Changes below are bIPS silence minus intact, using the fixed intact DNp15 readout. Intervals resample rooms jointly over signs and all repeated conditions (2,000 draws).

| Speed | Magnitude | Joint change | 95% room interval | Any-alarm change |
|---|---|---|---|---|
| 5.5 | 2.0 | +0.000 | [+0.000, +0.000] | +0.000 |
| 5.5 | 5.0 | +0.000 | [+0.000, +0.000] | +0.000 |
| 11.0 | 2.0 | +0.000 | [+0.000, +0.000] | -0.083 |
| 11.0 | 5.0 | +0.000 | [+0.000, +0.000] | -0.083 |
| 16.5 | 2.0 | -0.025 | [-0.058, +0.000] | -0.133 |
| 16.5 | 5.0 | +0.000 | [+0.000, +0.000] | -0.133 |


![All prespecified ablations at 2 deg/s](../results/final_openloop_milestone_v1/figures/ablations_2_deg_s.png)

The corresponding [5 deg/s comparison](../results/final_openloop_milestone_v1/figures/ablations_5_deg_s.png) retains every intervention and both readout policies.

These effects establish interventions in the specified equations. Their sign, speed dependence and comparison with retrained readouts determine whether the contribution is conditional, robust or unresolved; no uniform benefit is assumed. The full [ablation effects](../results/final_openloop_milestone_v1/analysis/ablation_effects.csv) separate bIPS silence, all-output cuts, direct DNp15 cuts, HS/H2 controls, LPi silence and sham. Source-family [chemical-current decomposition](../results/final_openloop_milestone_v1/analysis/mean_chemical_currents.csv) retains upstream/recurrent contributions in inherited arbitrary chemical-input units, not measured electrical current. Endpoint correlation and lesions are not proof of biological necessity.

Every episode passed bitwise sham parity and equivalence of bIPS silence versus all-output removal in remaining observable neurons. This controls the implementation and does not prove all proposed biological bIPS mechanisms. The inherited clutter generator places its three spheres on lateral signs +/−/+; 42 new rooms are cluttered and 42 empty, and the set is not mirror balanced. Unequal recurrent-family selection and asymmetric textures/geometry can contribute to raw left–right differences. This metadata-only limitation was recorded during test execution without changing inputs or criteria; it is not a post hoc explanation established from the response outcomes. Paired interventions share the same images, but raw lateral asymmetry alone does not establish biological specialization. The original candidate labels for uLPTCrn and H2rn retain their anatomical uncertainty. Electrical coupling is missing, and the T4/T5 source remains a functional surrogate.

## Numerical audit and retained failures

The known-data pilot exactly reproduced original-kernel rates and final hidden state (zero maximum discrepancy). Independent strict activation/Python sparse RK4 checks are archived. The numerical subset contains 27 known room/speed/yaw combinations, each with primary, half-pitch spatial, half image/input-step temporal and half solver-step profiles. Physical neighbor separation is 1 degree and nominal pooling radius 3 degrees; half-pitch doubles grid steps. Temporal outputs remain 100 Hz, and half-step solver refinement retains the inherited 1-ms forcing ramp.

Across 81 refinement comparisons, 14 failed at least one required gate; maximum external-score change was 0.398631, total decision flips 20, and maximum solver-refinement saved full-state discrepancy 1.20199e-10. These failures remain in [case-level numerical evidence](../results/final_openloop_milestone_v1/analysis/numerical_cases.csv). No parameter was adjusted to remove them. Spatial/temporal sensitivity limits an unqualified capability claim even if endpoint classification counts are favorable.

An independent FIR-convolution audit reconstructed every saved calibration/test score, decision and straight-episode alarm from raw rates/reference signals, and augmented least squares checked every train-only ridge fit. Independent audits verified all curve counts, empirical gate logic, clustered intervals, paired intervention effects and exact ablation ledgers. 1800 turning episodes shared bitwise-identical neural prefixes through yaw onset with their straight controls. All 60 stationary test episodes remained at zero raw neural activity. Four prospectively selected cases regenerated identical retinal, source and complete-state hashes. [Primary audit](../results/final_openloop_milestone_v1/analysis/audit.json); [additional independent audit](../results/final_openloop_milestone_v1/analysis/additional_independent_audit.json). Engineering refinement score differences and decision flips are separately archived in [comparator numerical sensitivity](../results/final_openloop_milestone_v1/analysis/comparator_numerical_sensitivity.csv); they do not introduce a new success criterion. These checks establish bounded numerical reproducibility, not physiological validity.

Storage is documented, not hidden: all observable rates, reference signals, epoch currents, recipes and hashes are retained. Full lossless movies, source drives and states are retained for one known pilot and four final replays; full states are retained for all numerical profiles. Other movies are deterministically regenerable, rather than all being stored. The model/data identity audit verified 47 parent input/report entries against existing immutable indexes. No previous evidence was overwritten.

## Physiological comparison and limits

Earlier inspected Erginkaya calcium comparisons support a chemical-opponency hypothesis but give mixed waveform agreement, including a quiet DNp15 fly that makes mean skill unstable. Keep mean, median and pooled-error conclusions distinct; do not exclude that fly or label reused recordings independent validation. The present walking/yaw test measures a different computational endpoint from the paper's physiological assays. [Erginkaya et al. 2025](https://www.nature.com/articles/s41593-025-01948-9).

The bounded independent-source audit did not yield an executable quantitative physiological benchmark: Suver's DNHS1 population curves report spike rate, and exact stimulus/voltage matching is unresolved; its HS curves report voltage. Pokusaeva publishes relevant HS voltage source data, but the archive/supplement could not be retrieved here and display registration remains unaudited. These are explicit evidence gaps, not absent published data and not biological disagreement. No independent numeric target was extracted or scored. [Source audit](FINAL_OPENLOOP_PHYSIOLOGY_AUDIT_V1.md); [Suver official article](https://authors.library.caltech.edu/records/mqzzc-va989); [Pokusaeva primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11470938/).

Published bilateral electrical-coupling effects make the zero-gap limitation relevant. We have not invented missing conductances, a voltage measurement conversion or a calcium filter to improve final yaw classification. Consequently neither a numerical pass nor a connectomic edge count establishes physiological validation, biological degeneracy or publication acceptance.

## Experimentally testable predictions and next decision

A matched walking assay could present both small yaw signs at the three speeds, record bilateral DNp15 and bIPS, and report missed turns together with spontaneous/straight-walking alarms. The model's signed fixed-readout bIPS effects and their speed dependence are quantitative computational predictions with uncertainty; test them using a manipulation with measured specificity, rather than assuming our mathematical lesion is biologically equivalent. LPi null-direction opponency and the bIPS direct-output versus broader-network effects can be assayed separately. A response-gain match alone will not validate a waveform or computation.

The computational final test is now closed. No additional gains, connection edits, decoder families, thresholds or scene exclusions are permitted inside V1. A future biological stage should retrieve and audit the published HS source archive, freeze a matched preferred/null benchmark, and address missing coupling only when conductances or justified physiological constraints exist. A future engineering stage can assess changing speeds, new scene families and physical cameras with its own criteria. Closed-loop robotics remains a later milestone.

## Reproduction and undergraduate explanation

[Reproduction instructions](FINAL_OPENLOOP_REPRODUCIBILITY_V1.md) include a label-free binocular-image-to-turn CLI and a neural-observation replay. The [reproduction addendum](FINAL_OPENLOOP_REPRODUCTION_ADDENDUM_V1.md) supports an isolated full rerun. The frozen methods commit is 80f3f2a; artifact/source hashes identify later interfaces and audits. The technical evidence and progress snapshot are archived before sealing.

We wanted to know whether this brain model can tell a small turn from ordinary forward movement, and whether bIPS helps. We tested the same pictures on intact and altered model copies in new virtual rooms, counted correct turns and false alarms, and checked whether numerical details changed the answer. The result is a finished fair test, with neural capability **failed** under the stated rules. Real-neuron validation is still missing. This separation matters because a simulator can run correctly and still be an incomplete model of a fly.

Final statuses: **research package complete; neural capability failed; physiological validation not established.**
