# Fixed temporal-component dissection V1

2026-11-03. Prospective computational mechanism test using inspected physiological
development data. No new constants, fitting, graph changes or fresh biological
validation. Preserve all previous experiments, including the combined filter's
improvement and its worsened slow-motion response.

## Factorial intervention

Four functional variants: no extra stage (`none`, existing gain baseline),
`slowing_only` (remove high-pass adaptation), `adaptation_only` (remove added
low-pass slowing), and `both` (previous combined stage). Read none/both neural
arrays from the sealed preceding study, checking image identity and receipts.
Simulate the two component-removal copies on identical retinal frames. This is
an intervention on a functional model, not a biological neuron/circuit lesion.

Retain the source's nominal ON/OFF low-pass constants54/44 ms and high-pass
constants318/296 ms, sigma0.121902687872575, detector delay30 ms, graph and
neural parameters. Source provenance and the distinction between response-fit
constants and membrane measurements remain as in [the preceding report](HS_UPSTREAM_TEMPORAL_REPORT_V1.md).
No added connections, calcium filter, response gain or sign change.

Slowing only: h'=(u-h)/lp, d'=(h-d)/delay, output h. Initialize h=d=u.
Adaptation only: g'=(u-g)/hp, d'=(u-g-d)/delay, output u-g. Initialize g=u,d=0.
Exact two-state transition under the previous held image; new direct input in
the adaptation-only current is causal. Existing spatial pooling, motion
opponency, rectification/routing and source clipping remain unchanged.

## Frozen cases and checks

Reuse the exact22-case manifest:16 primary frequency/contrast cases and6 image/
source refinements, phase zero, methods85 display. Four frequencies0.5/1/2.5/15 Hz,
both directions; contrasts0.1/0.25/0.5/0.75 plus frequency1 as the full-contrast
reference, both directions. Primary image/source1.25/2.5 ms, refined0.625/1.25 ms,
solver0.25 ms; unchanged60 Hz/four-bit square-wave display and1 ms forcing ramp.

At primary preferred2.5 Hz also halve the solver step to0.125 ms for both new
variants. Total44 new component solves+2 solver checks. One primary preferred
0.5 Hz reference replay adds two full source-to-neuron replays of none/both,
including input/rate/state/checkpoint hashes:48 total solves. Reference render
is sequential and in memory only to keep peak storage bounded. All22 generated
image hashes must match the old cases; none/both arrays remain references, not
duplicated in the new neural archives.

Three focused pre-run tests: exact transitions versus independent ODE integration
for both interventions; causal prefixes/reset/stationary outputs; analytic
steady-state transfer magnitude/phase at the four fixed frequencies. New14
numerical comparisons (6 temporal+1 solver per variant) retain the old dual
5% criteria and each variant's fixed primary preferred1 Hz reference. Preserve
the prior14 numerical results as reused evidence, not newly executed checks.
Zero pre-motion neural output <=1e-12 and record all clipping. No new spatial-
convergence claim.

## Mechanistic and development criteria

Right HSN/HSE/HSS equal mean atanh(rate), [2,4) minus[1,2), as before. Keep subtype
and signed-rate summaries. Compare the same seven frequency and seven contrast
coordinates against the exact existing joint bands. Normalize by each model's
own primary preferred reference. All biological data are already inspected.

Primary mechanistic predictions, frozen from the known combined-stage result:
slowing_only reduces absolute PD15 Hz normalized error relative to none;
removing adaptation improves PD0.5 normalized error (slowing_only versus both);
adding adaptation without slowing worsens PD0.5 error (adaptation_only versus
none). Evaluate each prediction explicitly without changing a margin.
Report raw and normalized two-factor effects: average slowing effect,
average adaptation effect and interaction both−slowing_only−adaptation_only+none.
Normalization can itself introduce apparent interaction; do not infer a new
synaptic nonlinearity or biological causality from a normalized interaction.

A new variant is eligible for further development only if its own7 numerical
checks pass, no clipping, both PD50/75 remain inside the contrast band, contrast
violations do not exceed both, contrast RMSE<=both+0.02, frequency RMSE<=both,
and PD0.5 absolute normalized error is strictly smaller than both. Nominate the
eligible variant with lowest frequency RMSE; slowing_only precedes adaptation_only
on an exact tie. This prospective discrete nomination is development selection,
not held-out validation or a biological acceptance threshold. Do not fit a
mixture or alter constants if neither qualifies.

Complete the whole fixed panel irrespective of outcomes; no additional variant
or walking simulation follows within this round. Biological-validation and
walking-advancement flags remain false for this partial inspected panel. Report
failures and unresolved null-direction suppression; component effects within the
model cannot establish biological causality.

## Resources and preservation

CPU cap4800 s, two workers,2 GiB peak each. Whole-run output estimate32 MiB,
cap64 MiB, free reserve20 GiB. No movie, full-source-drive archive, source ZIP
duplicate or full upstream reconstruction. Stream image frames; retain two new
wide-cell rate arrays, reference receipts and hashes. Freeze sources/dependencies
before outcomes; version code and decisions, append dated progress, save its
actual-date copy with completed report/sources, seal and rehash after writer
exit. Live progress/AGENTS remain outside immutable indexes.
