# Unscored speed-condition diagnostic — V1

Specified 2026-10-21 before fluorescence extraction/scoring of the audited
six-second speed-tuning sessions. This is a new-stimulus-condition diagnostic,
not a claim that all participating flies are previously unseen.

Use all 45 metadata-eligible native/WT pure-yaw sessions, with author ROI choices,
actual TimeAxis and recorded CW/CCW flags. Reuse the 13-s whole-fly calibration/
test assignments and separate reporter/background cohorts. Observation filter/
gain parameters come exclusively from the completed, prospectively specified
13-s coordinate-corrected diagnostics; no speed-tuning response may change them.
Report stimulus generalization on calibration flies separately from testing on
the existing held-out-fly partition. These animals' 13-s responses were already
inspected; only the six-second condition is newly scored.

Retain all nominal speeds (5.625, 11.25, 22.5, 45, 90, 180, 360, 720 degrees/s)
in the extracted measurement ledger. Numerical prediction is restricted in
advance to the first five: scaling the existing 45-degree/s, magnitude-0.5 proxy
linearly gives magnitudes at most one. The other three exceed the inherited
normalized clamp contract and remain unsupported. Do not clip or retune gains
to create high-speed predictions.

The world-azimuth meaning of the author CW/CCW flag is unresolved. Evaluate both
global alternatives: CW=positive and CW=negative, with CCW opposite. Do not pick
an orientation from fluorescence agreement or select it independently per fly.
Save errors for both hypotheses and the resulting error range. A best-case error
is a lower bound under an unresolved convention, not evidence of validation.

For both predetermined corrected proxies, both circuits and both world directions,
use the original 1-ms solver/10-ms input clock over [0,6] s, with motion over [2,4).
Keep neural graphs/gains unchanged. Calibrate nothing on this condition. Recorded
trial/ROI normalization remains the measured 1–2-s baseline rule with the same
finite-coverage and minimum-trial criteria as the 13-s benchmark.

Report complete trace and motion-window errors, last-0.5-s motion response,
fly-level uncertainty and explicit unsupported/missing-cohort counts. Retain
all measured high-speed responses without modeling them. Both signed and
rectified analytic proxies bypass the image frontend and lack its temporal/
contrast/frequency response. Therefore this study can expose proxy failures;
it cannot validate the complete image-to-calcium model or assign a unique
biological cause to mismatches. Exact display frames/refresh and source-specific
measurement constraints remain open gates.
