# Native T5 mixed-benchmark parameter-sensitivity pilot — protocol V1

Client date: 2026-10-12 (America/Belem). Audit timestamps use UTC.

Question: do substantially different **active** parameters preserve the published
cell-7/iteration-52 model's responses to the completed bar/grating benchmark?
This is a finite exploratory pilot, with rules frozen before new responses.
It is not a refit, new biological validation, or a population degeneracy test.

## Fixed inputs and readouts

Use all 18 moving bars and 8 moving gratings, with the native schedules, actual
saved observation clocks, zero initial states, and the source's 25-ms effective
model input offset. Replay the existing baseline bitwise. The 26 primary features
are the bars' 0.995-quantile author-relative peaks in [0,duration), and gratings'
half (q95−q05) amplitude after discarding cycle 1 and retaining cycles 2–3.
Keep the 13 author/native direction pairs: 9 bar pairs (odd index PD), 4 grating
pairs (even index PD). Use the existing response/difference floors of 0.065 mV,
absolute DSI floor 0.1, and denominator epsilon 6.5e-11 mV.

Only native inputs are needed: the image implementation has already been checked
against these schedules. Eight geometry templates sharing one parameter set are
not eight independent physiological cells. No new recordings are available or
needed for this bounded computational pilot. Existing observed voltages are
retained as historical context and do not select parameters or tolerances.

## Candidate bank, fixed before evaluation

Use one baseline, **80 candidate sets**, and four symmetry controls (85 sets,
2,210 trajectories). Active positive coordinates are E/I rise and decay times,
E/I Gaussian gains, and E/I widths. Centers use additive native-column changes
because the E center is close to zero. All values remain within published fitting
bounds; the unused first parameter is fixed except in its explicit control.

- 40 single-coordinate changes: factors 0.75, 0.9, 1.1, 1.25 for eight positive
  coordinates, and center offsets −0.5, −0.25, +0.25, +0.5 for each center.
- Eight coordinated changes: both gains ×0.75 or ×1.25; E or I gain ×0.8 with
  width ×1.25, or gain ×1.25 with width ×0.8; I decay ×0.75 with rise ×1.25;
  I decay ×1.1 with rise ×0.9.
- 32 deterministic random sets: seed 20261012, log-uniform positive-coordinate
  factors in [0.75,1.25], center offsets uniform in [−0.5,+0.5]. These are a
  fixed finite search, not parameter optimization or a distribution over biology.
- Controls: unused parameter ×1.25; swap E rise/decay labels; swap I labels;
  swap both. They must preserve output within 1e-8 mV and never count as wins.

Sort the two time constants within each E/I cascade before measuring parameter
distance. The cascades' convolution factors commute from zero initial states;
label permutations therefore do not provide distinct input/output mechanisms.
A candidate is **materially changed** if at least two of the eight canonical
positive coordinates differ by a multiplicative ratio ≥1.25 (either direction),
or a center differs by ≥0.5 native columns. This is a declared engineering
definition, not a statistically estimated biological distance.

## Prospective comparison and decision

Feature equivalence requires **every** primary feature within 5% of baseline
(denominator max(abs(baseline),0.065 mV)), all 13 DSI changes ≤0.02, and unchanged
resolved status, expected-sign flag and pass classification in every pair.
These inherited engineering margins do not represent experimental uncertainty.
Direction preservation alone is reported separately as robustness.

Secondary diagnostics retain stimulus-window means, all recorded-clock waveforms,
and filtered E/I conductances. Full-waveform equivalence additionally requires,
in every trial, max(abs(candidate−baseline)) ≤5% × max(max(abs(baseline)),0.065 mV).
Report relative maximum E/I conductance differences using a 1e-12 denominator
floor; a change ≥10% in either conductance in any trial is an explicit internal
mechanism diagnostic, not an additional criterion chosen after scoring.
Raw voltage maximum error and pooled RMS error remain visible.

Decision: if any materially changed candidate meets feature equivalence, record
`LIMITED_FEATURE_EQUIVALENCE_FOUND`; otherwise `NO_MATERIAL_EQUIVALENCE_IN_PILOT`.
Either outcome completes the pilot; neither proves or disproves neural degeneracy.
No adaptive expansion, data fitting, or thresholds changed after scores.

## Validation and provenance

Freeze config, candidate bank, methods, tests, scripts, input hashes and prior
seven artifact indexes before execution. Check all predecessor entries before
and after. Run meaningful tests of material-distance symmetry, center scaling,
complete-bank bounds and all-feature/pair gates. Review all 2,210 waveforms with
an independent matrix-exponential solver; independently recompute readouts,
direction classes and comparison outcomes. Preserve controls, failures and all
outputs. Reports/figures and local Git checkpoints complete the study; copy the
live progress report into the study, seal hashes, leave the live report appendable.

Do not infer T4, HS/H2, texture generalization, cell-population validity, exact
parameter non-identifiability, publication novelty, or biological degeneracy.
Additional cells/repeats and broader stimulus tests would be required for stronger
biological conclusions. A negative finite search cannot establish uniqueness.
