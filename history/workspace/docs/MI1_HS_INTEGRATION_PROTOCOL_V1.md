# Adaptive Mi1 branch to HS — fixed integration V1

2026-11-05. A separate development experiment; previous models, parameters,
reports, recordings and immutable artifacts remain unchanged. The recent Mi1
component result and all existing HS target panels are already known. This
experiment does not call those targets independent validation.

## Question and model copies

Does replacing ONLY Mi1 in the existing horizontal parallel-inhibition T4 model
improve HS motion responses? Earlier homogeneous slowing/adaptation studies
changed entire motion channels. The new intervention replaces the Mi1 branch
while leaving Tm3, Mi9, Mi4, CT1 and the T4 conductance integration fixed.

Three simultaneous intact MaleCNS graph copies:

1. `measured_Mi1`: previous `g1_k250_parallel_T5_slowing_only`, a sealed comparator.
2. `adaptive_Mi1`: Mi154ms low-pass followed by318ms high-pass, then existing
   branch rectification. These published nominal response-fit constants are
   fixed. All other upstream branches retain measured250ms-deconvolved kernels.
3. `Mi1_HP_removed`: remove the high-pass from2, retain its exact normalization
   and low-pass. This is a within-model component intervention, not a cell lesion.

Same original contrast normalization sigma, T4a/b routes, relative conductances,
voltage-to-drive bridge max(V,0)/60, T5 slowing-only source, all other sources,
LPi graph and numerical neural parameters. No graph edit, classifier optimization,
per-condition scale, fitted time constant or fresh physiological amplitude fit.

## Explicit coupling assumption

Mi1's earlier calcium fit cannot calibrate neural conductance. Do not inject its
250ms calcium observer or dF/F gain into the circuit. For the adaptive neural
branch use exact continuous two-state propagation under held contrast. Establish
a fixed scale before HS outputs: its discrete unit-impulse response sampled at
1/240s over1s has unit L2 norm, matching the author measured-filter convention.
Keep this scale at every finer dt and also in the HP-removed diagnostic. Preserve
full state memory rather than truncating the adaptive tail to1s. Static image
prehistory is equilibrium: adaptive output0, LP diagnostic output its steady
input. This is a transparent source-convention bridge, NOT a measured
voltage/release calibration or anatomical Mi1 reconstruction. Successful HS
scores cannot remove that limitation. Replace the old Mi1 kernel; do not
prepend another adaptation filter to an already measured intact kernel.

## Inputs, scores and frozen continuation rule

Exactly the previous methods85 field, binocular grating,60Hz refresh/four-bit
luminance and2s static/2s moving/1s static. Four frequencies0.5/1/2.5/15Hz,
preferred/null directions;50% contrast at1Hz both directions; stationary control:
11 primary inputs. Four inherited clock refinements (PD0.5,1,15 and half-contrast
ND), plus PD1 half-solver and0.5deg horizontal-sampling controls. Total15 inputs,
17 packed solves x3 copies. No movies or permanent large source bank.

Primary clocks: images1.25ms, source2.5ms, solver0.25ms. Fine images0.625ms,
source1.25ms; half solver0.125ms. Preserve inherited1ms forcing ramp. Readout is
right HSN/HSE/HSS equal mean atanh(rate), motion[2,4)s minus static[1,2)s,
normalized by each model's own positive preferred1Hz endpoint. Compare the SAME
seven frequency coordinates and existing bands, plus both half-contrast bounds.
These are previously inspected descriptive source bands, not verified
animal-level equivalence margins. Report absolute and normalized curves/signs.

Advance `adaptive_Mi1` to independent-recording work ONLY if all:

- All numerical/source parity checks pass, finite bounded sources, zero clipping;
- positive PD1 reference and nonnegative PD at all four frequencies;
- frequency RMSE strictly below the sealed comparator0.2960812708552639;
- frequency band violations no greater than comparator4;
- absolute full-contrast ND/PD error no worse than comparator0.16029395271063274;
- both half-contrast endpoints inside unchanged source bands;
- stationary endpoint and pre-motion drift <=5% of own PD1 reference +1e-7.

All conditions must hold; one improved metric cannot rescue a failed guard.
The HP-removed copy is descriptive and cannot replace the primary after scoring.
If any guard fails, STOP this candidate without tuning and do not consume another
independent recording. If every guard passes, freeze this exact whole-model
version before searching/matching independent HS recordings; if required
measurement coupling or recordings remain unavailable, report that gate rather
than claiming validation. No walking or closed-loop test in this experiment.

## Verification, budget and preservation

Before new HS outputs: impulse normalization, causal-prefix/static-equilibrium
and independent ODE/continuous-frequency checks. Check the continuous adaptive
branch plus calcium observer against the recent Mi1 proxy within2% relative RMS
after removing the KNOWN branch normalization, with no fitted alignment/gain.
Check packed backend against the unchanged single-copy backend on synthetic input.
During execution require comparator input/rate/final-state/checkpoint parity
with all available strict archived cases. All non-horizontal-T4 input columns
are shared exactly. Confirm18 numerical endpoint controls (6 per copy) within
the inherited5% own-PD1 normalization and1e-7 absolute limit. Independently
recompute endpoints via log1p and scalar scores/decision, and save raw group
responses for HS/H2/bIPS/DNp15 with their exploratory status.

One CPU worker,3600 total scientific CPU seconds,3GiB peak RSS,128MiB output cap,
20GiB free reserve. Record complete-case resources and failures; do not overwrite
partial failed cases. Verify prior Mi1 V2 and factorial indexes unchanged.
Append progress, save dated progress/report/method copies in this study; seal
after all writers exit and independently rehash afterward. Live progress and
AGENTS stay outside immutable indexes. Distinguish numerical reproducibility,
development agreement, supported model interventions and biological validation.
