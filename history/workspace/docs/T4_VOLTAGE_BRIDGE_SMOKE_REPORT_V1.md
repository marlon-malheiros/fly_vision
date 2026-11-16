# T4 voltage-to-network interface: bounded software check V1

13 November 2026. This is a retrospective technical check, not a physiology
study or walking benchmark. No sealed evidence or existing solver was changed.

## Outcome

An explicit engineering adapter can place a saved T4 voltage trace into the
correct T4 input column of the existing LPi graph, while preserving other
source columns and keeping direct drive off downstream cells. A sparse
one-cell graph smoke produces a finite downstream response, with zero response
in the zero-input control. This confirms wiring and unit-domain compatibility,
not a biologically validated synapse or a qualified integrated visual model.

The first numerical review **failed** its `1e-8` absolute model-rate guard:
the 1 ms and 0.5 ms historical-solver outputs differ by `1.3861291e-7`
(about 0.109% of the fine-solver maximum response). The deliberately strict
engineering guard was chosen for this diagnostic, not taken from biology.
The original smoke's peak is reproduced exactly by independently rebuilding
its input. [Failure record](../results/t4_voltage_bridge_smoke_v1/numerical_review_failure.json).

An exploratory third solver resolution halves the successive difference to
`6.9174941e-8`. Inspection shows that `FrozenGraph` uses the historical
boundary convention: it mixes toward the next input only during the last
solver substep before the next sample. Thus the transition duration changes
when the timestep changes. This is a code observation and a plausible source
of the sensitivity, not proof that earlier scientific conclusions are wrong.
[Refinement diagnostic](../results/t4_voltage_bridge_smoke_v1/refinement_diagnostic.json).

A separate post-failure reference holds each input constant over its 10 ms
interval and gives a `9.4849334e-13` maximum wide-rate difference between
1 ms and 0.5 ms integration, below the same `1e-8` guard. This passes a
numerical check for the **alternative hold convention only**; it does not
retroactively pass the historical solver or establish which input convention
best represents the physiology. The historical solver stays unchanged.
[Held-input review](../results/t4_voltage_bridge_smoke_v1/held_input_review.json).

## Interfaces and assumptions

* The published cable yields soma `voltage_mv` on a millisecond clock; its
  tested physical-mV output was baseline-subtracted for the prior assay.
* The graph expects one finite normalized drive in `[0,1]` per T4/T5 body ID
  at each input time, with exact source coverage. The value is a model unit,
  not measured transmitter release.
* The adapter uses `max(V_mV - resting_mV, 0) / span_mV`, with both numbers
  supplied explicitly; the smoke uses `-65 mV` and `65 mV`, consistent with a
  prior engineering interface. The mapping clips negative deflections to zero,
  rejects values above one rather than silently saturating, and has no claimed
  calibration as a synaptic or calcium model.
* Exact matching clocks are mandatory; no hidden resampling or future samples
  are introduced by the adapter. Nonselected input columns are preserved,
  and only explicitly identified T4a–d cells can be replaced.
* This adapter does not determine the retinal map, assign direction, generate
  voltage, model T5 or transfer the per-recording flash/early-motion
  calibration and alias ensemble to the walking eye. Those remain explicit
  work before a full-eye model can be constructed.

## Test and provenance

The graph has 13,579 source cells. This wiring check injects **one previously
inspected individual cable output**, selected from the stored cell 6 ND run,
into a T4a cell chosen by its existing direct HS/H2 weights. It sets every
other source, including all T5 cells, to zero. This is deliberately
artificial; the selected trace is not the qualified cell/registration ensemble,
does not correspond to the selected graph cell's measured receptive field,
and is not an independent animal, direction-selectivity test or walking
stimulus. Graph and voltage source SHA256 values, chosen body ID, clocks and
measured outputs are in [the smoke record](../results/t4_voltage_bridge_smoke_v1/result.json).

The separate [adapter](../src/male_optic_frontend/t4_voltage_bridge_v1.py)
and [smoke runner](../scripts/t4_voltage_bridge_smoke_v1.py) do not write
into previous studies. The post-failure [held-input reviewer](../scripts/review_t4_voltage_bridge_hold_v1.py)
uses the saved trace and frozen graph; no new NEURON simulation is performed.
The prior pinned NEURON environment is absent; NumPy and SciPy in the current
project environment were sufficient to replay the saved trace. The smoke
stores compact JSON and produces no movie. Free space before execution was
approximately 144 GiB; planned retained output was below 1 MiB and peak
process memory was not measured.

`pytest -q tests/test_t4_voltage_bridge_v1.py tests/test_t4_cable_matched_v1.py`
passes 13 checks covering identity/order, preserved T5 inputs, invalid data,
clock mismatch and existing cable-sampler behavior. These checks and the
solver comparison are numerical/software evidence, not biological validation.

## Stopping point

The small interface and wiring demonstration are complete. A new walking or
physiology test is **not** yet justified by this result. Next, define the
population-level spatial/directional assignment, explicit timing convention,
T5 handling and output mappings; evaluate the held-input reference and other
predeclared bridge alternatives with meaningful stimulus controls. The
previously passing decoder and T4 waveform result do not automatically carry
over. New test scenes and recordings must be checked for prior exposure.
