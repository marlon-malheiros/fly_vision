# Path to a working, biologically benchmarked neural model V1

1 November 2026. Planning decision and source-availability audit; no new neural simulation, fit or biological validation completed in this document. This is not an execution protocol with all acceptance rules frozen.

The target is an image-driven neural model that reliably reports small yaw during forward walking and agrees with specified neuronal measurements. The original 2-degree/s objective remains open. The existing 5-degree/s result is a useful intermediate reference, not a replacement objective. A learned neural reader, a native DNp15 output and physiological validation are separate claims.

| Requirement | What we have | What remains |
|---|---|---|
| Working image-to-neural simulation | Frozen functional frontend, MaleCNS circuit, LPi-expanded candidate, reproducible walking simulations | Frontend and downstream coupling remain only partly biologically constrained |
| Neural-only turn detection | Predefined secondary reader: 143/144 correctly signed 5-degree/s turns, no observed straight-walking alarms in the shared 24 fresh rooms | Original 2-degree/s criterion; independent confirmation beyond these now-inspected rooms |
| Agreement with recordings | Published T4 peak comparison, conditional T4/T5 and downstream comparisons, limited HS voltage assay | A prospectively specified multi-stimulus benchmark with explicit observation models and stronger independent evidence |
| Circuit mechanism | Anatomical audits and model perturbations; mixed LPi/family effects | A demonstrated bIPS benefit and biological support for the proposed mechanism |

[Current bounded result](NEURAL_POPULATION_MILESTONE_BRIEF_V1.md), [physiological source gate](PHYSIOLOGY_INTEGRATION_SOURCE_GATE_REPORT_V1.md), [LPi successes and regressions](HORIZONTAL_OPPONENCY_REPORT_V1.md), [HS benchmark and limitations](HS_VOLTAGE_BENCHMARK_REPORT_V1.md).

## A bounded next experiment

Reproduce the published FlyVis visual network together with its existing pretrained motion decoder as a separate reference. The earlier integration read only T4/T5; the full pretrained decoder was not run on the walking movies. It requires all 34 output cell types, so the old eight-type adapter cannot supply it directly.

The [authors' optic-flow example](https://turagalab.github.io/flyvis/examples/02_flyvision_optic_flow_task/) and [release v1.2.0 decoder source](https://raw.githubusercontent.com/TuragaLab/flyvis/v1.2.0/flyvis/task/decoder.py) identify a concrete implementation. This decoder is a task-trained artificial network. Its success would test available motion information; it would not reconstruct HS/H2/bIPS/DNp15 or establish their physiological validity.

The local checkpoint `data/derived/flyvis_r3/results/flow/0000/000/best_chkpt` still matches SHA-256 `d8a57a022aa18ca338599be713af9db29b89cde4b00098ffe42b78f0d583e46a` (49,378 bytes), independently rehashed today. The retained [checkpoint audit](../results/neural_population_readout_v1/analysis/published_decoder_availability.json) records the 34-input-type decoder weights. Release v1.2.0 source was inspected today; numerical equivalence to an executed local decoder remains untested. An additional guessed remote configuration path was unavailable; the local model metadata specifies `DecoderGAVP`, shape `[8, 2]`, kernel size 5 and no global pooling.

The simulation interpreter currently lacks FlyVis, Torch and h5py. A read-only audit initially failed while importing h5py, before checking the checkpoint. Repeating the hash/package check with the standard library succeeded. The saved output-type HDF5 was not reread, and the earlier 34-type inventory is not presented as a newly executed population check. A cached Torch runtime exists; restoring the compatible full FlyVis runtime is still necessary. Available disk space was about 819 MB, so begin with small diagnostic outputs and preserve all existing evidence.

## The sequence and decisions

1. **Reproduce the published pipeline.** Pin the release, checkpoint, runtime, cell ordering, units, preprocessing and initial-state procedure. Use native execution and an independent decoder arithmetic check on identical saved activity. Test stationary input and analytical motion controls with known geometry. Do not substitute zeros for the other 26 cell types or silently change angular scale. If native reproduction fails, resolve that implementation issue before walking claims.

2. **Locate the remaining loss of yaw information.** Compare neural population activity, the native motion decoder, and the unchanged MaleCNS outputs on already-inspected development rooms. Neural decoding success alongside downstream failure would support investigating the downstream interface or pooling; failure of one decoder would not prove that the population lacks yaw information. Any geometric reduction of decoded flow is an explicitly artificial readout. Keep it separate from the anatomical circuit claim.

3. **Build one evidence-constrained circuit candidate.** Select a change only after the diagnostic above and the existing physiological discrepancies identify a testable mechanism. Preserve the baseline and current successful reader. Use connectomic evidence for wiring and physiological data for dynamics and observation scales. Do not optimize anatomical weights to obtain yaw labels. Published fixed T4/T5 models are an alternative if the FlyVis route fails the declared cellular benchmarks; their spatial embedding, CT1 mapping and voltage-to-network conversion remain documented gaps, not solved interfaces.

4. **Require separate physiology and walking verdicts.** Before new candidate outcomes, specify physiological endpoints, uncertainty handling, calibration data, validation data and noninferiority/improvement margins. Compare T4/T5 direction and speed tuning, HS/H2 preferred/null responses, and bIPS/DNp15 selectivity and time courses wherever usable recordings exist. Use an explicit voltage/rate/calcium observation model. Retain low-response animals and per-animal errors. Previously inspected Erginkaya, Suver and HS material remains development or previously inspected comparison evidence. A new software run does not make it independent biological validation. If no suitable untouched recording set exists, report the restricted agreement and the exact measurement needed next.

5. **Freeze and test the candidate once on new rooms.** Keep training, threshold calibration and testing separate. Retain the existing behavioral requirements of at least 80% correctly signed detections, including each yaw sign, and at most 10% episode-level straight/stationary false alarms at every walking speed. Test 0/plus-or-minus 2/plus-or-minus 5 degrees/s and all three speeds. Add varying turn onset, sustained yaw and a separately generated environment family with definitions frozen beforehand. No onset, speed, depth or room label enters inference. Freeze numerical tolerances and space/time/solver controls for the new output units before execution. Report uncertainty and latency as well as counts. The engineering 2-degree/s specification is not an established behavioral threshold for real flies.

The immediate execution protocol should cover steps 1 and 2 only, with a fixed checkpoint, diagnostic stimulus set, numerical tolerances and resource budget. Later candidate construction depends on those findings; calling that entire adaptive sequence preregistered would be misleading. Each new stage gets its own freeze before outcomes, failures, report and evidence index. No closed-loop control is included.

## What counts as finishing

A **working neural detector** requires the frozen neural-only candidate to meet its declared detection, false-alarm and numerical criteria on untouched simulations. A **biologically benchmarked MaleCNS model** additionally requires the specified cellular comparisons to support its claimed scope; missing or failed measurements remain explicit. A successful external FlyVis decoder cannot by itself complete the MaleCNS or bIPS mechanism objectives. Neither criterion demands perfection across every neuron and environment, but both need positive evidence.

We want to find where the simulated brain loses the useful turn signal and repair that stage using biological evidence. We will first check an existing published neural system, then test any justified circuit change against both recordings and walking. This gives each experiment a specific decision and keeps a better classifier from being mistaken for a validated fly circuit.
