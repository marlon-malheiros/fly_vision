# Geometry-verification correction V2

24 October 2026. This corrects an independent verification method, not the
renderer, neural model, visual conditions, metric or acceptance tolerance.
The original V1 reviewer remains preserved with its original source identity.

A precheck on four fixed landmarks per eye exposed excessive truncation error
in its two-point central derivative at epsilon=1e-5 s. Near elevation ±86°,
azimuth can change rapidly under translation even during small yaw. Maximum
two-point errors are 5.35804e-5 and 5.35087e-5 rad/s in the checked s07 case,
above the unchanged 1e-5 tolerance. They arise in the numerical derivative
of fixed-landmark projection, not in the analytic flow or rendered images.

The V2 reviewer uses the fourth-order five-point stencil at the **same epsilon**:
[f(t−2h)−8f(t−h)+8f(t+h)−f(t+2h)]/(12h). Its precheck errors are 1.08489e-8
and 1.10057e-8 rad/s. The tolerance and all other review criteria remain fixed.
[Preserved precheck](../results/continuous_yaw_mechanisms_v1/flow_reprojection_precheck_v1.json).

The original scoring controller was already running with a frozen V1 reviewer
path. Its V1 attempt/failure is retained; the corrected review writes to a new
`independent_review_v2` directory and a separate V2 controller records completion.
No original output or failed review is overwritten. Train/calibration/held-out
data and selected readouts are not changed in this correction. The V2 source
and correction record are saved before its execution and before inspection of
probe/normalization outcomes.
