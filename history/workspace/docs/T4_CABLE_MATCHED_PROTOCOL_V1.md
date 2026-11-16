# Full published T4 cable matched-voltage comparison V1

2026-11-06. The user authorized another round following the literature advice.
The audit corrects the premise that author-code reproduction remains undone:
the full344-section model was already reproduced in October. Reuse those
unchanged references; do not present another native replay as new biology.
The November direct-voltage assay instead tested a different five-input source
adapter. The new work compares the full published cable with actual movies and
native electrical measurements, preserving both old implementations.

## Provenance and scope

Use Gruntman2018 Figure5 NEURON source, its12 fixed parameters, morphology,
seed300,99 excitatory/55 inhibitory sites and existing arbitrary-input wrapper.
No parameter, synapse, RF shift or latent sign is optimized. The author fit this
model to stationary flashes from the original experiment; moving stimulation
was a generalization condition. Its recordings are not an independent new lab
cohort, even if some files have not been scored by this project.

Cells1–5 and their early-localizer axes/late repetitions have already been
inspected. Call cells1–2 calibration and3–5 **retrospective comparison**, never
fresh validation. Reuse exact integer-clock response extraction and observer
references from the previous R2 correction; no new calcium observer. Raw images
and sample/event timestamps are read directly from the admitted MATs.

## Fixed image-to-source mapping

Map eleven author bins−5..5 to positions2.25deg apart on each cell's existing
canonical PD axis through the source-defined RF center. Native increasing bin
order is the author's PD. Sample the actual32×96 piecewise-constant pixels on
the centerline, including equal halfweights on exact pixel boundaries. A source
unit pulse represents the recorded bright bar: `(pixel−background)/(white−background)`.
This maps grey3 to0 and bright7 to1, matching native source pulse amplitude;
it is not a new gain fit. No contrast-energy normalizer, transverse RF average
or generic Mi1/Mi4 filter bank is inserted before the published cable. Its
upstream transformations are implicit in the stationary-flash fitted inputs,
as stated by the paper. Retinotopic transport/centerline integration remain
explicit assumptions; this does not validate individual MaleCNS T4 subtypes.

Use all recorded frame events, with300ms grey prehistory and the frame0 reset.
Exact cascades process piecewise-held frame inputs; unchanged wrapper replays
conductances at1ms with the author's linear resistance interpolation. Record
signed soma Vm at1ms and compare at the pre-existing2ms bin centers. Baseline
is[-250,−50)ms. Do not adjust latency, spatial scale, amplitude by condition,
preferred direction, trial selection or scoring window.

Three prespecified readouts from identical simulated Vm:

* Primary `cable_raw`: baseline-subtracted Vm in physical mV, gain1.
* Diagnostic `cable_calibrated`: one nonnegative zero-intercept scalar gain,
  fitted on cells1–2 with equal cell/condition weights.
* Diagnostic `cable_rectified`: apply the former `max(Vm+65,0)/65` bridge first,
  subtract its own baseline, and fit one such gain on cells1–2. It is an
  unmeasured release surrogate, not a replacement for voltage physiology.

Include the previous parallel-source outputs as archived negative comparators;
do not simulate or retune them again.

## Sequence, fixed rules and conditional advancement

1. Restore pinned NEURON8.2.7 in an isolated temporary environment; preserve
   the missing prior temporary environment and first sandbox DNS installation
   failure. Freeze all methods, sources, prior-reference/input hashes and this
   protocol before any new cable prediction.
2. Replay author PD/ND20/160ms against saved native trajectories, tolerance
   0.001mV. Also require344 sections and99/55 sites. Stop if reproduction fails.
3. Simulate cells1–2, all8 PD/ND×dwell mean conditions using both later trials.
   Compare0.1ms versus0.05ms on cell1 PD/ND20/160ms first later trial; maximum
   absolute difference≤0.005mV at scored bin centers. Lock diagnostic gains.
4. If numerical gates pass, simulate the same conditions in comparison cells3–5.
   MSE is equally weighted by condition and cell. References are zero and the
   early-only direction-blind waveform. Enumerate27 three-cell bootstraps with
   fixed gains. A waveform criterion requires positive pooled skills against
   both references, positive zero skill per cell, positive5th-percentile joint
   minimum bootstrap skill. These are the previous waveform rules, not a new
   physiological equivalence margin. Report inhibition using the unchanged
   localizer mask rule separately; zero qualifying masks means unqualified,
   never a successful inhibitory validation.
5. Only if `cable_raw` or `cable_calibrated` passes waveform/numerical rules,
   advance to three project-unscored moving-bar files, selected now by dates
   20160504/20160505/20160510 and earliest lexicographic MovingBar protocol per
   date, without response-based selection. Prefer raw if both qualify. Freeze
   selected readout and gains before acquisition/processing of those recordings.
   Author-fitted stationary-flash cohort overlap remains an explicit limitation.
   Apply the same early-only32-condition PD localizer and later PD/ND repeats
   with no gain update. Score identical waveform/inhibitory rules. Otherwise
   stop without opening those responses; do not train an encoder or add another
   model family during this round.

## Audits, budgets and reporting

One worker;1200 total scientific child-CPU seconds,2GiB RSS target,192MiB results
cap (including at most128MiB new raw data),20GiB free reserve. Temporary simulator
packages are separate, estimated<512MiB; no whole archive, generated movies or
full MaleCNS solve. New sources, if advancement qualifies, use verified ZIP
member ranges and receipts. Store compact11-channel inputs and soma traces;
do not retain full filter/cable fields. Original176MB MAT data are referenced,
never copied. Preserve failures; exclusive writes prevent result overwrite.

Independently reconstruct scalar pixel samples/event holds, exact-clock observed
means, calibrated gains and all final metrics/bootstrap cases. Verify all368
prior direct-voltage indexed files, distinguishing earlier intentional movie
retirements from corruption. Plot and explain supported results and failures.
Append dated progress, copy methods/progress before sealing, then verify after
all writers and the sealer have exited. No claim of full biological validation,
small-turn reliability or downstream mechanism follows from a component pass.
