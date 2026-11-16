# Independent environments and numerical convergence — V1

Completed numerical component: 2026-10-21, America/Belem. The broader validation and hardware goal remains incomplete. This report extends the sealed Studies A/B; it does not replace their evidence or change their criteria.

**Result:** the original circuit's DNp15 readout does not meet the frozen false-alarm requirement in the larger environment test. Its previous 20°/s fast-walking threshold also fails to survive finer panorama sampling. The expanded circuit has one qualifying 20°/s result at fast walking in the new rooms, but no consistent improvement across speeds or decoder conditions. These are reproducible computational findings, not physiological validation or a validated steering controller.

## Frozen experiment

The study completed **3,536 visual inputs through four circuit copies**, producing 14,144 graph trajectories. New generalization uses 56 independently generated rooms: eight training, eight calibration and 40 held out. A separate convergence sweep uses all 12 historical rooms, retaining their three training, three calibration and six held-out assignments. Each room has a stationary control and 33 walking conditions: three forward speeds (5.5, 11, 16.5 mm/s) crossed with yaw 0, ±2, ±5, ±10, ±20 and ±40°/s. Motion lasts 0.5–1.5 s within each two-second episode. New rooms vary seeds, geometry and obstacles under the frozen generator; this tests that declared distribution, not every natural environment.

The four copies are original intact, original with bilateral bIPS output silenced, expanded intact, and expanded with both added candidate families' outputs silenced. Every copy receives exactly the same source-drive array within a condition. The original graph contains 13,593 cells and 203,861 chemical edges; the expanded graph contains 13,618 cells and 204,201 chemical edges. The expanded model's 17 uLPTCrn and eight H2rn candidates retain the anatomical identification qualifications from Study B. No electrical conductance is added. Silencing added cells retains the expanded weight matrix and its normalization; it does not reconstruct the original graph. The original frontend, gains and neural equations remain frozen. Selective outgoing-edge and HS/H2 lesions remain available in Study A; this extension runs the four specified copies, not the entire previous lesion panel.

| Profile | Panorama pixel pitch | Frontend step | Neural input step | Solver step |
|---|---:|---:|---:|---:|
| Legacy | 1° | 5 ms | 10 ms | 1 ms |
| Spatial half | 0.5° | 5 ms | 10 ms | 1 ms |
| Spatial quarter | 0.25° | 5 ms | 10 ms | 1 ms |
| Quarter, fine time | 0.25° | 2.5 ms | 5 ms | 0.5 ms |

All four profiles cover the historical rooms; new rooms use the legacy profile. The retinal circuit grid remains 1°, with unchanged neighbor displacement and pooling. All neural trajectories are recorded every 10 ms. The executed historical response window contains 70 samples, 0.70–1.39 s; the floating-point 1.40-s endpoint is excluded in every profile. This convention is preserved rather than silently corrected.

Primary readouts transfer the sealed original intact decoder unchanged to every copy. Secondary decoders are fitted separately by copy, profile, role and known speed using training rooms only; maximum absolute straight-walking scores from calibration rooms set cutoffs. No held-out room enters either operation. No neural parameter is fitted. A threshold needs ≥80% detection, ≥80% raw yaw-sign accuracy and ≤10% straight false alarms, sustained at every larger tested magnitude. Raw sign accuracy includes nondetections; correctly directed detection is separately saved. An unresolved threshold is not a lower bound on a fly's sensitivity. [Protocol](VALIDATION_HARDWARE_PROTOCOL_V1.md), [frozen configuration](../configs/validation_hardware_v1.json), [prospective manifest](../results/validation_hardware_v1/prospective_manifest.json).

## Generalization and thresholds

For original intact DNp15, the unchanged decoder gives:

| Forward speed | Straight false alarms | Detection at ±2°/s | Raw sign accuracy at ±2°/s | Qualifying threshold |
|---|---:|---:|---:|---|
| 5.5 mm/s | 6/40 (15%) | 46/80 (57.5%) | 72/80 (90%) | Unresolved |
| 11 mm/s | 8/40 (20%) | 26/80 (32.5%) | 60/80 (75%) | Unresolved |
| 16.5 mm/s | 6/40 (15%) | 14/80 (17.5%) | 52/80 (65%) | Unresolved |

