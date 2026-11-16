# Horizontal opponency: two frozen development-stage tests, V1

2026-10-27. User authorizes both the recorded horizontal LPi reconstruction and
the alternative functional opponency diagnostic. Preserve every earlier graph,
frontend, recording, criterion and artifact. These are known development data,
not fresh physiological validation. No electrical conductance is invented.

## Inputs and candidates fixed before new responses

Use the eight sealed `aligned_100` source arrays: two dot seeds, yaw,
translation cue, left-only and right-only motion. The inherited 45 degree/s
dot protocols last 13 seconds. This does not test small walking yaw thresholds;
the translation cue is not a full 3D walking scene. Retain the inherited 10 ms
input clock, RK4 1 ms step, last-1-ms input ramp, parameters and zero initial state.

Four copies:

1. `expanded_intact`: reuse the sealed 13,618-cell expanded control exactly.
2. `lpi_intact`: append MaleCNS bodies 10066, 10308, 10436, 11041, 11709,
   13310 (LPi21/LPi12) in this order. Include every recorded incident chemical
   edge whose other endpoint belongs to this enlarged selection, including
   feedback and LPi-to-LPi edges. Keep the original old-to-old integer counts.
   Use negative presynaptic signs for these six GABA-consensus candidates and
   the inherited signs for all existing cells. Normalize each postsynaptic
   row by absolute incoming count sum, using the original normalization rule.
   The shared 20 ms pole and sign-as-NT approximation are explicit assumptions,
   not newly measured LPi physiology. Omitted partners are counted and retained
   as a ledger; no edges to them are invented.
3. `lpi_silent`: identical enlarged normalized graph, but clamp all six LPi
   outputs/states inactive. Do not renormalize. This distinguishes activity
   effects from the changed incoming denominators.
4. `functional_opponent`: keep the original expanded cells, parameters and
   all non-T4/T5-to-HS/H2 entries. Replace that one matrix block by a fixed
   balanced opponent diagnostic. For each target, source eye, and T4 versus T5
   class, let S be the sum of its existing direct weights from that group.
   HS preferred subtype is a, H2 preferred subtype b. Distribute +S over its
   recorded preferred edges in proportion to their original weights and -S
   uniformly over all opposite-subtype cells of the same eye and T4/T5 class.
   The direct current is S times (weighted preferred mean minus null mean).
   Remove the group's original null/vertical excitation; no renormalization or
   free gain. Equal preferred/null activity cancels, and preferred-only uniform
   activity retains the group's old total direct-current scale. If S is nonzero
   but no preferred edge exists, fail instead of selecting another rule.
   This adds artificial signed effective weights and changes spatial pooling.
   It is a sufficiency diagnostic, NOT an anatomical reconstruction, an LPi
   conductance estimate, or a biologically validated replacement frontend.

Use the already audited raw LPi incident-edge CSV, original integer core counts,
identities and NT predictions, with exact hashes and independent count checks.
No response-dependent membership, strength, time constant or decoder selection.

## Frozen analysis and decision rules

Primary observation mapping: transfer all eight original reporter/compartment
models without refitting. No new calcium-filter or gain search. Score all 234
known recording summaries with the inherited masks, clock, soma alignment,
normalizations and equal-fly aggregation. Retain the low-response DNp15 fly.
For primary DNp15/GC6f/WT and bIPS/sytGC7f, report full-window mean and median
per-fly skill, ratio of equal-fly mean squared errors, all per-fly errors and
leave-one-fly-out sensitivity. These are distinct estimands; none replaces old
primary results. Also report bilateral and unilateral performance separately.

Report every seed/side's raw HS, H2, bIPS and DNp15 motion means, peak-window
means, signed contrasts, yaw/translation magnitude indices and left-minus-right
traces. For DNp15, preferred yaw is first epoch on R, second on L; null is the
other epoch. Translation first epoch is the unwanted regressive response,
second the forward response. Report positive null/preferred and regressive/
forward ratios, plus the signed amplitudes. Epochs are 2–4 and 9–11 seconds;
steady windows 3.5–4 and 10.5–11; local baselines 1–2 and 8–9. Undefined ratios
when the preferred denominator is nonpositive are failures, never zero success.
The decision ratios use full-motion means after subtracting each local baseline;
steady-window ratios are reported as secondary diagnostics.

For each new active candidate, call the specific unwanted-response hypothesis
supported in this assay only if both ratios decrease versus expanded control
in all four seed/side cases while both desired amplitudes stay positive.
Compare LPi intact also against LPi silent to attribute changes within this
model to activity rather than normalization. Call a candidate worth external
benchmarking only if this sign/ratio condition holds AND primary DNp15 median
skill and pooled-error skill do not decrease AND bIPS mean magnitude index is
at least as close to the observed primary index. These are development decision
rules, not a quantitative biological acceptance threshold. Report every failed
component and all candidates even if no candidate qualifies.

## Numerical verification and alternatives

Before outcomes: compile every new Python source; test balanced/opposite/zero
functional currents; audit graph membership, signs, retained integer counts,
normalization, untouched functional blocks and exact silencing masks. Freeze
source/config/protocol/input hashes in Git before new neural responses.

After execution: replay expanded control for bitwise parity; independently
integrate saved 3.5–3.51 s checkpoints using Python RK4 and verify source-role
currents for all cases. For all three new variants run independent fixed-forcing
reference kernels at 1 ms (exact production parity) and 0.5 ms (maximum rate,
state and current error below 1e-7). Independently recompute recording metrics,
indices, aggregation and new ratios. Inspect figures; retain any failures.

If anatomy helps and criteria pass, freeze it for independent electrophysiology
and then new walking yaw tests. If only functional subtraction helps, missing
opponency is a useful computational hypothesis but the anatomical/dynamic
implementation remains unresolved; seek receptor/dynamics constraints rather
than tuning LPi strength for the desired answer. If neither helps, examine
stimulus/measurement and broader circuit omissions using new evidence. Further
H2rn cuts remain a narrow mechanism alternative, not a necessary next sweep.

Save code, full arrays, receipts, figures, a technical report and an undergraduate
explanation. Append progress, archive a dated progress copy, seal the study and
verify all indexed files after the sealing process exits. No closed-loop control.
