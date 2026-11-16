# Physiological factorial search V1

2026-11-04. The user authorizes an exhaustive search. This is exhaustive over the
finite grid below, **not all possible neural models or missing biological facts**.
All previously inspected recordings remain development data. No fresh-animal
validation, closed-loop work, yaw-decoder fit or biological-validation claim.

## Audit and finite hypotheses

Preserve every previous model/report/result, including the stopped T4 pilot.
Its contrast regression and fast preferred-sign error motivate this search.
Earlier full published T4/T5 population attempts, LPi additions, gain-only
observation fits, generic temporal components and decoder searches already have
results. Do not relaunch them as untried ideas. Recurrent T4/T5 chemical edges
are present (200,460 nonzero source rows); no feed-forward shortcut may drop them.

Cross all2x3x3x4=72 combinations:

1. Existing fixed contrast normalization off/on; **reuse** sigma from its earlier
   calibration, do not refit. With gain on, apply the retained7x7 contrast-energy
   rule to signed contrast before published T4 filtering. The footprint stays at
   seven1deg sample positions under horizontal refinement. A unit test verifies
   equivalence to the old2D rule, including elevation boundaries.
2. All three public author input-kernel files, deconvolved with200/250/300ms
   calcium assumptions. These are uncertainty in the measurement model, **not
   fitted neuron time constants**. Same Laguerre/PCHIP processing, FIR support,
   conductances, reversals, spacing and60mV voltage conversion.
3. Published parallel, Mi4-only and CT1-only architectures. Single-arm source
   gains follow the authored historical comparator (.3 surviving arm), not an
   anatomical lesion. They are diagnostic comparators; only parallel models can
   qualify for further development because the single-arm models fail known
   perturbation constraints. Never count a mutant kernel as a wildtype repair.
4. Four existing T5 functional partners: none/slowing/adaptation/both. Only T5
   channels change with this factor; vertical T4c/d always retain slowing-only.
   Horizontal T4a/b use the selected published source. No graph/neural parameters
   or subtype routing/eye coordinates change.

Thus24 primary candidates and48 historical-architecture diagnostic candidates
are all evaluated in the intact graph. Add four complete legacy frontend
reference copies and four matched T4a/b external-input-omission copies:80 graph
copies per screen. Input omission retains neurons and recurrent edges and is
not biological silencing. It localizes contributions within the model.

The voltage-to-network bridge remains unmeasured. Do not sweep arbitrary gains,
conductances or invented electrical connections to fit target curves. A common
positive observation multiplier cannot repair normalized ratios (it cancels);
record this analytic exclusion. Reusing frozen gain is a separately declared
functional assumption, not proof of anatomical gain circuitry.

## Source controls and numerical backend

For every gain/kernel/architecture family, reproduce WT and six measured-kernel
substitutions over the author's61 periodic-bar velocities and four outputs.
Retain all shifts, failures and aggregate/per-velocity direction preferences.
For a parallel primary candidate, the source gate requires all six known shift
directions plus aggregate PD preference for WT and both inhibitory substitutions.
The small Mi1 RNAi direction is not a significant experimental finding; these
are qualitative source-consistency checks, not six new independent validations.
Gain changes the source computation, so its compatibility must be tested anew.

The new packed-input backend copies inherited RK4, activation, active mask,
weights, parameters and the absolute1ms source ramp. Every copy has its own
external drive. Synthetic controls have already verified bitwise rates, final
states and checkpoints against the original binary, including states above the
approximation threshold. The original source and binary remain unchanged.
Performance selection of the1.25ms screen step used synthetic inputs only;
recorded responses did not choose the numerical method. No linear approximation
is used for neural screening.

All72 visual variants are evaluated at the cheaper1.25ms RK4 screen step.
Repeat **all80 copies** at the strict0.25ms step for primary PD1Hz and PD15Hz.
Use the inherited5% relative/reference endpoint test per copy. Failed numerical
checks are numerical uncertainty, not evidence of biological failure. At the
strict step, baseline neural rates/final/checkpoints must reproduce old results
bitwise; the nominal raw250ms/parallel/slowing partner must reproduce the stopped
pilot. All old corresponding images and four legacy source hashes must match.

All primary and confirmation images preserve methods85 field,60Hz/four-bit
display,0.04cycles/deg,5s static/moving/static timing, phase0 and both eyes.
Primary image/source clocks remain1.25/2.5ms. The published model uses the same
full360deg horizontal support, static FIR prehistory, row-wise embedding and
rectified voltage/60 as the pilot. All assumptions remain explicit.

