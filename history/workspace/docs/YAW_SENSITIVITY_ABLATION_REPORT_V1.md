# Study A — yaw detection and targeted ablations, V1

Completed 2026-10-19 (America/Belem). Frozen-model, open-loop computational study.

**Quantitative outcome.** Intact DNp15: 5.5 mm/s: unresolved deg/s, FPR 17%; 11 mm/s: unresolved deg/s, FPR 33%; 16.5 mm/s: 20 deg/s, FPR 0%. Bilateral bIPS silencing with the unchanged decoder: 5.5 mm/s: unresolved deg/s, FPR 33%; 11 mm/s: unresolved deg/s, FPR 33%; 16.5 mm/s: unresolved deg/s, FPR 67%. After lesion-specific decoder recalibration: 5.5 mm/s: unresolved deg/s, FPR 17%; 11 mm/s: unresolved deg/s, FPR 17%; 16.5 mm/s: 20 deg/s, FPR 0%. At 16.5 mm/s and ±2 deg/s, bIPS silencing leaves 0.854 times the intact absolute bilateral yaw separation. These statements distinguish response gain from false-alarm-controlled detection; numerical timing sensitivity is reported below.

We tested whether weak body yaw remains detectable during forward walking and whether the existing bIPS-associated edges help. The neural frontend, original graph and baseline parameters were preserved. Twelve separately defined graph copies received identical delivered input arrays. No missing electrical or chemical connection was invented.

## Design and evidence

Twelve new independently seeded 3D scenes were split into three training, three calibration and six held-out scenes. Each scene received 5.5/11/16.5 mm/s forward walking crossed with yaw 0,±2,±5,±10,±20,±40°/s, plus a stationary-fly control: 408 primary inputs. Sixteen additional visual inputs halved frontend, graph-input and solver clocks; four solver-only comparisons retained the original inputs. All twelve copies were run, including sham, bilateral/unilateral bIPS silencing, five specified bIPS outgoing-edge lesions, and HS/H2 silencing controls. No outgoing weight renormalization was performed. [Prospective protocol](YAW_SENSITIVITY_ABLATION_PROTOCOL_V1.md), [hash-frozen definitions](../results/yaw_sensitivity_ablation_v1/prospective_manifest.json).

Responses are signed tanh model units, not calibrated spikes, voltage or calcium. Negative values describe model inhibition. Each class is represented by mean left/right response during 0.7–1.4 s. A signed-yaw ridge readout is fitted only to training scenes, separately at each known speed. The maximum absolute straight-walking score on calibration scenes sets its detection cutoff. Held-out scenes never enter training or cutoff selection. Primary lesions use the unchanged intact readout; secondary analyses retrain only on each lesion’s training/calibration split. This distinguishes disruption of the original code from information recoverable by a newly calibrated decoder. No neural parameter is fitted.

A reported threshold must meet ≥80% detection, ≥80% yaw-sign accuracy and ≤10% false positives, sustained at all larger tested yaw magnitudes. Failing false-positive control makes the threshold unresolved, rather than a physical lower bound. Values ≤2°/s are only upper bounds on the tested grid. Reliability here is across six finite held-out environments, with 12 rotating and six straight cases per speed/magnitude. There are no simulated trial-noise replicates, fly psychophysical thresholds or statistical guarantees at a population false-positive level. Confidence intervals describe this small scene sample.

## Intact circuit results

| Class | Forward speed (mm/s) | Threshold (deg/s) | Straight false positives |
|---|---:|---|---:|
| HS | 5.5 | unresolved | 33.3% |
| HS | 11 | unresolved | 33.3% |
| HS | 16.5 | unresolved | 16.7% |
| H2 | 5.5 | 20 | 0.0% |
| H2 | 11 | 40 | 0.0% |
| H2 | 16.5 | 40 | 0.0% |
| bIPS | 5.5 | unresolved | 16.7% |
| bIPS | 11 | unresolved | 16.7% |
| bIPS | 16.5 | 20 | 0.0% |
| DNp15 | 5.5 | unresolved | 16.7% |
| DNp15 | 11 | unresolved | 33.3% |
| DNp15 | 16.5 | 20 | 0.0% |

All nonmonotonic detection, sign and correctly directed detection curves are retained. Sign accuracy uses the continuous score on every rotating case, including scores below the detection cutoff; correctly directed detection is tabulated separately. Generalization is to new rooms, with known walking speed and yaw magnitudes already present in training. A threshold failure is an experimental result under the frozen rule, not permission to adjust the cutoff or exclude scenes. [Full detection curves](../results/yaw_sensitivity_ablation_v1/detection_curves.csv), [threshold table](../results/yaw_sensitivity_ablation_v1/detection_thresholds.csv), [every held-out prediction](../results/yaw_sensitivity_ablation_v1/decoder_predictions.csv), [cell responses](../results/yaw_sensitivity_ablation_v1/cell_responses.csv).

