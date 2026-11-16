# Unchanged raw neural control: calibration and numerical qualification

2026-11-02. **The fixed raw-local neural decoder passes full development
calibration and all 81 numerical-refinement gates.** Independent test-room
performance and biological validation are separate claims.

## Candidate selection and frozen design

This is a new study following the sealed negative
[local-normalization pilot](LOCAL_SUBUNIT_PILOT_REPORT_V1.md). Its raw control
was nominated retrospectively after detecting 30/32 fast small turns. This
selection is explicit; the pilot's primary failure is preserved. The exact raw
model is copied without refitting. Mapping, activity floor, features, coefficients,
gain, 190-ms endpoint, negative monitoring and count criteria remain unchanged.
[Protocol](RAW_LOCAL_QUALIFICATION_PROTOCOL_V1.md),
[before-qualification freeze](../results/raw_local_qualification_v1/before_qualification.json).
Protocol/execution checkpoint: `d26cc93`.

The decoder observes 48 bilateral spatial features from co-located horizontal
T4/T5 rates and seven downstream role differences. The LPi-intact MaleCNS graph,
functional frontend and numerical parameters are frozen. No image-motion
estimator or true walking speed enters inference. This is an externally trained
artificial readout, not a reconstruction of a biological output synapse.

## Full calibration

Reuse the 80 pilot fast episodes, then extract the remaining 176 episodes in a
new namespace. All 256 episodes are from 16 previously inspected w development
rooms. One negative-only cutoff, **1.0391996879817291**, applies to all speeds
and magnitudes. Straight/static controls monitor callbacks 100..299 (two seconds),
while positives use callback 119 (190 ms after yaw onset).

| Speed (mm/s) | +/-2 joint /32 | Negative direction /16 | Positive direction /16 | Straight alarms /16 | +/-5 joint /32 |
|---|---:|---:|---:|---:|---:|
| 5.5 | 32 | 16 | 16 | 0 | 32 |
| 11 | 32 | 16 | 16 | 0 | 32 |
| 16.5 | 30 | 16 | 14 | 1 | 32 |

Static alarms: 0/16. Raw signs: 32/32 for every speed/magnitude. All six
speed/magnitude gates pass, including the per-direction requirements. The
common cutoff equals the prior fast-only cutoff; other negative groups do not
force it upward. These are development results, not independent generalization.
[All endpoints/peaks](../results/raw_local_qualification_v1/calibration_results.json),
[all score curves](../results/raw_local_qualification_v1/calibration_curves.npz).

## Numerical qualification

All 27 primary conditions (three worlds, three speeds, zero/+/-2 yaw) are
compared with each original refinement profile, for 81 comparisons and 108
solves. The required limit is absolute score difference <=0.2, unchanged signed
endpoint decisions, and unchanged straight-episode alarm status. All pass;
there are also zero individual callback decision flips.

| Refinement | Comparisons passed | Maximum absolute score error |
|---|---:|---:|
| 0.5-degree retinal sampling, matched angular frontend spacing | 27/27 | 0.1484741452 |
| Doubled image/input temporal sampling | 27/27 | 0.0752080020 |
| Half solver step, same one-ms forcing ramp | 27/27 | 1.68674e-9 |

[Spatial evidence](../results/raw_local_qualification_v1/spatial_numerical_results.json),
[temporal evidence](../results/raw_local_qualification_v1/temporal_numerical_results.json),
[solver evidence](../results/raw_local_qualification_v1/solver_numerical_results.json).
This checks the declared profiles, not convergence under every possible scene,
resolution or time step. It is not physiological validation.

![Calibration and all 81 numerical comparisons](../results/raw_local_qualification_v1/qualification_summary.png)

## Reproduction, independent checks and cost

All 284 additional observations (176 calibration plus 108 numerical) reproduce
original source/image hashes, re-pooled population activity, checkpoints and
final states. There are no source or dynamical parity failures. All 192
calibration turn/straight score prefixes match bitwise before yaw onset.

An independent reviewer checks all 256 calibration episodes, all six group
gates, all 81 numerical comparisons, and 62,696 callback scores (maximum score
difference 2.67e-15). It verifies exact equality with the pilot raw model and
unchanged pilot indexed files, without refitting. The earlier pilot separately
verified the fine feature arithmetic with literal windows and end-to-end replays.
[Independent review](../results/raw_local_qualification_v1/independent_review.json).

New observation CPU: **2,424.814721 seconds (40.41 CPU minutes)**, below the
3,600-second cap. Maximum worker RSS: 394,301,440 bytes. Extraction wall times:
211.07 seconds calibration, 240.80 spatial/primary, 103.43 temporal and 87.27
solver. Independent review: 0.442 seconds. These are computation timings, not
assistant usage or development effort. Persistent payload before figures and
completion copies is approximately 29 MB. Four one-thread CPU workers, no GPU,
no retained movies or full neural traces. There are no execution failures or
post-outcome corrections in this qualification study.

## Decision and remaining claims

The unchanged candidate is eligible for the separately frozen
[reserved-room test](RAW_LOCAL_HELDOUT_PROTOCOL_V1.md). It must pass all 24
previously unrendered st rooms under the same cutoff and original joint,
per-direction and false-alarm rules. Do not fit another candidate or adjust a
cutoff from those outcomes. Completion of this report establishes the development
and numerical gates only, not the untouched-room result.

The raw result does not establish that fine activity is indispensable: its
structured feature basis, spatial selection and bilateral constraint differ
from earlier decoders. The normalization hypothesis failed, and the successful
control is simpler. No unique causal explanation follows from this comparison.
Even if fresh testing passes, a decoder reading T4/T5 directly does not prove
that HS/H2/bIPS/DNp15 implements it, or that bIPS improves biological detection.
The surrogate frontend and missing justified physiological constraints remain.

## Reproduce

Exclusive stages are `prepare`, `calibration`, `assess_calibration`, followed
in order by `spatial`, `assess_spatial`, `temporal`, `assess_temporal`, `solver`,
`assess_solver`. Preserved results are never overwritten. A fresh execution
requires an isolated output namespace and retained dependencies. After sealing,
repeat the read-only integrity check with:

```bash
PYTHONDONTWRITEBYTECODE=1 <HOME>/Lab/mech_male_fly_cns/.venv/bin/python scripts/finish_raw_local_qualification_v1.py audit
```

## Undergraduate explanation

We kept the same simulated neural circuit and used its local motion signals
more effectively. The simple readout detects gentle turns at all walking speeds
in our development rooms. It also gives stable answers when we make the simulated
eye images and time steps more precise. This is progress toward a usable neural
detector. The next test is whether it works in rooms it has never seen; matching
real fly recordings remains a separate biological task.
