# Small-turn round V1: completed negative result

1 November 2026. **None of the 44 tested reader/operating-policy combinations meets
the complete +/-2-degree/s detection criterion across walking speeds.** No candidate
passes even the small-turn-only subset of the gates. Neither extra response time
nor the newly executed reduced circuit solves the problem. The previous bounded
[5-degree/s neural result](NEURAL_POPULATION_MILESTONE_BRIEF_V1.md) remains preserved;
no new biological-validation claim is made.

The round completes the finite experiments and their documented follow-ups. It
does not achieve the original reliable, biologically validated small-turn model.
[Decision](../results/small_turn_round_v1/final_decision.json),
[short explanation](SMALL_TURN_ROUND_TLDR_V1.md),
[reproduction](SMALL_TURN_ROUND_REPRODUCTION_V1.md).

## Executed alternatives and prospective boundaries

The [initial protocol](SMALL_TURN_ROUND_PROTOCOL_V1.md) and scientific sources were
frozen at Git `83e0e0e`, before the new fits/responses. Four readers reuse actual
archived MaleCNS or full-published-network activity; no original neuronal parameter
changes. They target +/-2 and zero training trials, excluding +/-5 from fitting.
Their alternatives are downstream-only linear softmax, spatial opponent-ratio
softmax, spatial MaleCNS nuisance-penalized ridge and full-published-population
nuisance-penalized ridge. The ratio is an observation transformation, distinct from
the earlier input-contrast-normalization experiment.

The newly executed reduced model comes from the released Ammer2023 Figure7a
equations. Fixed source filters, thresholds, gains, neural time constants and
conductance readout are retained. Applying this **vertical-motion motif along a
horizontal retinal coordinate is exploratory**, with declared retinal/adaptation
assumptions. Its states must not be called HS/H2/bIPS/DNp15. It does not modify the
MaleCNS graph. Both intact and the source-defined feedback block receive identical
movies; the block removes LPi-to-T4/T5 and reciprocal LPi interactions while
preserving feedforward inhibition. Each copy gets nuisance ridge and linear
softmax readers at 190, 490 and 990 ms after turn onset: 12 additional fits.

Before producing any calibration score file, the [operating amendment](SMALL_TURN_CUTOFF_AMENDMENT_V1.md)
adds an explicit <=10%-budgeted negative-only cutoff to the original maximum-negative
policy. The 16 fitted readers thus produce 32 policies. After the four existing
readers fail calibration, a separately frozen [temporal follow-up](SMALL_TURN_TEMPORAL_FOLLOWUP_V1.md)
adds score change and five-callback persistence, without refitting, for 12 further
policies. These are adaptive development stages, not one initial preregistration.
No further bank or acceptance-rule relaxation follows these outcomes.

The reduced model executes **640 walking episodes**, 384 in 24 training rooms and
256 in 16 disjoint calibration rooms. Every room has stationary control and all
5.5/11/16.5-mm/s by yaw0/+/-2/+/-5 conditions. Another **108 numerical-control runs**
cover three rooms, three speeds, three yaws and four profiles. Each run is evaluated
in two circuit copies. These are execution counts, not independent animals or
748 distinct physical conditions: some reference numerical cases repeat training
conditions. The existing-reader fits reuse earlier observations rather than adding
new MaleCNS/FlyVis simulations. All calibration rooms were previously inspected
in other studies; none of these counts is untouched-room validation.

## Results at the original 190-ms deadline

The criterion is >=80% correctly detected/signed turns, including each sign, and
<=10% straight/stationary episode false alarms at every speed, retained at +/-5.
All monitored negative callbacks in [1,3) count toward one alarm outcome per episode.
Inference receives neural history only, without speed, pose, room, true onset,
depth, same-room straight partner or direct image-motion estimate.

Entries below use the predeclared budgeted policy. MaleCNS and reduced-model rows
have 32 signed turns and 16 straight episodes per speed; native-population rows
have 12/6. This is a comparison of different representations/development samples,
not an identical-input physiological ablation or a controlled cross-model ranking.

