# Fixed neural readout with independent negative-only calibration

2026-11-02. **The final operating point passes the predefined two-degree/s
benchmark on a new 24-room test, with all 81 numerical gates retained.**
This is a bounded computational milestone. An earlier inspected cohort still
fails its false-alarm count at the new cutoff; broad reliability and biological
validation are not established.

## Motivation, separation and frozen conditions

The [first untouched test](RAW_LOCAL_HELDOUT_REPORT_V1.md) detected 48/48,
48/48 and 46/48 small turns, but produced 5/24 fast straight alarms. Its original
failure stays unchanged. A test-informed oracle interval suggested a possible
threshold repair; that interval was not used to select a numerical cutoff.

The [new protocol](RAW_LOCAL_CALIBRATION_REPAIR_PROTOCOL_V1.md) freezes one final
attempt: keep every neural weight, frontend/graph parameter, local feature/map,
training floor, temporal window and endpoint unchanged. Generate 40 new negative
calibration rooms and 24 different test rooms. The source checkpoint `82da8f8`
predates cutoff calculation. [Pre-calibration freeze](../results/raw_local_calibration_repair_v1/before_calibration.json),
[seeds/freshness](../results/raw_local_calibration_repair_v1/freshness_audit.json).

Calibration has 160 negative episodes: static plus 5.5/11/16.5 mm/s straight
walking in every rc room, three seconds each. Positive calibration images are
not generated. Take the 39th of 40 sorted two-second episode peaks per speed/static
group, then the maximum of the four. This rank rule was fixed before calibration
and gives cutoff **1.1329958232706985**. It lies outside the old test's oracle
feasible interval; no adjustment moves it into that interval.
[Cutoff and every peak](../results/raw_local_calibration_repair_v1/cutoff.json).

