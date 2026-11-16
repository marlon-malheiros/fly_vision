# Full published neural pipeline: completed investigation V1

1 November 2026. **No new candidate qualifies as a reliable 2-degree/s walking detector. Physiological validation of the complete MaleCNS pathway remains unestablished.** This completes the declared development experiments and their failure branches; it does not complete the original positive model objective.

The existing [bounded 5-degree/s neural-only result](NEURAL_POPULATION_MILESTONE_BRIEF_V1.md) is unchanged. Its 143/144 detections and zero observed straight alarms concern different held-out rooms and the prior model. They are not a paired comparison with the present development sample.

## Executed options

| Option | Execution and outcome |
|---|---|
| Full published FlyVis pipeline | Original 45,669-neuron, 1,513,231-edge network and pretrained 34-input-type decoder load strictly and run unchanged on CPU. Both canonical textures produce correctly signed responses to 2-degree/s image motion. |
| Original spherical retinal chart | 32 complete binocular walking episodes; three fixed neural-field readers fail detection/false-alarm criteria. |
| Perspective interface repair | Another 32 episodes, with source-matched perspective camera geometry and an independently checked projection Jacobian. All three fixed readers still fail. |
| Direct neural-population readout | 192 training and 96 calibration episodes. A linear decoder-field reader and a 32-unit neural-population reader fit training but fail separate-room calibration. |
| Direction-loss/symmetry repair | Two further fits to the same frozen neural observations. Neither qualifies. The physical image reflection is bitwise correct. |
| Physiological reconstruction | Existing published T4/T5 implementations, anatomical additions and recording comparisons were audited. Missing spatial/coupling constraints and mixed recording agreement prevent a newly justified complete physiological replacement. No missing connection or conductance was fabricated. |

There are **384 newly executed declared neural conditions**: 14 canonical, 64 walking-development, 18 numerical-refinement and 288 training/calibration trajectories, plus observer, moving-frame and replay checks. Earlier physiological experiments are existing evidence, not newly rerun simulations.

[Initial protocol](NEURAL_MODEL_OPTIONS_PROTOCOL_V1.md), [decoder-access correction](NEURAL_MODEL_OPTIONS_AUDIT_CORRECTION_R2.md), [fixed readers](NEURAL_MODEL_FLOW_READOUT_PROTOCOL_V1.md), [camera repair](NEURAL_MODEL_PERSPECTIVE_REPAIR_PROTOCOL_V1.md), [learned-reader results](PUBLISHED_POPULATION_YAW_REPORT_V1.md), [reproduction](NEURAL_MODEL_OPTIONS_REPRODUCTION_V1.md).

## What the full published model does and does not show

The checkpoint SHA-256 remains `d8a57a022aa18ca338599be713af9db29b89cde4b00098ffe42b78f0d583e46a`. Its original neural and decoder parameters are frozen. Unlike the older eight-type T4/T5 adapter, the native decoder receives all 34 actual output populations in their original order. The paired eyes are mirrored copies of the published right-eye network; this is a modeling assumption, not measured bilateral equality in MaleCNS.

The native decoder's training units are not degrees/s. A single two-by-two observation conversion is fitted from the eight declared plus/minus 60-degree/s canonical responses; the four plus/minus 2 controls are excluded. Walking readers use a causal 100-ms mean minus the same mean 200 ms earlier. No true speed, depth, room or turn-onset label enters inference. The readers are binocular mean, geometry-weighted mean and geometry-weighted median. They are external artificial readers, not HS/H2/bIPS/DNp15 reconstructions.

The two declared known rooms each receive stationary control and all 5.5/11/16.5-mm/s by 0/plus-or-minus 2/plus-or-minus 5-degree/s conditions. Different camera hypotheses intentionally produce different retinal images of the same physical scenes/trajectories. This is an interface comparison, not an identical-input ablation or a fair cross-study detector ranking.

At the fixed-one cutoff, all three readers alarm during both straight-walking episodes at every speed in both cameras. Raising each reader's common cutoff to eliminate the observed development alarms eliminates all 2-degree/s detections, and all 5-degree/s detections, in this sample. These cutoffs are descriptive development quantities, not validated thresholds. [Every spherical score/count](../results/neural_model_options_r2/analysis/flow_readout_summary.json), [perspective results](../results/neural_model_options_r2/perspective_repair_v1/summary.json).

![Representative complete traces](../results/neural_model_options_r2/figures/walking_transfer.png)

