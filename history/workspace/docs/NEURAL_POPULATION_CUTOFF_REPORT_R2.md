# Neural population cutoff calibration R2

31 October 2026. Completed paired computational extension.

**Outcome:** No cutoff/readout combination passes all behavioral and numerical requirements.

[Protocol](NEURAL_POPULATION_CUTOFF_PROTOCOL_R2.md), [before-test freeze](../results/neural_population_cutoff_r2/before_test.json), [all 60 curves](../results/neural_population_cutoff_r2/test_curves.csv), [independent review](../results/neural_population_cutoff_r2/review.json).

V1 calibration exposed false alarms. Before fresh test images, R2 freezes two negative-control-only calibration rules on the unchanged five neural scores. The 90th-percentile rule uses each room’s maximum absolute score over the full two-second monitoring interval, separately for stationary and each walking speed, then takes the largest group cutoff. The maximum rule is more conservative. Both retain a minimum cutoff of 1. No positive yaw trial chooses either cutoff; V1 positive calibration outcomes were already known and are not presented as blind validation. No coefficient, neural parameter, image input or original result changes. The primary is episode90/individual_linear.

Its global cutoff is 1.621939123; the maximum-control alternative is 2.337116268. The 24 new rooms / 384 trajectories are shared with V1: this is a paired comparison, not a second independent environment sample. Keep ≥39/48 joint detections, ≥20/24 each sign, and ≤2/24 endpoint/any straight and stationary alarms at both magnitudes and all speeds. Numerical score tolerance stays 0.2 in original score units with all 81 endpoint/any-alarm stability checks.

| Individual-neuron rule | Speed mm/s | ±2 joint /48 | −/+ /24 | Straight any /24 | ±5 joint /48 | Numerics pass? |
|---|---:|---:|---:|---:|---:|---|
| episode90/individual_linear | 5.5 | 48 | 24/24 | 0 | 48 | False |
| episode90/individual_linear | 11 | 42 | 22/20 | 0 | 48 | False |
| episode90/individual_linear | 16.5 | 26 | 13/13 | 0 | 48 | False |
| episode_max/individual_linear | 5.5 | 14 | 6/8 | 0 | 48 | True |
| episode_max/individual_linear | 11 | 8 | 5/3 | 0 | 48 | True |
| episode_max/individual_linear | 16.5 | 2 | 2/0 | 0 | 47 | True |

![Cutoff tradeoff](../results/neural_population_cutoff_r2/cutoff_comparison.png)

What calibration already establishes

The minimum common scalar cutoff that meets every calibration group’s false-alarm limit is 1.621939123. At that cutoff, the fixed individual-neuron score detects/signs only 18/32 fast small turns; 26/32 are required. Every lower cutoff violates a calibration false-alarm bound; every higher cutoff can only remove correct detections. Thus one global scalar cutoff cannot solve the observed calibration problem for this particular frozen score. This finite-data monotonic argument does not establish biological impossibility or exclude a different neural representation/readout.

Independent validation and limitations

Independently reconstructed all 320 negative-control peaks and both cutoff rules without NumPy quantiles. Verified all 810 numerical score differences stay identical to V1; independently recomputed the individual-neuron scores and threshold decisions for both rules across all 81 refinements. All 60 fresh-test curve rows/counts are independently reconstructed. The parent study supplies four exact neural replays and zero stationary full-state checks. Room bootstrap intervals summarize this finite sample; they do not provide a guarantee of population false-alarm rates.

These are external supervised neural readouts from a functional-surrogate/MaleCNS model. No anatomical connection or physiological mechanism was reconstructed, no bIPS benefit was demonstrated, and biological validation remains open. Rotation detection alone does not establish whether a turn was intended. No closed-loop control.

Undergraduate explanation — what we did, what we want, and why

We want simulated neural activity to tell a small turn apart from straight walking. We tried setting a higher alarm threshold using only straight and stationary examples. That reduces false alarms, but it also misses real turns. The saved results show the exact tradeoff. This tells us whether changing the alarm setting is enough for this reader; it does not tell us that real flies cannot solve the task.

Figure review: lines join only the three tested speeds; intermediate speeds were not evaluated. Coincident curves are intentional, and exact counts remain in the CSV tables. In V1 the two DNp15 readouts have identical counts, and the individual/spatial linear readouts share the plotted joint-detection counts. In R2 both raised-cutoff individual-neuron readers have zero observed fresh-room false alarms. PNGs were visually inspected; PDF versions are also preserved.

Supported secondary result at 5°/s — separate from the failed 2°/s target

The predefined secondary `episode_max/individual_linear` reader, with its cutoff 2.337116267814088 frozen from negative controls before test images, meets all declared behavioral criteria at ±5°/s: 48/48, 48/48 and 47/48 joint detections at 5.5/11/16.5 mm/s, with 0/24 endpoint and any-episode straight alarms at every speed and 0/24 stationary alarms. These are observed finite-sample counts, not population reliability guarantees. The primary `episode90` reader and the original all-magnitude target remain failed.

The already inspected ±5 behavior motivated a [separately frozen numerical addendum](NEURAL_POPULATION_FIVE_DEGREE_NUMERICS_ADDENDUM_V1.md). All 54 added ±5 comparisons pass the unchanged 0.2 score tolerance and endpoint-decision rule; maximum added discrepancy 0.1777535, independently reconstructed within 2.58e-14. Combined with its 81 previous 0/±2 checks, this reader passes all 135 declared comparisons. [Complete five-degree review](../results/neural_population_cutoff_r2/five_degree_numerics_v1/review.json), [all added comparisons](../results/neural_population_cutoff_r2/five_degree_numerics_v1/comparisons.csv).

This supports a bounded neural-only computational readout at the larger tested rate of 5°/s. It is a supervised linear observer of 45 frozen simulated neurons; it does not replace the connectome or use the image estimator. The HRC frontend remains a functional surrogate, the reader is not an anatomically identified downstream neuron, and physiological validation/bIPS-specific advantage remain unestablished. The model still fails the original 2°/s objective: this conservative reader detects/signs only 14/48, 8/48 and 2/48 small turns across speeds. No intermediate yaw rate was tested, so the exact detection threshold is unknown. This is a secondary outcome in the shared 24 test rooms, requiring independent confirmation before stronger generalization claims.

The follow-up execution was interrupted with SIGTERM after 35 complete cases; cause unestablished. All complete cases were verified/reused, six incomplete directories and the original log were preserved, and the identical frozen recipe completed all 72 cases on continuation. [Interruption record](../results/neural_population_cutoff_r2/five_degree_numerics_v1/failures/session_termination_v1/termination.json). No cutoff, coefficient or tolerance changed.

A post-test descriptive check of training data gives 48/48 ±5 detections and 0/24 straight alarms at each speed for this reader. It is training performance, not additional validation. [Training diagnostic](../results/neural_population_cutoff_r2/training_only_diagnostic.json).
