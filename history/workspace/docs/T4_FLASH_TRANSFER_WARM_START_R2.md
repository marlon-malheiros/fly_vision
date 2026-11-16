# Warm-start numerical correction R2

2026-11-06, after V1 flash-repeat scores and before any new motion score. V1
flash-calibrated repeat-test skills are positive against zero/spatially blind
references, but all four cached-template/image checks fail the unchanged
0.005mV tolerance(max0.010629mV). V1 then stops motion scoring as required.
Preserve every V1 template, calibration, score, stopped decision and diagnostic.

The diagnostic identifies a baseline-state discrepancy. Cold source templates
start at−65mV and were converted using `Vm+65`. Actual image runs spend300ms
in grey, with the source's finite SEClamp resistance floor on future-active
sites; measured pre-motion baseline is about−64.989882mV. Its~0.0101mV offset
matches the failed comparison scale. This is numerical source initialization,
not evidence of a biological voltage offset. Do not change that source floor,
any cable parameter, data, fit grid, trial split or success criterion.

Before executing R2, freeze this one finite repair: regenerate every nonzero
unique pattern template through the unchanged cable, with300ms grey prehistory,
then its nominal flash pulse and a fixed950ms total record. Baseline-subtract
using the same[-250,−50)ms window relative to pulse onset. Keep signed0.1ms
traces. Empty patterns remain exact zero. Use these warm templates in exactly
the frozen V1 registration/gain fit and repeat/motion scoring routines, with
no RF/delay-range expansion or criterion changes. Actual-image simulations,
including learned causal delays, remain the mandatory0.005mV parity check.
If it still fails, stop motion and report the numerical limitation.

R2 outputs reside separately under `warm_start_r2/`; source MAT files are
referenced once. A narrow MAT-loader path adapter resolves those read-only
sources to their V1 location; original frozen methods are imported unchanged.
Preserve all V1 results and hash both code paths. R2 refits only the same three
flash-derived registration parameters per cell, never a motion response.
The late flash repetitions have now been inspected; R2 is a numerical revision
of the same experiment, not a new independent biological validation cohort.
Original author stationary-fit cohort overlap and retrospective motion limits
also remain. No extra biological data is opened.
