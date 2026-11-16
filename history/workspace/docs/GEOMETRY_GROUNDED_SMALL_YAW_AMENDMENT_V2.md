# Small-yaw implementation amendment V2 before unused-room testing

25 October 2026. [Original scientific protocol](GEOMETRY_GROUNDED_SMALL_YAW_PROTOCOL_V1.md)
and checkpoint c2df8dc remain preserved. Its twenty known-room pilots and
64 H2 inputs execute in V1; no V1 development/test sweep was executed. The
previously unused rooms have not been generated or scored. The full main
study proceeds in **results/geometry_grounded_small_yaw_v2**, retaining V1.
Do not claim completion of an unexecuted 704-episode V1 main sweep.

The V1 image-only means show scene biases during fast forward walking:
LK straight estimates −0.648/−0.856°/s and subspace +0.428/+1.156°/s in the
two known pilot rooms. Ideal synthetic yaw accuracy therefore does not
establish walking accuracy. Add two predefined robust controls before
development and unused test outcomes: weighted median of the local
translation-cancelled LK yaw estimates (weights: existing conditioning ×
geometric information); weighted median of the per-block subspace yaw
estimates (weights: their existing residual angular information). There
is no fitted gain, bias, quantile, spatial scale or rejection threshold.
Both original weighted means remain reported. All four methods use the
same original derivative/support settings and calibration-cutoff rule.
This is an engineering readout revision based on known diagnostic rooms,
not a new biological pathway or a neural parameter fit.

The source-constrained T4 and T4/T5 neural versions are unchanged. Their
V1 H2 trajectories can be reused exactly with explicit copying/hash records.
V2 known pilots recompute image references on the identical saved movies;
retain copied V1 source/neural arrays and verify both original mean time
series within 1e-12. No new model is selected using H2 or pilot outcomes.

Use six independent one-thread CPU workers, within the host's twelve
logical CPUs. This changes throughput only. Use the already implemented
degree-13 small-argument tanh approximation, with libm fallback outside
|state|<=0.125, to accelerate the same neural equations. A predetermined
same-source comparison on s07 fast +2 T4 and s12 fast −2 T4/T5 uses strict
C++, accelerated C++ and full-prefix original Python. The new stricter
acceptance tolerance is 1e-12 for every recorded rate/final state; preserve
all outputs/timings. This is numerical acceleration, not neural tuning.
The V1 strict baseline and all numerical parameters remain unchanged.

Keep the 704 main episodes, four known training rooms, sixteen calibration
rooms and twenty-four fresh test rooms; original 80/80/10 gates, fixed ridge,
bootstrap and numerical checks. Report all four image methods and all
three neural versions, without choosing the best test result as a validated
biological model. Count multiple engineering controls as exploratory
comparisons. No true depth/speed/yaw, world labels, zero-yaw partner, learned
image gain/bias or neural trace enters the image estimators.

Freeze the V2 config, wrapper, robust implementation, unchanged V1 source
dependencies and explicit reuse before V2 outcomes; freeze readouts again
before generating unused-room inputs. Preserve failures and negative results.
An engineering success remains distinct from a reliable MaleCNS neural
detector. Previous physiological, registration, specimen and closed-loop
limitations remain.
