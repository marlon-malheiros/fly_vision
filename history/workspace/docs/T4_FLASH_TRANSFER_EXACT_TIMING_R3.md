# Recorded-pulse timing correction R3

2026-11-06. Preserve V1/R2, including their positive flash scores and stopped
motion decisions. Warm initialization repairs the~0.0101mV baseline difference,
but R2 still fails2/4 image/template checks(max0.008670mV). Metadata exposes
nominal-versus-recorded pulse durations: the four controls last20036,160016,
19998,160056us. No neural parameter or acceptance limit is changed.

Freeze this finite numerical refinement before R3 outcomes. For each nominal
dwell, derive the minimum, nominal and maximum logged bright-pulse duration
over **all** preselected flash trials, using timestamps only. For each nonempty
11-channel source pattern, simulate those three warm-start pulse durations
through the unchanged cable:300ms grey history, pulse,820ms stop,0.1ms solver,
1ms recordings. Empty input stays zero. Evaluate each actual trial's duration
by piecewise-linear interpolation between its two bracketing duration anchors.
No extrapolation; the exact metadata bounds cover every admitted trial.

This interpolation approximates the forward response as a function of tiny
display-duration jitter; it is not summing different spatial input channels,
altering dynamics or fitting voltage outcomes. Average the corresponding
predictions over the first three repetitions for calibration and last two for
repeat testing. Use the first calibration trial's duration for the numerical
controls. The same5×51 registration grid, analytic nonnegative gain, data
split, references, bootstrap and thresholds remain unchanged. Fit only flashes.

Retain the same0.005mV actual-image parity guard. Also directly simulate each
midpoint of the lower/nominal and nominal/upper duration intervals for native
positions0,+2 and nominal20,160ms(8 controls); compare the interpolated waveform
at the same1ms output times, tolerance0.005mV. These are numerical checks on
known input, not biological test data. Only valid numerical transport permits
retrospective motion simulation. Motion still uses the full actual recorded
frame-event stream, not this stationary-duration interpolation.

R3 outputs stay in `recorded_timing_r3/`; no raw file is duplicated. Full exact
per-trial/per-offset simulation would require2469 unique pulse inputs and about
38MB of1ms trace arrays before compression; this bounded anchor interpolation
is the resource-conscious alternative, with explicit error checks. Same256MiB
study cap/20GiB reserve/1200 child-CPU-second limits. Record resource estimates
and every failure. Late flash responses are inspected from V1/R2, so this is
the same experiment's numerical revision, never a fresh independent validation.
