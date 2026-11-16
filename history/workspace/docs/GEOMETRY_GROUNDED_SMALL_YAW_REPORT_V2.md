# Published direction fields and frozen MaleCNS small-turn detection V2

25 October 2026. **The published position-dependent direction-field
projection does not repair small-turn detection in this frozen neural
model.** All original graphs, parameters and sealed evidence are preserved.
The independent endpoint/fit/decision/bootstrap review passes; computational
reproducibility is separate from physiological validity.

## What changed, and what was frozen

Compare the unchanged functional baseline with two separate input versions:
published T4 directions only; and the same field transferred to T5 as an
explicit, less-constrained hypothesis. Source coordinates, identities,
polarity, temporal filters, spatial pooling, MaleCNS weights and neural
parameters do not change. The field is the deposited unsmoothed778-location
anatomical prediction from [Zhao et al. (2025)](https://www.nature.com/articles/s41586-025-09276-5).
Nearest-ray registration and parallel transport are cross-specimen modeling
assumptions; a linear projection of functional HRC fields is not a new
biophysical upstream reconstruction. Median nearest distance1.85°,95th
percentile4.70°,maximum16.96°;153/13,579sources exceed10°.

[Original protocol](GEOMETRY_GROUNDED_SMALL_YAW_PROTOCOL_V1.md),
[V2 amendment](GEOMETRY_GROUNDED_SMALL_YAW_AMENDMENT_V2.md),
[pre-outcome identities](../results/geometry_grounded_small_yaw_v2/before_v2_outcomes.json).
Prospective checkpoints are c2df8dc/78b705a; readouts are fixed before test
generation at8376261. V1's20known pilots and64H2inputs are preserved;
its planned704-episode main study was superseded before execution.

## Executed walking study

Completed704episodes: four known training rooms, sixteen calibration rooms
(four known+twelve new),24unused held-out rooms. Each room has three speeds
5.5/11/16.5mm/s ×yaw0/±2/±5°/s, plus stationary control. The1°retinal grid
and original2-s trajectory/motion epoch remain. Observation is the mean
over[0.70,1.40). Reuse120identical old primary baseline traces/inputs;
record reuse hashes. Allthree neural versions receive identical retinal
movies; source arrays,14-wide-cell traces and final states are retained.
No neural parameter is fitted.

Fit the existing two-feature left/right class decoder with ridge0.001 on
four training rooms only; set its cutoff to the maximum absolute straight
score in sixteen calibration rooms. There are36neural readouts and12image
cutoffs. None uses a held-out label for fitting or cutoff choice. All704
episodes finish without execution failures; development and held-out stages
take1003.7s and1515.5s, respectively (stage completion receipts).
[Execution](../results/geometry_grounded_small_yaw_v2/held_out_complete.json),
[readout freeze](../results/geometry_grounded_small_yaw_v2/readouts/before_test.json).

## Held-out DNp15 at±2°/s

Each speed has48signed turn cases and24straight controls. Raw sign is
sign(score) over every turn, including nondetections. The original rule
requires≥80%detection,≥80%raw-sign accuracy and≤10%observed false alarms,
with qualification also at the larger tested magnitude5°/s.

| Input version | Speed mm/s | Detected /48 | Correct raw sign /48 | False alarms /24 |
|---|---:|---:|---:|---:|
| Original | 5.5 | 21 | 42 | 2 |
| Original | 11 | 6 | 32 | 2 |
| Original | 16.5 | 5 | 28 | 1 |
| T4 field | 5.5 | 21 | 42 | 2 |
| T4 field | 11 | 6 | 32 | 1 |
| T4 field | 16.5 | 5 | 28 | 1 |
| T4/T5 hypothesis | 5.5 | 20 | 42 | 2 |
| T4/T5 hypothesis | 11 | 7 | 30 | 1 |
| T4/T5 hypothesis | 16.5 | 5 | 27 | 1 |

No version qualifies at2°/s; none has a qualifying2°/s threshold in HS,H2
or bIPS either. DNp15 qualifies at5°/s only at slow walking on this limited
2/5°/s grid. Faster grid thresholds remain unresolved. These results do not
replace the earlier larger-yaw sweeps or constitute biological thresholds.
At fast walking, neither field version improves detection even one case;
the T4/T5 hypothesis loses one raw-sign case. Paired room bootstrap preserves
all10000draws/48effects; no≥20-point fast improvement occurs.
[Every class/condition/threshold](../results/geometry_grounded_small_yaw_v2/analysis/test_detection_curves.json),
[paired effects](../results/geometry_grounded_small_yaw_v2/analysis/paired_effects.json).

## External H2 diagnostic remains a negative result

The two previously inspected upper-patch cells are diagnostics, not fresh
physiological validation. Use all bright/dark directions and the original
source-derived observation windows. No model variant is selected from these
errors.

| H2 cell | Original PD error | T4-only field | T4/T5 hypothesis |
|---|---:|---:|---:|
| 2 | 66.14° | 68.60° | 63.38° |
| 4 | 28.85° | 34.93° | 27.80° |

The field alone is insufficient in this projection/registration/renderer
approximation. This does not contradict the paper's eye-map result or
identify a unique erroneous connection. Exact pattern arrays, individual
eye geometry, physiological dynamics and electrical coupling remain unresolved.
[All signed H2 curves](../results/geometry_grounded_small_yaw_v2/analysis/h2_metrics.json).

## Numerical checks and image-reference limits

All792individual/class mean comparisons pass the fixed5%-with1e-5-floor
temporal criterion. The twenty known pilot movies and64H2movies reproduce
the original baseline source arrays exactly. Synthetic/cardinal controls
pass; two new-source strict/accelerated/original-Python comparisons differ
by at most8.67e-19against a1e-12criterion. Source/neural parameters remain
unchanged. The activation polynomial is an existing numerical acceleration,
with exact libm fallback outside its fixed small-state range.

The coarse image-only median references look promising on these24rooms,
but all four methods fail their independently frozen1°versus0.5°spatial
criterion.49/60reference checks pass; spatial changes reach0.762°/s.
These point classifications cannot support a resolution-stable detector
claim. Preserve every failure. A separate [finer-sampled reference
study](SMALL_YAW_IMAGE_REFERENCE_REPORT_V3.md) follows this specific failure.
[Numerical review](../results/geometry_grounded_small_yaw_v2/numerical_review.json).

Independent reconstruction checks11264feature rows,48readouts,5760test
predictions,96curves,48thresholds and every paired bootstrap draw. Maximum
feature discrepancy3.55e-15; coefficient1.53e-14; cutoff2.31e-14; score
3.55e-15; bootstrap0. A pre-test fixture caught unsupported NumPy Boolean
JSON serialization; the versioned wrapper converts scalars without changing
any scientific formula. No scoring failure or relaxed scientific gate is
claimed. [Independent review](../results/geometry_grounded_small_yaw_v2/independent_review.json),
[fixture](../results/geometry_grounded_small_yaw_v2/pretest_serialization_check.json).

## Interpretation and reproducibility

Control of false alarms alone is insufficient: the original fast DNp15
readout misses43/48turns and has only28/48correct raw signs. The observed
direction-field revisions do not solve that problem. No new bIPS lesion,
causal biological conclusion, conductance, neuron or closed-loop controller
is introduced. Missing uLPTCrns/H2rns physiology, electrical interactions,
retinal optics and measurement calibration remain. The recurrent mechanisms
of [Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9)
are not validated by this negative projection experiment.

Fresh-build exact subset replay and reproduction scope are documented in
[reproduction instructions](SMALL_TURN_IMPLEMENTATION_REPRODUCTION_V1.md).
No second full704-episode replay is claimed. All source/neural arrays,
movies, controls, negative outcomes and indexes are preserved. Live progress
and AGENTS.md remain outside immutable indexes, with dated progress copies
inside completed studies.

[Detection/false-alarm figure](../results/geometry_grounded_small_yaw_v2/figures/small_turn_counts_and_false_alarms_v2.png),
[curves](../results/geometry_grounded_small_yaw_v2/figures/held_out_detection_v2.png),
[H2 comparison](../results/geometry_grounded_small_yaw_v2/figures/h2_external_direction_field_comparison_v2.png).
Matching PDFs and the image-estimate figure are retained.

## Undergraduate explanation: what we did, what we want, and why

We want the brain model to notice small turns while the fly walks forward.
We gave it motion directions informed by a real eye map, but that change
did not make its turn decisions reliable. This is useful because it rules
out that simple change as a sufficient fix. We now need better evidence
about how visual motion is represented and combined, while keeping a
separate image-based reference to measure what a working detector should do.
