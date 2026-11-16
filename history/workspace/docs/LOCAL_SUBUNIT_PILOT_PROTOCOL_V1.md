# Local nonlinear neural subunits V1 — 2026-11-02

## Question and scope

Test whether normalization at co-located fine T4/T5 sites before wide-field
pooling improves small-turn decoding. This is one artificial neural-readout
architecture, with two matched controls and a fixed ridge penalty. No encoder
training, synaptic change, electrical conductance, metric-flow conversion or
physiological validation is implied. Local signal loss is a hypothesis, not a
diagnosed cause. The previously failed geometric weighted medians are different
readouts and remain negative results.

An outcome-blind feasibility audit precedes this protocol: one p00 fast +2
cached-input replay exposes all 13,624 rates using the unchanged observer with
an identity observation assignment. Re-pooling exactly reproduces archived
429-column activity, checkpoints and final state. No detector scores were
computed. Benchmark: 1.8033 seconds; 181,350,400 bytes peak RSS. Actual full rate
traces are not cached. Positive input arrays cover the endpoint. Historical
negative inputs end at 1.8 seconds, so they cannot replace three-second controls;
those are streamed through the original renderer/frontend without saving images.

Freeze this protocol, config, feature/training/execution code, anatomical map,
training-derived floor and input manifest before computing new local features
or fitting the detector. Already inspected p/w rooms are development data.
The reserved st rooms, previous np tests, and biological arrays are not accessed.

## Fixed local features and controls

Use only the unchanged LPi-intact graph and validated frontend/parameters.
For each eye and each horizontal family (T4a/b, T5a/b), anchor each actual a
neuron to the nearest b neuron in the declared eye-coordinate registration.
Retain only distances <=0.001 degrees: co-located functional sampling sites,
not asserted anatomical synapses or cell homologies. Ties follow the frozen
map and all actual IDs/distances are recorded. Exclude unmatched anchors by
geometry alone; report coverage. No new connections are inserted.

Clip each observed source-neuron rate at zero, then take its causal ten-callback
mean at 100 Hz. For each retained local pair define A and B as these means and
O=(A-B)/(epsilon+A+B). Epsilon is twice the median straight-walking horizontal
mean activity over all 24 p training rooms, speeds and callbacks 100..299.
That mean is computed from the old pooled activity weighted by bin cell counts,
clipped at zero per bin. It is a training-only activity scale proxy, not a
physiological parameter or true velocity. No calibration or positive labels
choose epsilon. Both eyes/families share this one fixed floor.

Assign sites to the same 6x4 eye-coordinate patches used in the archived observer.
The primary `local_before_pool` averages O within each patch. Matched control
`pool_before_normalize` averages A and B first, then computes the same ratio.
`raw_local` averages (A-B)/epsilon in the same patches. Empty patches are zero.
For each method take R-minus-L patch values, keeping T4 and T5 separate: 48
spatial features. Add seven R-minus-L means from actual downstream HS, H2, bIPS,
DNp15, uLPTCrn candidates, H2rn candidates and LPi (no one-to-one pairing assumed).
Use a causal ten-sample mean for downstream rates. For all 55 features subtract
their value 20 callbacks earlier. Local normalization therefore acts before
wide-field averaging and before differencing. No future frames, scene, speed,
depth, yaw label or onset clock enters inference. Fixed windows are continuously
defined; evaluation alone chooses callback 119 and negative monitoring windows.

Fit each of the three readouts once on p rooms: zero and +/-2 only, all speeds,
including static negatives. Equal total mass per sign, equal episodes per sign,
and uniform callback weights within negative episodes; scale weights to the
number of training episodes. Positive episodes use callback 119. Weighted RMS
scaling is training-only, without centering or intercept. Ridge is fixed at 10
on the summed episode loss, with no hyperparameter selection/CV/search. A
nonnegative scalar least-squares gain fitted on training samples expresses
scores in training-calibrated degree/s equivalents. No alternative wins by
calibration selection: the local-before-pool model is the sole primary.

