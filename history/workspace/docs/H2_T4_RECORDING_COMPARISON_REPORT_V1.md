# H2 recording comparison with detailed T4 population, V1

14 November 2026

## Result

The combined model **failed the prespecified directional test** against one real, previously inspected fly H2 recording. Its preferred direction differed from the recording by **14.31°**, within the 45° spacing of the sampled directions, but worse than the fixed body-horizontal reference at **6.38°**. The original functional model was closer, at **1.39°**. The rule required both at most 45° error and strictly less error than the reference. It was fixed before these predictions, although the recorded responses and older functional-model results were already known.

| Predictor | Direction error from recorded H2 |
| --- | ---: |
| Original functional model | 1.39° |
| Fixed body-horizontal reference | 6.38° |
| Detailed-T4 hybrid | 14.31° |

Thus adding this particular T4 population and bridge worsened the direction estimate on this recording. This does **not** identify the cause or show that the published T4 cable is biologically wrong. The result tests the complete set of chosen assumptions together: reconstructed visual input, T4 population registration, model initialization, assumed voltage-to-drive conversion, functional T5 and downstream graph. A closer error is also not proof of biological validity.

## What was compared

The recorded response is H2 cell 1, protocol 1, location (87, 13), with eight directions and bright and dark edges: 16 conditions. This is an identified downstream neuron in the experimental dataset associated with [Zhao et al. (2025)](https://www.nature.com/articles/s41586-025-09276-5). The exact experimental video frames were not available here: the test uses saved *reconstructions* of the stimulus family. The recorded fly was female and the connectome used for the model male. This is one recording location, already examined in previous work, and does not test independent animals or walking behavior.

Both predictions use the same frozen LPi graph and held-input solver. In the candidate, all 3,424 left-eye T4 cells use copies of the published detailed cable at their inherited model locations and axes; T5 and other inputs retain their functional model. The conversion `max(V_mV + 65, 0) / 65` to graph input is an engineering assumption, not measured synaptic release. These cable clones are not the earlier recording-specific T4 fitted ensemble. The original functional predictor retains the existing T4 and T5 inputs.

For each condition we calculated the baseline-subtracted response in the predetermined time window, averaged bright and dark curves, and used their eight-direction shapes to compare preferred directions. The recording is in spikes/second while model responses are in uncalibrated model units: the test does not equate their absolute amplitudes. The 45° cutoff is a fixed engineering criterion, not a biological equivalence margin. Full definitions and conditions: [protocol](H2_T4_RECORDING_COMPARISON_PROTOCOL_V1.md); [all 16 signed endpoints and decision](../results/h2_t4_recording_comparison_v1/decision.json).

As supplemental shape checks, dark-edge correlation with the measured eight-direction curve was **0.953** for both models; bright-edge correlation was **0.551** for the original and **0.377** for the hybrid. Under the adopted ON-only input convention, dark T4 input was zero, so the identical dark responses do not test the inserted T4 dynamics. Correlations are descriptive, not a replacement pass criterion.

## Uncertainty and checks

Using 10,000 previously generated repeat-resampling draws for this same recording, the descriptive 95% intervals for angular error were 0.16–11.10° for the original, 0.35–15.57° for the fixed reference, and 4.38–23.50° for the hybrid. The hybrid beat the reference in 2.13% of these draws. These intervals describe repeat variability within this recording only; they do not describe uncertainty across animals and do not change the fixed decision. [Uncertainty method lock](../results/h2_t4_recording_comparison_v1/before_uncertainty.json); [results](../results/h2_t4_recording_comparison_v1/repeat_uncertainty.json).

Numerical checks passed: independent sampling review covered 2,640 native positions (maximum contrast difference 6.94e-17); the two preselected cable timestep refinements stayed within 0.005 mV (maximum 0.001956 mV); and the selected network refinement stayed within 1e-8 model units (maximum 1.61e-11). An independent implementation recomputed all endpoints and the decision and replayed both full graphs for one fixed condition; maximum graph discrepancy was 4.34e-18. Thirteen focused tests passed. These checks support reproducibility of this calculation, not biological validity. [Input review](../results/h2_t4_recording_comparison_v1/input_review.json), [cable refinement](../results/h2_t4_recording_comparison_v1/cable_numerics.json), [graph results and refinement](../results/h2_t4_recording_comparison_v1/graph_outputs.json), [independent review](../results/h2_t4_recording_comparison_v1/independent_review.json).

Input-only admission covered every left T4 and all 16 cases. Exact full-sequence deduplication reduced the work to 1,160 nonzero input sequences; the cable worker ran 1,162 solves including two refinements, consuming 466.80 CPU seconds and peaking at 72,781,824 bytes RSS, below the 1,200 CPU-second limit. The graph stage consumed 81.51 CPU seconds and peaked at 248,590,336 bytes RSS. Approximately 32 MiB was retained before archiving; no retired movies were regenerated. [Preflight](../results/h2_t4_recording_comparison_v1/resource_preflight.json), [cable resources](../results/h2_t4_recording_comparison_v1/cable_resources.json), [model/source lock](../results/h2_t4_recording_comparison_v1/before_predictions.json).

## Interpretation and next decision

The specific hybrid is **not supported by this restricted directional test**, even though it lies within one sampled angular step. It would be premature to tune the bridge to this already inspected recording and call the improved fit a validation. The scientifically useful next step is to identify whether an exact-stimulus, independently recorded dataset can fairly test the T4-to-H2 connection, or whether the missing stimulus and bridge measurements make that comparison impossible. If a suitable dataset is available, define the comparison before examining its responses; otherwise report the missing evidence rather than continuing parameter tuning against this animal.
