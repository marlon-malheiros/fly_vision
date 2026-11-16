# Project overview for an independent second opinion

24 October 2026. Retrospective handoff of completed work and unresolved questions.
No new simulations, model changes or biological validation were performed for
this overview. Later generalization and sampling evidence qualifies the earlier
positive results; the original reports and failed attempts remain preserved.

We are developing a Drosophila visual-circuit model using the MaleCNS connectome.
The central question is: **can the circuit distinguish small body rotations from
the image motion caused by forward walking, and does bIPS improve that ability?**
Yaw means turning around the vertical axis; optic flow means the resulting
movement of images across the eyes. The long-term ambition is a physiologically
grounded sensorimotor model and eventually robotic control. The current research
is open-loop: prescribed movement generates images, and the circuit's responses
do not change the movement. A visual-only model cannot identify whether a turn
was intended without an additional intention or motor-related signal.

The existing pipeline is:

**3D environment → binocular retinal images → functional motion filters →
T4/T5-like drives → MaleCNS-derived network → HS/H2/bIPS/DNp15 responses →
statistical yaw readout.**

HS, H2, bIPS and DNp15 are neuron classes/families represented on both sides.
The baseline is a selected MaleCNS subnetwork containing 13,593 modeled cells:
13,579 T4/T5 sources and 14 cells
across these downstream groups, with 203,861 directed chemical connections.
Synaptic weights and rate equations contain modeling assumptions; connectome
anatomy alone does not determine their physiological dynamics. Activity is in
signed model units, not calibrated spikes, voltage or calcium fluorescence.
The frontend passed defined functional and numerical checks, but its imposed
direction-channel routing is a surrogate, not a validated reconstruction of
biological upstream visual circuitry.

**Work completed.** The initial 3D walking study tested forward translation,
pure yaw, combined motion and stationary controls. Study A then tested three
forward speeds (5.5, 11, 16.5 mm/s) crossed with yaw 0, ±2, ±5, ±10, ±20 and
±40°/s: 33 walking conditions plus one stationary control per room. It included
bilateral/unilateral bIPS silencing, selective removal of bIPS outputs, and
HS/H2 controls. Study B separately added 17 uLPTCrn and eight H2rn candidate
homologs and their recorded chemical connections, producing 13,618 cells and
204,201 connections. Additional studies tested 40 unfamiliar rooms, sampling
sensitivity and a conditional comparison with the published circuit equations.

The original model and earlier evidence were preserved. Original and ablated
networks received identical visual inputs. Decoder training and cutoff
calibration used separate development rooms; held-out rooms entered neither
fit. The main readout uses average bilateral responses during 0.70–1.39 s and
is given walking speed. It is an external analytical readout, not an established
biological decoder. The frozen threshold rule requires at least 80% detection
and 80% raw yaw-sign accuracy, with no more than 10% straight-walking false
alarms, at a candidate magnitude and every larger tested magnitude.

**The strongest generalization finding is a failure to establish reliable
small-turn detection.** With the original circuit/readout and legacy image
sampling in the 40-room extension, DNp15 gives:

| Forward speed | ±2°/s turns detected | Straight-walking false alarms |
|---:|---:|---:|
| 5.5 mm/s | 46/80 (57.5%) | 6/40 (15%) |
| 11 mm/s | 26/80 (32.5%) | 8/40 (20%) |
| 16.5 mm/s | 14/80 (17.5%) | 6/40 (15%) |

Larger turns are more detectable, but the false-alarm rule leaves original
DNp15 thresholds unresolved at all three speeds. Some other larger-turn results
qualify, such as H2 at 20°/s at slow walking. These failures therefore concern
the specified readouts and criteria; they do not prove that all yaw information
is absent. The observations are deterministic scene tests, not independent
flies or noisy neural trials. They are not estimates of a biological threshold.
[Consolidated results](YAW_BIPS_EVIDENCE_SYNTHESIS_V1.md).

**bIPS changes signal gain and bilateral balance.** In the larger legacy-profile
test, suppressing bIPS outputs increased fast-walking DNp15 false alarms from
6/40 to 14/40 with the fixed readout. Its effects were not uniformly beneficial
across speeds and metrics, and yaw-dependent responses remained after silencing.
Some earlier lesion-specific recalibration recovered performance, while later
development-only retraining did not consistently generalize. Consequently,
neither indispensable bIPS information nor a sufficient decoder-only repair is
established. Lesion effects demonstrate causality within the equations, not
biological causality.