Detection at ±5°/s is 97.5%, 67.5% and 36.25%, respectively. At ±20°/s it is 100%, 100% and 98.75%, but the straight-control failure still prevents qualifying original DNp15 thresholds. The 95% Wilson interval for 6/40 false positives is 7.1–29.1%; for 8/40 it is 10.5–34.8%. These intervals describe finite sampled rooms, not repeated noisy neural trials or biological animals.

Expanded intact DNp15 transfers to a 20°/s threshold at 16.5 mm/s with 4/40 false positives, exactly the 10% observed-rate limit. Its false-positive interval is 4.0–23.1%, so that finite-grid result does not guarantee a ≤10% population false-positive rate. Its ±2°/s detection at that speed is only 11.25%. Slower-speed thresholds remain unresolved. After development-only decoder retraining, original intact DNp15 has 40% false positives at every speed; expanded intact has 37.5%, 37.5% and 40%. Retraining under the frozen procedure therefore does not solve generalization.

Original HS and bIPS have unresolved primary thresholds at all speeds. H2 qualifies at 20°/s at 5.5 mm/s with 4/40 false positives, and fails false-positive control at the two faster speeds. Expanded H2 has the same qualifying slow-speed result. Expanded bIPS at fast walking has only 1/40 false positives, but fails the complete detection criterion through the tested magnitudes. This preserves the distinction between low false alarms and useful rotation detection. All 480 threshold rows, 2,400 curve rows and 67,584 predictions remain available. [Thresholds](../results/validation_hardware_v1/detection_thresholds.csv), [curves and intervals](../results/validation_hardware_v1/detection_curves.csv), [every prediction](../results/validation_hardware_v1/decoder_predictions.csv).

![All four neuron groups](../results/validation_hardware_v1/scientific_report_v1_r3/figures/generalization_intact_all_classes.png)

## bIPS and added-family effects

At 16.5 mm/s, bIPS silencing raises unchanged DNp15-readout false positives from 6/40 to 14/40; lesion-specific retraining yields 16/40. At 5.5 mm/s the fixed-readout count stays 6/40; at 11 mm/s it changes from 8/40 to 6/40. The data do not support a uniform improvement from bIPS at every speed, or a robust threshold recovered by retraining in the new rooms.

Silencing added families in the expanded model changes fast-walking fixed-readout false positives from 4/40 to 5/40, losing that qualifying threshold. Retraining gives 16/40, as for the original circuit. This one-room cutoff difference is insufficient to establish a generally superior reconstructed circuit.

A **post-score descriptive** paired response analysis separates decoder behavior from neural asymmetry. Define bilateral asymmetry A = left DNp15 − right DNp15, and the odd yaw response as [A(+yaw) − A(−yaw)]/2. Across the same 40 held-out rooms at fast walking, the ratio of median absolute odd responses, bIPS-silenced/intact, is 0.8566 at ±2°/s and 0.8576 at ±20°/s. bIPS output therefore contributes to response gain in this model, while substantial yaw-dependent asymmetry remains after its removal. The mean straight asymmetry also shifts by +3.84×10⁻⁵ model units. That baseline shift can affect a previously calibrated decoder.

For added-family silence within the expanded graph, the corresponding ratios are 1.0295 and 1.0646: silencing slightly increases odd response magnitude while worsening the fast fixed-readout false-positive count. Response amplitude alone is not evidence of improved detection. These paired diagnostics and their scene bootstrap intervals were added after scoring and do not redefine the frozen acceptance rule. They demonstrate effects within these equations, not biological causality or indispensable biological information. [All paired room values](../results/validation_hardware_v1/scientific_report_v1_r3/postscore_dnp15_scene_pairs.csv), [post-score summaries and intervals](../results/validation_hardware_v1/scientific_report_v1_r3/postscore_dnp15_mechanism_summary.csv).

![Ablation and retraining](../results/validation_hardware_v1/scientific_report_v1_r3/figures/dnp15_ablation_and_retraining.png)

![Paired neural responses](../results/validation_hardware_v1/scientific_report_v1_r3/figures/paired_dnp15_asymmetry.png)

## Numerical convergence and independent checks

