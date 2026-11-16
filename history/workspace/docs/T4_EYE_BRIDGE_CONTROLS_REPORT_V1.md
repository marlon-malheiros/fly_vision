# T4 eye mapping and held-input controls V1

13 November 2026. This completed a bounded **software and numerical** stage.
It is not a new biological validation, eye-wide neural simulation, or walking
test. The [frozen protocol](T4_EYE_BRIDGE_CONTROLS_PROTOCOL_V1.md) precedes
all 20 generated image inputs and 28 cable outputs.

## What changed and what passed

The separate [held-input solver](../src/male_optic_frontend/held_input_graph_v2.py)
applies the preceding sample throughout each half-open interval. It preserves
the graph and parameters and does not change the historical solver. A unit
test reproduces an analytical step response, verifies causality, timestep
convergence and exact source IDs. The earlier smoke's historical-solver
failure remains preserved in [its report](T4_VOLTAGE_BRIDGE_SMOKE_REPORT_V1.md).

The existing source inventory maps exactly to the LPi graph's **13,579**
T4/T5 identities, types and sides, with finite positions and unit axes. Of
these, 6,861 are T4 and 6,718 T5; 76 axes across the entire inventory were
imputed from another same-type/eye cell. This check confirms internal
consistency, not anatomical ground truth. Four non-imputed horizontal T4a/b
cells, one of each type per eye, were selected by the frozen coordinate rule.
[Mapping and selections](../results/t4_eye_bridge_controls_v1/mapping.json).

Each cell received five independently generated local-image controls: grey,
bright bars moving along the local axis in both directions, and dark bars in
both directions. Images were streamed and only sampled contrast and hashes
retained. These were four separate local patches, not a shared full-eye movie.
All 20 sampled inputs met their defined properties; no T5 inputs were supplied.

The original 344-section NEURON cable completed all 28 planned solves,
including eight bright-bar solver refinements. The maximum 0.1 versus 0.05 ms
voltage difference was **0.002720548 mV**, below the predeclared 0.005 mV
guard. The new network solver's maximum 1 versus 0.5 ms wide-output difference
was **1.167599e-12** model units, below the predeclared `1e-8` numerical
guard. Both bright-bar directions produced finite nonzero downstream outputs;
grey and dark-bar controls yielded zero under the declared ON contrast rule.
[Cable checks](../results/t4_eye_bridge_controls_v1/cable_numerics.json),
[network checks](../results/t4_eye_bridge_controls_v1/network_numerics.json).

An independent scalar reviewer recomputed 1,980 sampled image contrasts
(maximum error `8.72e-15`), rechecked frozen source/input hashes, and matched
the versioned solver to a separately written held-input graph reference in a
one-cell case (maximum difference zero). [Review](../results/t4_eye_bridge_controls_v1/independent_review.json).
Nineteen focused solver, adapter and existing cable-sampler tests pass.

## Interpretation and limitations

The user-visible direction labels indicate stimulus travel along an inherited
local axis. They do **not** establish preferred/null biological directions.
The two aggregate network peaks differ, but they combine four separate local
patches and do not establish any physiological direction preference. Dark
bars on a grey background produce zero here because the input adapter keeps
only increments above grey; no T5/OFF input was modeled in this control.

The formula `max(V_mV + 65, 0)/65` is a historical engineering assumption,
not measured presynaptic release. The four graph cells are not the individual
recorded cells in the reserved transfer study; its per-cell delay, localizer,
registration aliases and waveform qualification do not automatically carry
over. All other 13,575 sources, including T5, are set to zero. Thus the tests
show that a few local image streams can pass through the cable, assumed bridge
and a timestep-stable network, not that a complete biologically constrained
visual system has been established.

## Resources and next boundary

The pinned Python 3.11 / NEURON 8.2.7 / NumPy 1.26.4 environment was restored
under `/tmp`; an initial sandbox DNS failure and first approval-review timeout
preceded the successful retry. The scientific worker reports 8.867 CPU seconds
and 58,191,872 bytes peak RSS for the 28 solves. Those figures exclude image
generation, graph runs, independent review and installation. Results before
method snapshots occupied 515,904 bytes; no movies or new raw recordings were
retained. [Worker resources](../results/t4_eye_bridge_controls_v1/resources.json).

The next meaningful step is an explicit shared-image, full-population design
with T4/T5 handling and an admissible registration policy. It must retain a
declared voltage-to-drive assumption and define numerical/physiology gates
before a walking comparison. The old neural-only decoder qualification does
not automatically transfer. More bridge families and downstream physiology
are separate unresolved checks; no exhaustive parameter search is justified
by this technical pass.
