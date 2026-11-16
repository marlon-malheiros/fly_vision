# Small hybrid T4 walking pilot V1

13 November 2026. This is a small exploratory software/numerical test on
**one previously inspected development room**, not a held-out walking result
or biological validation. The [protocol](HYBRID_T4_WALKING_PILOT_PROTOCOL_V1.md)
was fixed before computing the hybrid outputs.

## Result

The detailed published T4 cable can receive the same saved walking images as
the functional frontend, replace four T4a/b inputs in the network, and run
through the LPi circuit and a fixed artificial decoder. The other 13,575
T4/T5 source inputs remain bit-identical. Four of 6,861 T4 cells is roughly
0.058%; this is a partial hybrid, not the complete detailed eye.

At 1.19 seconds, 190 ms after turn onset, the existing fixed decoder gives:

| Input in one known room | Functional score | Hybrid score |
|---|---:|---:|
| Straight | -0.192244 | -0.247002 |
| -2°/s turn | -2.390323 | -2.443414 |
| +2°/s turn | +1.991506 | +1.934957 |

The unchanged cutoff is `1.132996`: at this single checked time, both versions
give no straight alarm and the expected sign for both turns. That is a
descriptive observation, not a three-trial estimate of reliability, a
whole-episode false-alarm test, proof of a benefit, or a pass on unseen rooms.
The hybrid scores were not used to fit or tune any parameter or threshold.
[Outcomes and traces](../results/hybrid_t4_walking_pilot_v1/outcomes.json).

Both versions were run with the new held-input timing rule on the frozen LPi
graph; this differs from the historical solver used in the previously
qualified neural-only benchmark. The earlier benchmark's 24-room result does
not automatically transfer. The decoder is an artificial readout and not a
biologically identified neural circuit.

## Images, mapping and physics

The pilot reuses the existing `f00` scene at 11 mm/s with straight and
±2°/s paths. Walking begins at 0.5 s, yaw at 1.0 s. All three sets of saved
images and functional source drives were verified against their old receipts;
the original functional frontend was replayed from the same
retinal images with **zero** maximum source difference in each case. Retinal
images, source inputs and selected-cell image samples are identical through
the yaw onset. No fresh scene, animal or raw recording was used.
[Input audit](../results/hybrid_t4_walking_pilot_v1/input_audit.json).

The four cell positions and axes are the already frozen, non-imputed
inventory selections from the earlier local-image control. The full T4 model
receives eleven positions and nine transverse samples, with a 3-second hold of
the first image. The functional frontend uses its own historical
initialization; this difference is explicit. The model's somatic voltage is
converted to normalized drive using `max(V+65,0)/65`, an **engineering
assumption**, not measured synaptic release. The retained T4 recording study's
cell-specific flash registrations, alias ensemble and waveform qualification
are not automatically transferred to these four model cells.

The largest instantaneous change in any of the four selected source drives
was `0.0938993` normalized units; the maximum absolute downstream-wide rate
change was approximately `7.88e-5` model units. These changes combine the
different source dynamics, prehistory and output conversion. They do not
isolate which difference caused the score change.

## Numerical and independent checks

All 12 cable 0.1 versus 0.05 ms comparisons pass the unchanged `0.005 mV`
guard; the largest difference is `0.00168937 mV`. Straight-case functional
and hybrid graph 1 versus 0.5 ms refinements both pass the `1e-8` model-rate
guard, with largest difference `1.111e-11`. A separate Python reference
matches the hybrid graph within `9.76e-19`. Pre-yaw neural prefixes are
identical across the three trajectories within each version.

Independent scalar code checks 792 selected native-position image samples
(maximum error `1.67e-16`), reproduces both graph variants in a selected
turning case within `1.31e-18`, and independently recomputes both fixed
decoder scores at 1.19 s within `1.34e-15`. Separate bookkeeping verifies
all 12 voltage-to-drive columns and all saved summaries.
[Cable checks](../results/hybrid_t4_walking_pilot_v1/cable_review.json),
[independent review](../results/hybrid_t4_walking_pilot_v1/independent_review.json),
[bookkeeping](../results/hybrid_t4_walking_pilot_v1/bookkeeping_review.json).
Twenty focused existing solver/bridge/cable tests pass.

## Resources and next step

The cable worker used 34.10 CPU seconds and peaked at 77,475,840 bytes RSS
for 24 solves; graph execution, including refinements, used 25.47 process CPU
seconds, 25.56 wall seconds and peaked at 282,763,264 bytes RSS. These figures
exclude input replay, reviews, initialization and hashing. About 155 MiB of
existing retina archives were read in place; no new movie or recording was
created. The study output before snapshots occupied under 2 MiB.

The justified next question is whether a **larger, explicitly mapped set**
of detailed T4 cells can be integrated at practical cost while retaining T5
and matched inputs. The one-room result gives a reason to continue; it does
not establish that expanding the replacement will preserve its decisions.
Population registration, the voltage-to-release relation, physiological
agreement, new-room walking reliability and bIPS effects in this hybrid
remain separate open questions.
