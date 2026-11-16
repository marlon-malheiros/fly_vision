# HS temporal refinement V1 — frozen numerical follow-up

2026-11-02. Resolve the four reported temporal flags without changing the graph,
sigma, neural or frontend time constants, retinal geometry, 60 Hz/four-bit
stimulus, phases, observation model or tolerances. This is numerical verification,
not a new biological validation or a neural repair. Prior frequency recordings
and model outcomes are already inspected development evidence.

Exactly fourteen binocular input cases, both original and calibrated-gain
frontends. Preferred direction, phase zero, methods85 display only. Frequencies
0.5/1/2.5/15 Hz have middle (image 1.25 ms, source 2.5 ms) and fine (image
0.625 ms, source 1.25 ms) cases. At the two flagged frequencies also include:
solver_control (image 2.5 ms, source 5 ms), image_only (1.25/5 ms), and
fine_image (0.625/2.5 ms). All new primary solves use 0.25 ms RK4. Preserve the
compiled solver's absolute 1 ms forcing ramp; all source/solver ratios are
integers and every source interval exceeds the ramp duration.

The two solver_control inputs must match the sealed temporal cases bitwise in
image and source hashes. Replay each at the old 1 ms solver step and require
bitwise rates, final state and checkpoints. These four additional model solves
are included in the CPU budget. New observation solves total 28; exact replays
four. Source arrays exist in memory only; retain compact 100 Hz wide-cell rates,
summaries and hashes, not movies or full T4/T5 time series.

Endpoint: right HSN/HSE/HSS equal mean of atanh(rate), [2,4) seconds minus [1,2),
unchanged from the earlier round. Every numerical comparison uses the old,
fixed phase-zero PD1 Hz primary reference for its own frontend. Pass iff
abs(a-b) <= .05*max(abs(a),abs(reference))+1e-7 AND
abs(a-b)/abs(reference) <= .05. No tolerance relaxation, curve renormalization
to hide endpoint differences or outcome-driven extra refinement.

Primary numerical gate: middle→fine at all four frequencies/two frontends,
middle→fine_image and fine_image→fine at both flagged frequencies/two frontends,
and old temporal→solver_control at the flagged frequencies/two frontends.
Twenty endpoint checks in total. Supporting comparisons isolate image/source
contributions at the intermediate resolution and retain the old coarse failures.
Passing establishes agreement on these grids/endpoints only; it does not prove
asymptotic convergence, all phases/directions/frequencies or spatial convergence.
Failure ends this bounded round. Additional grids would need a new protocol.

Report all cases, replay failures and fine-grid frequency ratios. Compare the
sampled four-point subset with the already known source curve only descriptively;
do not substitute it for the sealed complete 15-coordinate biological test.
Numerical agreement cannot authorize biological-validation or walking-advancement
claims. No parameter fit, decoder change, new synapses or external data acquisition.

Whole-run estimate 32 MiB, cap 64 MiB, reserve 20 GiB; no source ZIP duplication.
CPU cap 3600 s, two workers, peak RSS cap 2 GiB per worker. Resource limits checked
before launch and between completions; in-flight work may finish after failure.
Freeze source/config/protocol and exact dependencies before any new execution.
Preserve all old artifacts. Independent endpoint arithmetic uses log1p rather
than atanh and checks every pass/fail decision. Save a dated progress snapshot,
source/report snapshots and an immutable index, then audit after writer exit.
