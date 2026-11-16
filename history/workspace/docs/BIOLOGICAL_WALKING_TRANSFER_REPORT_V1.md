# Independent-animal bIPS transfer supplement V1

27 October 2026. Predeclared response-property decision:
**NOT SUPPORTED**.
This is a separate newly scored animal test; the main immobilized-fly experiment
and all of its outcomes remain unchanged.

## New animal evidence

Metadata identified four native bIPS/sytGC7f/axon animals absent from prior
observed-trace analyses and all main calibration/test assignments. Each has a
matching 13-s yaw/translation protocol; three also have unilateral conditions.
Their metadata and source identities were frozen before their response arrays
were read. No parameter was fitted on these animals. The main immobilized-cohort
observation model transfers unchanged, as do every circuit parameter and all
three rendering hypotheses. The original paper and source metadata were already
known: this tests new individual animals, rather than discovering the paper's
reported preference or collecting new experiments ourselves.

| Animal identity (exact genotype / date / fly) | Recorded magnitude index | Primary model index |
|---|---:|---:|
| R25F07AD VT014724DBD sytGC7f 20xUASmCherry / 210819 / 1 | 0.1561 | -0.0436 |
| R25F07AD VT014724DBD sytGC7f 20xUASmCherry / 210828 / 1 | 0.0567 | -0.0435 |
| R25F07AD VT014724DBD sytGC7f / 210330 / 2 | 0.0637 | -0.1658 |
| R25F07AD VT014724DBD sytGC7f / 210401 / 1 | -0.2434 | -0.0436 |

Across 4 paired animals the recorded mean index is
0.0083, with 95% fly-bootstrap interval
[-0.1666208379903097, 0.13127577987137196]. The primary predicted mean is
-0.0741. Positive values indicate stronger translation
than yaw epoch contrast; this is not the paper's signed discrimination index.
The prospective bIPS gate requires the measured interval wholly positive,
model mean inside it and positive model sign across all three hypotheses.
Individual rows retain exact genotype strings, including the two mCherry
coexpression backgrounds; the four-fly aggregate is not a population claim
across all bIPS genetic backgrounds. With two animals per exact genotype,
genotype effects and sampling uncertainty are not separately established.

![Independent animal results](../results/biological_selectivity_benchmark_v1/walking_transfer_v1/figures/independent_bIPS.png)

## Error and stimulus transfer

The gain/filter was learned from other, immobilized flies on bilateral stimuli.
Unilateral conditions were also absent from calibration. Skill compares each
fly's MSE with its own measured zero-response comparator before equal-fly
aggregation. Support requires at least three flies and a lower 95% bound above
zero. Positive skill alone does not validate selectivity or exact waveforms.

The primary model mean is inside the broad measured selectivity interval, so
these four animals alone do not show a resolved selectivity mismatch. They also
do not establish the expected positive preference. Primary bilateral waveform
skill is negative with a wholly negative bootstrap interval; the unchanged
immobilized-cohort measurement fit transfers poorly here. Neither observation
identifies behavioral-state modulation, genotype or a specific missing connection
as the cause. All four animals are now inspected data for future model changes.

| Profile | Conditions | Animals | Mean fly skill | 95% interval | Supported |
|---|---|---:|---:|---|---|
| aligned_100 | bilateral | 4 | -2.6074 | [-4.876456999329905, -0.40395843301179624] | False |
| aligned_100 | unilateral | 3 | -1.2373 | [-3.3698790256207203, 0.26874174874635215] | False |
| aligned_50 | bilateral | 4 | -2.4278 | [-4.643018713240652, -0.3143874699527126] | False |
| aligned_50 | unilateral | 3 | -1.0762 | [-3.0412881881496943, 0.32281830867160655] | False |
| pitched_100 | bilateral | 4 | -0.2772 | [-1.0395530883304362, 0.32343018478663216] | False |
| pitched_100 | unilateral | 3 | -0.0535 | [-0.9236119387116611, 0.4263402755794228] | False |

## Meaning and limits

The source label is `prepType=walking`. This establishes a walking preparation,
not continuous walking during each stimulus, actual forward speed or an
unintended body turn. No behavioral state trace is analyzed here. These are
therefore not matched small-turn walking recordings. New DNp15 animals are
unavailable in this supplement. The two cell groups' joint biological validation
cannot follow from a bIPS-only result.

Exact trial dot arrays, display refresh, head/neurite registration and absolute
photometry remain unresolved. The same approximate stimulus-family assumptions
as the main study apply. A mismatch cannot uniquely identify circuit anatomy,
missing electrical coupling, indicator mapping or behavioral-state modulation
as its cause. No missing connection or physiological parameter was invented,
and neither this dataset nor its outcome changes the engineering hybrid rule.

The independent review re-indexed raw source tensors and checked all 14
trace summaries, predictions, fly contrasts, bootstrap intervals and decisions
with a separate normalization and filter implementation. Maximum arithmetic
discrepancy is 2.13163e-14. Numerical reproducibility is distinct from biological
agreement. All measurements, exclusions, predictions and alternative profiles
are retained in the supplement directory.

[Protocol](BIOLOGICAL_WALKING_TRANSFER_PROTOCOL_V1.md) ·
[Main benchmark](BIOLOGICAL_SELECTIVITY_BENCHMARK_REPORT_V1.md) ·
[Animal/source freeze](../results/biological_selectivity_benchmark_v1/walking_transfer_v1/before_observations.json) ·
[Complete numerical summary](../results/biological_selectivity_benchmark_v1/walking_transfer_v1/summary.json) ·
[Independent review](../results/biological_selectivity_benchmark_v1/walking_transfer_v1/independent_review.json).

## Undergraduate explanation

We found additional recordings from flies that had not been used to fit or test
our model. We used the already fixed model to predict their bIPS responses,
without adjusting it to these animals. This is a stronger biological check than
comparing the model only with familiar examples. It still does not tell us
whether the model detects tiny turns during real walking, because the recording
labels do not provide the required matched movements and small-turn trials.
