# What is acceptable for the small-turn goal?

26 October 2026. **Perfection is unnecessary. We need useful performance,
clear uncertainty and biological claims supported by the appropriate
evidence.** This is a retrospective review of existing evidence, not a
new experiment or a change to any completed study's acceptance criteria.

## The current computational target

The frozen project rule is a practical benchmark, not a published
biological threshold or a universal standard:

| Measure | Existing requirement | In the current sample |
|---|---|---|
| Detect actual turns | At least80% | At least39/48signed turns |
| Recover raw left/right sign over all turns | At least80%, including nondetections | At least39/48correct signs |
| Avoid false alarms during straight walking | At most10% | At most2/24straight-room controls |

For qualification at2°/s, these criteria must pass at every claimed walking
speed and also at the larger tested magnitude5°/s. Tests use unused rooms;
parameters/readouts/cutoffs must be fixed before inspecting their outcomes.
Some errors are allowed. Perfect48/48classification is not required.
[Original yaw protocol](YAW_SENSITIVITY_ABLATION_PROTOCOL_V1.md),
[V4protocol](SMALL_TURN_TARGET_DECISION_PROTOCOL_V4.md).

The target±2°/s denotes angular velocity, not a fixed2°change of heading.
We have not established that2°/s is the fly's biological detection limit.
Changing this target would define another question, not repair an old
failed result.

## What the evidence currently permits

The two median image references exceed these observed-count requirements
on their V4rooms:48/48detected with correct directions and0/24false alarms
per speed. This supports the declared finite engineering benchmark under
their0.5°sampling, geometric assumptions and noiseless room generator.
It does not establish performance with sensor noise, other motion axes,
shorter decisions, unfamiliar environment families or a physical robot.
[Sealed V4report](SMALL_TURN_TARGET_DECISION_REPORT_V4.md).

The original V2DNp15 readout detects21/48,6/48and5/48±2°/s turns at
5.5,11and16.5mm/s. These are substantial misses, not a model falling just
short of perfection. Its raw-sign counts are42/48,32/48and28/48; straight
false alarms2/24,2/24and1/24. The published-field variants do not repair
the small-turn benchmark. This does not prove that every possible readout
of every internal state lacks yaw information.
[Sealed V2report](GEOMETRY_GROUNDED_SMALL_YAW_REPORT_V2.md).

Zero false alarms in24independent rooms still has a two-sided95%Wilson
upper bound of13.8%. Meeting the observed≤10%rule is therefore weaker
than establishing a population false-alarm rate below10%. Both signs and
repeated speeds share rooms; they are not independent animals. Stronger
generalization claims need an independently specified sampling plan and
uncertainty criteria before new testing. Threshold estimation should
include sampling, goodness-of-fit and uncertainty assessment, as discussed
by [Wichmann and Hill (2001)](https://pubmed.ncbi.nlm.nih.gov/11800458/).

## One metric to add prospectively

Detection and raw direction are separate original metrics. Passing both
at80%does not necessarily mean80%of turns are both detected and assigned
the correct direction. Their intersection can be as low as60%in general;
with48cases and39successes on each marginal metric, the finite lower
bound is30/48(62.5%). Do not silently combine or rename these measures.

This review adds the joint count as a **retrospective diagnostic only**:
number of actual turns producing a nonzero decision with the correct
sign. It is21/48,6/48and5/48for original DNp15, and48/48per speed for both
V4median references. Thus this clarification does not rescue the neural
result or undermine those reference successes.
[All120condition summaries](../results/small_turn_acceptance_review_v1/metrics.json),
[input-hash and arithmetic review](../results/small_turn_acceptance_review_v1/review.json).

Recommendation for a future study: explicitly require at least80%of turns
to be both detected and given the correct direction, alongside the
false-alarm criterion. This is a proposed new operational criterion,
not an activated rule or retrospective reclassification. Required latency
and robustness conditions also need specifying before deployment claims.

## A useful neural explanation has a different evidence requirement

A neural model need not reproduce every recorded response exactly or make
each individual HS,H2,bIPSandDNp15cell a perfect turn classifier. A
reasonable goal is to explain the transformation across the circuit and
make testable predictions consistent with measurements and their
uncertainty. This is a methodological recommendation, not a claim that
our model currently meets it.

[Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9)
compare stimulus selectivity, bilateral asymmetry and perturbation effects.
Their physiological comparisons distinguish HS from DNp15; their model
uses physiological calibration and tests additional stimuli. These
measurements motivate circuit-level comparisons, rather than demanding
identical classification performance from all four cell groups. They do
not establish our80/80/10project rule or validate our frozen model.

For our project, acceptable physiological evidence requires matched
stimuli, a justified mapping from simulated activity to the recording
signal, and separate calibration and held-out validation. Reproducible
simulation alone cannot supply this. A reproducible negative result—such
as a constrained model or bIPSlesion failing a prediction—is a valid
scientific finding, while the relevant capability claim remains unmet.

## Acceptable and unacceptable conclusions

Acceptable: report finite test performance with errors and uncertainty;
identify the conditions that fail; retain a biologically constrained
negative result; narrow the claim to the conditions actually tested.

Unacceptable: lower an old acceptance bar after seeing failure; tune
unmeasured connections merely to improve classification; use test rooms
for fitting; hide false alarms or failed speeds; treat an image-based
reference as a neural mechanism; claim biological causality from a model
lesion or biological validation from a numerical replay.

The recommendation is to keep the existing modest computational bar and
investigate why the current neural readout misses it. We should pursue a
supported explanation, not optimize toward100%at any biological cost.

## Undergraduate explanation: what we did, what we want, and why

We checked what success actually means. The detector can miss some turns
and still be useful; it also needs to avoid repeatedly calling straight
walking a turn. Our image tool passes the current test, while the brain
model misses too many turns. We want to explain that gap using biological
evidence, because a realistic explanation matters more than a perfect
score in an easy simulation.
