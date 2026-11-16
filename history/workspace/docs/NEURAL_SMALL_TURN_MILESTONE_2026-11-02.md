# Small-turn neural model: milestone and limits

2026-11-02. **A neural-only readout now passes the predefined two-degree/s
simulation benchmark on a fresh 24-room test. Broad reliability and biological
validation remain open.**

## Our goal

Detect gentle body rotations during forward walking from simulated neural
activity, without an image-motion estimator or knowledge of true walking speed.
At 2 degrees/s, the fly changes heading by only 0.38 degrees during the 190-ms
decision window. We require at least 80% correct signed detections in each
direction at all three walking speeds, with at most 10% observed no-turn alarms.
This is a project benchmark, not a measured biological threshold.

## What we achieved

The final fixed model/cutoff was tested on 24 new rt rooms after 40 separate
negative-only calibration rooms. None of the new test responses chose a weight,
threshold or feature.

| Forward speed | Small turns detected with correct direction | Straight-walking alarms |
|---|---:|---:|
| 5.5 mm/s | 48/48 | 0/24 |
| 11 mm/s | 48/48 | 0/24 |
| 16.5 mm/s | 42/48 | 0/24 |

Fast direction counts are 21/24 in each direction. Larger +/-5-degree/s turns
are 48/48 at every speed; stationary alarms are 0/24. All 81 numerical-refinement
checks pass at the final cutoff. Independent arithmetic and exact replay checks
pass. [Final technical report](RAW_LOCAL_CALIBRATION_REPAIR_REPORT_V1.md),
[all fresh results](../results/raw_local_calibration_repair_v1/test_results.json).

## What changed, and why

The validated frontend, LPi-intact MaleCNS connectivity and neural parameters
stay frozen. We changed the artificial readout: it combines local T4/T5 signals
and downstream activity with structured bilateral features. It is neural-only,
but its learned output weights are not identified biological synapses.

The original local-normalization hypothesis failed (20/32 fast small turns).
Its raw comparison gave 30/32, prompting a separately frozen qualification.
That model passed development and all numerical checks but failed its first
new-room test because fast straight walking produced 5/24 alarms. We preserved
the failure, froze one negative-only calibration repair, and evaluated it on a
different new test. No encoder training or invented connectivity was needed
for this finite result.

On identical final-test neural scores, the earlier cutoff gives 45/48 fast
detections with 5/24 alarms; the new independently calibrated cutoff gives
42/48 with zero alarms. This directly demonstrates the decision tradeoff in
the model, without changing any neuron's response.

## Limits we must retain

- The earlier inspected st cohort still has **3/24 fast alarms** at the new
  cutoff. That result is not relabeled as a pass. The model is not reliable in
  every tested cohort; the new result is a bounded qualification.
- Twenty-four fresh rooms do not certify a population false-alarm rate below
  10%. More independent negatives and uncertainty estimates are needed for a
  stronger reliability claim, with the model/cutoff kept fixed.
- The same noiseless static-room generator supplies development and tests.
  Realistic noise, moving objects, other motion axes and hardware are untested.
- The readout accesses T4/T5 directly. It does not establish the biological
  HS/H2/bIPS/DNp15 mechanism, physiological validity or bIPS causality.
- Biological response mismatches remain because neuron dynamics were unchanged.
  No closed-loop motor controller was implemented.

## Evidence trail

1. [Local-subunit pilot: primary failure and raw control](LOCAL_SUBUNIT_PILOT_REPORT_V1.md).
2. [Unchanged raw control: development and all 81 refinements](RAW_LOCAL_QUALIFICATION_REPORT_V1.md).
3. [First untouched test: fast false-alarm failure](RAW_LOCAL_HELDOUT_REPORT_V1.md).
4. [Independent negative-only calibration and final untouched test](RAW_LOCAL_CALIBRATION_REPAIR_REPORT_V1.md).

All stages are separately versioned, with frozen criteria, exact sources,
quantitative outcomes and completion indexes. Compact features/scores and
recipes replace movie accumulation; all previous evidence is preserved under
the documented storage-retirement policy. The live
[progress report](PROJECT_PROGRESS_REPORT.md) records decisions and limitations.

## What is next

Keep this candidate fixed. The next reliability test should estimate false-alarm
uncertainty on a larger predeclared independent negative population, without
adjusting its threshold. The biological task requires matched recordings and
explicit measurement models, followed by controlled circuit-ablation comparisons.
A decoder pass alone cannot answer whether bIPS contributes biologically.

## Professor-ready paragraph

We obtained a neural-only open-loop decoder that meets our predefined small-yaw
simulation benchmark while preserving the MaleCNS circuit and frontend. With
an independently calibrated alarm threshold, a fresh 24-room test detected
48/48, 48/48 and 42/48 +/-2-degree/s turns across increasing walking speeds,
with zero observed straight-walking alarms, and retained all 81 numerical
checks. The normalization hypothesis and an earlier false-alarm failure are
preserved; the older cohort still contains a 3/24 fast-alarm counterexample
under the final cutoff. This is a bounded computational result, not physiological
validation or proof of a bIPS mechanism. Broader error-rate testing and matched
neural recordings are the next evidence needed.

## TL;DR

We can now read small turns from the frozen neural model well enough to pass
one rigorously held-out simulation benchmark. Some environments still cause
false alarms, and we have not shown that real fly neurons use this readout.
