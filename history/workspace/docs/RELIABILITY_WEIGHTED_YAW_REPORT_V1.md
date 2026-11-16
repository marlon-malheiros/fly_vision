# Reliability-weighted local-motion yaw detection, V1

Completed 2026-10-26. Frozen inference checkpoint: `b6305c6`.

**The fixed confidence-weighted registered readout passes the existing
small-turn capability criteria in 24 fresh simulated rooms.** At each forward
speed it detects 48/48 ±2-degree/s turns with 48/48 correct directions; straight
false alarms are 0/24, 0/24 and 1/24. The same criteria also pass at ±5 degrees/s.
The unchanged spatial-weight comparator fails the false-alarm criterion at
medium and fast speeds. This is an engineering readout result. The original
MaleCNS circuit was preserved and was not repaired or physiologically validated.

## Question, provenance and frozen conditions

The [previous study](SEQUENTIAL_SMALL_TURN_REPAIRS_REPORT_V1.md) found that its
engineered local-velocity registered readout detected most small turns but
produced 4/24 fast straight-walking alarms. It did not establish that the
original neural signals or DNp15 output solved the task. This new study tests
one change to that engineering readout: give less weight to locally ambiguous
image-motion estimates. See the [prospective protocol](RELIABILITY_WEIGHTED_YAW_PROTOCOL_V1.md),
[configuration](../configs/reliability_weighted_yaw_v1.json),
[pre-development freeze](../results/reliability_weighted_yaw_v1/before_development.json)
and [pre-test freeze](../results/reliability_weighted_yaw_v1/before_test.json).

No parameters, cutoffs or neural weights were fitted. Preserve the original
source locations, duplicated ON/OFF local-velocity encoding, standard-plaid
conversion coefficients, clipping, four-neighbor channel interpolation,
8-degree sparse readout lattice, geometry and temporal averaging. The new
registered median weights are `te**2 * det(M)/trace(M)**2`, versus `te**2` in
the comparator. `M` is the local Lucas–Kanade image-gradient tensor; invalid
flow sites receive zero confidence. Confidence is sampled at the common
readout sites. Both versions receive the same motion values and images.

The extra cue measures local image conditioning. It is not calibrated neural
reliability or a noise-variance estimate; it is insensitive to a common
contrast scaling where the tensor remains valid. Its presence is an explicit
hybrid image/geometry modeling assumption. It does not supply the true yaw.
The original T4/T5 frontend and original MaleCNS dynamics are not replaced by
a claimed biological computation in this experiment.

Development used 112 archived episodes from four known training rooms and
16 known straight-calibration rooms, for implementation checks only. All
original source drives and old sparse/dense estimates reproduce exactly.
The inspected z-room outcomes were not used as a new held-out test. No
candidate selection or retuning followed development or new test outcomes.

The [seed audit](../results/reliability_weighted_yaw_v1/seed_audit.json) checks
all prior scene inventories: 24 q-room seeds are disjoint from 116 previously
listed seeds. Each new room supplies 15 moving conditions plus a stationary
control: 384 fresh episodes in total. Room geometry/textures use the previous
generative family, with 12 empty rooms and 12 containing three spheres.
All five predefined methods use identical binocular 1-degree movies, exact
forward/yaw trajectories and a 0.3-mm eye baseline. The inference function
accepts images and fixed sampling/geometry, never simulator speed, yaw, depth,
surface, intended motion or a paired straight-test episode. The renderer and
scoring use their labels separately. [Plans](../results/reliability_weighted_yaw_v1/plans.json).

## Primary results

Episode scores average 70 estimates from 0.70 through 1.39 seconds. The
unchanged fixed cutoff is 1 degree/s. At each speed/magnitude the frozen rule
requires at least 39/48 detections, 39/48 correct raw directions, and at most
2/24 straight alarms. Raw-direction accuracy includes undetected turns.
Undefined estimates count as failures; there were none.

| Forward speed (mm/s) | Old readout: ±2 detected | New readout: ±2 detected | New correct raw directions | Straight alarms, old → new | New criterion |
|---|---:|---:|---:|---:|---|
| 5.5 | 48/48 | 48/48 | 48/48 | 1/24 → 0/24 | Pass |
| 11 | 45/48 | 48/48 | 48/48 | 3/24 → 0/24 | Pass |
| 16.5 | 45/48 | 48/48 | 48/48 | 4/24 → 1/24 | Pass |

At ±5 degrees/s the old and new registered readouts both detect 48/48 turns
with 48/48 correct directions at every speed. Straight alarms are the same
straight trials shown above; they are not new independent observations.
The new readout therefore passes all six speed/magnitude capability checks.
All its detected turns also have the correct sign. All 24 stationary cases
score exactly zero for every method.

