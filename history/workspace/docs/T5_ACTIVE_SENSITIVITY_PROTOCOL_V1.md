# Active T5 sensitivity and excitation/inhibition compensation — protocol V1

Client date: 2026-10-12 (America/Belem). Evidence timestamps use UTC.

Question: is the existing model's response-preserving flexibility confined to
filter timing, or can substantially different final excitation/inhibition also
preserve responses? A bounded local sensitivity analysis followed by a fixed
model-guided candidate bank answers a computational question. It adds no cells,
recordings, population validation, publication novelty or biological degeneracy.

## Inputs, coordinates and response sensitivity

Use all 78 previously completed native inputs: 18 original bars, 8 original
gratings, 32 challenge bars, 20 challenge gratings. Preserve their recorded or
synthetic clocks, source schedules, initial conditions and effective onset.
Replay all baseline voltages bitwise. Primary features are unchanged bar q0.995
peaks and grating half(q95−q05) amplitudes in their frozen windows; signed means
use the same respective windows. Grating means use each trial's neutral baseline.
Stack primary then mean: 156 features, scaled by max(abs(baseline feature),0.065 mV).
Rows are unweighted beyond that engineering normalization; no experimental error
bars or equal-population interpretation is inferred from the number of rows.

Canonical coordinates: log of sorted E fast/slow poles, sorted I fast/slow poles,
E/I gains, E/I Gaussian widths, plus additive E/I centers in native columns.
Time-unit rescaling leaves log derivatives unchanged. The unused parameter stays
fixed. Pole crossings are sorted back to the canonical quotient; permutations
cannot create a material candidate or a mechanism difference by themselves.

Central differences at **h=0.005 and 0.0025** in all ten coordinates. Use the
smaller-step Jacobian for candidate generation; larger step is a declared
stability check. Require relative Frobenius difference ≤5% and each column's
relative difference ≤10% (1e-12 denominator floor). If unstable, retain the
analysis and label its sensitivity interpretation provisional; actual candidate
response checks remain valid. Do not change the steps after scores.

Analyze singular values and right singular vectors of the full 156×10 Jacobian
and its gain/width/center-only 156×6 submatrix. The latter excludes timing to avoid
merely rediscovering the known cascade compensation. Deterministic vector sign:
largest absolute component positive. Report numerical rank with standard
machine-epsilon threshold, not an exact global identifiability claim. Units and
normalization affect singular values; small values imply local low sensitivity
under this metric, not an exact output null space.

## Frozen algorithm for 40 derived candidates

Parameters are generated **after** derivatives by the following frozen rule,
then the resulting bank is hashed before their response scores. This is
exploratory, model-guided parameter search on the same benchmark, not independent
held-out validation or physiological refitting.

- Full SVD: last two vectors, normalized to maximum absolute coordinate one;
  steps ±0.1, ±log(1.25), ±log(1.5): 12 candidates.
- Gain/spatial-only SVD: same two vectors and six signed steps, embedded into
  ten coordinates with all timing fixed: 12 candidates.
- Prescribed gain directions (E,I)=(1,1) or (1,−1) in log space; steps
  ±log(1.1), ±log(1.25). Compensate centers/widths only with linear least squares
  (rcond=1e-8), keeping all clocks fixed: 8 candidates.
- The same gain patterns/steps, with all eight non-gain coordinates available
  through ridge compensation minimizing mean squared normalized feature change
  plus 0.01×squared coordinate norm: 8 candidates.

Report all candidates. Reject values outside published parameter bounds without
clipping, replacement, iterative optimization, extra steps or adaptive expansion.
Pole sorting is recorded. Baseline, the known timing alternative, exact pole-swap
and E-gain ×0.75 mismatch references never count as new candidate wins.
At most 84 parameter sets / **6,552 trajectories**: baseline, 40 derivative sets,
40 generated sets and 3 references. Rejected generated sets reduce execution.

## Prospective output and mechanism gates

Every one of the 78 primary features and signed means must remain within 5%,
using the same response floor. All 39 direction pairs in each readout must keep
their raw sign, resolution and pass classes, and DSI differences ≤0.02. All
recorded-clock voltage traces must have max difference ≤5% of their baseline
trace maximum magnitude (floor 0.065 mV). Preserve weak/reversed baseline cases.
These are engineering tolerances, not uncertainty estimates or physiological fit.

Material distance retains the previous definition: ≥1.25 multiplicative distance
in at least two canonical positive coordinates, or ≥0.5-column center shift.
Compute final filtered conductance differences per E/I channel and trial,
normalized by that channel's baseline peak (floor 1e-12). A **material**, fully
output-equivalent candidate with **both E and I** differing ≥10% somewhere in the
benchmark qualifies as an E/I compensation candidate. Differences may occur in
different trials; report their locations and do not infer simultaneous changes
in a recorded neuron. Either channel alone ≥10% is a separate weaker category.
Intermediate filter-state or pole-label changes do not meet this mechanism gate.

Decision precedence over newly generated valid candidates only:

1. `E_I_COMPENSATION_CANDIDATE_FOUND`: material, all output gates, both conductances ≥10%.
2. `SINGLE_CHANNEL_COMPENSATION_ONLY`: material, all gates, either conductance ≥10%.
3. `ONLY_SMALL_CONDUCTANCE_EQUIVALENCE`: material output equivalence, neither ≥10%.
4. `NO_MATERIAL_OUTPUT_EQUIVALENCE_IN_LOCAL_BANK`: no new material equivalent set.

A negative bank is not proof of uniqueness or impossibility. Controls: known
timing reference retains previously verified primary/waveform equivalence over
all 78 conditions; score its newly combined mean gate separately. Pole swap
preserves voltage within 1e-8 mV; gain mismatch fails primary equivalence and
differs by >1e-4 mV. None can satisfy the new-candidate decision by itself.

## Validation and reporting

Test real input loading, complete windows/pairs, canonical baseline identity,
unused/pole symmetry, analytic finite differences, SVD reconstruction, gain
constraints, deterministic 40-set generation and bounds rejection before freeze.
Freeze code/config/plans/tests/inputs before derivative responses. Verify all nine
prior seals and their entries before/after. Review every executed voltage and
four-state trajectory with independent matrix-exponential integration, independent
stimulus reconstruction, quantiles/means, pair classes, all candidate/mechanism
decisions, finite-difference arithmetic, SVD reconstruction/orthogonality and
linear compensation equations. Numerical tolerances stay 1e-8 for waveforms/states,
1e-10 readouts and 1e-6 absolute scaled-Jacobian agreement. Record failures,
step sensitivity, rejected candidates, control scores and every new candidate.

Complete detailed report, simple summary, figures, append-only progress, local Git
checkpoint, study progress snapshot and immutable index. No remote publication.
Further evidence for biological claims would need independent cells/repeats and
appropriate stimuli; this analysis neither supplies nor estimates that evidence.