| Reader | Correct +/-2 turns: slow / medium / fast | Straight alarms: slow / medium / fast |
|---|---:|---:|
| Downstream softmax | 6 / 9 / 6 of 32 | 0 / 0 / 1 of 16 |
| Opponent-ratio softmax | **32 / 17 / 9 of 32** | 0 / 0 / 1 of 16 |
| Spatial MaleCNS nuisance ridge | **20 / 15 / 14 of 32** | 0 / 0 / 1 of 16 |
| Full published-population nuisance ridge | 0 / 0 / 0 of 12 | 0 / 0 / 0 of 6 |
| Reduced intact, nuisance ridge | 0 / 0 / 0 of 32 | 0 / 0 / 1 of 16 |
| Reduced intact, softmax | 0 / 0 / 0 of 32 | 0 / 0 / 1 of 16 |
| Reduced feedback block, nuisance ridge | 1 / 0 / 1 of 32 | 0 / 0 / 1 of 16 |
| Reduced feedback block, softmax | 1 / 1 / 1 of 32 | 0 / 1 / 1 of 16 |

All three new MaleCNS-derived base readers get the **raw turn direction correct in
32/32 cases at every speed**. The spatial nuisance reader has the highest
worst-speed detection rate among this bank, but only 14/32=43.75% at fast walking.
The ratio reader is strongest at slow walking, reaching 32/32, but drops to
9/32=28.125% at fast walking. These are development findings and do not replace the
required all-speed criterion. The 190-ms reduced intact/blocked comparisons remain
negative; refitting different readers in each copy prevents attributing their
score differences solely to a circuit interaction.

The conservative ratio policy gives 32/16/9 detections and zero observed calibration
alarms. Relaxing only to the permitted negative false-alarm budget gives 32/17/9;
this does not rescue the target. Lowering its common cutoff further necessarily
violates an observed group budget. Zero maximum-negative calibration alarms are
true by construction and are not evidence of generalization.

The six temporal scores and both their policies also fail. Neither 490 nor 990 ms
qualifies for the reduced circuit, even as a slower secondary capability. At those
latencies its budgeted small-turn detections range from zero to two of 32 per speed.
Extra response time therefore does not rescue these particular representations
and readers; this does not exclude every possible integration rule.

[All 192 original policy rows](../results/small_turn_round_v1/analysis/all_policy_summary.json),
[all 72 temporal rows](../results/small_turn_round_v1/analysis/temporal_summary.json),
[existing-reader score streams](../results/small_turn_round_v1/existing/calibration_predictions.npz),
[reduced-reader score streams](../results/small_turn_round_v1/reduced/calibration_predictions.npz),
[temporal score streams](../results/small_turn_round_v1/analysis/temporal_predictions.npz).

![Every combination](../results/small_turn_round_v1/figures/all_candidates.png)

## What the failures explain

The evidence separates direction sensitivity from reliable detection. A forced
left/right choice can be correct on every actual turn while a classifier also
assigns strong turn-like confidence to some straight-walking segments. Those
segments force the cutoff upward, removing small turns, especially at higher speed.
The negative examples span the whole monitored walk rather than just one quiet
instant. Good training error does not establish this separation in another room.

For example, the ratio reader's budgeted cutoff is 0.989742. Its fast-turn scores
span values well below that boundary, while some straight-walking peaks approach
one. The nuisance reader's cutoff is 0.942384. The minimum .5 policy floor is
inactive; it is the observed negative scores that set these cutoffs. Independent
rank and counterfactual diagnostics retain all sign/score overlap, without using
paired straight controls during inference. [Score overlap](../results/small_turn_round_v1/analysis/score_overlap.json),
[fixed-score cutoff certificates](../results/small_turn_round_v1/analysis/scalar_threshold_certificates.json).
These certificates concern the tested scalar scores, common thresholds and
observed calibration sample only; they do not prove that neural information is
absent or that biological tiny-turn detection is impossible.

![Confidence overlap](../results/small_turn_round_v1/figures/score_overlap.png)

The reduced circuit has no exact-constant/floor-normalized features in any fit;
its failure is not explained by an untrained constant-feature extrapolation in
this audit. [Diagnostic](../results/small_turn_round_v1/analysis/constant_feature_audit.json).
It introduces opponent dynamics but still lacks evidence for a quantitatively
correct horizontal retinal/pooling model. Existing MaleCNS LPi feedback was already
present before this round; adding those edges again is not a new repair.

## Numerical and independent evidence

Literal author filtering agrees within 9.06e-16; both source recurrence conditions
match exactly. Causal output prefixes and pre-yaw retinal prefixes agree bitwise.
A fresh full walking-image replay verifies its saved hash, executes literal author
functions independently for every patch in both copies, and reproduces all three
saved feature vectors exactly after declared float32 storage.
[Source check](../results/small_turn_round_v1/source_review.json),
[literal full-path replay](../results/small_turn_round_v1/analysis/literal_full_path_replay.json).

