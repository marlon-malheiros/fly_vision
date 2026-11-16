# Neural population readout V1 — completed finite experiment

31 October 2026. Original neural model and previous results preserved.

**Outcome:** No tested neural-only readout passes all declared behavioral and numerical gates.

This experiment asks whether retaining spatial neural activity repairs the tested small-turn readout. It does not reconstruct missing biological circuitry or establish physiological validity. The fixed primary is spatial_mlp; all other candidates and failures are retained.

[Frozen protocol](NEURAL_POPULATION_READOUT_PROTOCOL_V1.md), [pre-test freeze](../results/neural_population_readout_v1/before_test.json), [complete numerical evidence](../results/neural_population_readout_v1/analysis/test_curves.csv), [independent review](../results/neural_population_readout_v1/independent_final_review.json).

We kept the functional HRC frontend, all 13,624 neural states, recurrent chemical connectivity, LPi expansion and baseline parameters frozen. Only observation/pooling and separate artificial supervised readouts changed. Actual T4/T5 tanh rates are averaged into 384 fixed retinal bins (6 × 4 per eye and subtype); all 45 downstream neurons are retained individually. The 32-hidden-unit tanh readout is a task-trained neural network appended as an information probe, not measured fly connectivity. No image-motion estimator, image confidence, true speed, depth, scene or onset label enters inference.

Training uses 24 previously inspected p rooms; diagnostic calibration uses 16 previously inspected w rooms. Straight/stationary negatives cover all 200 callbacks from 1 through 2.99 seconds; turn positives use the fixed 1.19-second endpoint. Four fits are frozen before calibration scoring and fresh test images, without early stopping, hyperparameter search or calibration threshold fitting. The prior DNp15 fit is a fifth unchanged reference. The test has 24 new seed-disjoint rooms / 384 episodes, balanced mirrored/clutter conditions, at three speeds and yaw 0/±2/±5, plus stationary. Same environment family; deterministic simulations, not biological replicates.

| Readout | Speed mm/s | ±2 joint /48 | Each sign −/+ /24 | Straight any /24 | ±5 joint /48 | All behavior + numerics |
|---|---:|---:|---:|---:|---:|---|
| dnp_linear | 5.5 | 48 | 24/24 | 0 | 48 | False |
| dnp_linear | 11 | 48 | 24/24 | 1 | 48 | False |
| dnp_linear | 16.5 | 44 | 22/22 | 10 | 48 | False |
| individual_linear | 5.5 | 48 | 24/24 | 0 | 48 | False |
| individual_linear | 11 | 48 | 24/24 | 0 | 48 | False |
| individual_linear | 16.5 | 46 | 23/23 | 9 | 48 | False |
| spatial_linear | 5.5 | 48 | 24/24 | 0 | 48 | False |
| spatial_linear | 11 | 48 | 24/24 | 10 | 48 | False |
| spatial_linear | 16.5 | 46 | 23/23 | 22 | 48 | False |
| spatial_mlp | 5.5 | 48 | 24/24 | 0 | 48 | False |
| spatial_mlp | 11 | 46 | 23/23 | 19 | 48 | False |
| spatial_mlp | 16.5 | 34 | 17/17 | 13 | 48 | False |
| frozen_dnp_reference | 5.5 | 48 | 24/24 | 0 | 48 | False |
| frozen_dnp_reference | 11 | 48 | 24/24 | 1 | 48 | False |
| frozen_dnp_reference | 16.5 | 44 | 22/22 | 10 | 48 | False |

Success requires at least 39/48 detections, correct raw signs and joint detections, at least 20/24 each sign, and at most 2/24 endpoint/any-episode straight and stationary false alarms at every speed and both magnitudes. Numerical qualification separately requires every one of 81 space/time/solver comparisons to remain within 0.2 score units and preserve endpoint and any-alarm decisions. A negative verdict cannot be rescued by selecting favorable rooms or dropping numerical failures.

![All neural-only comparisons](../results/neural_population_readout_v1/figures/neural_population_comparison.png)

Numerical reproducibility and limitations

The new observer matches the original kernel bitwise on individual outputs, final states and checkpoints for a nonzero saved input. Independent full-state pooling checks pass. Weighted linear fits are independently recomputed using augmented least squares; the MLP inference is checked against PyTorch and preserved training predictions. Full-state stationary controls, direct-window prediction arithmetic, every test curve/count, future-modified neural-prefix equality and four separately rendered/reintegrated first-room replays are checked. These establish implementation consistency, not biological validity. [Observer review](../results/neural_population_readout_v1/observer_preflight.json), [fit review](../results/neural_population_readout_v1/fit_review.json), [all refinement results](../results/neural_population_readout_v1/analysis/numerical_comparisons.csv).

