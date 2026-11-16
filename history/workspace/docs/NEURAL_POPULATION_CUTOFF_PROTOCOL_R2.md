# Neural population cutoff R2 — prospective fresh-test extension

31 October 2026. V1 development/calibration outcomes have been inspected and
show straight-walking false alarms. V1 weights, threshold, criteria and results
remain unchanged. This is a separately identified development extension, frozen
before examining negative-control episode maxima or generating any np test
images. No claim that this rule was prospective in the earlier V1 experiment.

Question: do negative-control-calibrated cutoffs improve the frozen neural-only
readouts? Preserve all five V1 scores and neural parameters. Compute each known
w-room stationary/straight episode's maximum |score| over callbacks [1,3).
Use the 16 calibration rooms only; never use positive yaw trials to choose a
cutoff. Two fixed rules, each with one global cutoff across speeds:

* `episode90`: maximum of the empirical 90th percentile, NumPy `method=higher`,
  for each of stationary and the three walking-speed groups, bounded below by 1.
  For 16 rooms this uses the 15th ordered peak, leaving at most one calibration
  episode above it per group. This is empirical calibration, not a population
  false-alarm guarantee.
* `episode_max`: maximum peak over all four groups, bounded below by 1.

The primary is `episode90/individual_linear`: it is the only newly fitted V1
candidate passing all 81 numerical comparisons before this extension. Retain
every rule/readout and failure, without choosing a winner from the fresh test.
Freeze cutoffs before scoring positive calibration trials or generating/scoring
fresh test images. Test on the same 24 new np rooms / 384 neural trajectories
as V1; identical inputs and scores, with only the separate decision cutoff
different. Test sets are shared paired comparisons, not independent replications.

Keep ≥80% joint/detection/raw-direction accuracy and ≥80% each sign at ±2/±5,
≤10% endpoint/any-episode straight and stationary alarms, all speeds and zero
undefined monitoring callbacks. Preserve the endpoint 1.19 s and full straight
monitoring [1,3). Keep absolute score-refinement tolerance 0.2, all 81
space/time/solver checks, and endpoint/any-episode decision stability under the
same newly frozen cutoff. Do not divide scores by the new cutoff to make their
numerical errors look smaller. No graph edge, neural time constant, input
encoding, readout coefficient or physiological observation model changes.

This tests calibration of artificial neural readouts, not repair or validation
of the biological DNp15 circuit. No image estimator or closed loop.