At 16.5 mm/s in the six historical held-out rooms, original intact DNp15 has the previous 20°/s legacy threshold with 0/6 straight false alarms. Finer spatial profiles give 2/6 false alarms at 0.5° and 3/6 at 0.25°; the fine-time profile gives 2/6. All three refined thresholds are unresolved. Development-only refitting also leaves every refined DNp15 threshold unresolved. Thus the legacy threshold is not established as a resolution-independent circuit prediction.

The frozen all-cell comparisons against legacy flag **3,998/4,896 mean summaries** and **4,270/4,896 yaw-minus-straight contrast summaries** above 10%, using the declared 10⁻⁵ mean and 10⁻⁷ contrast floors. There are **701 changed decisions among 19,008 comparisons**, across both decoder modes, all roles and four copies. Secondary decision changes include both changed inputs and profile-specific refitting; they cannot isolate rendering effects alone. All flags and failures remain saved. [Numerical table](../results/validation_hardware_v1/numerical_refinement.csv), [decision comparisons](../results/validation_hardware_v1/refinement_decisions.csv).

![Full convergence sweep](../results/validation_hardware_v1/scientific_report_v1_r3/figures/dnp15_full_profile_convergence.png)

Post-score adjacent-profile diagnostics show smaller changes at finer spatial sampling: original intact has 308/408 all-cell mean flags from 1° to 0.5°, and 18/408 from 0.5° to 0.25°. Quarter sampling to the fine-time profile has zero mean flags but 15/408 all-cell contrast flags. For the DNp15 pair alone, the final comparison has zero mean and contrast flags. These descriptive improvements do not rescue the failed thresholds, establish full-network convergence, or separate frontend, neural-input and solver clocks, which were refined jointly in that final profile. [All adjacent comparisons](../results/validation_hardware_v1/scientific_report_v1_r3/postscore_adjacent_profile_comparisons.csv).

![Adjacent comparisons](../results/validation_hardware_v1/scientific_report_v1_r3/figures/adjacent_profile_diagnostic.png)

The independent arithmetic review checked all 3,536 receipt-matched outputs, all training/calibration/test memberships, 240 decoder fits using augmented least squares rather than normal equations, every score and decision, all thresholds, scene-paired bootstrap intervals using multinomial weights, Wilson intervals by score-test inversion, and every refinement summary. Maximum response discrepancy is 3.04×10⁻¹⁸; coefficient discrepancy 1.30×10⁻¹³; score discrepancy 1.43×10⁻¹⁴. It reverified all 2,950 predecessor index entries. The 2,112 scores within the declared 10⁻¹⁰ cutoff-review band are exclusively the silenced bIPS population's retrained zero-score/zero-cutoff cases, not nonzero held-out DNp15 cutoff ties. Scientific decisions remain unchanged. [Independent review](../results/validation_hardware_v1/analysis_review_v1_r2/independent_review.json), [129,744 cell diagnostics](../results/validation_hardware_v1/analysis_review_v1_r2/cell_refinement_diagnostics.csv.gz).

Separately, eight complete inputs (two fixed scene/condition pairs across all profiles) were regenerated with identical saved drive/time digests. Thirty-two original Python-equation neural replays, including all four intervention copies, match rates within 8.68×10⁻¹⁹ and full final states within 1.09×10⁻¹⁹. Independent vectorized raycasting and explicit four-corner interpolation exactly match 23,120 retained retinal pixels at 80 eye/time checkpoints. Small-yaw landmark reprojection across both eyes and three walking speeds agrees with analytical angular flow within 5.48×10⁻⁷ rad/s. This extends selected implementation checks, not all-trial independent solver replay. [Checks](../results/validation_hardware_v1/geometry_replay_review_v1/checks_complete.json), [case ledger](../results/validation_hardware_v1/geometry_replay_review_v1/before_execution.json).

Over those selected checkpoints, mean per-checkpoint retinal RMS discrepancy from direct receptor rays falls from 0.01681 luminance units at 1° to 0.00817 at 0.5° and 0.00284 at 0.25°. This supports a sampling-sensitivity diagnosis. Direct rays and finer panoramas do not establish a real fly's optical aperture, and these checks do not isolate aliasing as the sole cause of the neural changes. [Sampling evidence](../results/validation_hardware_v1/geometry_replay_review_v1/retinal_sampling.csv).