![Detection](../results/yaw_sensitivity_ablation_v1/figures/detection_curves.png)

![Direction](../results/yaw_sensitivity_ablation_v1/figures/direction_accuracy.png)

## bIPS-associated mechanisms and controls

The following DNp15 results use the intact readout. They measure model lesion effects, including baseline biases that can raise false positives. Full secondary retraining results are available in the threshold table and figure.

| Graph copy | 5.5 mm/s | 11 mm/s | 16.5 mm/s |
|---|---|---|---|
| intact | unresolved | unresolved | 20 |
| sham | unresolved | unresolved | 20 |
| bips_silence | unresolved | unresolved | unresolved |
| bips_left_silence | 5 | 10 | 10 |
| bips_right_silence | unresolved | unresolved | unresolved |
| bips_out_all | unresolved | unresolved | unresolved |
| bips_to_dnp15 | unresolved | unresolved | unresolved |
| bips_to_hs | unresolved | unresolved | 20 |
| bips_to_h2 | unresolved | unresolved | 20 |
| bips_recurrent | unresolved | unresolved | 20 |
| hs_silence | 40 | >40_under_rule | >40_under_rule |
| h2_silence | unresolved | unresolved | 10 |

Silencing emitted bIPS rates and removing all bIPS outputs are equivalent outside bIPS in these equations; this is an implementation control, not two independent biological findings. Selective lesions isolate existing bIPS→DNp15, bIPS→HS, bIPS→H2 and bIPS→bIPS interactions. Removing HS/H2 also preserves their feedback effects on T4/T5; the circuit was never reduced to a feedforward approximation. Grouped chemical inputs distinguish direct removal from indirect recurrent changes.

![DNp15 responses](../results/yaw_sensitivity_ablation_v1/figures/dn_yaw_response_and_lesions.png)

![Lesion detection](../results/yaw_sensitivity_ablation_v1/figures/dn_ablation_detection.png)

![Thresholds](../results/yaw_sensitivity_ablation_v1/figures/dn_thresholds_and_retraining.png)

![False positives](../results/yaw_sensitivity_ablation_v1/figures/dn_false_positives.png)

![Currents](../results/yaw_sensitivity_ablation_v1/figures/dn_current_decomposition.png)

## Numerical validation and failures

Additional spatial diagnostic (no neural-input change): mean retinal luminance RMS error against direct rays is 0.02055 at 1-degree pitch and 0.01099 at half pitch over eighty checkpoints per pitch. Maximum point errors are 0.5255 and 0.4556, respectively. These image-only checks do not establish spatial convergence of the full frontend or decoder. [All sampling errors](../results/yaw_sensitivity_ablation_v1/spatial_luminance_errors.csv), [prospective diagnostic addendum](../results/yaw_sensitivity_ablation_v1/spatial_diagnostic_addendum.json).

Forty-two preflight tests passed, including exact streamed-input reproduction of a historical full-movie run. The compiled implementation matched the original historical solver within 4.4e−18. New-source checks covered every retained retinal checkpoint, with maximum error 0. Eight full source movies were independently filtered/pooled (4,345,280 channel checks; error 3.33e-09). Small-yaw angular-flow error was 4.01e-09 rad/s; scalar depth error 0 mm. Twenty-four circuit-copy trajectories matched the Python reference within 3.47e-18. All final grouped currents were reconstructed; error 7.05e-19.

Temporal checks flagged 0 mean summaries and 0 yaw-minus-straight contrast summaries above 10%; worst relative changes were 4.11% and 4.86%, using the predefined 1e−5/1e−7 floors. There were 33 decoder-decision changes among the recorded comparisons. Every flag and changed decision is retained. Solver-only differences are reported separately. These subset checks do not establish universal temporal/spatial convergence or anatomical optical registration.

The initial launcher failed before any trial because Python’s forkserver socket was sandbox-blocked. An additive fork launcher recovered execution without changing frozen scientific methods. Preserved failure files: 1. No failed neural condition was replaced to obtain favorable performance. [Launcher amendment](../results/yaw_sensitivity_ablation_v1/launcher_amendment_v1.json), [numerical review](../results/yaw_sensitivity_ablation_v1/numerical_review.json), [arithmetic review](../results/yaw_sensitivity_ablation_v1/statistics_review.json).