Straight-yaw RMSE falls from 0.419/0.664/0.825 to 0.184/0.354/0.466 degrees/s
across increasing speeds. ±2-degree/s turn RMSE falls from
0.402/0.647/0.809 to 0.186/0.337/0.476 degrees/s. These errors remain
nonzero despite all primary turn classifications passing.

[All 30 speed/magnitude curves](../results/reliability_weighted_yaw_v1/analysis/curves.csv),
[all 1,920 predictions](../results/reliability_weighted_yaw_v1/analysis/predictions.json),
[stationary controls](../results/reliability_weighted_yaw_v1/analysis/stationary.json).

![Frozen criteria and observed outcomes](../results/reliability_weighted_yaw_v1/figures/acceptance.png)

The primary and dense-reference counts coincide, so their traces overlap.
The fixed acceptance lines are unchanged. [PDF](../results/reliability_weighted_yaw_v1/figures/acceptance.pdf).

## Paired effects, remaining false alarm and uncertainty

The original comparator and new readout are evaluated on the same fresh
rooms. At medium/fast speeds the observed small-turn detection gain is
6.25 percentage points and the net alarm reduction is 12.5 points. Room-paired
10,000-draw descriptive bootstrap intervals for fast detection gain are
[0, 14.6] points and for fast false-alarm change [-29.2, +4.2] points.
The latter includes zero; do not present the small-sample difference as a
conclusive population-level improvement. All paired differences and draws
are retained and independently reconstructed from predictions.
[Paired effects](../results/reliability_weighted_yaw_v1/analysis/paired_effects.json),
[bootstrap arrays](../results/reliability_weighted_yaw_v1/analysis/paired_bootstrap.npz).

The new fast false alarm is **q15, +1.11653 degrees/s with zero actual yaw**;
the dense image reference also alarms there (+1.10651 degrees/s). The four
old fast alarms in q08/q13/q18/q22 are removed, but weighting introduces
this different alarm. This rejects any claim that confidence identifies and
removes every misleading region or guarantees correct straight estimates.

At each speed there are only 24 independent room instances. A 95% Wilson
interval for 0/24 alarms extends to approximately 13.8%; for 1/24 it is
approximately [0.74%, 20.24%]. Passing the observed <=10% requirement does
not establish a population false-alarm rate <=10%. The two turn signs and
three speeds reuse rooms and are correlated. Marginal Wilson turn intervals
are descriptive; paired-room effects retain that clustering. There is no
claim of multiplicity-adjusted statistical significance or universal detection.
[Intervals and caveat](../results/reliability_weighted_yaw_v1/analysis/rate_intervals.json).

![Straight-walking errors in every fresh room](../results/reliability_weighted_yaw_v1/figures/straight_errors.png)

Zero actual yaw in every panel; dashed lines are the ±1-degree/s decision
boundary. [PDF](../results/reliability_weighted_yaw_v1/figures/straight_errors.pdf).

## Fixed secondary comparisons

| Readout | ±2 detections at 5.5/11/16.5 mm/s | Straight alarms at the same speeds | All behavioral gates |
|---|---|---|---|
| Registered, old weights | 48/45/45 of 48 | 1/3/4 of 24 | Fail |
| **Registered, confidence (primary)** | **48/48/48 of 48** | **0/0/1 of 24** | **Pass** |
| Sparse lattice, old weights | 48/46/44 of 48 | 1/1/3 of 24 | Fail |
| Sparse lattice, confidence | 48/48/47 of 48 | 0/1/2 of 24 | Pass |
| Dense image reference, confidence | 48/48/48 of 48 | 0/0/1 of 24 | Pass |

The lattice diagnostics reinforce that weighting can help on this test,
but do not replace the primary method. Registered and dense estimates are
not identical: fast straight RMSE is 0.466 versus 0.421 degrees/s. Channel
interpolation, spatial support and clipping remain distinct computations.

## Numerical checks and reproduction

All required checks pass, within their stated scope:

- 112 primary archived cases and six sampling-control cases reproduce source
  drives and both prior sparse readouts exactly; archived dense scores also
  match exactly at their shared timestamps.
- All 30 method/case/refinement score checks pass the unchanged 0.2-degree/s
  tolerance. Maximum primary registered-confidence difference is 0.079625
  degrees/s over the three predefined f00 cases (0, -2, +2 at 16.5 mm/s).
  This covers 0.5-degree versus 1-degree images and halved image/readout steps;
  it is not a uniform numerical bound across every test environment.
- Eight analytic/binocular geometry checks recover yaw despite independently
  varying depth; independent landmark finite differences differ by at most
  5.02e-7 degrees/s. Six tensor checks cover flat/edge/2D texture, contrast
  scaling, independent derivatives/convolution and median weight scaling.
- Independent NumPy and compiled rendering agree in 18 known-frame checks.
  A separate review of three predefined fresh cases at three times in both
  eyes confirms the retained fresh images against NumPy rendering.
