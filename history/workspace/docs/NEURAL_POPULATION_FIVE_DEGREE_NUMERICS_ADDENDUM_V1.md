# Five-degree/s numerical follow-up — frozen addendum

31 October 2026. This follow-up is motivated by the already inspected fresh-room
secondary ±5°/s behavior: R2 episode_max/individual_linear has 48/48, 48/48 and
47/48 joint detections across speeds, with zero straight/stationary alarms.
The original ±2°/s objective and V1/R2 overall failures remain unchanged. No
new model/cutoff is selected or fitted. This is a targeted numerical extension,
not a fresh independent behavioral test or physiological validation.

Before computing new refinement responses, freeze these conditions: reuse the
same f00/p00/p01 worlds, frozen frontend, LPi-expanded graph, observer and
individual_linear coefficients. Add yaw ±5 at all three walking speeds, ending
at 1.30 s, for each primary/spatial/temporal/solver profile. Same physical
parameters as V1: 1-degree/5-ms images/10-ms inputs/1-ms RK4; finer 0.5-degree
space with unchanged physical detector offsets/pool, 2.5-ms images/5-ms inputs,
and 0.5-ms RK4. There are 72 new trajectories and 54 new paired comparisons.

For the frozen episode_max/individual_linear cutoff 2.337116267814088, require
the unchanged endpoint decision at 1.19 s and score discrepancy ≤0.2 in
original units for every new comparison. Keep all previous 81 comparisons;
no failure is dropped or score rescaled. Independently reconstruct every new
score difference using direct means and scalar weighted sums. Preserve all
trajectories, hashes and failures. Positive monitoring beyond the fixed
deadline is not the criterion being tested.

Only if all 135 comparisons and all predefined ±5 behavioral gates pass may
we describe a bounded secondary neural-only readout result at 5°/s. Do not
claim that 2°/s succeeds, that this is the biological DNp15 mechanism, or that
the true detection threshold lies at an untested intermediate rate. The same
24 behavioral rooms are reused; no new biological validation or closed loop.