## Biological interpretation and experimental predictions

Erginkaya et al. describe recurrent inhibitory interactions and stronger rotational selectivity downstream. The current model tests only the bIPS-associated interactions present in its reduced chemical graph. The paper’s display stimuli, calcium readouts and manipulations differ from these depth-aware 3D images and idealized rate clamps. Its qualitative mechanism motivates the lesions; this is not quantitative physiological validation. DNp15 GABA-A perturbation affects multiple inhibitory sources and is not equivalent to deleting bIPS outputs. The paper reports that directly recording DNp15 during bIPS-TNT silencing was prevented by a genetic expression problem, so that paired model lesion is a prediction rather than reproduction of an available recording. [Primary study](https://www.nature.com/articles/s41593-025-01948-9). Electrical interactions are relevant experimentally but absent here; uLPTCrns and H2rns are also absent from this graph. Their absence cannot establish their irrelevance, and no surrogate connection was inserted. [Pokusaeva et al.](https://doi.org/10.1038/s41467-024-53173-w). Walking-dependent visual gain and nonvisual signals remain absent. [Fujiwara et al.](https://pubmed.ncbi.nlm.nih.gov/27798632/).

Experimentally testable predictions are the full speed-by-yaw response curves; DNp15 bilateral response shifts after unilateral versus bilateral bIPS perturbation; and differences between bIPS-output perturbation and upstream HS/H2 suppression. Compare neural asymmetry and false positives as well as mean amplitude. Validate them with matched visual stimuli, explicit calcium/voltage measurement models and independent flies before inferring biological causality. Model-specific signs and magnitudes, including negative or unresolved detection findings, are tabulated rather than assumed from the literature.

## Reproduction and undergraduate explanation

Run the versioned launcher, numerical review, frozen analysis, arithmetic review and report scripts with the recorded Python/compiler environment. Full source drives, readout trajectories, currents, final states and checkpoints are indexed. Complete panoramas and intermediate full-network histories are regenerable, rather than duplicated for thousands of graph-copy trials. Both previous seals are preserved. [Reproduction instructions](YAW_SENSITIVITY_ABLATION_REPRODUCTION_V1.md).

We asked how small a turn the model can notice while the fly keeps moving forward. We showed the same images to the intact circuit and to copies with selected neurons silenced or connections removed. A separate calculation learned response patterns from some rooms and was tested in unfamiliar rooms. This tells us which existing connections help or hinder detection inside this computer model. The purpose is to produce precise predictions for experiments; it does not show that a real fly has the same threshold, and it does not yet control a walking robot.

## Supported interpretation and negative findings

The frozen analysis does **not** establish reliable 2–5°/s detection across walking speeds. At ±2°/s, intact DNp15 detects 8/12, 4/12 and 3/12 rotations at 5.5, 11 and 16.5 mm/s, respectively; straight false alarms are 1/6, 2/6 and 0/6. At fast walking, its 20°/s primary-grid threshold combines 12/12 detections, correct signs and zero observed straight false alarms. Zero observed false alarms in six rooms does not guarantee a ≤10% population rate.

bIPS helps preserve the **original calibrated code**: at fast walking, bilateral silencing raises fixed-readout false alarms from 0/6 to 4/6. Removing only bIPS→DNp15 raises them to 3/6; bIPS→HS, bIPS→H2 and recurrent bIPS lesions retain the intact 20°/s threshold. Together with the current decomposition, this supports a direct inhibitory contribution to output balance within this model. It does not establish that bIPS supplies indispensable yaw information: lesion-specific retraining restores the fast 20°/s threshold after bilateral silence or direct-output deletion.

The apparent fixed-readout benefit of left bIPS silence (5/10/10°/s thresholds) and detriment of right silence are retained. The benefit disappears after lesion-specific recalibration, consistent with a shifted bilateral code/calibration bias rather than a general information gain. HS suppression strongly reduces signed yaw responses; H2 suppression has mixed readout-dependent effects. These negative and asymmetric results do not support a simple claim that every inhibitory or upstream component always improves classification.

There are 33 changed decisions among 1,536 joint-clock comparisons, despite all mean/contrast summaries remaining below the predefined 10% flag. No intact DNp15 decision changes in this selected refinement subset; intact H2 changes a +2°/s case from a wrong-sign detection to no detection. The 20°/s threshold itself was not fully re-estimated on a finer-clock train/calibration/test sweep. It is therefore a primary-resolution grid result, with partial numerical checks and the separately reported spatial-sampling limitation.
