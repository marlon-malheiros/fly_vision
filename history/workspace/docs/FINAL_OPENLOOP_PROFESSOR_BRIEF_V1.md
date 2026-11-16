# Professor brief: final open-loop milestone

2026-10-30. Study started 2026-10-29.

We completed a frozen test of whether bilateral DNp15 activity in our LPi-strengthened MaleCNS model supports small yaw-onset detection during forward walking, and whether bIPS improves it. We ran 2,424 new image episodes in 84 independent virtual rooms, using ten intact/control/lesion copies, fixed train-only external readouts, and 60 untouched test rooms. All three walking speeds and both yaw signs were scored, with straight-walking false alarms counted over two seconds.

| Speed mm/s | Yaw magnitude deg/s | Joint /120 | Negative /60 | Positive /60 | Straight endpoint /60 | Straight any alarm /60 | Criterion |
|---|---|---|---|---|---|---|---|
| 5.5 | 2 | 120 | 60 | 60 | 0 | 0 | pass |
| 5.5 | 5 | 120 | 60 | 60 | 0 | 0 | pass |
| 11 | 2 | 116 | 59 | 57 | 0 | 6 | pass |
| 11 | 5 | 120 | 60 | 60 | 0 | 6 | pass |
| 16.5 | 2 | 108 | 55 | 53 | 2 | 36 | fail |
| 16.5 | 5 | 120 | 60 | 60 | 2 | 36 | fail |


Combined neural capability: **failed**. Empirical detection gate: **fail**. Numerical capability gate: **fail** (14/81 refinement comparisons failed at least one gate). With the unchanged intact readout, bIPS silence reduced joint detection with an entirely negative nominal 95% interval in 0/6 primary speed/magnitude conditions, increased it with an entirely positive interval in 0/6, and had an interval including zero in 6/6. These repeated-condition intervals are descriptive and are not adjusted for multiple comparisons. A robust bIPS-dependent small-turn solution was not demonstrated because the intact candidate did not meet the full empirical target. Full lesion effects and paired room intervals are in the technical report; engineering comparators are identified separately. No neural, observation, cutoff or decoder-family tuning followed final inspection.

The code/graph/input identities, numerical checks and four deterministic replays are preserved. This establishes a reproducible computational result, not biological validation. The available independent physiology sources still have access/stimulus/measurement matching gaps; missing electrical coupling and the functional T4/T5 surrogate remain material limitations.

The next biological step is a separately frozen comparison against the published HS voltage source data, after its display registration and per-cell controls are audited. Model bIPS/LPi perturbations suggest experiments but do not establish biological causality. Closed-loop robotic control is deferred.

[Complete technical report](FINAL_OPENLOOP_MILESTONE_REPORT_V1.md).
