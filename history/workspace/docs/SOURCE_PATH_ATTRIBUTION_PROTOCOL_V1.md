# Recurrent source-path accounting for the small-turn gap V1

26 October 2026. A bounded mechanistic investigation, preserving all sealed
results, neural parameters and original detection criteria. Existing outcomes
are known. Freeze the new decomposition and checks before computing its
components; this is a retrospective analysis, not a new held-out detection
benchmark.

Prior work establishes nonzero local yaw gain, scene-dependent offsets,
bilateral sampling asymmetry and approximately linear recorded downstream
activity. Label/loader consistency, generic saturation, broad decoder feature
searches and unconstrained circuit expansion are closed branches within their
tested scope. The input-mapping audit explicitly did not account for recurrent
neural outputs. That is the distinct question here.

## Question and fixed execution plan

Which existing external T4/T5 input groups contribute to the frozen circuit's
straight-walking offset and small-turn response? Do their contributions explain
why the published direction-field projection had little effect? Include all
sixteen eye x subtype groups and all original recurrent connections. No group
or model variant is selected from the new results.

1. Reuse all704retained V2primary episodes and all three fixed input versions.
   Their original4/16/24room split labels are retained for description, not
   reused as fresh validation of a newly selected classifier. Verify source
   arrays/network outputs against the old immutable index as each is consumed.
2. Construct the discrete adjoint of the zero-origin linearization of the
   original rate equations, using the original chemical matrix, parameters,
   1-msRK4boundary convention,10-mssource timestamps, motion initialization and
   [0.70,1.40)mean window. Output eight means: L/RforHS,H2,bIPS,DNp15. Retain
   T4/T5recurrence and wide-cell feedback. Empty electrical matrices remain
   empty; no electrical effect is inferred.
3. Contract the fixed source-to-output response kernel with each episode's
   actual source drives. Sum components by source eye and exact T4/T5subtype.
   This is accounting in a separately labeled linear approximation, not a
   replacement of the original nonlinear model. Archive kernels and every
   component; do not normalize groups or adjust gains.
4. Compare reconstructed means against original nonlinear outputs for all
   conditions. Primitive endpoint criterion:1%relative error with1e-5floor;
   bilateral differences:5%with the same floor. Also reconstruct scores of
   every existing frozen two-feature decoder; require absolute error≤0.02°/s
   before interpreting its decomposition. Original decisions remain the
   authoritative classification evidence. Approximate scores near a boundary
   cannot replace them.
5. Independently check adjoints against dense augmented-state RK4polynomials
   on a small recurrent toy system, including every input impulse: tolerance
   1e-12. On the four predetermined known walking controls, run all three
   versions through a fresh, separately generated linear forward solver and
   compare with adjoint endpoints within1e-10. Do not edit the old solver.
6. On those same four controls, independently replay the strict original
   nonlinear baseline intact and with each of the sixteen source groups'
   external drives omitted:68nonlinear trajectories, plus12linear trajectories.
   Omission removes external visual drive only; neurons and recurrent synapses
   remain. Compare actual intact-minus-omitted endpoints and bilateral
   differences with the group's predicted contribution under the same1%/5%
   floor criteria. All groups and all failed checks are reported. Effects are
   causal within these specified model interventions, not biological lesions
   or proof of biological causality.

## Analysis and evidence rules

For each room/speed/role/version, retain straight output q0=L−R, odd small-yaw
response [q(+2)−q(−2)]/2 and gain dividing that response by2°/s. Compare scene
variation of q0 with the size of the odd response. Apply the same contrasts to
all source-group contributions. Report cancellation explicitly; signed
components can oppose each other, so no percentages are reported as unique
causal shares. Within-room straight/turn contrasts are descriptive analysis,
not inputs to a working detector or a test-time baseline correction.

Retain the original decoder intercept separately from source contributions.
Report direction-field changes per group with unchanged network transfer.
No new decoder fit, cutoff search, weight balancing, retinotopic remapping,
noise calibration or circuit expansion. Failed approximation gates limit the
corresponding attribution claim; they do not trigger a relaxed tolerance.
Results cannot establish information loss for every possible neural decoder.

Produce reproducible code, full numerical evidence, independent checks,
figures, a concise report and an undergraduate explanation of what we did,
what we want and why. Append progress, preserve failures, retain a dated
progress copy and seal the completed study with live progress/AGENTS.md
excluded. Do not implement closed-loop control or claim physiological
validation, publication acceptance or completion of the broader PhD goal.