Correctly signed pure-motion responses therefore do not establish reliable yaw detection during translation. Failure is already present in a route that does not include bIPS/DNp15; it cannot be attributed solely to that downstream pathway. Failure of these readers also does not prove that all information is absent from the neural population.

## Numerical evidence and preserved failures

Independent double-precision decoder calculations agree within 6.77e-7 on canonical checks and 5.44e-7 on a moving frame. Independent neuron updates agree within 2.92e-7. All satisfy the frozen 2e-5 arithmetic limits. A full canonical replay is bitwise equal. [Canonical arithmetic](../results/neural_model_options_r2/analysis/canonical_arithmetic.json), [moving-frame check](../results/neural_model_options_r2/analysis/active_arithmetic_review.json).

The independently frozen refinement study uses nine-by-nine versus five-by-five aperture integration, finer physical image/neural steps, and finer neural integration with identical visual holds. Post-update native clocks are explicitly aligned. Of 18 comparisons per reader, 13 binocular comparisons satisfy the 0.2 score tolerance; neither geometry reader satisfies it in any of its 18 comparisons. The largest score discrepancy is 1.83091. Thus these failed fixed readers also lack the declared numerical qualification. [All 54 comparisons](../results/neural_model_options_r2/numerics_v1/comparisons.json).

Separate direct arithmetic reproduces 192 episode-reader summaries, all 72 curve rows and 108 refinement/cutoff comparisons; maximum discrepancies are 2.14e-14 and 1.07e-14. Passing a review means the saved failures are reproducible, not that their scientific gates passed. [Independent score review](../results/neural_model_options_r2/analysis/independent_flow_review.json), [numerical review](../results/neural_model_options_r2/numerics_v1/independent_review.json).

Restricted DNS, missing YAML, NumPy-versus-Tensor coordinate access, float32 spatial-reduction equality, reuse of an unrendered seed reservation, duplicate review-dictionary fields and a checker normalization-dtype error are preserved in separate failure files/source versions. Corrections retain neural parameters and scientific acceptance limits. Original V1 and setup directories remain available; exact failed sources are archived rather than inferred from the current source file.

## Biological constraints and the recommended alternative

The [evidence ledger](../results/neural_model_options_r2/analysis/biological_constraints.json) retains partial T4/T5 comparisons, the known H2 average direction error of 16.72 degrees versus a 13.76-degree body-horizontal reference, the broad HS voltage-ratio constraint and mixed bIPS/DNp15 waveform effects. These are meaningful comparisons with explicit stimulus/measurement assumptions; they do not validate the complete circuit. The standalone published visual network does not contain the named HS/H2/bIPS/DNp15 pathway.

Adding unspecified LPi feedback is not a new repair: the current LPi-expanded MaleCNS graph already contains **7,493 LPi-to-T4/T5**, **14,799 T4/T5-to-LPi** and **nine LPi-to-LPi** chemical edges. It has zero electrical edges. [Actual graph audit](../results/neural_model_options_r2/analysis/existing_lpi_feedback_audit.json). Synapse counts alone do not establish receptor strength, time constants or a physiological voltage-to-drive mapping.

The better next direction is a **reduced, physiology-calibrated motion-opponent circuit**, with the known anatomical graph retained and identifiable dynamics calibrated to neuronal measurements before another yaw-classification study. The released [Ammer et al. model](https://doi.gin.g-node.org/10.12751/g-node.7v3pe6/) provides a concrete implementation reference; its code/notebook were recovered and hashed without downloading the bulk archive. [Recovered sources](../data/raw/neural_completion_options_v1/ammer_model/source_manifest.json). They have not been executed here as a new walking model or physiological benchmark. Their vertical-motion circuit cannot supply measured horizontal HS/H2 parameters automatically. Any proposed horizontal transfer needs its own documented assumptions and evidence. The existing working 5-degree/s reader remains a comparator.

No experiment here proves that 2-degree/s neural detection is impossible. What fails is this finite collection of frozen representations/readers under the declared conditions. A complete biologically supported solution cannot be established by simulation alone while its necessary physiological coupling/registration constraints and eligible independent comparisons remain unresolved. Existing public data can support narrower comparisons; unavailable constraints must remain explicit.

We wanted a neural model that notices a tiny turn while the fly walks. We ran a complete existing neural visual system, corrected its camera interface, tested spatial readers and checked their calculations. These systems respond to simple motion but confuse scenery changes with turns in the walking tests. We now have reproducible negative results and a concrete biological calibration route, rather than evidence for a successful 2-degree/s circuit.
