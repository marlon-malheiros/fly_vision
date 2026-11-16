# Published-circuit boundary comparison V1

24 October 2026. Authorized follow-up to the completed image-sampling diagnostic.
This protocol is written before new circuit replays and comparison analysis.
The two rooms and their original outcomes have already been inspected; this is
a conditional diagnostic, not held-out validation or a new threshold study.

## Scope fixed before execution

Audit Erginkaya et al. (2025), DOI 10.1038/s41593-025-01948-9, its current public
repository, Zenodo inventory, source spreadsheets and supplement. Preserve the
downloaded source and failed retrievals. Transcribe Extended Data Fig. 9c's
**signed** coefficients; inhibitory table entries already contain their minus
sign. The methods write these as subtractions of positive magnitudes. Table
subscripts use target-first naming for the middle layer, unlike the methods.
Interpret the entries by their row and biological edge, without applying a
second minus sign.

The author simulator was not located in the current public repository during
the initial audit. Therefore do not claim a full published-model reproduction.
Do not invent detector spacing, retinal pooling, recurrent dynamics, clipping,
calcium kernels, conductances, neural connections or controller parameters.
Implement the printed **unrectified simultaneous steady-state equations** as
an explicitly conditional reference. No motor control is implemented.

## Inputs and finite runs

Use all 44 **direct-ray** inputs from the sealed sampling diagnostic: s07/s12,
5.5/11/16.5 mm/s crossed with yaw 0/±2/±5/±20°/s, plus one stationary control
per room. Images, receptor grid and 5-ms image/10-ms source clocks stay fixed.
Reuse the saved 13,579-source drives; do not rerender or retune.

Replay the original frozen 13,593-cell graph twice per input: intact and
bilateral bIPS silencing, with the existing intervention definition, unchanged
parameters and 1-ms solver. Retain 88 trajectories, final states, per-role
chemical currents at output cells, input hashes and intervention ledgers.
Intact replays must match saved rates/final states within 1e-10; failure stops
interpretation and is retained. Compare chemical contributions in pre-activation
state units, including the fixed chemical gain, rather than labeling them Hz.

At each saved 10-ms sample, pass the intact replay's left/right HS and H2 rates
to the printed paper middle/output circuit. Primary HS input is the mean of all
four original HS cells per side, consistent with existing project readouts.
A fixed anatomical sensitivity analysis uses HSN/HSE/HSS only, because the
frozen group also contains HST. H2 side labels are the existing graph labels;
the paper equations explicitly use contralateral H2 at middle/output cells.
This aggregation is our interface assumption, not the author's original visual
input. Replaying the intact inputs also during reference bIPS silencing clamps
the HS/H2 boundary: it does not reproduce lesion-induced upstream feedback.

Solve the four simultaneous B/U equations exactly by linear algebra; compare
intact and B_L=B_R=0 with U and DNp15 recomputed. Save both HS definitions and
both conditions: 176 conditional reference traces. No time constant is added.
Also compute the full printed four-channel-to-output transfer for unit basis
inputs, bilateral forward/backward inputs and the two yaw patterns. Those
abstract channels are not a reconstruction of the published HR frontend.

## Fixed analysis and interpretation

Use the original 70-sample window, indices [70,140), 0.70–1.39 s. Report all
cell/side means, left-minus-right differences, yaw-minus-matched-straight
contrasts, and odd responses [difference(+yaw)-difference(-yaw)]/2 at 2/5/20°/s.
Report the original frozen DNp15 decoder's scores/decisions for the original
graph copies only. Do not apply it to the differently scaled reference or fit
a new decoder. No reference detection threshold or false-positive rate is
claimed. Preserve negative responses and undefined normalized asymmetry as
null with the raw numerator/denominator; do not invent an epsilon.

Inspect original weighted connectivity by role and side, and compare effective
motifs with the printed reference. Describe divergence at this clamped boundary
without attributing it uniquely to any missing neuron, electrical synapse,
frontend stage or physiology. No new biological reconstruction or repair is
authorized by numerical agreement alone.

## Numerical checks and stopping rule

Independently solve the paper equations with rational arithmetic and derive
sum/difference gains; compare to float64 matrix inversion (tolerance 1e-12).
Check bilateral exchange equivariance, homogeneity, equation residuals,
stationary controls, bIPS clamping and source identity coverage. Replay one
fixed nonzero case with the original Python solver, checking both interventions
within 1e-10. Independently recalculate saved summaries and decoder decisions.
The finite study stops after the specified replays and reviews, including any
negative scientific outcome. Numerical checks establish implementation
consistency, not measured fly optics or physiological validation.

Publish a versioned report, figure/tables, evidence inventory, reproduction
commands, limitations and an undergraduate what/we-want/why explanation.
Append live progress; save a dated progress copy before sealing. Preserve all
previous results and the unfinished V9 hardware benchmark.
