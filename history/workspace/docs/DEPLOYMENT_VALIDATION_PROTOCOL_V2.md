# Separate deployment validation — V2

Specified 2026-10-21 before inspecting the V2 deployment clock comparisons.
Scientific studies and all of their frozen methods remain unchanged.

The original portable runtime passes numerical replay but misses its 10-ms
input-update budget under the concurrent study workload. V2 replaces Python
frontend array processing with independently checked C++ implementation of the
same functions. The optional degree-13 activation acceleration has already
matched libm to double precision on its fixed small-argument domain. These are
numerical implementation changes, not physiological parameter improvements.

## Prospective numerical and functional checks

1. Compare both deployment frontend implementations on complete, previously
   saved walking stimuli, retaining all original clocks, retinal images and
   graph parameters. Tolerance for routed input is 1e-7, inherited from source
   regeneration checks; rates from the same timestep must agree within 1e-10.
2. Separately test a 2-ms RK4 deployment clock against the original 1-ms clock
   on every one of the 408 original primary source sequences. These exact
   drives and original responses already exist; this is a declared numerical
   approximation study, not new held-out biological validation. Preserve raw
   trajectories, source hashes, per-cell means, yaw-minus-straight contrasts and
   every fixed-decoder decision change. No gain, source cadence or graph changes.
3. Mean/contrast discrepancies above 10% with the inherited 1e-5/1e-7 floors
   are flags. A deployment equivalence claim requires no flags and no changed
   decisions over the declared test set. Report the absolute discrepancies too.
   A failed gate is not permission to alter the thresholds or select cases.
   Default strict 1-ms replay remains available regardless of this result.
4. Match the exact original episode readout: separate L/R features, supplied
   known speed (5.5, 11 or 16.5 mm/s), the executed 0.7–1.4-s response mask and
   preserved intact decoders. Do not call this an instantaneous yaw controller.
5. Test frame order, missing samples, invalid luminance/shapes, reset, model
   integrity and standalone export. Reject incomplete/off-clock input rather
   than silently filling unknown visual fields or advancing a stale stream.

## CPU performance evidence

Measure strict and accelerated frontends with 1-ms and 2-ms neural clocks in
an interleaved benchmark. Save every processing duration; report median, p95,
p99, maximum, missed 10-ms input budgets and peak resident memory. Include both
frontend frames per neural update. Identify concurrent load and exclude image
rendering/acquisition explicitly. Repeat under idle study conditions after the
long simulations if necessary. Finite host measurements are not a hard-real-time
guarantee and do not establish performance on an untested board or camera.

The output is a source/model package, independently runnable replay and
episode readout, plus numerical/performance tables and a limitations report.
No motors, closed-loop locomotion, synthetic electrical weights or neural-gain
tuning are part of this deployment validation.

## Pre-comparison readout correction

An independent saved-clock check found that the original expression
`(time >= .7) & (time <= 1.4)` selects 70 samples at a 10-ms clock, from
0.7000000000000001 through 1.3900000000000001 s. The 1.4-s grid point is stored
as 1.4000000000000001 and is excluded. The deployment episode readout now matches
that executed mask exactly; its output is emitted at 1.4 s. The old reports'
description of an inclusive window did not expose this floating-point detail.
No sealed evidence or running scientific code changed. An intentionally
integer-indexed 71-sample analysis would require a separately versioned sensitivity
comparison, not replacement of the original result. This correction was made
before deployment-clock outcomes or physiological response fitting.