**Adding recorded anatomy did not establish a consistent improvement.** The
expanded circuit has one qualifying transferred-readout result in the larger
test: 20°/s at fast walking, with 4/40 false alarms. This is not robust small-turn
detection. Candidate homologies remain qualified, electrical conductances are
unavailable, and adding neurons changes old input weights through the inherited
normalization rule. That scaling confound must be separated from signals carried
by the new neurons. An anatomically constrained upstream replacement of the
functional frontend also remained unsuccessful at its integration gate.
[Study B](ANATOMICAL_STRENGTHENING_REPORT_V1.md).

**Image sampling is a demonstrated contributor, but not a complete explanation.**
An earlier six-room fast-walking 20°/s threshold failed under finer sampling.
A later controlled study ran 44 inputs through five image profiles, retaining
220 trajectories. Panorama interpolation averages nearby rays, so refining it
also changes input smoothing. The two finest profiles agreed categorically
with direct rays in these two known rooms, but the complete frozen numerical
stability gate failed. Direct rays still produced one straight false alarm in
two rooms at every speed. Those tiny diagnostic counts are not population
rates. Direct rays are a synthetic point-sampling reference, not measured fly
optics or proof of grid/time convergence.
[Sampling study](IMAGE_SAMPLING_DIAGNOSTIC_REPORT_V1.md).

**The published comparison was conditional.** Erginkaya et al. (2025) provide
central circuit equations and fitted weights. Their exact walking-agent source
was not located in the audited public snapshot, and key frontend/dynamics
details remain unspecified for faithful reproduction. We therefore replayed
the original circuit and supplied its intact HS/H2 responses to a reconstruction
of the printed steady-state middle/output equations. We completed 88 original
network runs and 176 reference traces, including two HS aggregation definitions.
The reference lesion clamps HS/H2 inputs; the original full-network lesion
allows upstream feedback. They are distinct interventions.

Both circuits show bIPS-associated amplification of turning-related bilateral
differences in this diagnostic. In the two-room ±2°/s comparison, bIPS silencing
reduces original odd DNp15 response by about 14–15% and the all-HS reference by
about 21%. These are response changes, not detection accuracies. No yaw decoder
or threshold was established for the reference. A second complete execution
reproduces all 1,848 arrays from 264 trajectory files bit for bit; this verifies numerical
reproducibility, not biological accuracy or full author-model reproduction.
[Comparison and limitations](PUBLISHED_CIRCUIT_COMPARISON_REPORT_V1.md),
[primary paper](https://www.nature.com/articles/s41593-025-01948-9).

**What remains unresolved.** The unique source of false alarms has not been
identified. Plausible contributors include stimulus sampling, the functional
frontend, circuit weights/normalization, omitted electrical or recurrent
interactions, and the readout's limited features and time window. Published
physiological data exist, but exact stimulus matching, cell/side/compartment
mapping, activity-to-measurement conversion and independent validation remain
incomplete. Existing physiological diagnostics do not validate the full
image-to-neuron pipeline. Missing conductances or connections have not been
invented to obtain favorable detection results.

A portable Linux CPU runtime also exists as a separate engineering output.
Numerical runtime checks passed within their stated scopes, but timing and
physical deployment qualification remain incomplete; the latest measured-clock
benchmark stopped at a thread-verification failure. No closed-loop locomotion
or autonomous robot has been demonstrated. Hardware work does not resolve the
biological or detection limitations above.
[Live project record](PROJECT_PROGRESS_REPORT.md).

Our current recommendation is to freeze and numerically qualify a defined
visual input, use controlled scene symmetry/asymmetry to trace the first
misleading bilateral signal, resolve the published simulator and physiological
measurement gaps, and test one evidence-supported revision on separate new
environments. This is a proposed next study, not an executed repair or guarantee
that the next modification will succeed.

For the second opinion, we would particularly value answers to these questions:

1. Is small-yaw classification the right immediate scientific objective, or
   should a matched physiological response benchmark come first?
2. Which experiment would most decisively separate a visual-input problem, a
   circuit-model problem and a readout problem?
3. What can be concluded about bIPS from the existing lesion and normalization
   controls, and what additional control is essential?
4. What is the minimum biological evidence needed before changing the circuit,
   and is exact author-code reproduction necessary for the next useful result?

In undergraduate terms: **we have a reproducible model that responds to turns
and a clearer account of how bIPS changes that response. It still confuses some
straight walking with turning. We want to explain that confusion and test any
improvement against both unfamiliar scenes and real neural measurements.**
