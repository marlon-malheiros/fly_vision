# Neural temporal-change readout during established walking, V1

2026-10-27. Scientific recipe checkpoint `473c872`; execution-only R2 checkpoint
`a79036f`. The original frontend, graph, neural parameters and previous studies
are preserved. This study changes external decoding, not the neural circuit.

**Sensitivity improves substantially, but the reliability problem is not fixed.**
The primary DNp15 change readout detects 138/144 small turns by the 200-ms
deadline, versus 11/144 with the unchanged legacy readout on identical trials.
Raw direction is correct in 143/144 cases, and all 138 detected turns have the
correct direction. However, straight alarms exceed the frozen target at slow
and fast speeds, and repeated monitoring alarms in 54/72 straight episodes.
The engineering reference also fails its fast-speed false-alarm target here.
No tested method passes every endpoint condition on this fresh-room set.

## Fixed question and intervention

The [completed onset experiment](ONGOING_WALKING_YAW_REPORT_V1.md) showed
direction-dependent neural responses but poor frozen classification. It did
not establish that the population lacks yaw information. Test one specific
readout change: each side's current 100-ms mean activity minus its own mean
200 ms earlier. At the 1.2-s deadline the feature is [1.10,1.20) minus
[0.90,1.00). This is a fixed causal sliding stencil with no onset argument,
future images, counterfactual straight trajectory or image-confidence input.

The primary candidate is DNp15. A task-matched absolute-activity readout
controls for recalibration alone; the old absolute readout and successful
engineering detector remain fixed comparisons. HS/H2/bIPS are secondary roles
using the same two new recipes. No choice among methods is made after testing.
This is a transient turn-onset feature; a sustained-yaw detector is not implied.
[Protocol](NEURAL_CHANGE_READOUT_PROTOCOL_V1.md),
[configuration](../configs/neural_change_readout_v1.json),
[feature code](../src/male_optic_frontend/neural_change_readout_v1.py).

Use p00--p07 from the earlier, already inspected study for coefficient fitting:
40 conditions per role/speed, including straight and +/-2 and +/-5 degrees/s.
Use only straight episodes from p08--p23 for threshold calibration. All p rooms
are known development data, not independent validation. Apply the historical
standardized linear ridge fit, penalty 0.001 and unpenalized intercept. Each
threshold is the maximum absolute straight calibration score across 16 rooms.
No window, threshold or regularization search is performed. There are 24 new
role/speed/mode fits. The experiment supplies known walking speed; this is not
a single speed-independent decoder. No neural or physiological parameter is fit.

| Speed (mm/s) | Legacy DNp15 cutoff | Matched absolute cutoff | Change cutoff |
|---|---:|---:|---:|
| 5.5 | 2.07641 | 3.44791 | 0.20731 |
| 11 | 6.01793 | 5.59708 | 0.58545 |
| 16.5 | 6.23828 | 6.29558 | 0.93473 |

Cutoffs are decoder-equivalent degrees/s, not measured neuronal units.
Zero calibration-straight alarms follow from the maximum rule and are not
validation evidence. [All fitted readouts](../results/neural_change_readout_v1/calibration/readouts.json),
[all development predictions](../results/neural_change_readout_v1/calibration/predictions.json),
[pre-test freeze](../results/neural_change_readout_v1/before_test.json).

## Independent new environments and frozen targets

Generate 24 w rooms with seeds 202610277000--202610277023, disjoint from 188
prior distinct scene seeds. They use the same textured-room/clutter family,
balanced empty/three-sphere scenes. Each has three speeds crossed with
0,+/-2,+/-5 degrees/s plus stationary: **384 new episodes**. Walking starts
at 0.5 s, yaw at 1.0 s; continue to 1.8 s without resetting neural/frontend
state. Reuse the original exact piecewise trajectory, binocular geometry,
1-degree retina, 5-ms images, 10-ms network inputs and 1-ms solver.
All methods within an episode receive identical retinal images/trajectories.
[Seed audit](../results/neural_change_readout_v1/seed_audit.json),
[plans](../results/neural_change_readout_v1/plans.json).

At every speed and both yaw magnitudes keep >=80% detection, >=80% raw-sign
accuracy including undetected turns and <=10% observed straight alarms:
>=39/48 detections/signs and <=2/24 alarms. Stationary neural trajectories
are checked raw and left unclassified because no speed-zero decoder exists.
These historical criteria were not changed after any new scores.

## Primary endpoint results

Values below are ordered by walking speed **5.5 / 11 / 16.5 mm/s**.
Straight controls are shared between magnitudes, not extra independent trials.

| DNp15 system or reference | +/-2 detections, of 48 | Raw signs, of 48 | Straight alarms, of 24 | All-speed target |
|---|---|---|---|---|
| Legacy DNp15 | 8 / 1 / 2 | 41 / 32 / 32 | 1 / 1 / 2 | Fail |
| Matched absolute DNp15 | 11 / 3 / 3 | 39 / 30 / 29 | 1 / 1 / 1 | Fail |
| **Change DNp15, primary** | **48 / 48 / 42** | **48 / 48 / 47** | **3 / 2 / 5** | **Fail** |
| Fixed engineering reference | 48 / 46 / 45 | 48 / 48 / 48 | 0 / 2 / 3 | Fail |

