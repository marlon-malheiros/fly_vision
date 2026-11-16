# Finer image sampling: stable yaw estimates, failed alarm policy V3

25 October 2026. **The finer image estimators pass their numerical checks,
but none meets the declared small-turn reliability rule at all three
walking speeds.** This completed negative result is preserved. It is
separate from the [frozen neural comparison](GEOMETRY_GROUNDED_SMALL_YAW_REPORT_V2.md)
and the later [prospective decision-policy study](SMALL_TURN_TARGET_DECISION_REPORT_V4.md).

## Purpose and methods

V2's image references failed spatial refinement at 1° sampling. V3 keeps
the same four algorithms and the same 0.2°/s numerical tolerance, using
0.5° images with 0.25° spatial and 2.5-ms temporal controls. It changes no
MaleCNS graph, neural parameter, frontend gain, estimator gain or bias.
The extra image samples are an information difference from the original
1° neural input; this is an engineering reference, not a neural repair.
[Frozen protocol](SMALL_YAW_IMAGE_REFERENCE_PROTOCOL_V3.md),
[pre-outcome identities](../results/small_yaw_image_reference_v3/before_predictions.json).
Prospective source checkpoints: b967430 and e483e5a.

The LK method estimates local angular image motion, then eliminates the
forward-translation depth contribution using the known eye geometry. The
subspace method eliminates three local-plane depth coefficients from
brightness-constancy equations before solving for yaw. Preserve their
original means and the previously specified weighted medians. Local
gradient conditioning and geometric information determine the weights;
there is no fitted gain, bias or nuisance predictor.

These controls draw on [Lucas and Kanade (1981)](https://publications.ri.cmu.edu/an-iterative-image-registration-technique-with-an-application-to-stereo-vision-ijcai)
and motion/depth separation such as [Heeger and Jepson (1992)](https://www.cns.nyu.edu/heegerlab/index.php?id=heeger-ijcv92&page=publications).
Our restricted local-plane yaw implementation is not a reproduction of
those authors' software. It assumes a stationary world, body-forward
translation and yaw-only rotation. Images, timestamps and fixed eye
geometry enter the estimator; true speed/yaw, depth, surfaces, body pose
and a same-room straight test partner do not.

Retain the exact estimator support h=[−60,60), elevation=[−48,48), with
four-degree rendering margins. Process the frames needed for the original
70 estimates at 0.70,0.71,…,1.39 s. Average those estimates over the same
observation interval. Centered derivatives require 10 ms of future data;
this is offline processing, not a demonstrated real-time controller.

## Executed study and frozen decisions

Completed 48 straight calibration episodes in sixteen development rooms,
384 test episodes in 24 additional unused rooms u00–u23, and nine known
numerical controls. Each test room has three speeds (5.5,11,16.5 mm/s)
times yaw 0/±2/±5°/s, plus a stationary control: sixteen conditions.
New seeds start at 202610252000 and are disjoint from V2. Tests ran in
535.2 s with zero execution failures.

Freeze twelve cutoffs before test-image generation: for each method/speed,
the maximum absolute straight estimate in the sixteen calibration rooms.
No test label enters fitting. Qualification requires ≥80% turn detection,
≥80% raw-sign accuracy over all turns including nondetections, and ≤10%
observed straight false alarms, with qualification also at ±5°/s.
[Cutoff freeze](../results/small_yaw_image_reference_v3/before_test.json),
[execution](../results/small_yaw_image_reference_v3/held_out_complete.json).

## All methods at ±2°/s

Each entry lists counts at speeds 5.5 /11 /16.5 mm/s, in that order.
There are 48 signed turn cases and 24 straight controls per speed.

| Method | Detected /48 | Correct raw sign /48 | Straight false alarms /24 |
|---|---|---|---|
| LK mean | 26 /3 /5 | 47 /45 /45 | 1 /0 /1 |
| Subspace mean | 48 /48 /48 | 48 /48 /48 | 3 /4 /4 |
| LK median | 48 /48 /48 | 48 /48 /48 | 8 /5 /6 |
| Subspace median | 48 /48 /48 | 48 /48 /48 | 4 /4 /3 |

The median references estimate small rotations accurately, but their
cutoffs are sufficiently close to zero that small residual straight-motion
errors trigger alarms. LK-median ±2°/s RMSE is 0.068/0.102/0.134°/s;
subspace-median RMSE is 0.163/0.233/0.314°/s. Accurate signs and estimates
do not rescue a failed declared alarm policy. No reliable all-speed
±2°/s detector is established by V3.
[Every curve, RMSE and undefined count](../results/small_yaw_image_reference_v3/analysis/curves.json),
[finite-grid thresholds](../results/small_yaw_image_reference_v3/analysis/thresholds.json),
[figure](../results/small_yaw_image_reference_v3/figures/failed_calibration_policy_v3.png).
Scalar CSV copies accompany the authoritative JSON, including all failures.

## Numerical verification and uncertainty

All 24 temporal/spatial method comparisons pass the unchanged 0.2°/s
criterion on the three fixed fast-walking controls (straight,−2,+2°/s).
All crop checks pass: luminance matches exactly and largest mean-estimate
discrepancy is 2.71e−11°/s against a 1e−8 tolerance. This supports numerical
stability on these controls, not a uniform error bound over all rooms.
[Complete numerical review](../results/small_yaw_image_reference_v3/numerical_review.json).

Independent reconstruction verifies all 432 primary episodes, twelve
cutoffs,1536 predictions,24 curves,twelve thresholds and all 10000 room
bootstrap draws. Maximum score discrepancy is 2.67e−15°/s, bootstrap
discrepancy zero. Both signs of a turn stay together when resampling a
room. Wilson intervals use the 24 independent straight-room controls;
repeated speeds and signs are not independent animals.
[Independent review](../results/small_yaw_image_reference_v3/independent_review.json),
[intervals](../results/small_yaw_image_reference_v3/analysis/intervals.json).

Four predetermined fresh source-build replays, including fine-time and
quarter-degree controls, reproduce all retained arrays exactly. No second
full 432-episode replay is claimed.
[Replay receipt](../results/small_turn_reproduction_image_v3/complete.json),
[reproduction instructions](SMALL_TURN_IMPLEMENTATION_REPRODUCTION_V1.md).

## Interpretation and limitations

This failure localizes an engineering issue: the tested continuous
estimates can contain small-turn information while a particular alarm
policy does not generalize. It does not identify the cause of the original
neural circuit's failure. The new policy motivated by this result is
separately frozen and tested on new rooms in V4; V3 remains a failure under
its own rule. There is no threshold search followed by relabeling the
same test rooms as validation.

The scenes are noiseless and generated by one family of textured 3D
environments. Optical blur, sensor noise, natural head motion, pitch/roll,
free translation direction and behavioral detection latency are untested.
No new bIPS lesion or biological-causality inference occurs. This image
control cannot validate the recurrent physiology of
[Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9)
or supply missing electrical coupling, uLPTCrns or H2rns constraints.

## Undergraduate explanation: what we did, what we want, and why

We want to notice a small turn during forward walking without constantly
raising false alarms. We increased image detail and checked that the
estimated turn rate stopped changing much with numerical resolution.
The estimates improved, but the old alarm rule still confused tiny
straight-walking errors with turns. That tells us to test the decision
rule separately, while keeping the brain-model problem unresolved.