## Biological comparison, limitations and predictions

The experimental work motivating this project identifies recurrent inhibition and lateral disinhibition as contributors to extracting rotational motion during translation. Our paired lesions show gain and baseline effects in the available chemical graph, but its broader false-alarm and convergence failures prevent claiming reproduction of robust biological rotation detection. [Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9).

Electrical interactions remain an explicit missing biological constraint: experiments implicate bilateral HS–H2 electrical coupling in course control. Adding unmeasured conductances to obtain favorable classifications would not resolve that gap. Nonvisual walking-related inputs to HS are also absent from this visual-only model. [Pokusaeva et al. (2024)](https://www.nature.com/articles/s41467-024-53173-w), [Fujiwara et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/27798632/). The functional T4/T5 surrogate is still imposed direction-channel routing, and anatomical registration, physiological time constants, synaptic dynamics and calibrated observation models remain incomplete. The separately reported calcium diagnostics bypass images and reuse test flies; they do not validate this complete image-to-neuron system. [Physiological diagnostic report](CORRECTED_PHYSIOLOGICAL_DIAGNOSTICS_REPORT_V2.md), [anatomical evidence and gaps](ANATOMICAL_STRENGTHENING_REPORT_V1.md).

Testable model predictions include the full speed-dependent bilateral response curves, the roughly 14% reduction in fast-walking odd DNp15 asymmetry after bilateral bIPS-output suppression, and accompanying straight-response shifts. Matched visual stimuli and independent experimental measurements are needed to test their signs and magnitudes. Numerical lesion effects are not proof of biological causality. The current data do not justify a reliable 2–5°/s biological threshold, a consistent benefit from the added candidate families, or closed-loop motor control.

## Reproduction, failures and hardware boundary

The original protocol and source manifest remain unchanged. Storage continued after an explicitly preserved interruption using lossless ZIP_LZMA; the original 639 files were retained and every completed output now verifies. Analysis initially failed before scoring because `scripts` was absent from `PYTHONPATH`; the unchanged analysis completed with `PYTHONPATH=src:scripts`. The first independent review had a root-bracketing bug for zero false positives; its source/log/failure remain preserved, and the corrected review passed without changing intervals or scientific tolerances. The first plotting run rejected tiny roundoff differences at Wilson endpoints. The next version draws saved interval endpoints directly; a later presentation revision moves legends away from data. Earlier outputs remain intact. [Storage amendment](VALIDATION_HARDWARE_STORAGE_AMENDMENT_V2.md), [failed review](../results/validation_hardware_v1/analysis_review_v1), [initial plotting failure](../results/validation_hardware_v1/scientific_reporting_execution_v1.log), [reproduction commands](VALIDATION_GENERALIZATION_CONVERGENCE_REPRODUCTION_V1.md).

The user selected portable Linux CPU first. The existing CPU runtime preserves the 1-ms solver; GPU remains optional. CPU timing tests have missed the 10-ms budget, and even the separately reported GPU stress test missed 1,096/60,000 deadlines. Raw-camera package completion, target-specific latency and physical deployment are separate unfinished engineering work. No camera calibration, robot performance, hard-real-time guarantee or physiological validation follows from this numerical component. [CPU/GPU timing report](CUDA_DEPLOYMENT_PROGRESS_REPORT_V1.md), [sustained replay](SUSTAINED_CUDA_REPLAY_REPORT_V1.md), [camera contract](CAMERA_INPUT_CONTRACT_V1.md).

## Undergraduate explanation: what we did, what we want and why

We want to understand how a fly notices an unwanted turn while walking forward, then turn that understanding into a useful vision system for real hardware. We showed the same simulated walking scenes to the original neural model and to copies with selected neurons silenced, tested unfamiliar rooms, and repeated the calculations with finer image sampling. The software calculations are reproducible, and bIPS changes the strength and balance of the output responses. However, the model still mistakes some straight walking for turning, and its earlier detection threshold changes when image sampling becomes finer. That tells us which predictions remain uncertain and what needs improvement before trusting a robot to steer from them. The next engineering target is a portable Linux CPU perception package; biological validation and eventual motor control still require further evidence.
