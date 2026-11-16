# Small-turn implementation milestone V4

25 October 2026. **A separate image-based reference now detects the tested
±2°/s turns reliably in new simulated rooms. The frozen MaleCNS neural
circuit remains unreliable.** This is a material engineering advance toward
the small-turn goal, with a reproducible reference for future neural work.
It is not physiological validation or completion of the broader PhD goal.

## Main finding

On 24 previously unused rooms, both median methods detect **48/48 signed
±2°/s turns, with 48/48 correct directions and 0/24 straight false alarms
at each speed: 5.5,11 and16.5 mm/s**. Both also detect all48 ±5°/s turns
per speed with correct directions. All methods, failures and prior studies
are retained. Numerical evidence and independent reconstruction pass.

![All four methods and failures](../results/small_turn_target_decision_v4/figures/target_detection_counts_v4.png)

This follows two specific negative results: the published direction-field
projection did not repair the neural detector in [V2](GEOMETRY_GROUNDED_SMALL_YAW_REPORT_V2.md),
and finer, numerically stable image estimates still failed their original
alarm policy in [V3](SMALL_YAW_IMAGE_REFERENCE_REPORT_V3.md). Those completed
results have not been reclassified as successes.

## What changed and why it is a new prospective test

Only an engineering decision rule changes. Given a yaw estimate in °/s,
choose the nearest equal-cost hypothesis among {straight=0, left=−2,
right=+2}, preferring straight on a tie. The assignment's minimum target
2°/s therefore fixes the boundary algebraically at **1°/s**. This is a
declared engineering operating point, not a fitted biological parameter or
an estimate of a fly's sensory threshold. The primary rule needs no walking
speed or calibration sample at inference.

V3's observed failure motivated this policy. Freeze it at source checkpoint
**c5c1ce8**, before producing the V4 test images. Previously inspected rooms
are development evidence. V4 uses 24 fresh rooms w00–w23, seeds
202610253000 onward, disjoint from both V2 and V3. Also apply the unchanged
V3 calibration cutoffs to the identical estimates as a secondary comparison;
do not refit them. No threshold sweep, fitted image gain/bias or neural
parameter adjustment occurs.
[Protocol](SMALL_TURN_TARGET_DECISION_PROTOCOL_V4.md),
[pre-outcome identities](../results/small_turn_target_decision_v4/before_predictions.json),
[pre-test freeze](../results/small_turn_target_decision_v4/before_test.json).

## Image estimator and executed conditions