All 108 declared aperture/time/solver runs completed. For each reduced reader there
are 81 actual refinement comparisons, evaluated under two policies (162 rows).
**All three feedback-blocked nuisance readers pass every numerical criterion**,
with maximum score differences 0.17123, 0.18592 and 0.14512. They still fail walking
detection. Thus the negative result persists in numerically qualified candidates;
smaller steps alone do not rescue those fixed readers. Every other reduced reader
fails at least one declared refinement; the largest score difference is 1.21553.
No tolerance is relaxed. Passing readers are not a proof that all source states
or optical assumptions are physiologically correct.
[All 1,944 policy/comparison rows](../results/small_turn_round_v1/numerics/comparisons.json),
[per-reader counts](../results/small_turn_round_v1/numerics/summary.json).

Independent Torch inference checks **199,752 original calibration predictions** and
direct temporal arithmetic checks **77,952 further predictions**, with maximum
errors 1.09e-14 and 9.33e-15. Separate counting reproduces every cutoff and all
264 policy summary rows; all 640 reduced episode artifacts are rehashed. Another
review reproduces all numerical comparison/decision rows exactly and rehashes
all 976 frozen prior inputs. Nine focused tests pass.
[Full curves](../results/small_turn_round_v1/analysis/full_curve_review.json),
[decisions](../results/small_turn_round_v1/analysis/decision_review.json),
[numerics/preservation](../results/small_turn_round_v1/analysis/numerical_independent_review.json),
[tests](../results/small_turn_round_v1/analysis/focused_tests.xml).
These implementation/reproducibility passes do not turn failed scientific gates
into successes.

Two operational failures are preserved: the NumPy-integer summary JSON export and
a reviewer launched before its required calibration export existed. The first
uses a separately versioned [scalar-only R2 correction](SMALL_TURN_SERIALIZATION_CORRECTION_R2.md);
the unchanged second reviewer succeeds after its dependency completes. No neural
simulation failed and no neural fit was repeated to improve an observed outcome.

The initial flat methods copy used basenames, so the new driver and module shared
one archive name. Their full-path source hashes and pre-outcome Git versions remain
unchanged. Final packaging verifies every original frozen source against its
initial digest and archives it under its full relative path; the original flat
copy remains untouched. This corrects an archival-layout limitation without
changing any scientific source or result.

## Biological scope and the next distinct alternative

The public [Ammer et al. study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620086/)
provides evidence for multilevel opponent inhibition and a released computational
reference. This round reproduces that code and tests an explicitly assumed
horizontal application. It does **not** fit new recordings, validate its horizontal
parameters, recreate the anatomical HS/H2-bIPS-DNp15 pathway or establish a
biological detection threshold. Source-model agreement is numerical reproduction;
the earlier mixed physiological comparisons remain unchanged.

The original objective is not shown to be impossible. What fails is this finite
collection of fixed encoders, readers and policies under the stated criteria.
One specific biological cause is not identified. The tests show an unresolved
separation/generalization problem and, for some reduced readers, additional
numerical sensitivity. They exclude a simple common-cutoff rescue of the tested
scores in this calibration sample, and they show that more waiting and the tested
source feedback motif are insufficient here.

A distinct next option would be a separately versioned **neural visual encoder
trained on diverse walking optic flow**, with anatomical constraints preserved and
physiological agreement tested independently. Unlike another readout-only fit,
this would change how the new encoder represents motion; it has not been executed
in this round. Training against known physical image motion would be an explicit
task-optimization assumption, not biological calibration or permission to invent
connections. A physiological model still needs matched neuronal measurements and
independent tests of any calibrated dynamics. These are alternatives for a new
research decision, not promised solutions or reasons to relabel the present failure.

All 24 reserved fresh rooms remain unrendered because nothing qualifies. The
previous models, 5-degree result and failures remain available. There is no
closed-loop controller or physical deployment in this study.

We wanted a neural model to notice tiny turns without falsely reporting turns
during straight walking. We tested new ways to read the simulated neurons, a
published smaller circuit, different response times and numerical refinements.
The neurons often contain the correct turn direction, but the tested decision
systems still confuse some straight walks with turns. This round gives a clearer
failure diagnosis, not a completed small-turn neural model.
