# Where the neural-model work stands

1 November 2026.

**Our goal:** a fly-like neural model that detects tiny body turns during walking and agrees with real neuronal recordings.

**What we completed:** 384 new neural simulation conditions, a full published neural vision pipeline, two camera interfaces, four learned readers, numerical checks and independent reviews. We preserved the original models and results. The best previous neural-only reader still detects 143/144 simulated 5-degree/s turns with zero observed straight-walking alarms in its 24 held-out rooms.

**What did not work:** none of the new candidates meets the 2-degree/s goal. At cutoffs that remove calibration false alarms, the strongest new classifier detects only 1/12 fast small turns. No candidate advances to the reserved new rooms. Good training performance did not carry over to other rooms.

**Why biology remains open:** wiring alone does not give the correct dynamics, optical mapping or measurement model. LPi feedback is already present; simply adding it again is not a solution. Existing recording comparisons are partial and mixed. Simulations cannot manufacture the missing biological evidence.

**Better next direction:** build a smaller, physiology-calibrated motion-opponent circuit using the available anatomical evidence and published implementation references. Verify neuronal responses before extending its yaw task. Keep the successful 5-degree/s reader as a working comparison, and keep 2 degrees/s as an explicitly unfinished target. This does not prove that tiny-turn detection is impossible.

[Complete findings and limitations](NEURAL_MODEL_OPTIONS_REPORT_V1.md), [all learned-reader results](PUBLISHED_POPULATION_YAW_REPORT_V1.md).

**TL;DR:** We have a bounded 5-degree/s neural detector. The tested stronger pipelines and repairs still fail at 2 degrees/s. The next useful work is physiological calibration, with independent recording tests, rather than claiming a validated fly circuit from classification alone.
