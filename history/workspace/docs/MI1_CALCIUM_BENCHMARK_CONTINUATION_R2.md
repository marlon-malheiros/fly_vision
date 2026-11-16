# Mi1 benchmark R2 — stop before opening reserved responses

2026-11-05. Original scientific freeze: commit `40e4c92`. No original code,
model, coefficient, data, acceptance criterion or result is changed.

## What was inspected before this continuation

Development processing finished for 113 ROIs in ten flies. All five independently
development-calibrated nonnegative gains equal exactly zero. Development mean
curves and per-animal stimulus-correlation selection counts were then inspected.
The development cohort contains both positive and negative stimulus-correlated
responses; individual primary unscaled shape cosines range from approximately
-0.839 to +0.635. These are development observations, not reserved-animal evidence.
The six reserved flies have NOT been processed or scored. Complete MATLAB files
were necessarily loaded in memory, as disclosed in V1, but response access was
restricted by metadata before normalization/scoring.

## Why stop now

For locked gain zero, every prediction is identically zero. Its MSE equals the
zero-baseline MSE on ANY finite test response. Therefore skill cannot be strictly
positive; the similarly zero-gain low-pass baseline cannot be outperformed.
The frozen acceptance rule is already mathematically unattainable. Stop without
processing reserved responses, preserving those flies for a better justified
future experiment. This is an explicit execution-plan deviation, not a relaxed
acceptance threshold or a held-out test result. The V1 test/review/report stages
are not executed because they would unnecessarily process reserved responses.

## Bounded completion

Keep V1 methods, before-execution hashes, raw development arrays and calibration
lock unchanged. Compute development-only error/correlation/selection summaries;
do not fit any new gains or select a winning model. Response-based Q>0.5
sensitivity is descriptive and cannot establish independent validation. Report
the mixture and arbitrary single positive gain as possible measurement/cohort
limitations rather than claiming a unique biological mechanism failed.

Independently verify the source preprocessing in Octave using ONLY development
flyIDs selected before calling the author helper. Check direct convolution and
explicit observer recurrence, plus 240/480 Hz refinement for first ROI per each
of ten development flies (50 candidate cases). Independently recompute scalar
metrics and nonnegative gain algebra. The existing 2% numerical tolerance and
budgets stay unchanged. No reserved response normalization, model fit, selection,
curve, score or feedback reconstruction. Preserve any failures.

Finalize figures, a report explaining the stopped primary result and conditional
next alternatives, resources, live progress and immutable snapshot/seal, with a
separate post-exit integrity check. Preserve old indexes. Do not describe the
113-ROI review as a 177-ROI numerical check or claim all six test animals passed
or failed biologically. This study establishes neither new small-turn performance
nor full biological validation.
