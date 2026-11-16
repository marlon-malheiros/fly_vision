# H2 upper-field discrepancy diagnostic V1

25 October 2026. This bounded follow-up builds on the sealed [H2 benchmark
V2](H2_FROZEN_MODEL_BENCHMARK_REPORT_V2.md). Existing recordings, model errors,
and anatomy are already inspected. Retrospective inspection localized several
large errors and weak model responses to display position (87,36). This
selection is exploratory, not independent confirmation. Include all six
available recordings there, including cell 3 with its smaller error. Cell 7
has no admitted pose for this position and remains excluded for missing
metadata. Never infer its pose. No new biological data or fitted parameters.

## Fixed questions and scope

1. Retrospectively describe all 39 existing positions by display patch, model
   amplitude, error and reference error. Measure source-chart support as a
   geometrical marker, not a measured biological receptive field.
2. Extend the previous pixel-phase controls to all six upper-patch recordings,
   all 16 directions and both polarities: edge_phase=-0.5,+0.5 LED. For cell 5
   only, whose author metadata report 2 degrees head yaw, evaluate signed
   head_yaw=-2,+2 degrees. Cell 6 shares its primary input pose but reports
   zero yaw; do not treat cell 5's uncertainty as cell 6's biological bound.
   Report every variant; never select one to repair the result.
3. Use the same protocols' lower patch (87,21) as a paired within-animal
   comparison. In separate circuit instances, zero every incoming chemical
   weight to left H2 body 10019 from non-T4/T5 cells. Anatomy identifies four
   such edges: two HS and two bIPS. Retain the complete rest of the graph,
   including recurrent input to T4/T5. Replay identical saved source arrays
   for all 12 upper/lower recording positions. This tests the direct wide-cell
   afferents to H2, not every bIPS influence or every recurrent pathway.
   Preserve traces and final states. Record exact edge identities/weights and
   enforce that these are the only changed weights. No neuron is silenced.

## Fixed implementation and measurements

Reuse unchanged original frontend, renderer, graph, gains, clocks and
observation rule from benchmark V1. Model t=1 s onset, primary input 5 ms,
RK4 1 ms; same dimensionless baseline-subtracted mean H2 rate over each
recording's source-derived response window. Average bright/dark curves
before minimum subtraction and vector PD. Retain per-polarity curves,
amplitudes, DSI, undefined PDs and every condition-to-case mapping.
Circular errors use atan2; flat/vector criteria remain 1e-12. No threshold
or decoder fitting. Changes are descriptive; no biological acceptance gate.

For geometric support, transform each left T4/T5 source's assigned body
azimuth/elevation to continuous display coordinates with the frozen arena
inverse, then nearest LED floor(x+0.5), radius <=10. Count direct H2 afferents
and sum their absolute original chemical weights inside the patch. Also
report all 317 display-center visibility counts in the inherited eye grid.
This omits pooling spillover and uses imposed source retinotopy; it is a
support diagnostic, not an anatomical RF reconstruction or causal test of
retinotopy. Do not normalize/reweight connections to increase support.

## Numerical checks frozen before new outcomes

For upper-patch cells 2 (largest existing error) and 4 (80-ms steps), run
every direction/polarity (64 cases): (a) identical saved inputs with RK4
0.5 ms; (b) rerender at 2.5-ms frontend/input with RK4 0.5 ms. Check each
endpoint against 5% of the primary absolute endpoint +1e-7 model-rate units.
Also report the full-curve PD change and whether it exceeds 1 degree as an
explicit numerical diagnostic, not a physiological tolerance. Do not replace
primary predictions or relax gates after failure. Finer sampling of the
phase/head-angle variants is outside this finite scope.

Independently replay the lesioned graph using the original Python
FrozenGraph for cell 2, upper patch, dark, relOrt=0 and 4. Compare every
wide-cell rate and final state with <=1e-10 absolute tolerance. Independently
reconstruct endpoint integration and vector PD from saved traces, verify
input hashes and four-edge-only mutation. Existing sealed dependency hashes
must verify before execution and again on completion. Preserve errors/logs.

## Interpretation and deliverables

Report directional shifts, signed changes in absolute error, response
amplitude ratios and both sampling variants, including negative findings.
If stimulus variants alter errors substantially, stimulus uncertainty
remains a plausible contributor, not proof of the exact true pattern. If
removing direct HS/bIPS inputs barely shifts H2 PD, those inputs do not
explain this mismatch in this frozen model; upstream recurrent circuitry,
surrogate direction channels/retinotopy and stimulus/animal differences
remain possible. Never claim model lesion effects establish biological
causality or that failure identifies one unique upstream cause.

Produce code/config, complete new numerical evidence and mappings, figures,
a separate report ending with undergraduate what/we want/why, reproduction
instructions, dated progress snapshot and immutable artifact index. Keep
the live progress report and AGENTS.md outside the index. No yaw sweep,
new conductance/connectivity, calibration, controller, or overwrite of
earlier results. Freeze this protocol, code, plans and identities before
new results, explicitly acknowledging the known selection data.

Pre-freeze correction: initial preparation stopped on a missing matched
position because (87,13) belongs to a different recording protocol. Metadata
inspection identified (87,21) as the lower patch actually presented within
each upper-patch protocol. Corrected before any new simulation or score;
preserve the failed preparation receipt. No outcomes chose the pairing.