Keep all four V3 algorithms: local Lucas–Kanade flow followed by forward
depth cancellation, direct local-plane brightness-subspace yaw fitting,
and their weighted-median variants. The approaches build on classical
[local image-motion estimation](https://publications.ri.cmu.edu/an-iterative-image-registration-technique-with-an-application-to-stereo-vision-ijcai)
and [motion/depth separation](https://www.cns.nyu.edu/heegerlab/index.php?id=heeger-ijcv92&page=publications);
our restricted implementation is not an author-code reproduction.

Inputs are binocular luminance sequences, timestamps and fixed eye
geometry. The estimator assumes body-forward translation, yaw-only
rotation and stationary surroundings. It receives no true yaw, speed,
depth, surface labels, body pose or same-room straight partner. Simulator
truth defines the generated trajectory and is used for scoring only.

Retain 0.5° sampling and the exact V3 crop, physical derivative supports,
median weights and 70-estimate mean over [0.70,1.40) s. This has more retinal
samples than the original 1° neural model and a stronger geometric prior.
Centered derivatives use 10 ms of future data. The 0.7-s mean and offline
computation do not establish a fast behavioral response or live deployment.

Execute 384 episodes: 24 rooms ×[three speeds ×yaw0/±2/±5°/s plus stationary
control]. Execution takes 463.1 s with zero failures. Retain all cropped
images, instantaneous estimates, truth labels, scene descriptions and
receipts. The rule's observed reliability requirements remain unchanged:
≥80% detection,≥80% raw-sign accuracy and≤10% straight false alarms at the
target and larger tested magnitude.
[Execution receipt](../results/small_turn_target_decision_v4/held_out_complete.json).

## Complete ±2°/s comparison

Entries list speeds 5.5 /11 /16.5 mm/s. Denominators are 48 signed turn
cases and 24 straight-room controls per speed. Raw sign includes every
turn independently of detection.

| Fixed-target method | Detected /48 | Correct raw sign /48 | False alarms /24 | Qualifies at all speeds? |
|---|---|---|---|---|
| LK mean | 42 /40 /39 | 46 /46 /45 | 6 /8 /10 | No |
| Subspace mean | 48 /48 /47 | 48 /48 /48 | 0 /1 /1 | Yes |
| LK median | 48 /48 /48 | 48 /48 /48 | 0 /0 /0 | Yes |
| Subspace median | 48 /48 /48 | 48 /48 /48 | 0 /0 /0 | Yes |

At±5°/s every method detects48/48 turns with48/48correct signs per speed;
LK mean still fails its straight false-alarm gate. All estimates are
defined. The smallest tested qualifying magnitude is2°/s for three methods;
the only tested nonzero magnitudes are2and5°/s. Sensitivity below2°/s and
a continuous threshold remain unmeasured.

LK-median ±2°/s RMSE is0.0496/0.0766/0.1010°/s; subspace-median RMSE
is0.1101/0.1338/0.1546°/s. Across straight and±2°/s cases at all speeds,
their smallest observed distances from the1°/s decision boundary are
0.790and0.455°/s. These are descriptive margins in the tested rooms,
not worst-case robustness guarantees.
[Authoritative curves/RMSE](../results/small_turn_target_decision_v4/analysis/curves.json),
[threshold grid](../results/small_turn_target_decision_v4/analysis/thresholds.json),
[estimates and boundary](../results/small_turn_target_decision_v4/figures/continuous_estimates_and_fixed_boundary_v4.png).
Convenience CSV tables omit nested fields retained in the JSON.

## Preserve the failed policy and negative methods

Applying V3's unchanged calibration policy on the same V4 estimates gives:

| Unchanged calibration method | Detected /48 | Correct raw sign /48 | False alarms /24 |
|---|---|---|---|
| LK mean | 26 /2 /4 | 46 /46 /45 | 3 /0 /0 |
| Subspace mean | 48 /48 /48 | 48 /48 /48 | 1 /1 /1 |
| LK median | 48 /48 /48 | 48 /48 /48 | 3 /3 /2 |
| Subspace median | 48 /48 /48 | 48 /48 /48 | 0 /0 /0 |

Some unchanged policies also qualify on this new finite set despite
failing V3. Thus the new policy is not uniquely necessary or guaranteed
to improve every method in every room. For LK median it removes the
observed straight false alarms here without losing±2°/s detections.
LK mean fails under the new rule, exposing estimation errors rather than
an alarm-only problem. Report all four methods and both rules.
[Paired policy figure](../results/small_turn_target_decision_v4/figures/paired_decision_policy_false_alarms_v4.png),
[all decisions](../results/small_turn_target_decision_v4/analysis/predictions.json).

## Numerical checks, independent review and uncertainty

V4 reuses the unchanged V3 estimator's passed numerical evidence with
hashes: all24fixed temporal/spatial comparisons meet the0.2°/s tolerance,
and all crop controls pass. No new full convergence sweep is claimed.
Independent V4 review verifies384input receipts,3072predictions across
both policies,48curves,24thresholds,disjoint scene seeds and10000room
bootstrap draws. Decisions are independently checked by squared distances
to the three hypotheses, including straight-preferring ties. Maximum
score discrepancy is2.67e−15°/s; bootstrap discrepancy iszero.
[Numerical evidence reuse](../results/small_turn_target_decision_v4/numerical_evidence_reuse.json),
[independent review](../results/small_turn_target_decision_v4/independent_review.json).

Four predetermined fresh source-build replays reproduce all retained
images/estimates and all associated scores/decisions exactly. This is a
subset replay, not a second384-episode execution. Numerical reproducibility
is separate from biological validity.
[Replay](../results/small_turn_reproduction_target_v4/complete.json),
[instructions and environment](SMALL_TURN_IMPLEMENTATION_REPRODUCTION_V1.md).

Both signs and all speeds share the same24rooms. Do not count them as
independent animals or pool72straight trials as72independent rooms.
Zero false alarms in24rooms has a95%Wilson upper bound of about13.8%;
the observed≤10%criterion is not a demonstrated population bound.
Room-bootstrap intervals are descriptive. Repeated prospective revisions
after development failures do not establish formal statistical significance.
[Complete intervals/draws](../results/small_turn_target_decision_v4/analysis/intervals.json).

## What changed for the research goal

We now have an implemented reference that recovers the specified small
turns from simulated images under declared geometric assumptions. It
provides an achievable benchmark for the neural model and separates image
estimation from alarm-policy failure. This does not prove that the
original1°neural inputs contain enough information or identify a unique
cause of the neural mismatch.

Original fast DNp15 in V2 detects only5/48±2°/s turns, with28/48correct
raw directions. The T4 field leaves detection unchanged; the T4/T5
hypothesis also detects5/48. No neural repair, new bIPS mechanism or
biological causality is established. The geometry-based computation is
not evidence that the fly implements the same algorithm.

The noiseless same-family rooms do not validate optical blur, sensor
noise, naturalistic head/body motion, pitch/roll, dynamic objects or
arbitrary translation. No physiological measurement model is newly
calibrated; missing electrical interactions and uLPTCrns/H2rns evidence
remain unresolved. The reference does not quantitatively validate
[Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9).
No connectivity or conductance was invented, and no controller or physical
robot was implemented.

The next neural question is whether independently justified visual
encoding and bilateral pooling can retain the rotation information that
the reference uses. Any such revision needs separate evidence, matched
input sampling and fresh held-out tests. The successful reference and
failed neural versions remain available for that comparison.

## Undergraduate explanation: what we did, what we want, and why

We want the fly brain model to notice a small accidental turn while
walking forward. We built a separate image-based measuring tool that now
spots the tested small turns in new virtual rooms without false alarms.
The brain model still misses many of them. This is progress because we
have a working reference to compare against; the next research problem is
to explain how a biologically supported neural circuit could achieve it.