Change DNp15 detects and correctly signs all 48/48 +/-5 turns at every speed,
but shared false-alarm failures remain. It passes both endpoint magnitudes
only at 11 mm/s. The engineering reference also detects/signs every +/-5 turn,
but fails its fast false-alarm gate. Recalibration of absolute DNp15 activity
alone detects only 17/144 small turns; this specific control does not repair
the transfer problem. [All 156 endpoint curves](../results/neural_change_readout_v1/analysis/curves.csv),
[all 14,976 phase/feature rows](../results/neural_change_readout_v1/analysis/predictions.json).

![Frozen readout comparison](../results/neural_change_readout_v1/figures/readout_comparison.png)

[PDF](../results/neural_change_readout_v1/figures/readout_comparison.pdf).
Coincident plotted points are retained; exact counts are in the table and CSV.

## Repeated monitoring and late responses fail

Count any alarm during 80 rolling decisions in each constant straight-walking
episode from 1.0 through 1.79 s. This is a room/episode incidence, not the
fraction of callbacks that alarm and not 80 independent observations.

| System | Any-alarm rooms, of 24, at 5.5 / 11 / 16.5 mm/s |
|---|---|
| Legacy DNp15 | 3 / 2 / 4 |
| Matched absolute DNp15 | 1 / 1 / 1 |
| **Change DNp15** | **19 / 12 / 23** |
| Engineering reference | 0 / 2 / 5 |

The primary fails the <=10% rolling diagnostic at every speed, despite high
turn-onset sensitivity. This is unacceptable evidence for claiming reliable
continuous small-turn monitoring. Calibration used one fixed straight endpoint
per room, not the maximum over every rolling time. That mismatch is a concrete
limitation; it does not authorize fitting a new threshold on the test rooms.
[Rolling curves](../results/neural_change_readout_v1/analysis/rolling_curves.csv),
[all rolling room outcomes](../results/neural_change_readout_v1/analysis/rolling_predictions.json).

The fixed late endpoint uses the last 100-ms window [1.70,1.80) minus
[1.50,1.60), not the prior report's 700-ms mean. Change DNp15 detects only
13/48, 3/48 and 6/48 +/-2 cases there, with raw signs 26/48, 27/48 and 24/48
and straight alarms 9/24, 3/24 and 2/24. The transient feature cannot be claimed
to measure continuing steady yaw. All pre-event and late predictions remain
in the phase table, including unsuccessful secondary methods.

## Other roles and descriptive error inspection

| Change readout | +/-2 detections, of 48, by speed | Raw signs, of 48 | Endpoint alarms, of 24 |
|---|---|---|---|
| HS | 48 / 48 / 24 | 48 / 48 / 43 | 1 / 2 / 5 |
| H2 | 43 / 5 / 0 | 48 / 44 / 40 | 2 / 1 / 0 |
| bIPS | 48 / 31 / 18 | 48 / 48 / 42 | 2 / 1 / 3 |

None qualifies across all speeds/magnitudes; none is promoted over DNp15.
No new bIPS lesion or within-circuit causal intervention was performed.

Descriptive inspection after scoring identifies DNp15 endpoint alarms in
slow rooms w10/w14/w17, medium w07/w19 and fast w05/w12/w13/w15/w19. Its six
missed small turns are all fast: w01 +2, w05 -2, w12 +2, w13 +2, w15 +2 and
w19 +2. Five of those rooms also alarm while straight. The w15 +2 raw score
is -0.07761, causing the single raw-direction error, but remains undetected.
These observations are not new frozen success rules, causal diagnoses or
scene-specific inference corrections. Complete scores, not just mistakes,
are retained in the predictions table.

The reference's fast alarms are w03/w04/w08; its missed turns in those rooms
are respectively +2/-2/+2. Prior successful p/q/r-room observations remain
unchanged. Their numerical reproduction does not guarantee every later
same-family room set will pass the observed false-alarm target.

## Numerical checks, audit and preserved execution failure

Four targeted synthetic tests pass: constant-offset cancellation/transient
response, future-prefix invariance, exact sample stencil, and invalid-clock/
missing-side rejection. Independent scalar reconstruction checks 1,344 known
feature pairs (maximum error 1.74e-18). All 24 fits reproduce using augmented
least squares rather than the production normal-equation solve: maximum
coefficient discrepancy 2.31e-14, threshold discrepancy 1.07e-14.
[Calibration audit](../results/neural_change_readout_v1/calibration_review.json).

