# Causal and shorter-window yaw detection, V1

Completed 2026-10-27. Inference/protocol checkpoint: `f545180`.

**A causal 100-ms engineering readout passes the frozen early and late
small-turn endpoint targets and the host CPU budget. Continuous monitoring
still exceeds the observed false-alarm target at the fastest speed: 3/24
straight rooms alarm at some point, versus the allowance of 2/24.** Both
findings are retained; endpoint success is not a claim of robust continuous
control. The original MaleCNS circuit remains unchanged.

## Fixed design and prospective selection

Build on the sealed [reliability-weighted readout](RELIABILITY_WEIGHTED_YAW_REPORT_V1.md).
Keep source coordinates, standard-stimulus velocity scale, duplicated ON/OFF
engineering channels, clipping, four-neighbor interpolation, confidence/geometry
weights and the 1-degree/s decision cutoff unchanged. Neither implementation
receives the true speed, yaw, depth, onset or intended movement.

Two fixed causal temporal schemes were compared:

- `delayed_centered`: the previous five-image calculation returned when its
  last image arrives, with its 10-ms intrinsic delay explicitly recorded.
  This is causality by acknowledging the previous lookahead cost.
- `backward_current`: a three-image second-order backward temporal derivative
  and spatial gradients at the current image, with no derivative lookahead.

Each uses 100/200/300/500/700-ms trailing means. The [protocol](CAUSAL_SHORT_WINDOW_YAW_PROTOCOL_V1.md),
[config](../configs/causal_short_window_yaw_v1.json) and analysis grid were
[frozen before development](../results/causal_short_window_yaw_v1/before_development.json).
No new threshold or physiological parameter was fitted.

Use 112 known episodes from four development turn rooms and 16 additional
straight-calibration rooms to select the fastest candidate passing all early
and late capability checks and its predefined numerical controls. The rule
selects **backward_current/100 ms**. Its result is
[frozen before fresh images](../results/causal_short_window_yaw_v1/before_test.json),
with the [selection and every candidate](../results/causal_short_window_yaw_v1/selection.json)
and [all development curves](../results/causal_short_window_yaw_v1/analysis/development_curves.csv)
retained. The small development set does not establish population optimality.

The [new seed inventory](../results/causal_short_window_yaw_v1/seed_audit.json)
excludes all previous scene seeds. Test 24 fresh r rooms, balanced empty/three-
sphere environments, with 15 moving conditions and one stationary condition
per room: 384 episodes. Speeds are 5.5/11/16.5 mm/s, yaw 0, ±2 and ±5 degrees/s.
Use identical 1-degree binocular images for both implementations. The scene
family, source mapping, 0.3-mm eye baseline and exact trajectories are unchanged.

Translation and yaw both begin at 0.5 s, as in the previous experiment.
This is not yet a new yaw perturbation imposed during established walking.
The detector processes images chronologically; event labels only locate
evaluation windows after the outputs have been generated.

## What the latency labels mean

An early score averages signal-time samples in `[0.5, 0.5+W)`; a late score
averages `[1.4-W, 1.4)`. The 700-ms delayed late condition reproduces the old
long-window benchmark at its signal times. Keep image arrival and signal
timestamps separate; never imply that a delayed estimate was available earlier.

At 100-Hz readout, the selected 100-ms early score uses ten estimates at
0.50, 0.51, ..., 0.59 s. Its last required image is available 90 ms after
motion onset. The conservative bin-boundary/window label is 100 ms. CPU time
must be added. This is an evaluation convention, not a measured biological or
camera-to-actuator latency. Median first correct rolling crossing is 90 ms
among detected turns, censored by the first eligible fully post-onset window;
it does not demonstrate that 90 ms is a minimum detection latency.

## Selected primary: early and late endpoint results

The historical criteria remain >=80% detected turns, >=80% correct raw signs
including undetected turns, and <=10% observed straight false alarms at each
speed, for ±2 and sustained at ±5 degrees/s. With 24 rooms this means at least
39/48 detections, 39/48 raw signs and at most 2/24 alarms. No undefined endpoint
scores occurred. All 12 selected endpoint/speed/magnitude checks pass.

| Speed (mm/s) | Early ±2 detected | Early raw signs correct | Early straight alarms | Late ±2 detected | Late raw signs correct | Late straight alarms |
|---|---:|---:|---:|---:|---:|---:|
| 5.5 | 48/48 | 48/48 | 0/24 | 48/48 | 48/48 | 1/24 |
| 11 | 47/48 | 48/48 | 1/24 | 47/48 | 48/48 | 1/24 |
| 16.5 | 46/48 | 47/48 | 1/24 | 47/48 | 47/48 | 1/24 |

At ±5 degrees/s, all 48/48 turns are detected with correct raw direction at
both endpoints and all speeds. The straight trials are shared with the ±2
comparison, not independent extra observations. Every detected selected turn
also has the correct direction; one fast raw-sign error belongs to an
undetected turn. All 24 stationary episodes score exactly zero.