This uses a finite-sample rank-calibration principle: for ideal continuous,
exchangeable negative scores, the k-th order statistic of n calibration scores
has marginal future exceedance probability (n+1-k)/(n+1). The earlier rank 15
of 16 corresponds to 2/17, whereas rank 39 of 40 corresponds to 2/41. The usual
rank argument and calibration uncertainty are described by
[Angelopoulos and Bates, Sections 1.1, 3.2 and Appendix D](https://arxiv.org/html/2107.07511v6).
These are idealized explanatory probabilities, not verified conditional error
bounds for our fixed-stratified simulator worlds. The 5% design parameter is
not a claim of 95% biological confidence.

After cutoff freeze, all old w development gates pass: +/-2 joint counts
32/32, 32/32, 29/32; fast directions 15/16 and 14/16; zero straight/static alarms;
all +/-5 groups 32/32. All 81 numerical score/endpoint/episode gates also pass
with this cutoff, using the already preserved scores because neural weights
are unchanged. [Pretest gates](../results/raw_local_calibration_repair_v1/pretest_gates.json),
[before-rt freeze](../results/raw_local_calibration_repair_v1/before_test.json).

## Fresh test result

All 384 rt conditions were completed before assessment, without any test-based
change. Each room has static plus three walking speeds times zero/+/-2/+/-5.
Positive endpoint: callback 119, 190 ms after yaw onset. Straight/static controls:
all callbacks 100..299. One common fixed cutoff; no true speed or image estimator
enters readout inference.

| Forward speed (mm/s) | +/-2 joint /48 | Negative /24 | Positive /24 | Straight alarms /24 | +/-5 joint /48 |
|---|---:|---:|---:|---:|---:|
| 5.5 | 48 | 24 | 24 | 0 | 48 |
| 11 | 48 | 24 | 24 | 0 | 48 |
| 16.5 | 42 | 21 | 21 | 0 | 48 |

Static alarms: 0/24. All raw turn signs are correct, including six fast small
turns below threshold. Every joint, per-direction and false-alarm gate passes
at both magnitudes/all speeds. The project criteria are observed counts, not
a biological detection threshold or a population-confidence guarantee.
[All outcomes](../results/raw_local_calibration_repair_v1/test_results.json).

![Final independently calibrated test](../results/raw_local_calibration_repair_v1/calibration_repair_summary.png)

## Paired cutoff effect and retained counterexample

To separate cutoff effects from different room cohorts, a post-hoc descriptive
comparison applies the two already fixed cutoffs to identical saved scores.
It selects no model or threshold. On the new rt fast episodes, the old cutoff
would detect 45/48 small turns with 5/24 false alarms; the independently chosen
cutoff detects 42/48 with 0/24 alarms. Thus the cutoff change removes five alarms
at a cost of three detected turns in those same neural responses, retaining the
original directional sensitivity requirements.

On the older st cohort, the new cutoff retains 46/48 small-turn detections but
reduces alarms only from 5/24 to **3/24**, still above its allowance. That remains
a counterexample to a claim that every room cohort passes. It is now inspected
development evidence, not the new validation set. Do not pool cohorts into a
new post-hoc acceptance rule or relabel the old failed study as successful.
[Paired operating points](../results/raw_local_calibration_repair_v1/paired_operating_points.json),
[old-cohort reassessment declared before rt assessment](../results/raw_local_calibration_repair_v1/old_st_reassessment_after_cutoff_freeze.json).

## Numerical evidence, independent review and cost

All 81 previous refinements retain the original <=0.2 score-error, endpoint and
negative-episode decision requirements with the new cutoff. Maximum score errors
remain 0.1484741452 spatial, 0.0752080020 temporal and 1.68674e-9 solver. These
profiles cover three numerical-control worlds, not every possible new scene.

An independent reviewer verifies the 39-of-40 rank, all 160 negative calibration
episodes and 384 test episodes, 99,008 callback scores (maximum difference
1.78e-15), all six development gates and all 81 numerical comparisons, all
288 pre-onset rate/feature/score prefix matches, four exact input/feature/score
replays and twelve paired operating-point summaries. It verifies original
qualification indexed files and exact preservation of model weights. Earlier
literal-window checks of the same feature code remain preserved; no neural or
statistical model is refit during review.
[Independent review](../results/raw_local_calibration_repair_v1/independent_review.json).

New observation CPU including replay is **4,818.502578 seconds (80.31 CPU
minutes)**, below the 6,000-second cap. Peak worker RSS: 263,184,384 bytes.
Four one-thread CPU workers, no GPU. CPU/computation timings are distinct from
assistant usage and development effort. No movies or full neural traces saved;
all compact feature/score arrays, source/image digests, worlds, recipes, methods
and failures are retained. Exact bytes are in the completion receipt. There
were no observation, budget, source-drift or score-review failures. An auxiliary
post-run zero-drive byte check initially assumed float64 and failed. The inherited
frontend source arrays are actually float32; the R2 audit uses that verified
dtype and confirms all 88 static hashes across new calibration/new test/old test,
plus zero moving-source overlap between cohorts. The failed assumption and R2
check are retained. No input, model, prediction, cutoff or criterion changed.
[R2 input audit](../results/raw_local_calibration_repair_v1/input_novelty_audit_r2.json).

## What is achieved and what remains

Achieved: one frozen neural-only readout passes the declared finite fresh-room
two-degree/s simulation benchmark across all three speeds at 190 ms, retains
larger-turn sensitivity and numerical qualification, and uses a cutoff set with
independent negative controls. The original local-normalization hypothesis and
first held-out operating point remain failed results.

Not established: universal reliability, a statistically certified population
false-alarm rate <=10%, performance with realistic sensory/neural noise, other
motion axes or moving objects, physical hardware performance, a biological
two-degree/s threshold, physiological accuracy, or bIPS's causal contribution.
Zero alarms in 24 fresh rooms is still a small sample. The older 3/24 counterexample
is material. A larger predeclared independent negative-only test would strengthen
error-rate estimates without another threshold adjustment.

The readout directly uses T4/T5 along with downstream roles; it is a task-trained
artificial output stage. It does not demonstrate that the anatomical HS/H2/bIPS/
DNp15 pathway computes this decision. Since neural dynamics were unchanged,
previous mismatches with biological recordings remain. Missing justified
electrical/upstream constraints and candidate neuronal identities stay unresolved.
Matched physiological benchmarking and controlled circuit interventions are
separate next milestones. No closed-loop locomotion was implemented.

## Reproduction and model files

The executable stages are `prepare`, `calibration`, `calibrate`, `test`, `assess`,
`replay` using `scripts/raw_local_calibration_repair_v1.py`; completed outputs
are exclusive-write. A full replay requires an isolated output namespace and
the retained baseline dependencies. The fixed operating point is specified by
[model.json](../results/raw_local_calibration_repair_v1/model.json),
[cutoff.json](../results/raw_local_calibration_repair_v1/cutoff.json),
[local_map.npz](../results/raw_local_calibration_repair_v1/local_map.npz),
[training_floor.json](../results/raw_local_calibration_repair_v1/training_floor.json)
and the frozen original graph/frontend. A repeatable read-only completion check:

```bash
PYTHONDONTWRITEBYTECODE=1 <HOME>/Lab/mech_male_fly_cns/.venv/bin/python scripts/finish_raw_local_calibration_repair_v1.py audit
```

## Undergraduate explanation

We want to notice a gentle body turn while the fly walks forward. We kept the
same simulated neurons and learned a simple way to combine their local motion
signals. The extra normalization we expected to help failed, but its simpler
comparison worked better. An initial test then showed too many false alarms.
We set a new alarm threshold using only new straight-walking examples and tested
it on different rooms: it detected every slow/medium turn and 42 of 48 fast turns,
with no false alarms in that new test. This meets our simulation milestone.
Some older rooms remain difficult, and matching real fly neurons is still a
separate unfinished task.