## Stage order, gates and stop rule

1. Extract the 240 p training episodes, fit all three models, then hash-freeze
   coefficients and inference implementation before accessing new w features.
2. Extract only the 80 w fast-walking episodes (0, +/-2, +/-5). Choose each new
   method's cutoff from fast straight negatives only: the order statistic that
   allows <=1/16 strict |score|>cutoff episode alarms. This is a provisional
   diagnostic cutoff, not the eventual cross-speed cutoff. It is the lowest
   cutoff that could possibly meet the common-cutoff gate, making it a necessary
   fast-speed feasibility test. Controls are descriptive, not substitutes for
   the primary. Require >=26/32 signed detections and >=13/16 in each direction
   for +/-2 AND +/-5 at callback 119 (190 ms after onset).
3. If the primary fails, stop the pilot. Do not select a control, change features,
   floor, ridge, thresholds or latency, inspect reserved rooms, run a policy bank
   or train an encoder. This closes this local-readout hypothesis under its
   specified settings; it does not prove information absence or impossibility.
4. If the primary passes, extract the remaining 176 w episodes. Use one common
   negative-only cutoff: maximum of per-speed/static order statistics allowing
   <=1/16 alarms per group. Apply >=26/32 joint and >=13/16 per sign, both yaw
   magnitudes at every walking speed, plus <=1/16 static alarms. No refitting.
5. Only a full calibration pass can trigger a separately recorded full-run cost
   estimate/freeze for the original 81 spatial/temporal/solver refinement
   comparisons and reserved-room testing. Require max score error <=0.2 and
   unchanged endpoint/negative-episode alarm decisions for all 81. Do not use
   nine checks as a substitute. Keep the existing 24-room signed detection and
   false-alarm acceptance criteria for fresh testing. Do not count development
   performance as independent generalization.

Straight/static negatives are monitored continuously at callbacks 100..299,
never only at the positive endpoint. Preserve all compact feature/score curves,
per-room endpoints, negative peaks, scores, counts, source and observer hashes,
states/parity receipts, numerical failures and exceptions. Reproduce the original
45-neuron baseline and previous energy model on the corresponding archived w
episodes using their original coefficients and full-calibration cutoffs.

## Validation and resource boundaries

For every new observation require source-drive SHA equality with its archived
summary, bitwise equality after old pooling, and bitwise checkpoints/final state.
Verify the retained old observation, summary, source and graph hashes against
their own receipts/locked records; do not run full retired-movie availability
checks or regenerate movies. Verify pre-onset feature and score prefix equality
for matching straight/turn episodes. Focused tests cover nonlinear operation
order, prefix causality, empty bins, mirror antisymmetry of the artificial
feature map, and episode-level cutoff behavior. Independently reproduce chosen
features and all scores using literal windows and loops rather than the fitting
implementation; this checks arithmetic, not physiological realism or an
independent model fit. Report training fit and calibration results separately.

At most four one-thread CPU workers, no GPU, <=1 GiB RSS per worker, <=3,600
aggregate observation CPU seconds, <=120 seconds for fitting/scoring, <=512 MiB
total persistent new-study output, >=20 GiB free disk reserve. One output batch
may finish after the coordinator discovers a resource limit; preserve/report
that failure and stop rather than relaxing limits. An audit-based planning
estimate is <=120 MiB compact features plus <100 MiB scoring/report/archive
overhead, with full rates/images temporary in memory only. Historical episode
timings imply roughly 30–60 CPU minutes for the training/fast gate; actual CPU
and peak memory are recorded. Remaining calibration is conditional on both
scientific and resource gates, not automatic authorization to exceed the cap.

Do not label a successful external decoder as a repaired anatomical pathway or
as evidence that bIPS improves biological detection. Matched physiology and
controlled circuit ablations would require separate measurement models and
prospective analyses. Missing constraints remain explicit. Snapshot the live
progress report inside the completion archive and keep live AGENTS/progress
outside its immutable index. Preserve all previous evidence and this pilot's
failures.
