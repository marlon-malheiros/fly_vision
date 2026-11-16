# Mi1 calcium benchmark V1 — prospective component test

Frozen before inspecting response curves or amplitudes, 2026-11-05. Follow the
existing C2/C3 metadata split unchanged: six control/four C2-silenced development
flies, three control/three silenced reserved flies. MATLAB loading necessarily
reads complete files into memory; development code accesses fluorescence only
after checking the animal partition. No holdout scoring until calibration locks.
Known paper-level qualitative findings have been read; this is a quantitatively
reserved-animal test, not an unseen biological hypothesis.

## Question and fixed candidates

Does the existing measured Mi1 branch predict independent Mi1 calcium flash
responses? Primary: Gonzalez-Suarez 2022 Mi1 kernel, source-deconvolved with
250 ms assumption, existing Laguerre smoothing/PCHIP port, causal convolution,
existing branch half-wave rectification, then a linear first-order 250 ms calcium
observer. Spatial blur has unit gain for uniform fields. The observer is an
explicit small-signal approximation, not an identified GCaMP6f transfer function.
Do not deconvolve the source kernel a second time.

Predeclared secondary diagnostics: source kernels deconvolved at 200/300 ms with
matched 200/300 ms observers; signed 250 ms branch without rectification; and the
existing fixed 54 ms Mi1 low-pass surrogate with 250 ms observer. No candidate
selection or rescue of primary acceptance using secondary results. No new C2
wiring or efficacy parameters. Measured intact kernels already include network
feedback; adding invented feedback risks double counting.

## Stimulus, preprocessing and calibration

Use logged binary `istim` at 10 Hz, piecewise constant between samples; no image
movies needed for this spatially uniform component test. Causal zero initial
states, 1/240 s integration, observed at logged sample instants. Original absolute
brightness/retinal coverage is not recoverable, so this is temporal contrast
matching rather than exact photometric reproduction. For each ROI normalize
`idSignal1` by its complete-trace mean and subtract one, as the authors do.
Align every eligible falling edge and average the following 130 samples
(0–12.9 s). Match the authors' strict end-of-trace exclusion exactly. Fixed 130
comes from metadata (100-sample cycle x 1.3), not response optimization. Center
each model's complete predicted trace before identical epoch averaging. Do not
subtract an extra epoch-specific baseline, detrend, shift latency or fit offsets.

All available ROIs enter the primary analysis; average within animal first,
then weight animals equally. Only nonfinite data, zero fluorescence means or
missing eligible epochs cause a declared execution failure, not silent exclusion.
For each candidate fit ONE nonnegative gain on the six control development
animal means by least squares over all 130 samples. No other fitting. C2
development and holdout use this same intact prediction/gain as a transfer
challenge, NOT a simulation of C2 silencing. Reserve all six test animals until
calibration JSON and hashes are written. No refitting after test inspection.

## Scoring and decision, fixed before outcomes

Primary score is animal-weighted pooled skill = 1 - sum(MSE)/sum(mean(y^2)),
against the zero dF/F prediction; report per-animal skills, pooled RMSE,
correlation and ON/OFF window errors. Report mean and median per-animal skills
but do not use their potentially unstable mean as the primary statistic.
Windows: OFF 0–5 s, ON 5–10 s, OFF 10–13 s (logged transitions may vary slightly).
No response-amplitude exclusions. Secondary author-like Q>0.5 ROI selection
is disclosed as target-dependent sensitivity analysis, never the primary test.
Summarize ON peak (5–7 s), plateau (9–10 s), and OFF (3–5 s) descriptively.

Limited intact-component acceptance requires ALL: primary pooled holdout skill
>0; all three control holdout animal skills >0; pooled control holdout MSE less
than the separately development-calibrated fixed 54 ms baseline; numerical checks
pass. Report exact leave-one-test-animal-out pooled skill range and all animal
values; n=3 is insufficient for broad population certainty. No arbitrary target
error cutoff is claimed to represent physiological validity. Passing means only
successful transfer on this experiment under this observation model. Failure
does not identify whether the kernel, rectification, observer or stimulus mismatch
is biologically responsible. Neither outcome validates MaleCNS, yaw or C2 mechanisms.

## Verification, preservation and budget

Before outcomes: synthetic alignment/no-leakage/gain checks. After evaluation:
compare Python epoch extraction to original MATLAB helper in Octave (only a
filename/function-name compatibility copy); independent direct convolution and
explicit observer recurrence; 1/480 s refinement on first ROI per animal with
fixed gains, relative epoch RMS <=2% for every candidate. Verify old C2/C3 and
factorial artifact indexes unchanged. Preserve failures, do not tune after failure.
One CPU worker, <=600 CPU seconds, <=16 MiB new outputs, >=20 GiB free reserve.
Reference existing recordings/kernels by SHA256 rather than duplicating them.
Save all animal/ROI predictions, coefficients, selection flags, metrics and
figures. Append live progress, copy dated progress/report/code into the completed
study, and seal only after scientific/report writers exit. Live AGENTS/progress
remain outside immutable indexes. Report numerical checks separately from
physiological agreement. No walking/graph changes or closed-loop control.
