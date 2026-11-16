# Branch-specific adaptive Mi1 integration and HS motion test V1

Completed2026-11-05. **Decision: STOP this candidate without retuning.**
Full biological validation remains unestablished. This executes the proposed
next milestone: one fixed branch integration, matched HS motion cases, numerical
controls and a stopping decision. It is not another classifier optimization.

## What was tested

The [protocol](MI1_HS_INTEGRATION_PROTOCOL_V1.md), equations, input cases and
stop criteria were committed at `0197d2c` before new visual-network responses.
All HS recording targets and prior integration results were already known.
Thus this is DEVELOPMENT, not independent physiological validation. No new
recording or fresh animal was consumed. Recent Mi1 calcium evidence motivates
the candidate; it does not calibrate its synaptic coupling or certify the circuit.

Three copies of the same complete selected LPi MaleCNS chemical graph use
identical visual input and numerical parameters. The comparator is the sealed
`g1_k250_parallel_T5_slowing_only` model. The candidate replaces only Mi1 in
its parallel-inhibition horizontal T4 mechanism: nominal54ms low-pass then318ms
high-pass, followed by branch rectification. Tm3, Mi9, Mi4, CT1, their measured
filters, spatial offsets and conductance parameters are unchanged. T5 and all
non-horizontal-T4 sources retain the same slowing-only frontend. The diagnostic
removes Mi1 high-pass while retaining its low-pass AND candidate scale.

The existing contrast normalization, old-to-old connectivity, source-to-body
mapping, eye registration, neural poles/gains and classifier remain fixed. No
parameter is fitted to these HS responses; no biological connection is invented.
The earlier homogeneous-channel adaptation experiments are different
interventions and remain unchanged. This candidate substitutes a Mi1 branch,
without adding another filter in front of an intact measured Mi1 kernel.

## Coupling and physiological limitations

The adaptive branch is propagated exactly as a continuous two-state system with
held images, retaining full memory and equilibrium static prehistory. Its
1/240s one-second impulse has unit L2 norm under the source convention; fixed
scale is5.510152702. That SAME
scale is used for the HP-removed control and all clock refinements. Calcium
gain2.972928 and250ms observation dynamics from the Mi1 benchmark are NOT placed
into the neural pathway. The unchanged T4 bridge remains max(V,0)/60.

This normalization matches a model convention, not measured Mi1 voltage or
synaptic release. Its relation to other input conductances is not physiologically
calibrated. The 1D horizontal embedding, inherited count-to-weight normalization,
uniform single-neuron dynamics and missing electrical conductances remain
limitations. A failure cannot uniquely identify the adaptive mechanism as wrong;
a success could not eliminate these coupling assumptions. This is a functional
Mi1 proxy rather than an anatomical Mi1 reconstruction.

## Inputs and quantitative results

Fifteen binocular image cases,17 packed solves and three graph copies (51
trajectories) completed: four frequencies0.5/1/2.5/15Hz in preferred/null
directions;1Hz half-contrast preferred/null; stationary; four inherited finer
clock inputs; and two additional preferred1Hz solver/horizontal-sampling solves.
Display60Hz/four-bit, methods85 field,2s static/2s moving/1s static. Primary
image/source/solver steps1.25/2.5/0.25ms; fine0.625/1.25ms, half solver0.125ms.
The readout is right HSN/HSE/HSS mean atanh(rate), motion[2,4)s minus static
[1,2)s, divided by own preferred1Hz. This is an arbitrary-unit graded-state
proxy, not calibrated membrane voltage. The source bands are descriptive known
recording comparisons, with prior stimulus-label/animal-identity qualifications.

| Model | Frequency RMSE | Band violations | Full ND error | PD50/full | PD15/full |
|---|---:|---:|---:|---:|---:|
| measured_Mi1 | 0.296081 | 4/7 | 0.160294 | 0.962157 | -0.075529 |
| adaptive_Mi1 | 0.276927 | 6/7 | 0.220500 | 0.965364 | 0.138937 |
| Mi1_HP_removed | 0.339270 | 5/7 | 0.041037 | 0.960942 | -0.126208 |

| Hz | Recorded PD | Comparator PD | Adaptive PD | HP removed PD | Recorded ND | Adaptive ND |
|---|---:|---:|---:|---:|---:|---:|
| 0.5 | 1.068203 | 0.605873 | 0.689090 | 0.605239 | -0.355941 | -0.081373 |
| 1 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | -0.299986 | -0.109600 |
| 2.5 | 0.676028 | 1.225406 | 1.165452 | 1.288368 | -0.045738 | -0.113635 |
| 15 | 0.076436 | -0.075529 | 0.138937 | -0.126208 | -0.070846 | 0.111932 |

The adaptive branch changes the preferred15Hz ratio from
-0.075529 to
+0.138937; the recorded value is
+0.076436. In the HP-removed diagnostic that ratio is
-0.126208.
However, the adaptive null15Hz ratio is
+0.111932, versus recorded
-0.070846. The preferred-sign improvement therefore coexists with
incorrect opposite-direction excitation. Frequency RMSE improves while band
violations increase. This is a demonstrated conditional effect of the fixed
high-pass component inside these equations, not proof that manipulating Mi1
in a living fly would produce the same outcome.

