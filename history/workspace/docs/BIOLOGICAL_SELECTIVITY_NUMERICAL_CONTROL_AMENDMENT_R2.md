# Fixed-waveform numerical control correction R2

27 October 2026, after the original numerical preflight and before observation
calibration or main biological outcomes. The failed original comparison remains
saved, with maximum wide-field difference 5.0348701128992944e-5 at 9.06 s.
No acceptance tolerance is changed and no production source is edited.

Inspection of the unchanged streaming C++ kernel identifies the mismatch:
it holds the previous input through the source interval except for its last
solver step. That last step evaluates previous, midpoint and next input at RK4
stages. Refining 1 ms to 0.5 ms therefore shortens the input ramp as well as the
integration step. It is not convergence on the same time-varying forcing.

Create an isolated numerical-reference kernel that expresses this ramp with
the **fixed original 1-ms width**, independently of integration step. The
production 1-ms solver, graph, frontend, source sequence and all neural
parameters remain unchanged. No biological ramp duration is inferred: this
only makes the inherited numerical forcing convention explicit.

Freeze reference source before executing it. Require a 1-ms reference replay
to match all production source and wide-field trajectories exactly. Then
compare 0.5-ms and 0.25-ms reference steps with that same fixed 1-ms ramp.
Retain the original 1e-7 maximum wide-field tolerance for each comparison.
This corrects the control's input matching; it does not erase the original
failure or claim that a different input interpolation is biologically valid.

Complete the existing batch/streaming frontend check, which the original
assertion prevented from running. Keep original raster and quadrature
differences as descriptive sensitivity, without a new acceptance floor.
Proceed to the original main study only if the corrected matched-input checks
pass. If they fail, retain the failure and report the primary experiment as
numerically unresolved; do not relax its tolerance or tune neural parameters.
