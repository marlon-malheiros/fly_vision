# Published-circuit boundary comparison V1

24 October 2026. Completed finite circuit diagnostic; original models and earlier
results preserved. [Prospective protocol](PUBLISHED_CIRCUIT_COMPARISON_PROTOCOL_V1.md),
[reproduction](PUBLISHED_CIRCUIT_COMPARISON_REPRODUCTION_V1.md).

**Finding:** the published central motif and our frozen circuit both strengthen
left–right yaw-dependent signals through bIPS-associated processing in these
diagnostic inputs. Their architectures and gains differ. This establishes a
shared qualitative computation, **not** that the published model fixes our small-
turn false alarms. A faithful full image-to-response comparison remains
unavailable because the author simulator and important frontend implementation
details were not located. The executed comparison therefore starts at a clearly
declared HS/H2 boundary.

## What could be reconstructed

The [primary paper](https://www.nature.com/articles/s41593-025-01948-9), Agent
simulations methods and Extended Data Fig. 9c provide steady-state equations
and manually fitted signed weights. Its four-channel HR frontend has 50-ms
high-pass and 15-ms low-pass filters. The authors describe fitting response
amplitudes, not deriving these coefficients directly from synapse counts.

The current [public repository](https://github.com/ChiappeLab/Erginkaya_et_al_2025)
matches cached commit `b1b59653a9758335cfff28a81d42010ea6ff082a`. Its 50 script/
helper files contain experimental analysis; the walking-agent implementation
was not located. The Zenodo archive's 5,518-entry central directory contains
behavior and preprocessed recordings, with no matching model-code path. The
paper's source spreadsheets and supplement did not supply a simulator or the
missing frontend implementation. This audit concerns the inspected public
snapshot and inventories; it does not establish that code exists nowhere else
or exhaustively inspect every MATLAB data variable.
[Audit findings](../results/published_circuit_comparison_v1/audit/audit_findings.json),
[preserved article, parameter image and supplement](../results/published_circuit_comparison_v1/audit/primary_sources),
[ZIP inventory](../results/published_circuit_comparison_v1/audit/zenodo_archive_inventory.json).

We implemented the printed **unrectified simultaneous steady-state equations**,
using the inhibitory signs already present in the parameter table. No second
minus sign, neural time constant, clipping rule or calcium kernel was added.
This is our conditional equation reconstruction, not an execution of author
code. Unknown detector spacing/pooling, numerical filters, recurrent handling,
exact simulator scenes and observation kernels prevent a faithful end-to-end
claim. H2rns are also absent from the paper's simplified circuit.
[Signed weights and assumptions](../configs/published_circuit_comparison_v1.json).

## Executed comparison

Used the 44 sealed **direct-ray** inputs from the sampling diagnostic: two known
rooms, three walking speeds (5.5/11/16.5 mm/s), yaw 0/±2/±5/±20°/s and stationary
controls. Reused identical saved T4/T5 drives, retaining the original frontend,
graph, numerical parameters and clocks. This does not qualify receptor optics,
grid/time convergence or fresh-environment performance.

Completed **88 full original-network trajectories**: intact and bilateral bIPS
silencing for every input. The 44 intact rate/final-state arrays match their
saved predecessors bit for bit. Retained source hashes, intervention ledgers,
all trajectories/final states and 6,160 per-cell/per-role mean chemical-current
entries. Currents include the fixed chemical gain and remain model state units.

At each recorded time, supplied the intact original HS/H2 rates to the printed
middle/output equations, both intact and with B_L=B_R=0. Primary HS input is
the four-cell class mean per side. A fixed sensitivity comparison excludes HST,
using HSN/HSE/HSS only. These are interface assumptions, not anatomical evidence
for the author's detector pooling. They produce **176 reference traces**.
The reference lesion keeps HS/H2 inputs fixed; the original full-network lesion
allows upstream feedback to change. Neither is an experimental intervention.

All means use indices [70,140), 0.70–1.39 s. Reported differences are left minus
right. The odd component is half the difference between positive and negative
yaw responses. Only the original circuit receives the original frozen decoder;
there is no fitted decoder, detection threshold or false-positive estimate for
the differently scaled reference.
[Complete execution](../results/published_circuit_comparison_v1/execution_complete.json),
[all means/contrasts/currents/scores](../results/published_circuit_comparison_v1/analysis).

## What the mechanism comparison shows

Let Δ mean left minus right and Σ mean left plus right. Eliminating the printed
middle-layer equations gives the exact conditional reference gains:

| DNp15 component | Intact reference | bIPS clamped to zero |
|---|---:|---:|
| Coefficient on ΣHS | 47/130 = 0.361538 | 0.700000 |
| Coefficient on ΔHS | 233/270 = 0.862963 | 0.700000 |
| Coefficient on ΣH2 | 0.300000 | 0.300000 |
| Coefficient on ΔH2 | −0.300000 | −0.300000 |

Thus the intact motif reduces the shared HS component by 48.35% and increases
the differential HS component by 23.28%, relative to its silenced condition.
These percentages concern **HS transfer coefficients**, not overall detection
accuracy or every mixed HS/H2 response. In the printed final parameter set,
direct H2→bIPS and H2→uLPTCrn coefficients are zero, despite those anatomical
pathways. The fitted motif must not be mistaken for a measured conductance map.
[Independent rational derivation](../results/published_circuit_comparison_v1/independent_review/exact_reference_gains.json).

![Exact reference gains](../results/published_circuit_comparison_v1/presentation/reference_transfer_gains.png)

For ±2°/s in the six room/speed combinations, bIPS silencing leaves **85.40–
85.61%** of intact odd DNp15 difference in the original graph. It leaves
**79.17–79.32%** in the all-HS reference, or **79.10–79.27%** in the classic-HS
reference. Both therefore lose some yaw-dependent response, with different
conditional gains. These are paired deterministic diagnostic values, not
biological variability, performance rankings or evidence that one added neuron
would repair detection.
[Every paired value](../results/published_circuit_comparison_v1/presentation/paired_dnp15_odd_effects.csv).

Original HS odd responses retain 99.971–99.973% and H2 retain 100.092–100.101%
under silencing in this subset. The much larger DNp15 change therefore emerges
mainly downstream of these class-mean boundary signals here. The retained
current decomposition and graph show a strong contralateral inhibitory bIPS→
DNp15 path, alongside ipsilateral HS excitation and contralateral H2 excitation.
Unlike the reference, the frozen graph lacks uLPTCrns, retains nonzero H2→bIPS
input, and has weak bIPS feedback to HS/H2. Weight sums are normalized model
weights, not raw synapse counts or coefficients directly commensurate with the
reference's population-mean inputs. We do not add a missing connection.
[Original connectivity by role/side](../results/published_circuit_comparison_v1/analysis/original_connectivity.csv),
[current decomposition](../results/published_circuit_comparison_v1/analysis/currents.csv).

![Full DNp15 differences](../results/published_circuit_comparison_v1/presentation/matched_boundary_responses.png)

Nonzero straight-walking differences remain visible at yaw zero, including in
the conditional reference. A linear gain on bilateral input differences can
also transmit scene-induced imbalance; it is not automatically a reliable
rotation classifier. Reference transient behavior and absolute response size
are not physiological comparisons. The original lesion can be scored with its
unchanged readout:

| Speed (mm/s) | Intact straight alarms | Silenced straight alarms | Intact ±2°/s detections | Silenced detections |
|---:|---:|---:|---:|---:|
| 5.5 | 1/2 | 1/2 | 3/4 | 2/4 |
| 11 | 1/2 | 1/2 | 1/4 | 1/4 |
| 16.5 | 1/2 | 2/2 | 1/4 | 3/4 |

The fast lesion's extra detections accompany extra false alarms. This repeats
the distinction between response gain and useful detection. These two known
rooms do not provide population false-positive rates or new yaw thresholds.
[Diagnostic counts and raw sign counts](../results/published_circuit_comparison_v1/presentation/original_diagnostic_counts.csv).

## Validation, failures and practical limits

Independent review verifies 352 output-file hashes, 880 reference arrays, all
1,232 mean rows and contrast/odd arithmetic, all 6,160 current summaries and
84 frozen original decoder scores. Matrix solutions agree with independently
eliminated equations within 1.31×10⁻¹⁸; checked equation residuals are below
4.34×10⁻¹⁹. Bilateral exchange, homogeneity, rational gain identities and zero
stationary responses pass. Original Python RK4 independently checks one
nonzero small-yaw input (+2°/s) in both conditions: maximum rate/final-state/
final-current differences are 8.68×10⁻¹⁹, 8.14×10⁻²⁰ and 2.72×10⁻²⁰.
No temporal convergence or physiological validation follows from these checks.
[Independent review](../results/published_circuit_comparison_v1/independent_review/review.json).

Signed reference responses were retained: 12,471 of 353,760 reference scalar
entries are negative; stationary asymmetry with zero denominator is explicitly
undefined. No artificial rectification or denominator epsilon makes them look
more physiological. Download/optional-dependency failures remain in the audit.

The first alternate-directory reproduction failed because spawned workers used
the original default path. Exclusive directory creation prevented overwriting;
all main evidence stayed unchanged. The failed wrapper/log/namespace are
preserved. A corrected supported wrapper sets each child's destination and
repeats the finite study in a fresh R2 namespace. All 264 trajectory files'
1,848 arrays agree bit for bit, and ten numerical-summary files are byte
identical. Both independent reviews pass; both figures were visually inspected.
All 50 copied public script blobs also match the retrieved GitHub tree.
The low-level driver's direct
alternate-directory run flag is unsupported; use the documented wrapper.
Refer to the completion review for the exact verification scope.
[Full second-execution review](../results/published_circuit_comparison_v1/completion_review.json),
[Failed attempt](../results/published_circuit_reproduction_main_v1.log),
[reproduction guide](PUBLISHED_CIRCUIT_COMPARISON_REPRODUCTION_V1.md).

The current result does not locate a unique cause of remaining false alarms.
Missing electrical synapses, neuron identities/side mapping, the visual
surrogate, aggregation and physiological parameters remain relevant constraints.
The paper's higher-yaw calcium/behavior findings do not quantitatively validate
our ±2°/s detector. Earlier decoder retraining also failed generalization; a new
fit alone is not an established repair. Prior [physiological diagnostic limits](CORRECTED_PHYSIOLOGICAL_DIAGNOSTICS_REPORT_V2.md)
still apply. No closed-loop or hardware deployment was added.

## Next evidence and experimentally testable predictions

First obtain or locate the exact agent source/configuration and visual stimulus
implementation, then compare both full pipelines under prospectively matched
inputs. Resolve the HS/H2 side/compartment and calcium measurement mapping
before physiological fitting, with separate calibration and validation animals.
This is the remaining prerequisite to the proposed end-to-end comparison.

A testable hypothesis is that verified bilateral bIPS suppression reduces the
odd bilateral DNp15 response to small yaw while shifting straight-walking
balance. Measure both responses across speeds with matched optic flow, rather
than counting increased activity as improved detection. Another is that the
network suppresses bilateral common input more than differential input; matched
bilateral recordings could test this transfer pattern. Our exact gains and
model lesion percentages are computational predictions, not estimates of fly
firing rates or proof of biological causality.

## Undergraduate explanation: what we did, what we want, and why

We gave our circuit and a reconstruction of the paper's central circuit the same
HS/H2 signals, then checked how bIPS changes the left–right response. Both can
make turning signals stronger, but a stronger signal can still confuse an
uneven visual scene with a turn. We want reliable small-turn detection, not
just activity that increases during motion. This comparison explains part of
the computation and identifies what evidence is missing before changing the
model. It does not yet give us a validated fix.