The primary frozen guards that fail: **frequency_violations, null_error**.
Full per-model guards and source/endpoint values are in
[comparisons.json](../results/mi1_hs_integration_v1/comparisons.json);
[frequency figure](../results/mi1_hs_integration_v1/frequency_comparison.png).
Absolute endpoints and both half-contrast values are retained, including
unfavorable signs. No diagnostic replaces the primary after scoring. Group
HS/H2/bIPS/DNp15 left/right endpoints are retained in
[group_responses.csv](../results/mi1_hs_integration_v1/group_responses.csv);
only the predefined HS readout is scored physiologically in this study.

Static and moving HS means are separately retained in
[HS_epoch_means.csv](../results/mi1_hs_integration_v1/HS_epoch_means.csv), so a
change in baseline cannot be mistaken for a direct increase in evoked activity.
An explicitly exploratory reconstruction retains T4a/b external-drive pools
for the SAME1/15Hz preferred/null cases; its ranges match the saved runs. These
are bounded injected visual signals, not recorded T4 neural activity, and no
new circuit solve/lesion is performed. See
[interface pools](../results/mi1_hs_integration_v1/T4_external_drive_pools_exploratory.csv).

## Verification and resources

Three impulse/static/independent-ODE/causality test functions pass. On synthetic
input the packed and old single-copy backend match bitwise in rates, final
states and checkpoints. The continuous branch plus calcium observer reproduces
the recent Mi1 proxy within0.660653% RMS after removing the KNOWN source scale,
without fitting a sign, gain or time shift.

All15 comparator trajectories and their complete final-state/checkpoint hashes
match strict archived runs bitwise. The non-horizontal-T4 source columns are
shared across copies. A separate reconstruction through the ORIGINAL factorial
rendering code verifies the entire preferred1Hz comparator input byte-for-byte.
All45 primary/fine model endpoints are independently reconstructed via log1p;
the primary analyzer independently reconstructs scalar frequency scores and bands.
Numerical endpoint controls pass18/18; maximum normalized change
1.078843%. This verifies implementation
consistency, not biological correctness. Every old Mi1 V2/factorial/source index
rechecks unchanged, excluding historically retired movie archives from this claim.

Case CPU2015.14s; independent full-source reconstruction
CPU176.74s; peak case RSS
1.266GiB. These are recorded case/review
costs, not a claim that earlier pre-freeze setup CPU was measured. One worker,
3600scientificCPU-second cap,3GiB peak,128MiB output,20GiB reserve. No movies
or permanent input-bank archive. NumPy scalar JSON types are converted by a
separately frozen transport adapter; no scientific formula changes. Runtime
failures, if present, are retained separately and must be disclosed below.

## Decision and what follows

The chosen candidate's advancement flag is **False**. The independent-HS
stage is conditional on ALL development guards. This report does not relabel
known source data as held out. The diagnostic is a model component intervention,
not a biological cell lesion or proof that a synapse causes the computation.

This exact candidate is closed without retuning. The independent-HS stage was not executed because its predeclared development gate fails. No new independent recording was consumed. The next useful constraint is paired preferred/null motion selectivity at the T4 interface and physiological Mi1/Tm3 output coupling, rather than another HS classifier or output-gain fit.

The supported alternatives are to constrain Mi1/Tm3 relative conductances,
output coupling and spatial motion responses using independent physiological
measurements, or use an upstream circuit whose motion selectivity is already
independently constrained. Repeatedly normalizing branches against these same
HS responses is not independent validation. A single positive output-observation
gain cannot repair the normalized preferred/null discrepancies, because it
cancels in the ratio to the same preferred1Hz reference. Relative branch coupling
and nonlinear measurement models remain distinct, untested possibilities.

The recent limited Mi1 flash result remains valid in its original scope and
does not automatically validate an integrated motion circuit. These results
do not establish biological impossibility, downstream bIPS/DNp15 physiology,
electrical-circuit validity or a biological2deg/s threshold. The original
artificial small-turn readout and its bounded qualification remain unchanged;
no new walking result is inherited by this candidate.

## Reproduction and preservation

Scientific project Python with `PYTHONDONTWRITEBYTECODE=1`,
`OPENBLAS_NUM_THREADS=1`, `PYTHONPATH=src`. Run
`scripts/mi1_hs_integration_v1.py prepare`, then
`scripts/mi1_hs_integration_cli_v1.py freeze_io`, `run`, `analyze`; then this
completion script with `review` and `report`; finally transport CLI `seal`
and `verify` in separate processes after writer exit. Inputs are checksum-linked
to old artifacts; never overwrite this study on replay. Before-response source
manifests, all compact trajectories, source/state hashes, numerical controls,
exact methods/report and dated progress copy are retained. Live progress and
AGENTS remain outside the seal.

## Undergraduate explanation

We want a neural fly model that detects gentle turns and agrees with real
neurons. We asked whether the Mi1 component that predicted flashes also helps
the larger motion circuit. We replaced only that component and kept the rest
fixed. It corrected the response to fast motion in the preferred direction,
but the model also responded incorrectly to fast motion in the opposite
direction. We stop this particular integration because it does not meet all
the rules set beforehand. Passing a flash test and working correctly inside
a motion circuit are different requirements. The earlier functional turn
detector is preserved, but this study does not complete biological validation.

## Post-outcome interface appendix

The [interface diagnostic](MI1_HS_INTERFACE_DIAGNOSTIC_V1.md) quantifies the already reconstructed input pools: at15Hz the absolute difference between opposite-direction right-eye T4a/b pool means declines about95–97%. This concerns external-drive pool averages, not cellwise biological T4 selectivity or a unique causal pathway. It supports constraining intermediate T4 motion tuning before another full-HS integration attempt. All original criteria/results remain unchanged.