[All 7,680 endpoint predictions](../results/causal_short_window_yaw_v1/analysis/predictions.json),
[all 120 endpoint curves](../results/causal_short_window_yaw_v1/analysis/curves.csv),
[marginal descriptive intervals](../results/causal_short_window_yaw_v1/analysis/intervals.json).

![Selected primary, endpoint and repeated-decision outcomes](../results/causal_short_window_yaw_v1/figures/selected_candidate.png)

The any-rolling-alarm line represents a different event than an alarm at one
endpoint. [PDF](../results/causal_short_window_yaw_v1/figures/selected_candidate.pdf).

## Continuous monitoring: a preserved negative result

The selected 100-ms detector issues 81 eligible rolling scores per episode
over the fully post-onset signal interval. Counting a room once if it ever
alarms during straight walking gives **1/24, 1/24 and 3/24** across speeds.
The fast rate is **12.5%**, which misses the <=10% operational check. This is
distinct from the unchanged historical endpoint gate; neither gate is relabeled.

The fast alarm rooms are r06, r15 and r18. r15 has a persistent scene offset:
at 16.5 mm/s its straight scores are -2.4263 early and -2.7777 degrees/s late;
its +2-degree/s turn scores are -0.3817 and -0.4734 and remain undetected.
At medium speed the corresponding turn also never crosses the decision
threshold. r18's early fast +2 score is 0.9732, narrowly below the fixed cutoff,
but becomes detected later. We did not raise/lower a threshold to change these
outcomes. Other fast straight alarms occur between the chosen endpoints.

Across the entire eligible rolling interval, ±2 turns ever detected with the
correct sign number 48/48, 47/48 and 47/48. These cumulative counts are not the
early endpoint counts and do not erase misses. All individual rolling scores,
first-crossing times and room alarm indicators are retained.
[Rolling episodes](../results/causal_short_window_yaw_v1/analysis/rolling_episodes.json),
[rolling curves](../results/causal_short_window_yaw_v1/analysis/rolling_curves.csv).

## Predefined window comparisons

All ten predeclared method/window combinations pass the fresh endpoint
behavioral targets in this batch. This does not establish that all pass their
development or numerical gates. Delayed_centered/100 ms fails one numerical
control, and several longer choices failed development endpoint checks.
The selected primary remains backward_current/100 ms.

| Nominal window | Rolling straight alarms at 5.5/11/16.5 mm/s, both derivatives |
|---|---|
| 100 ms | 1/1/3 of 24 |
| 200 ms | 1/1/2 of 24 |
| 300 ms | 1/1/2 of 24 |
| 500 ms | 0/1/1 of 24 |
| 700 ms | 0/1/1 of 24 |

The 200-ms variants are useful candidates for a separate confirmation of
continuous monitoring. They are not promoted to replace the prospective
primary after seeing these outcomes. Longer windows also provide fewer
eligible repeated decisions in the same finite episode; their any-alarm
comparisons combine averaging and exposure effects. No per-hour false-alarm
rate, optimal window or real-world detection threshold is established.

![Predeclared endpoint window comparisons at fastest walking speed](../results/causal_short_window_yaw_v1/figures/window_tradeoff.png)

Many traces coincide. Curves show behavioral counts, not a claim that every
numerical gate passes. [PDF](../results/causal_short_window_yaw_v1/figures/window_tradeoff.pdf).

## Serial CPU timing

After simulation workers exited, benchmark only the selected single-method
streaming pipeline and its trailing mean. Four fixed known/fresh cases, five
repeats each, follow a discarded whole-episode warm-up per case. Include
image validation/copying, bounded history, motion calculation, source sampling,
confidence weighting, median and trailing averaging. Exclude setup, rendering,
disk reads and camera transfer. Use a monotonic high-resolution clock.

| Output-producing callback, 1,840 measured calls | Time |
|---|---:|
| Mean | 7.71 ms |
| Median | 7.59 ms |
| 95th percentile | 8.63 ms |
| 99th percentile | 9.35 ms |
| Maximum | 12.53 ms |

Mean and 95th percentile pass the predefined 10-ms soft output budget on this
host. Total measured push processing is 14.27 s for 18.4 s of nominal streams.
Constructor setup is recorded separately (approximately 45--67 ms). The
maximum exceeds 10 ms: no hard-deadline guarantee, paced live-camera test or
complete physical end-to-end latency is claimed. Other window/method CPU
budgets were not independently benchmarked here.
[Timing summary](../results/causal_short_window_yaw_v1/runtime_review.json),
[all timing samples](../results/causal_short_window_yaw_v1/runtime_samples.npz),
[online/batch functional parity](../results/causal_short_window_yaw_v1/runtime_pipeline_review.json).

## Numerical checks, reproduction and audit correction

112 primary archived cases and six controls reproduce delayed-centered source
drives and old weighted yaw estimates exactly. Future-modified input prefixes
are identical; input order and timestamp checks pass. Polynomial derivative
checks and independent moment/convolution checks differ by less than 5e-15.