## Screen, selection and confirmation

Ten primary cases: four frequencies0.5/1/2.5/15Hz x PD/ND, plus half-contrast
PD/ND at1Hz. Save every copy's rates/endpoints and source hashes. Use the same
right HSN/HSE/HSS mean atanh(rate), [2,4) minus[1,2), existing target bands,
and each model's own positive PD1Hz anchor. Invalid/nonpositive anchors remain
reported and fail qualification. Do not drop flies, change bands or fit scores.

Freeze new-study development guards before candidate outputs:

- both all-copy strict-step controls pass;
- source gate passes and architecture is parallel;
- positive PD1Hz and all four preferred endpoints nonnegative (the last pilot's
  sign error motivates this **new prospective** guard; no old decision changes);
- frequency normalized RMSE<=0.29721958636380597, band violations<=4;
- full-contrast null/PD error<=0.18569700730084931 versus the existing contrast
  target, and both half-contrast coordinates inside their existing bands.

These are development-improvement gates, not complete physiological acceptance.
Rank all72 transparently and retain Pareto trade-offs. For confirmation, select
up to three **parallel** candidates with different gain/kernel families: take
the best T5 partner within each of the six families, then rank families by
(number of failed development guards, number of nine primary band violations,
maximum standardized primary discrepancy, nine-coordinate RMSE, fixed ID).
The source-consistent families rank ahead of failed source gates. No reranking
after confirmation. Failed-source finalists may be retained as diagnostics if
no source-consistent family exists; they cannot qualify.

Re-evaluate those finalists at strict0.25ms over all ten primary cases, reusing
the two complete strict screen cases, and a stationary control. Check four
joint image/source refinements (PD0.5/1/15Hz and half-contrast ND), plus one
half-solver and one0.5deg horizontal-sampling control at PD1Hz. Numerical tests
retain5% tolerances. Stationary endpoint/baseline drift each must be<=5% of the
strict PD1Hz reference. All source drives must remain finite[0,1] with no clipping.
Keep all source/measurement/functional-model assumptions separate.

A constant-input fixed point and contractive error bound may screen stationary
stability for every variant without another5s sweep. Use the actual graph's
L-infinity contraction (<1) and a verified residual bound, not a linearized
model. Direct stationary finalist simulations remain mandatory; report the
analytic bound and actual checks separately.

Only if a finalist passes **all** strict development/source/numerical/stationary
guards, expand it to the full existing frequency/contrast bank: add0.1/0.2/5/7.5Hz
both directions and contrast0.1/0.25/0.75 both directions (14 cases), without
refitting. Those are confirmation conditions unused for selection in this round,
but older inspected recordings and gain-calibration contrasts are **not fresh
validation**. Preserve source missingness/bands and exclude the original PD10/25
calibration coordinates from acceptance. If none qualifies, stop after finalist
verification rather than spend more simulations on known failing candidates.
Phase pi/2 robustness at0.5/15Hz PD/ND is likewise conditional on qualification;
it is not matched-stimulus physiological validation. No unused animal/walking
cohort is consumed by this search.

The search is exhaustive at the declared screen resolution. Strict confirmation
of three finalists cannot prove that no unselected model would benefit from
additional numerical refinement. Do not describe a finite-grid failure as proof
that no biologically valid neural model can exist, or a selected fit as validation.

## Budget, evidence and completion

One worker, <=10,800 scientific CPU seconds,3GiB peak RSS, estimated256MiB and
512MiB hard final output cap,20GiB free reserve. Packed external inputs are
transient RAM (about1GiB nominal), never disk archives. No movies or duplicated
raw source ZIPs. Record per-case resources even on failure. Stop new cases on
budget failure and explicitly report any incomplete search instead of inventing
coverage. Synthetic backend tests/acquisition preparation are accounted separately.

Hash the228-file pilot,59-file source study,230-file temporal study and their
used dependencies. Freeze exact code, protocol/config/tests/candidate registry
before real candidate outcomes. Save numerical tables, failed cases, figures,
source gates, complete search/ranking/confirmation evidence and an undergraduate
explanation. Append dated live progress, save a dated snapshot, seal and rehash
after writer exit. Live progress and AGENTS remain outside immutable indexes.