The primary frontend remains a functional surrogate; eye registration, pooled receptive fields and neural parameters remain only partially biologically constrained. The learned readouts can exploit a controlled turn onset and deterministic signals; no neural noise, arbitrary trajectories, physical camera, sustained-yaw decoding or closed-loop behavior was validated. Empty bins remain zero and no missing anatomical connection is invented. Task-supervised readout weights are modeling assumptions, not evidence that HS/bIPS/DNp15 implements this mapping. No new bIPS benefit or biological causality is established.

Why this is not another published-model repetition

The earlier [published-circuit reconstruction](PUBLISHED_CIRCUIT_COMPARISON_REPORT_V1.md) and [author coupling reproduction](POKUSAEVA_GAP_REPRODUCTION_REPORT_V1.md) already showed qualitative rotation selectivity without a successful small-turn walking detector. Their linear global pooling does not establish a solution to scene-induced imbalance. This study preserves spatial and individual-cell information instead of rerunning those gains. The prior [spatial repair](SEQUENTIAL_SMALL_TURN_REPAIRS_REPORT_V1.md) used fixed geometric channel-to-velocity projection; the present readouts learn from actual recurrent neural rates. Neither is an anatomical reconstruction.

What can be tested experimentally and what to do next

Record spatially separated visual-motion populations together with downstream cells during matched forward speeds and small imposed yaw. Compare cross-validated yaw information before and after wide-field pooling, and count straight-walking false alarms alongside turn sensitivity. A spatial advantage in this model would motivate testing pooling loss; a failure does not prove biological impossibility. Next alternatives are independent physiological constraints on receptive-field integration, or a separately frozen multiscale visual encoding study. Do not call more global gain or the already successful external image branch a biological repair. No outcomes here justify adding unmeasured electrical conductances or optimizing anatomical edges solely for classification.

Undergraduate explanation — what we did, what we want, and why

We want a neural model that notices a small turn while the fly is already walking forward. Earlier readouts averaged many neurons together and could confuse uneven scenery with a turn. Here we kept more of the pattern across the simulated neurons and trained separate readers of that activity. We tested those readers on new rooms and checked that finer numerical sampling did not change the answer. A working reader would show useful information exists in these neural signals; it would still need biological evidence before we could say the fly uses the same mechanism. A failed reader tells us which tested approach to stop repeating.

Completion notes from the independent review

All 640 known-room, 108 numerical and 384 fresh-room trajectories completed without simulation failures. The independent review checks 277,440 finite scores (maximum discrepancy 3.47e-13), all 30 final curve rows, all 24 zero stationary full states, and four bitwise full replays. The individual-neuron linear readout detects/signs 46/48 fast small turns but alarms in 9/24 fast straight rooms (at most 2/24 allowed). The primary spatial MLP gives 34/48 and 13/24. No tested readout qualifies. Only the individual-neuron readout passes all 81 numerical comparisons (maximum discrepancy 0.185551); the spatial linear/MLP have eight/nine failures, with maxima 0.449250/0.391901.

The strong frozen spatial-MLP weighted training MSE of 0.001622 did not transfer to reliable new-room detection. Six-by-four retinal pooling, finite training data and this particular decoder architecture remain limitations; this experiment cannot establish that all source-neuron information or all neural readouts are inadequate.

Operational failures are preserved: an auxiliary workspace omitted the tests folder; the main simulation interpreter lacked Torch; and an old-review index audit first guessed the wrong completion-directory name. The corrected workspace preflight passes, the unchanged fit executes in the recorded cached CPU runtime, and all seven parent indexes (21,887 files) rehash correctly. These are packaging/dependency/path failures, separate from the scientific failures above. [Runtime and failures](../results/neural_population_readout_v1/runtime_r2/before_training.json), [portability correction](../results/neural_population_readout_v1/portability_r2/review.json), [prior preservation](../results/neural_population_readout_v1/prior_preservation_review.json), [reproduction guide](NEURAL_POPULATION_REPRODUCTION_V1.md).

A separate [cutoff extension](NEURAL_POPULATION_CUTOFF_REPORT_R2.md) preserves this V1 result and assesses negative-control calibration. Its ±5-degree/s secondary behavior is checked in an explicitly post-test numerical addendum; it cannot retroactively complete the ±2-degree/s target.

An exploratory [source audit](../results/neural_population_readout_v1/analysis/published_decoder_availability.json) verifies pretrained motion-decoder weights in the existing FlyVis checkpoint. It expects 34 visual cell types, while the earlier integration used only T4/T5. The [authors’ native decoder example](https://turagalab.github.io/flyvis/examples/02_flyvision_optic_flow_task/) identifies a specific next alternative; no native-decoder walking result has been executed here. It is a task-trained reader of neural activity, not an anatomical HS/bIPS/DNp15 reconstruction.

Figure review: lines join only the three tested speeds; intermediate speeds were not evaluated. Coincident curves are intentional, and exact counts remain in the CSV tables. In V1 the two DNp15 readouts have identical counts, and the individual/spatial linear readouts share the plotted joint-detection counts. In R2 both raised-cutoff individual-neuron readers have zero observed fresh-room false alarms. PNGs were visually inspected; PDF versions are also preserved.