- Independent scalar weighted medians verify all 107,520 sparse frame
  estimates. All 1,920 predictions and 30 curve counts reproduce; paired
  differences and bootstrap arrays reproduce exactly from saved predictions.
- Four predefined fresh episodes are executed again in a separate replay
  directory. All retained retina/source/readout arrays reproduce exactly.
  This is a subset replay in the same environment, not a second complete sweep.
- Both PNG figures were visually inspected; corresponding PDF exports are
  retained. Coincident acceptance traces are explicitly disclosed above.

The 112 development episodes took 33.80 s, six control episodes 6.09 s, and
384 fresh episodes 253.65 s on the available CPU, excluding subsequent review
and archival work. There were zero execution failures in these sweeps.
These batch runtimes do not establish per-frame real-time feasibility.

[Numerical review](../results/reliability_weighted_yaw_v1/numerical_review.json),
[independent arithmetic review](../results/reliability_weighted_yaw_v1/analysis_review.json),
[fresh rendering/statistics review](../results/reliability_weighted_yaw_v1/fresh_evidence_review.json),
[replay review](../results/reliability_weighted_yaw_v1/reproduction_review.json),
[figure review](../results/reliability_weighted_yaw_v1/figures_review.json).

## Supported conclusion and practical limits

Under the frozen forward/yaw geometry, noiseless synthetic images and long
observation window, adding an image-conditioning cue to the existing local
spatial readout improves the observed paired results enough to satisfy every
predeclared capability gate. The intervention is isolated within this
engineering algorithm. It supports retaining local motion and conditioning
information as a useful computational hypothesis, not a demonstrated neural
implementation or proof of biological causality.

The original frozen graph, frontend, source identities and numeric parameters
remain unchanged. No new original-network DNp15 trajectories were simulated
here. Its previously documented failures therefore remain unresolved; this
study does not show that DNp15 now detects small turns or that bIPS supplies
this image-confidence cue. Electrical synapses, missing neurons, CT1 dynamics
and physiological benchmarking were not reconstructed by this change.

The algorithm still uses 10 ms of future images and a 0.7-s averaging window.
It assumes a known forward translation axis and yaw, and does not test gait,
roll/pitch, lateral motion, camera noise, moving objects or physical hardware.
It detects image-derived net rotation, not movement intention. The new rooms
are independent instances within the same family, not real-world environments.

The next bounded engineering experiment is to freeze a causal implementation
and test shorter observation windows on a separate fresh set, preserving the
present successful method as the reference. A biologically grounded circuit
repair remains a separate research objective requiring anatomical and
physiological constraints. No closed-loop controller was introduced here.

## Reproduction and archival evidence

Source: [inference module](../src/male_optic_frontend/reliability_weighted_yaw_v1.py),
[study driver](../scripts/reliability_weighted_yaw_v1.py),
[independent reviewer](../scripts/review_reliability_weighted_yaw_v1.py),
[fresh evidence check](../scripts/check_reliability_fresh_evidence_v1.py),
[sealer](../scripts/finish_reliability_weighted_yaw_v1.py).

In a separate checkout/workspace containing the required original/parent
datasets and no existing `results/reliability_weighted_yaw_v1` directory,
set `PYTHONPATH=src:scripts`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1` and
a writable `MPLCONFIGDIR`. Use the recorded Python/NumPy/SciPy environment.
Run the driver stages `prepare`, `development`, `controls`; reviewer
`numerics`; driver `freeze_test`, `held_out`, `analyze`, `replay`; reviewer
`review`; and the fresh evidence check. The supplemental validator's fixed
case selection is recorded in its own receipt before primary scoring. All
writers use exclusive creation and refuse to overwrite this completed run.
`prepare` also prevents reusing a test seed listed in another local study.

[Environment](../results/reliability_weighted_yaw_v1/environment.json),
[completion](../results/reliability_weighted_yaw_v1/completion_v1/completion.json),
[artifact index](../results/reliability_weighted_yaw_v1/completion_v1/artifact_index.json),
[post-exit integrity review](../results/reliability_weighted_yaw_postseal_v1.json).
The final progress snapshot is inside the completion directory. Live
AGENTS.md and the progress report remain outside the immutable index.

## Undergraduate explanation: what we did, what we want, and why

We want a simulated fly to notice a small turn even while walking forward.
Some image regions make motion difficult to judge, so treating every region
equally caused false turns. We kept the motion estimates and decision rule
the same, but gave clearer regions more influence. In 24 new virtual rooms,
this version detected every tested small turn and reduced false alarms enough
to pass our existing target at every walking speed. That gives us a working
engineering result to build on. We still need to show it can respond quickly
using only past images and establish how a real fly circuit could perform a
comparable computation.
