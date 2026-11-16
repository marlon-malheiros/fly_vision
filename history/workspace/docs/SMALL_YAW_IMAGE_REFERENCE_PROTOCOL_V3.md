# Finer-sampled image-only small-yaw reference V3

25 October 2026. Continue the user-authorized goal after a specific violated
prediction, preserving V1/V2 and their original rules. All 792 V2 neural
temporal mean checks pass. The four V2 image references fail their 0.2°/s
spatial diagnostic at 1° versus 0.5° images; differences reach 0.762°/s.
Both median controls change by 0.237–0.312°/s. This is numerical evidence
for insufficient sampling in these reference estimators, not a biological
defect or evidence that simply changing a neural gain would repair yaw.
No V2 held-out detection score has been inspected when this follow-up is
specified. V2's complete neural test proceeds and is retained separately.

Implement the **same four fixed image algorithms** from V2 at 0.5° angular
sampling, with a separate 0.25° spatial check and 2.5-ms temporal check.
Keep the 0.2°/s tolerance. Do not change windows, derivative order, physical
LK support (±2°), geometric assumptions, plane model, median weights, gains
or cutoff criterion. No neural model is added or retuned. Finer input
sampling is an engineering reference and does not establish a fly's optical
acceptance angle or improve the frozen neural circuit by itself.

For efficiency render h=[-64,64], elevation=[-52,52], retaining the exact
physical estimator support h=[-60,60), elevation=[-48,48). The four-degree
margin covers derivatives/filtering. Ray tracing is pointwise, so this
pruning must reproduce the matching crop of the full 0.5° controls within
1e-7 luminance and 1e-8°/s mean-estimate discrepancy. Retain lossless cropped
images and maps. Process only frames [0.69,1.40] needed for the original
mean [0.70,1.40), keeping estimate timestamps every 10 ms at 0.70…1.39.
The prescribed 2-s SE(2) trajectory, motion interval, eye geometry, textures
and origins are unchanged. This skips unused frames rather than changing
the observed motion. Centered derivatives remain an offline calculation.

Use the same sixteen development/calibration worlds as V2, three straight
walking speeds, 48 calibration episodes. No gain/bias or nuisance predictor
is learned from them; choose only the original maximum-absolute-straight
cutoff. Freeze cutoffs, code, sampling and criterion before generating
fresh tests. Use **24 new rooms**, IDs u00–u23 and seeds 202610252000 onward,
disjoint from every V2 scene. Each receives three speeds ×yaw0/±2/±5 plus
stationary control: 384 test episodes. Primary total is432 episodes.
Known s07 fast0/±2 controls at primary/fine-time/fine-space add nine cases.

Numerical criteria: each algorithm's mean yaw changes by at most0.2°/s on
all three s07 fast controls under temporal and spatial refinement. Report
every method and failure; a failed algorithm cannot support a reliable
detector claim. Reuse the old full0.5° controls only for crop identity checks.
Do not continue refining resolution on fresh test outcomes. If this level
fails, report that failure before choosing another independently versioned
implementation and unused test set.

Retain the original reliability rule: ≥80% ±2°/s detection, ≥80% raw-sign
accuracy (including every turn independently of detection), ≤10% observed
straight false alarms, and qualification also at±5°/s. For24rooms each
speed has48signed turn cases/magnitude and24straight cases. Report counts,
undefined estimates, conditional RMSE and finite-sample Wilson intervals
for the24independent straight-room controls. Resample rooms (both signed
turns together),10000draws,seed202610252337, for descriptive detection/sign
intervals; do not count two signs in one room as independent animals.
Retain resampling indices and every interval draw;
these are scene tests, not physiological sensitivity or population bounds.
No same-room straight test partner may enter a turn's estimate. Show all
four methods without selecting a favorable test result as a biological model.

A numerically passing engineering reference that meets the±2 criterion at
all three speeds is a material implemented capability toward the small-turn
goal. It is **not** a repaired MaleCNS model, an interpretation of bIPS,
proof that the original1° neural inputs retain sufficient information, a
calibrated biological threshold or a closed-loop controller. The extra
retinal samples are an explicit information difference from the frozen
neural study. Preserve the distinction in the final beginner explanation.

Use existing CPU software/datasets only. Version code/protocol, retain all
inputs/outputs/failures, independently verify geometry, scores/cutoffs and
numerical gates, produce figures/report/reproduction instructions, append
dated project progress, save a dated copy and seal with live progress and
AGENTS.md outside the artifact index.