The primary change DNp15 passes six existing f00 spatial/temporal comparisons
at the unchanged 0.2-degree/s score criterion; maximum difference 0.15156.
Across all role/mode comparisons, 25 of 72 fail. Absolute DNp15 reaches 0.24515
and fails. An independent scalar audit verifies every score difference and
pass/fail flag, retaining all failures. These three known cases give no uniform
bound over w rooms or all timestamps. Raw neural sampling sensitivity is not
therefore claimed solved. The inherited identical-model, fixed-forcing solver
check passes separately (maximum half-step rate difference 1.98e-11).
[Numerical results](../results/neural_change_readout_v1/numerical_review.json),
[independent arithmetic](../results/neural_change_readout_v1/numerical_arithmetic_review.json),
[original solver evidence](../results/ongoing_walking_yaw_v1/numerical_review.json).

The first execution attempt failed 384 jobs in 10.81 s before writing any
retinal/neural arrays. Spawned workers used the preceding study's default
world directory. Preserve all errors and empty directories. The separate R2
runner corrects worker-local initialization, passes a no-rendering spawn probe
and runs the unchanged scientific recipe. Its 384 simulations complete with
zero failures in 990.19 s. The original failed sweep is not counted as a pass.
Four predefined whole-episode replays reproduce all 84 arrays exactly; replay
overlapped part of the sweep, so the wall-clock total is not a CPU benchmark.
[Original failure](../results/neural_change_readout_v1/execution_failure_v1/held_out_complete.json),
[correction freeze](../results/neural_change_readout_v1/execution_revision_2/before_execution.json),
[worker probe](../results/neural_change_readout_v1/execution_revision_2/worker_probe.json),
[successful execution](../results/neural_change_readout_v1/held_out_complete.json),
[replay](../results/neural_change_readout_v1/reproduction_review.json).
Inherited episode-summary fields describe the unchanged simulator; new external
decoder calibration is recorded separately in the calibration files.

The complete independent fresh-data audit passes: it reconstructs 14,976 phase
rows, all 156 endpoint curves, 74,880 rolling scores and 39 rolling curves.
It independently checks reference weighted medians, all stationary neural
zeros, shared retinal/source/network/reference prefixes and full neural state
through yaw onset. Selected fresh images agree with independent NumPy rendering.
These are numerical reproducibility checks, not physiological validation.
The PNG was visually inspected and the matching PDF header/export checked.
[Fresh-data audit](../results/neural_change_readout_v1/analysis_review.json),
[Figure review](../results/neural_change_readout_v1/figures_review.json).

## Supported interpretation and limits

The unchanged neural representation supports substantially better transient
yaw decoding with a causal own-history feature than either tested absolute
readout. That is a demonstrated effect within this external decoding pipeline,
and argues against treating poor legacy classification as absence of usable
neural yaw information. The result does not identify a unique circuit defect
or prove that flies implement this temporal subtraction. Increased sensitivity
and greatly increased rolling alarms coexist; the full reliability target
is still unmet. No threshold was retuned after inspecting w-room errors.

Only 24 new instances of one simulated scene family were tested. Reusing rooms
across speeds/signs does not make those trials independent biological samples.
Observed rates and descriptive Wilson intervals are not population guarantees.
No gait, neural/camera noise, changing forward speeds, randomized/smooth yaw
onsets, movement intention or physical deployment was validated. This is
supervised postprocessing of a functional surrogate, not a reconstructed
physiological readout. Missing circuit constraints remain unresolved; no
electrical synapses or absent neurons/connections were invented. Matched
recordings and explicit voltage/calcium measurement models with independent
calibration/validation are required before physiological claims.
[Descriptive intervals](../results/neural_change_readout_v1/analysis/rate_intervals.json).

## Reproducibility and archive

[Driver](../scripts/neural_change_readout_v1.py),
[independent reviewer](../scripts/review_neural_change_readout_v1.py),
[R2 execution wrapper](../scripts/run_neural_change_readout_v1_r2.py),
[archival/control reviewer](../scripts/finish_neural_change_readout_v1.py).
In a separate workspace with the parent inputs and no new study output, use
`PYTHONPATH=src:scripts`, BLAS/OMP threads 1 and a writable `MPLCONFIGDIR`.
Run driver `prepare`, `calibration`, reviewer `calibration`, driver `numerics`,
then `freeze_test`. The original driver `held_out` reproduces the preserved
worker-path failure; run R2 `prepare`, `worker_probe`, `run` to correct execution
without changing inference. Then run driver `analyze`, `replay`, reviewer
`review` and finisher `controls`; inspect figures before sealing. Writes are
exclusive and new seeds are guarded against prior local scene inventories.
[Completion](../results/neural_change_readout_v1/completion_v1/completion.json),
[index](../results/neural_change_readout_v1/completion_v1/artifact_index.json),
[post-exit verification](../results/neural_change_readout_postseal_v1.json).

## Simple explanation: what we did, what we want and why

We want the simulated neural circuit's activity to tell us reliably when a
walking fly starts turning. We tried reading the change from each group's
recent activity instead of just its overall level. That recovered most small
turns, showing that useful turn information is present. But it also sounded
too many alarms while the fly walked straight. We have improved sensitivity,
not finished the reliability fix. This experiment separates those two issues
and prevents us from presenting a sensitive detector as a dependable one.