Of 120 predefined refinement checks, one fails: delayed_centered/100 ms, late
fast straight f00, differs by 0.206674 degrees/s on the finer retinal grid,
exceeding the unchanged 0.2-degree/s gate. The selected backward_current/100 ms
passes its controls; its maximum error is 0.188391 degrees/s. These checks cover
three known conditions and are not a uniform test-set error bound. All failures
are retained. [Numerical review](../results/causal_short_window_yaw_v1/numerical_review.json).

Independent review reconstructs endpoint means/counts and rolling means from
saved stream evidence, source-local weighted medians, the development selection,
timing statistics, and original readout parity on three predefined fresh cases.
Fresh rendering agrees with NumPy. Four fixed episode replays reproduce every
retina/source/stream/rolling array exactly; these are subset replays in the same
environment, not a second full sweep. Both PNG figures were visually inspected
and matching PDF exports retained.

The initial audit completed its assertions but failed while writing a NumPy
boolean to JSON. Its partial output remains untouched. A separately versioned
R2 wrapper converts NumPy scalars to equivalent Python scalars only at output
and reruns the same frozen audit to a new path. No inference, criterion, score
or simulation changed. [Preserved failure](../results/causal_short_window_yaw_v1/review_revision_2/failure.json),
[R2 audit](../results/causal_short_window_yaw_v1/review_revision_2/analysis_review.json),
[replay](../results/causal_short_window_yaw_v1/reproduction_review.json),
[figure review](../results/causal_short_window_yaw_v1/figures_review.json).

Development/control/fresh sweeps took 64.69/11.79/433.68 s respectively with
zero simulation execution failures. The audit-output failure above is reported
separately and preserved, not counted as a successful original audit write.

## Interpretation and practical boundary

The supported advance is a fast, past/current-image engineering readout that
generalizes under the frozen endpoint benchmark and fits a measured soft CPU
budget. It is not yet a reliable continuous turn alarm at the fastest speed.
Neither this result nor the successful previous long-window reference repairs
DNp15 or establishes a biological reliability mechanism. The original graph,
frontend and parameters remain frozen; no new MaleCNS trajectories or controller
were added.

Only 24 fresh rooms from the same synthetic family were tested. One alarm in
24 has a descriptive 95% Wilson upper bound around 20.2%; observed <=10% is not
a population guarantee. Turn signs, speeds, endpoints and rolling scores reuse
rooms and are correlated. No multiplicity-adjusted population claim is made.
No gait, noise, roll/pitch, lateral motion, moving objects, physical camera or
intention inference is tested. A yaw onset during established forward walking
and prospective confirmation of a practical monitoring window remain next
experimental questions. Closed-loop control remains deferred.

## Reproduction and preserved evidence

[Streaming implementation](../src/male_optic_frontend/causal_short_window_yaw_v1.py),
[driver](../scripts/causal_short_window_yaw_v1.py),
[frozen independent reviewer](../scripts/review_causal_short_window_yaw_v1.py),
[reviewer output correction](../scripts/review_causal_short_window_yaw_v1_r2.py),
[online checker](../scripts/check_causal_runtime_pipeline_v1.py),
[sealer](../scripts/finish_causal_short_window_yaw_v1.py).

In a separate workspace with the required original/parent data and no existing
study output, set `PYTHONPATH=src:scripts`, BLAS/OMP threads to 1 and a writable
`MPLCONFIGDIR`. Run driver `prepare`, `development`, `controls`; reviewer
`numerics`; driver `select`, `held_out`, `analyze`. With other workers exited,
run `benchmark`; then `replay`, the online checker and reviewer `review`.
The frozen original reviewer reproduces the documented JSON-output failure;
run the R2 wrapper to retain that failure and complete the unchanged audit at
its new destination. All writes are exclusive, so this finished run is never
overwritten. A full rerun needs a separate workspace and preserves seed guards.
[Environment](../results/causal_short_window_yaw_v1/environment.json),
[completion](../results/causal_short_window_yaw_v1/completion_v1/completion.json),
[index](../results/causal_short_window_yaw_v1/completion_v1/artifact_index.json),
[post-exit integrity](../results/causal_short_window_yaw_postseal_v1.json).

## Undergraduate explanation: what we did, what we want, and why

We want the simulated fly to notice a small turn quickly enough to help correct
it. We changed the engineering detector so it uses only images already received
and tested much shorter averaging windows. A 100-ms version met our original
accuracy targets in new rooms and processed updates fast enough for the measured
CPU budget. Watching continuously revealed a remaining problem: at the fastest
walking speed, three straight-walking rooms produced a false turn alarm, while
our allowance is two. Longer windows reduced those alarms in this comparison,
so we now have a measured speed-versus-reliability tradeoff to test further.
This advances the practical detector while the question of how the real fly
neural circuit performs the computation remains open.
