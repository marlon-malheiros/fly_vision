# Male optic frontend / MaleCNS: complete technical status and research handoff

**Version:** V1, 8 November 2026, America/Belem.  
**Workspace:** `<WORKSPACE>`.  
**Purpose:** consolidate goals, implementations, positive results, failures, biological constraints, computing resources and genuinely outstanding work. This is a retrospective evidence synthesis, with selected fresh integrity/hardware checks. It introduces **no new neural experiment, parameter fit or biological-validation claim**.

The study-specific protocols, corrected reports and numerical artifacts linked below remain authoritative for their own conditions. Older summaries describe earlier states; they must not override later results. The [live progress report](docs/PROJECT_PROGRESS_REPORT.md) records the development trail. A [machine-readable evidence snapshot](results/project_technical_status_2026_11_08_v1/key_evidence.json), [selected archive audit](results/project_technical_status_2026_11_08_v1/selected_study_integrity.json) and [document catalog](results/project_technical_status_2026_11_08_v1/document_catalog.json) accompany this handoff.

## 1. Executive assessment

**We have a functioning research platform, a bounded neural-only small-turn simulation success, and several limited physiological prediction successes. We do not yet have one end-to-end model that combines those successes into a broadly reliable, physiologically validated walking circuit.**

The strongest results belong to different model versions and different assays:

| Objective | Current evidence | What it does not establish |
|---|---|---|
| Convert images into direction-sensitive neural input | Fixed-neighbor functional frontend passes its declared engineering controls, covers 13,579 T4/T5 targets and drives the frozen connectome | Anatomically emergent or fully physiological T4/T5 computation |
| Simulate walking optic flow | Binocular 3D rendering, prescribed translation/yaw, analytical flow and numerical controls are implemented | Leg mechanics, independent head stabilization, natural sensory noise or active steering |
| Detect small turns from neural activity | A frozen artificial neural-only readout passes a fresh 24-room ±2°/s benchmark at all three walking speeds | Universal reliability, a biological decoder or an identified bIPS mechanism |
| Provide an engineering comparison | Dense image-only and hybrid methods pass a separate 60-room small-turn benchmark | Neural necessity or biological validation; image-only is at least as good in that study |
| Constrain central circuitry anatomically | Recorded uLPTCrn/H2rn candidate chemical pathways and six horizontal LPi cells were added in separate versions | Complete circuitry, measured electrical conductances or correct dynamics from anatomy alone |
| Predict physiology | Restricted Mi1, T4c measurement-transfer and T4 voltage-transfer tests pass within their declared scopes | That one whole model reproduces every neuron, stimulus, compartment and behavioral state |
| Run portable software | CPU packages, camera-like replay interfaces and historical GPU implementations exist | A calibrated live camera/robot or guaranteed real-time deadlines |
| Control a fly/robot | No closed-loop controller is established | Autonomous locomotion or compensation of unintended turns |

**Important clarification of previous short updates:** saying that broad small-turn reliability is unfinished must not erase the actual bounded 2°/s neural-only success of 2 November. Conversely, the new T4 voltage success of 6 November does not transfer that decoder qualification to a new frontend. These are separate achievements that still need a justified integration.

**Most recent scientific milestone:** a T4 geometry-uncertainty ensemble, designated primary before testing the reserved responses, passes its frozen moving-bar waveform criterion with **33.13% lower pooled MSE than a direction-blind reference**. One of its three cells is slightly worse than that reference. The author's stationary-fit cohort overlaps these recordings, and permitted per-cell calibration uses stationary responses and early motion localizers. This is restricted stimulus-transfer evidence, not independent-laboratory or whole-system validation. [Reserved T4 report](docs/T4_RESERVED_TRANSFER_REPORT_V1.md).

## 2. What we are trying to achieve

### 2.1 Central scientific question

Can a visual circuit based on the male *Drosophila* connectome detect a small body rotation while the animal walks forward, and does bIPS-associated circuitry improve this computation?

Forward motion creates strong image motion even if the fly does not turn. Rotation adds another pattern. The scientific challenge is to explain how neural circuits separate these components across depth, texture, speed and behavioral state, and to make predictions that can be compared with neural recordings and perturbations.

The immediate original assignment was an **open-loop** study: prescribe movement, render its images, run the existing frontend/network and measure HS, H2, bIPS and DNp15. Later work added sensitivity thresholds, targeted lesions, anatomical reconstruction, stronger physiological comparisons and hardware feasibility.

The long-term PhD ambition is a physiologically grounded sensorimotor model that can eventually support an autonomous robotic agent. That ambition is broader than the completed experiments.

### 2.2 Three objectives that must remain separate

1. **Functional utility:** does a defined decoder detect turns under stated conditions?
2. **Biological explanation:** does a specified model predict the activity and perturbation responses of the relevant real neurons?
3. **Engineering deployment:** can the computation run with calibrated sensors, acceptable latency and reliable data handling on the intended machine?

A pass in one column is not evidence that the other columns passed. Faster execution cannot fix a physiological mismatch. A decoder can extract useful information from a neural population without representing the biological downstream circuit. A good single-cell physiological prediction does not establish behavioral reliability.

### 2.3 Scope and constraints retained throughout

- Preserve original baselines and sealed evidence; develop changes in identified versions.
- Freeze conditions, splits, ablations and analysis criteria before new test outcomes.
- Use identical inputs for paired intact/lesioned circuits.
- Separate decoder fitting, cutoff calibration and held-out testing.
- Do not invent missing chemical connections, electrical conductances or measured physiology.
- Report negative outcomes and numerical failures rather than adjusting criteria to obtain a pass.
- Distinguish exploratory diagnostics from prospective tests.
- Defer closed-loop motor control until the open-loop scientific questions are adequately resolved.

“Frozen” means a reproducible comparator and a fair test. It does not mean the model is assumed correct forever. New, separately versioned models and development-only calibration are allowed when scientifically justified.

## 3. Terminology and units

| Term | Meaning in this project |
|---|---|
| Optic flow | Image motion caused by movement of the observer and/or objects |
| Translation | Movement of the fly through space without necessarily changing heading |
| Yaw | Rotation about the vertical body axis: a left/right change of heading |
| °/s | Angular velocity. At 2°/s, a 190-ms decision interval contains only 0.38° of heading change |
| mm/s | Translational walking speed; it is not an angular retinal speed |
| T4 / T5 | Early motion-selective neuron classes associated with bright-edge/ON and dark-edge/OFF processing; their subtypes represent different direction channels |
| HS | Horizontal system wide-field visual neurons; this model includes several HS subtypes on each side |
| H2 | A bilateral class of horizontal optic-flow-sensitive neurons |
| bIPS | The central inhibitory cell class represented by PS321/bIPS in the selected graph |
| DNp15 | A descending neuron class studied as an optic-flow output; older literature comparisons include DNHS1 identity correspondence |
| uLPTCrn / H2rn | Candidate recurrent-neuron families added using qualified connectomic identity/homology evidence |
| LPi | Lobula plate intrinsic neurons; the reconstructed horizontal MaleCNS LPi12/LPi21 candidates must not be confused with vertical LPi3–4/4–3 names |
| Mi1, Tm3, Mi4, Mi9, CT1 | Upstream visual pathways/components considered in physiological motion models; a named functional branch is not automatically a reconstructed anatomical neuron |
| PD / ND | Preferred direction / opposite, null direction under the stated localization rule |
| FPR | False-positive rate: straight-walking cases incorrectly reported as turns |
| Neural-only readout | An analytical decoder whose inference inputs are neural activity features; it can still have artificial learned weights |
| Biological validation | Predictive agreement with suitable real measurements under explicit stimulus, identity, measurement and independence assumptions |
| Numerical verification | Evidence that the implementation solves the specified equations and analysis correctly |
| Skill | `1 − model_MSE / reference_MSE`; it is not accuracy or a percentage of biological validity |

The inherited network uses signed model states and `tanh` rates. They are **not calibrated spikes/s, mV or calcium fluorescence**. The published T4 cable produces electrical voltage in mV. ArcLight and GCaMP measurements use different fluorescence units. These quantities cannot be interchanged by naming them all “neural activity.”

The visual model estimates net rotation. Without an efference copy, motor command or another intention signal, it cannot tell whether physically identical rotation was intended or accidental.

## 4. Architecture and distinct model versions

### 4.1 Main walking pipeline

```text
Prescribed trajectory in a seeded 3D room
  → separate left/right retinal images
  → declared eye-chart sampling and visual motion frontend
  → body-ID-indexed T4/T5-like drive
  → selected MaleCNS recurrent chemical network
  → bilateral HS/H2/bIPS/DNp15 and/or local T4/T5 activity
  → external analytical yaw readout
```

The newer physiological reference is a separate branch:

```text
Actual stored LED images + recorded display clocks
  → eleven sampled retinal inputs
  → published fixed T4 conductance/cable model
  → signed somatic voltage prediction in mV
  → comparison with recorded voltage

Still missing for this qualified candidate:
  justified full-eye/contrast/T5 treatment and voltage-to-network coupling
  → integrated MaleCNS walking model
  → fresh walking and downstream physiological qualification
```

### 4.2 Network inventory

| Version | Modeled cells | Selected chemical connections | Added content / limits |
|---|---:|---:|---|
| Original walking baseline | 13,593 | 203,861 | 13,579 T4/T5 sources plus 8 HS, 2 H2, 2 bIPS, 2 DNp15; no modeled gap edges |
| Anatomically strengthened chemical graph | 13,618 | 204,201 | Adds 17 uLPTCrn and 8 H2rn candidates, with 340 added recorded pairs |
| Horizontal LPi graph | 13,624 | See its graph ledger | Adds six LPi12/LPi21 cells and 22,338 included connection pairs involving them; 276,577 corresponding synapses |
| Full published FlyVis comparison | 45,669 | 1,513,231 | A distinct pretrained visual network with a native 34-output-population decoder; not the named MaleCNS downstream pathway |
| Published T4 cable | One reconstructed cell, 344 sections | 99 excitatory and 55 inhibitory sites | A detailed fixed physiological component; not a complete fly or the original rate graph |

Connection-pair counts, synapse counts, model input sites and compartment counts describe different objects. They must not be compared as though they were the same network size.

The larger structural audit examined a 65,799-neuron/1,967,771-edge export and streamed a 151,856,684-row raw connection table. These are **audited source datasets**, not the cell count of the selected walking simulation. CT1 contacts exist in the larger anatomy even though a filtered export omitted CT1; counts alone do not recover local branch placement. [Functional report](docs/PROFESSOR_FUNCTIONAL_FRONTEND_TECHNICAL_REPORT_V1.md), [Study B](docs/ANATOMICAL_STRENGTHENING_REPORT_V1.md), [LPi reconstruction](docs/HORIZONTAL_OPPONENCY_REPORT_V1.md).

### 4.3 Functional frontend equations and assumptions

For normalized luminance `L`, the frozen surrogate separates local contrast:

```text
c_ON  = max(2L − 1, 0)
c_OFF = max(1 − 2L, 0)
τ ḋ = c − d,                         τ = 30 ms
s_H = d(h−1,e)c(h+1,e) − d(h+1,e)c(h−1,e)
s_V = d(h,e−1)c(h,e+1) − d(h,e+1)c(h,e−1)
```

It averages signed fields over a 7×7 window before positive/opponent rectification, producing eight ON/OFF cardinal channels. The regular retinal grid is 173×173, with 1° pitch and ±1-site neighbors. All eight channels are sampled before fixed subtype routing.

The mapping from those channels to T4a–d/T5a–d slots is a **declared surrogate wiring assumption**. The delay, spatial pooling, eye-chart conventions and normalized drive scale are explicit choices, not a complete fitted biological upstream circuit. Correct direction-sensitive computation from pixels is therefore established more strongly than biological emergence of each subtype's preferred direction. [Equations and parameter provenance](docs/PROFESSOR_FUNCTIONAL_FRONTEND_TECHNICAL_REPORT_V1.md).

### 4.4 Network dynamics and normalization

The recurrent model has inherited low-pass state dynamics, signed chemical coupling and `tanh` readout; its exact gain, normalization, pole and forcing conventions are recorded per study. Representative inherited settings in the horizontal-opponency study are a 20-ms node pole, chemical gain `0.873579331825114`, drive gain `0.21936608020509474` and RK4 integration at 1 ms. These are model parameters, not measured time constants for every cell.

Adding presynaptic neurons changes postsynaptic weight-normalization denominators. Study B changes 10,894 old-core entries through that rule even though the underlying old-to-old counts are preserved. A new-family-silent copy retains those denominators and isolates normalization from transmitted new-cell activity. Zero electrical edges mean no electrical coupling is modeled; they do not establish that the biological circuit lacks it.

## 5. Development history and what was actually completed

This table is a navigation synthesis, not a claim that every historical decision was preregistered. Early development predates Git history; later freezes and seals are much stronger.

| Period | Work | Outcome and present interpretation |
|---|---|---|
| Early diagnostic | Corrected direction-blind input, eye charts and FlyVis integration | Required diagnostic executed; weak/incomplete tuning preserved |
| Early October | Published T4/T5 recovery, native controls, causal initialization repairs, texture/grating checks | Useful source reproduction; incomplete general image transfer; real initialization defects corrected |
| 13 October | Fixed-neighbor functional frontend | Declared engineering benchmark passes; physiological emergence remains a different claim |
| 15 October | Original virtual walking study | Large yaw discriminable across three scenes; qualitative downstream selectivity agreement |
| 19 October | Study A thresholds and lesions | Low-speed/weak-yaw failures; model-specific bIPS effects quantified |
| 19 October | Study B chemical reconstruction | Supported new anatomy added; no consistent small-yaw/physiology improvement |
| 21–24 October | More rooms, sampling diagnostics, published-circuit comparisons, CPU/GPU/camera work | Generalization and numerical limits expose earlier optimistic thresholds; engineering progress is separate |
| 25–27 October | Geometry fields, small-yaw alternatives, family dissection and LPi reconstruction | Several hypotheses tested and closed; opponent inhibition partially repairs directional response signs |
| 29–30 October | Final open-loop neural/lesion milestone and dense-image hybrid | Large, frozen DNp15-only small-turn test fails; separate hybrid/image engineering benchmark passes |
| 1 November | Full FlyVis walking/readout options; storage retirement | Tested new routes fail their 2°/s gates; large obsolete image caches deliberately deleted |
| 2 November | Raw local neural readout and negative-only cutoff calibration | A new 24-room neural-only 2°/s benchmark passes, with an older false-alarm counterexample retained |
| 2–5 November | HS contrast/frequency studies, fixed physiology search, Mi1 and T4/T5 source-stage tests | Several partial improvements and limited Mi1 success; no whole-model physiological pass |
| 5–6 November | T4c indicator relation, matched T4 voltage, flash timing/geometry audits | Restricted measurement prediction passes; older adapter/motion transfer fails; ambiguity identified |
| 6 November | Prospective reserved T4 transfer | Frozen physical-mV candidate passes a limited new moving-response test |
| 8 November | This synthesis | Reconciles scope/chronology, checks selected archives and current hardware; no new scientific experiment |

Source navigation: [early overall review](docs/PROJECT_OVERALL_REVIEW_V1.md), [development audit trail](docs/PROJECT_DEVELOPMENT_AUDIT_TRAIL_V2.md), [October second-opinion overview](docs/SECOND_OPINION_PROJECT_OVERVIEW_V1.md), [live progress](docs/PROJECT_PROGRESS_REPORT.md).

## 6. Original virtual walking and Studies A/B

### 6.1 Physical visual simulation

The original renderer uses textured box rooms and spheres, separate eye origins 0.3 mm apart and 2 mm above the floor, with 360×180 equirectangular images at 1° pitch. Rays hit the nearest surface. Motion integrates body-forward translation and yaw consistently, producing curved paths for combined motion. Eye baseline, body height and optical conventions are scenario assumptions, not specimen measurements.

The initial 2-s episodes move during 0.5–1.5 s. Forward speeds are 5.5, 11 and 16.5 mm/s. The first large-yaw study uses ±55.5°/s and 12 conditions per scene: stationary, three forward-only, two yaw-only and six combined conditions. Across three scenes that is 36 primary episodes. DNp15 and the all-cell decoder each classify all 24 held-out scene conditions correctly; DNp15's yaw/translation index exceeds HS in 9/9 scene/speed comparisons. This is a finite deterministic result at large yaw. [Initial report](docs/VIRTUAL_WALKING_OPENLOOP_REPORT_V1.md).

Analytical controls check translational inverse-depth dependence, rotation's central-camera depth independence, flow superposition, scalar ray intersections and finite-landmark reprojection. Later source/solver checks distinguish input discretization from integration error. Numerical convergence is never inferred for every input from a few representative refinements.

### 6.2 Study A: conditions and results

Study A crosses three walking speeds with yaw `0, ±2, ±5, ±10, ±20, ±40°/s`: **33 walking conditions plus one stationary control per room**. Twelve rooms split 3 training /3 calibration /6 held-out supply 408 primary inputs. Twelve graph copies include intact/sham, bilateral/unilateral bIPS silencing, targeted bIPS outputs and HS/H2 controls.

The original DNp15 readout detects ±2°/s turns in **8/12, 4/12 and 3/12** cases across increasing speeds. Its straight false alarms are **1/6, 2/6 and 0/6**. Under the original resolution, a 20°/s threshold qualifies at the fastest speed, but later finer-image and larger-room work prevents treating it as a generally converged threshold. The later 40-room DNp15 results are 46/80, 26/80 and 14/80 small-turn detections with 6/40, 8/40 and 6/40 straight alarms. [Study A](docs/YAW_SENSITIVITY_ABLATION_REPORT_V1.md), [later evidence synthesis](docs/YAW_BIPS_EVIDENCE_SYNTHESIS_V1.md).

“Unresolved threshold” often means false-alarm control failed, not that the circuit contains no yaw signal. Thresholds use a project rule—at least80% detection/sign accuracy and at most10% observed straight alarms—not a measured biological sensory limit.

### 6.3 What we learned about bIPS

With a fixed intact decoder, bIPS perturbations change DNp15 gain and bilateral baseline balance. In the larger legacy-profile test, fast straight alarms increase from 6/40 to 14/40 after bIPS suppression. In the original six-room test, bilateral suppression changes fast alarms from0/6 to4/6, and a direct bIPS→DNp15 cut yields3/6.

However, lesion-specific recalibration can recover the earlier fast threshold. Substantial yaw-dependent activity survives silencing. Therefore the results support a role in **shaping a particular response code**, not a demonstrated indispensable source of yaw information. Unilateral improvements can be calibration shifts rather than genuine information gains. Idealized output silencing, deleting selected chemical edges, TNT perturbations and receptor manipulations are different interventions.

The artificial neural-only decoder that later passes 2°/s reads T4/T5 directly and does not establish that the anatomical HS/H2→bIPS→DNp15 pathway implements that decision. Computational lesion effects establish causality inside the equations, not biological causality. [bIPS synthesis](docs/PROFESSOR_YAW_BIPS_SUMMARY_V1.md).

### 6.4 Study B and normalization controls

The anatomical expansion preserves original neuron ordering/counts and adds25 candidate recurrent cells. Candidate homologies and transmitter predictions remain qualified. Another80,833 recorded incident pairs to omitted partner types remain outside the selection.

At ±2°/s, expanded DNp15 bilateral separation is about72% of the original, and about74% when both added families are silent. Much of that amplitude change therefore persists without their transmitted activity and is attributable to inherited normalization within this model. Added anatomy does not automatically improve task performance or physiology. [Study B report and ledgers](docs/ANATOMICAL_STRENGTHENING_REPORT_V1.md).

## 7. Small-turn reliability: failures, engineering success and neural-only success

### 7.1 What failed before the bounded success

Direct bilateral mean/change readouts, longer averaging, several spatial population readers, published direction fields, gain/inhibitory calibrations, nuisance-suppression readers and full pretrained FlyVis routes were tested in separate protocols. Many fit development data but fail new-room false-alarm control or numerical refinement. A 2,424-episode final open-loop study with60 final test rooms fails its predeclared DNp15 small-turn capability goal. That failed release remains failed. [Final open-loop milestone](docs/FINAL_OPENLOOP_MILESTONE_REPORT_V1.md).

The full FlyVis network does respond correctly to canonical slow image motion, but several walking readers fail once forward translation and scene structure are present. Both spherical and perspective input hypotheses were executed. Merely proposing to “use an existing neural vision model” is therefore not an untried solution. [Full neural options](docs/NEURAL_MODEL_OPTIONS_REPORT_V1.md), [sequential repairs](docs/SEQUENTIAL_SMALL_TURN_REPAIRS_REPORT_V1.md).

### 7.2 Engineering image/hybrid reference

The dense image branch uses a geometric projection to reject forward-translation flow and estimate yaw. It assumes body-forward translation, yaw-only rotation and stationary surroundings. The clearly labeled hybrid combines image and neural evidence.

In60 untouched rooms, hybrid ±2°/s correctly directed detections are120/120,120/120 and115/120 across speeds, with0/60 straight alarms per speed. The image-only method detects120/120 at every speed with the same zero alarms. Thus this experiment supplies an engineering reference but demonstrates **no added reliability benefit from the neural branch**. It does not validate biological circuitry. [Hybrid report](docs/DENSE_IMAGE_HYBRID_REPORT_R3.md).

### 7.3 The neural-only 2°/s milestone that must not be omitted

A later readout preserves the frontend, LPi-intact graph and neural parameters while changing the artificial analysis of local T4/T5 and downstream signals. It receives neither an image-motion estimate nor true walking speed at inference. A fixed threshold is calibrated using40 new negative-only rooms, then frozen before24 different new test rooms.

| Walking speed | Correctly detected ±2°/s turns | Each sign | Straight alarms | Correctly detected ±5°/s turns |
|---:|---:|---:|---:|---:|
|5.5 mm/s|48/48|24/24 each|0/24|48/48|
|11 mm/s|48/48|24/24 each|0/24|48/48|
|16.5 mm/s|42/48|21/24 each|0/24|48/48|

Stationary alarms are0/24. The endpoint is190 ms after yaw onset. All81 retained numerical gates pass. The fixed cutoff is`1.1329958232706985`, obtained by the predefined39-of-40 negative-episode rank rule, not by moving it into an interval chosen from the final test.

This is a genuine bounded computational success. It is not universal reliability: an older inspected cohort still has3/24 fast straight alarms under that cutoff. Zero alarms in24 rooms does not statistically certify a population false-alarm probability below10%; rooms also come from one noiseless static-scene generator. Noise, moving objects, other motion axes and physical cameras are separate tests. [Milestone](docs/NEURAL_SMALL_TURN_MILESTONE_2026-11-02.md), [full report](docs/RAW_LOCAL_CALIBRATION_REPAIR_REPORT_V1.md), [machine-readable outcomes](results/raw_local_calibration_repair_v1/test_results.json).

## 8. Anatomical mechanisms and downstream physiology

### 8.1 Family dissection and the DNp15 mismatch

The uLPTCrn/H2rn2×2 dissection finds heterogeneous side-dependent contributions to bIPS preference. H2rn-family silencing has the larger conditional effect in those assays; neither family alone is universally necessary for a positive index. Existing current accounting makes another broad H2rn pathway sweep a lower priority than it first appeared.

The DNp15 metadata audit checks16 sessions/46 arrays and finds no supported soma/neurite/clock indexing repair. Waveform mismatch has amplitude and shape components. An oracle gain fitted to each known trace is a descriptive upper bound, not an admissible common physiological model. [Family dissection](docs/BIOLOGICAL_FAMILY_DISSECTION_REPORT_V1.md).

A quiet fly strongly affects mean per-fly skill. For the known primary DNp15 cohort, four of five fixed skills are positive; the fifth is−2.84770 because its zero-response denominator is small. Mean skill is−0.25730, median+0.34686, and ratio-of-pooled-errors skill+0.33117. None replaces the frozen primary retrospectively, and the quiet animal is not removed. Reporting only the negative mean or only the favorable median would both be incomplete. [Statistics and opponency audit](docs/SECOND_OPINION_OPPONENCY_AUDIT_V1.md).

### 8.2 Horizontal LPi reconstruction

Six source-supported horizontal LPi candidates and their recorded chemical edges are incorporated in a separate version, with LPi-silent normalization and functional-opponent controls. These MaleCNS candidates have GABA consensus predictions; transmitter prediction is not direct receptor measurement. Naming them as the vertical glutamatergic LPi3–4/4–3 circuit would be an anatomical error.

Recorded LPi changes mean DNp15 null-yaw response from+0.002516 to−0.000616 in the known45°/s display assay. The same enlarged graph with LPi silent remains positive, distinguishing transmitted activity from normalization. But preferred responses also shrink, regressive translation remains positive and recording metrics are mixed. Mean DNp15 skill improves to+0.09978 while pooled-error skill worsens; bIPS full-waveform skill falls despite an improved selectivity index. No candidate passes the complete frozen advancement rule. “Add missing LPi” is therefore an already executed partial repair, not an untouched universal fix. [LPi report](docs/HORIZONTAL_OPPONENCY_REPORT_V1.md).

### 8.3 Physiological evidence matrix

Different rows concern different versions and observation models. They cannot be combined into a claim that one model passed the whole circuit.

| Target / assay | Supported result | Material unresolved issue |
|---|---|---|
| H2 direction curves | An exploratory model comparison is completed; mean PD error16.72° versus13.76° for a body-horizontal geometric reference | Approximate stimulus/pose mapping and limited specificity; no whole-circuit physiological pass |
| HS contrast | Functional normalization improves half-contrast PD ratio from21.8% toward recorded91.4%; a gain-control candidate predicts94.8% | Other PD/ND contrasts and frequency tuning still fail |
| HS temporal/frequency processing | A72-model fixed factorial search and refinements are completed | No primary candidate passes all guards; confirmed finalists have wrong preferred15-Hz sign |
| Adaptive Mi1 proxy | Restricted positive-ROI, independent-repetition calcium prediction passes in qualified reserved control animals | Approximate observation/coupling model, narrow temporal assay; its whole-network integration later fails |
| Adaptive Mi1→HS integration | Complete candidate/control network comparisons and numerical checks | Adaptive version has6/7 frequency-band violations and wrong null behavior; stopped without retuning |
| T4/T5 source-stage direction screen | Four candidate representations are measured and independently checked | D=1 versus recorded development bands; no candidate advances; numerical edge repair does not repair biology |
| bIPS/DNp15 calcium | Some known-data waveform/index agreement and mechanistic improvements | Exact modified G3 arrays, indicator/compartment mapping, inspection history and mixed full-waveform agreement |
| T4c indicator relation | Restricted population static rectified-linear prediction passes | Unpaired cohorts, non-mV voltage-indicator units and negative calcium responses missed |
| T4 moving-bar voltage | Latest reserved physical-mV waveform test passes | Three cells, permitted local calibration, author fit overlap, finite geometry and incomplete inhibition evidence |

Evidence: [H2 comparison](docs/H2_FROZEN_MODEL_BENCHMARK_REPORT_V2.md), [HS gain/frequency](docs/HS_GAIN_TRANSFER_REPORT_V1.md), [factorial conclusion](docs/PHYSIOLOGICAL_FACTORIAL_SEARCH_CONCLUSION_R2.md), [Mi1 resolution](docs/MI1_VALIDATION_RESOLUTION_REPORT_V2.md), [Mi1 integration](docs/MI1_HS_INTEGRATION_REPORT_V1.md), [T4/T5 screen](docs/T4T5_STAGE_BENCHMARK_REPORT_V1.md), [sampling correction](docs/T4T5_SAMPLING_DIAGNOSTIC_REPORT_R3.md).

## 9. The recent T4 route: what changed and why it matters

### 9.1 Measurement relation before dynamics

The T4c comparison uses13 voltage-indicator and11 calcium sessions from distinct cohorts, with separate development and held-out recording dates. A development-fitted rectified-linear map gives held-out zero/reference skills0.730495/0.627874 and joint lower0.051865, passing its limited rule. It cannot reproduce negative calcium means in four directions. This is not an identified mV-to-calcium or voltage-to-release mapping, and its gain must not be transferred to horizontal T4 or MaleCNS drives. [Observation report](docs/T4_OBSERVATION_TRANSFER_REPORT_V1.md).

### 9.2 From a simplified adapter to the complete published cable

The earlier direct-voltage test removes calcium uncertainty but both simplified source representations fail against a direction-blind reference. The unchanged344-section published T4 cable then reduces MSE51.89% relative to the prior signed adapter on known cells3–5, yet still fails the full motion criterion. This distinguishes a material improvement from a complete biological qualification. [Direct voltage](docs/T4_DIRECT_VOLTAGE_REPORT_V1.md), [cable comparison](docs/T4_CABLE_MATCHED_REPORT_V1.md).

### 9.3 Stationary registration, timing and numerical repairs

The flash-transfer study uses820 trials/164 conditions, first3 repeats for calibration and last2 for repeat prediction. It fits only retinal offset, causal delay and nonnegative observation gain; neural parameters remain fixed.

Two numerical transport failures are preserved. Cold templates disagree with a300-ms-warmed actual-image run because the finite resistance floor shifts the resting baseline. Warm templates fix that offset but nominal pulse lengths still fail some parity checks. Recorded durations differ by tens of microseconds; min/nominal/max duration anchors and interpolation restore the unchanged0.005-mV guard. Numerical correctness is repaired without loosening the threshold.

The final calibrated flash-repeat criterion passes, but motion transfer still fails. Cell5 improves while cell4 worsens. Good prediction of a flash does not imply good prediction of a moving image. [Flash report and R1/R2/R3 history](docs/T4_FLASH_TRANSFER_REPORT_V1.md).

### 9.4 Geometric non-identifiability

The finite2D audit finds exactly equivalent stationary input patterns at multiple registrations. Cells3/4/5 have5/2/2 aliases of their selected position. For cells4/5, diagonal flash sequences cannot distinguish some horizontal from vertical shifts, although the moving inputs differ. This is input non-identifiability under a stated finite grid and sampling convention, not proof of biological neural degeneracy.

The predefined gain-preserving ensemble still fails; its secondary physical-mV ensemble passes the old-data criterion with reference skill0.252524 and lower0.133000. This secondary is then explicitly selected as the **next prospective candidate**, before the reserved comparison, rather than relabeled as an independent success on the old cells. [Geometry report](docs/T4_GEOMETRY_IDENTIFIABILITY_REPORT_V1.md).

### 9.5 Reserved test: strongest recent component evidence

New project-reserved author cells6–8 supply820 flash and288 motion trials. Early repeats localize PD; stationary first-three repeats select registration/timing. All fits, aliases and predictions are locked before later motion-response scoring. Seven selected MAT members occupy298,112,788bytes; the full archive is not downloaded.

| Candidate | RMSE(mV) | Zero skill | Direction-blind skill | Joint lower statistic | Rule |
|---|---:|---:|---:|---:|---|
| Frozen primary physical-mV ensemble |4.872612|0.726160|0.331340|0.102679|Pass|
| Flash-gain diagnostic |4.662535|0.749263|0.387755|0.226646|Pass|

Primary per-cell reference skills are−0.006834,+0.695480,+0.572348. All cells remain included. Cell8's calibration chooses spatial boundary−2; the grid is not expanded. No later motion response fits a parameter. Stationary physical-mV repeat prediction also passes, with zero/reference skills0.625520/0.321202.

All8 interpolation,12 actual-image and12 solver checks pass the unchanged0.005-mV guard; worst solver error0.003022693mV. Independent reconstruction checks820 flash traces,96 localizers,765 fits,75 geometry stacks and571,956 scalar pixel evaluations, with metric differences below1.46e−13.

Inhibition remains unqualified: early160-ms ND masks have0/362/63 bins, but later means in the nonempty masks are positive, not confirmed sustained inhibition. The model predicts positive means there too. No negative-mask failure is hidden by removing animals.

The result is **prospective for this project's reserved moving responses**, with localizers/calibration allowed. The authors' stationary-fit population overlaps the cohort; it is not independent of their original fit. The failed old primary, old scalar approximations and other cells' mismatches remain valid evidence. [Full reserved report](docs/T4_RESERVED_TRANSFER_REPORT_V1.md), [decision](results/t4_reserved_transfer_v1/decision.json), [independent review](results/t4_reserved_transfer_v1/independent_review.json).

### 9.6 What this milestone has not yet changed

The qualified cable/registration ensemble has **not been shown to improve walking-yaw detection inside MaleCNS**. Earlier physiological populations and full-eye integrations were attempted, but they are not the same qualified candidate with its new registration rule. No T5 counterpart, full spatial transfer or voltage-to-connectome-drive bridge inherits validation automatically. A single-cell voltage is not a calibrated presynaptic release signal. These are concrete integration gaps, not reasons to deny the component success.

## 10. Why things went wrong

There is no evidence for one universal cause explaining every failed branch.

| Failure source | Demonstrated evidence | What remains hypothetical |
|---|---|---|
| Original directional shortcut / imposed routing | Input shortcut was audited; corrected pixel-only paths and fixed surrogate routing are explicit | Surrogate routing does not prove biological emergence |
| Future-dependent initialization | A T4 image-clamp prefix discrepancy0.150695mV is repaired to0 in an earlier version | That bug was not the sole cause of later texture failures |
| Scene-dependent bilateral signals | Straight walking in asymmetric scenes creates false yaw scores in several fixed readouts | A unique missing biological neuron or pathway |
| Spatial sampling | Some early thresholds change with finer images; panorama interpolation changes smoothing | That all remaining errors disappear with infinite resolution |
| Numerical decision margins | Small state differences can cross a classifier cutoff despite stable mean responses | That stable averages alone certify all decisions |
| Missing opponent circuitry | Recorded LPi activity changes null-yaw sign in the model | That LPi alone fixes every waveform or small-turn failure |
| Network normalization | New-cell additions rescale old inputs, independently of new-cell activity | A universal beneficial effect of adding more anatomy |
| Contrast / temporal dynamics | HS contrast compression and frequency/ND errors persist in identified candidate families | Arbitrary new filters being the unique biological repair |
| Observation/identity mismatch | Indicator, compartment, side and voltage/rate distinctions materially affect comparisons | A single scalar observation gain being adequate everywhere |
| RF/timing registration | Exact flash aliases and recorded pulse-duration corrections are demonstrated | Continuous true RF location or the sole cause of all physiology errors |
| Statistics | Low-response flies make mean per-fly ratios unstable; pooled and median estimands differ | Permission to discard unfavorable animals or change the primary endpoint |
| Implementation/provenance | Label indexing, unsigned clocks, serialization, source-label ordering and open-writer seals caused real failures | That passing a software audit proves biological truth |

Notable corrected engineering failures include a sandbox-blocked launcher, malformed/NaN metadata, unsigned timestamp subtraction, globally numbered cell6 stimulus IDs, stale descriptive helper fields, reporter-cohort lookup errors and indexing a still-open log. Their corrections are recorded as new versions; scientific thresholds and old failed arrays remain preserved.

The investigation also suffered from scope expansion: a functioning input interface, a successful decoder, a physiological model and a real-time robot were sometimes discussed as one “working solution.” The report separates them because they require different evidence and resources.

## 11. What biological validation means here

A satisfactory test needs a named model version; identified neuron/side/compartment; matched or explicitly approximate stimuli; a justified measurement model; calibration data kept apart from scoring; quantitative references and uncertainty; and independent numerical controls.

It is not expected to be a literal1:1 trace match. Real recordings vary across cells, animals, behavioral states, indicators and noise. But this does not excuse systematic wrong-direction, wrong-frequency or contrast-response errors. A useful model should predict the relevant quantities better than strong declared references, within a stated domain, and retain negative results outside it.

Validation is also not achieved by repeated trial-and-error on the same test. Once outcomes inform a revision, those recordings become development evidence for that revision. Fresh animals, repetitions, stimulus families or other genuinely reserved quantities then support a new test, with the distinction stated precisely.

Some partial biological validation is now supported for specific components and assays. **Full biological validation of the current walking network is not supported.** It is equally unsupported to conclude that biological validation or neural small-turn detection is impossible in principle.

## 12. Hardware, software and engineering status

### 12.1 Current machine: directly inspected8 November

| Item | Current observation | Interpretation |
|---|---|---|
| CPU | Intel Core i5-12450H;8 physical cores,12 logical CPUs;reported maximum4.4GHz | Local laptop-class Linux computation, not an embedded-board benchmark |
| RAM / swap | About15GiB RAM and15GiB swap; snapshot has about4.4GiB memory available and5.9GiB swap used | Shared instantaneous system load; not a model-only memory requirement |
| OS | Fedora Linux44 KDE; kernel7.2.15-200.fc44.x86_64 | Current environment snapshot, not every historical run's environment |
| Display devices | Intel integrated graphics and NVIDIA GeForce RTX2050 detected by PCI enumeration | Physical GPU exists |
| NVIDIA runtime | `nvidia-smi` cannot communicate with the driver | GPU execution is not currently verified usable; historical successful GPU results remain historical results |
| Project filesystem | About475GiB total,326GiB used,147GiB available | Whole filesystem space, not just project occupancy |
| Project `du` footprint |166,355,054,592bytes, about154.9GiB | A filesystem block-counter observation; not a claim that every byte is essential |
| `/tmp` | About7.7GiB tmpfs; about6.4GiB available at inspection | Temporary environments are volatile and compete with memory-backed storage |

Exact commands/output are retained in the [hardware snapshot](results/project_technical_status_2026_11_08_v1/hardware_and_repository.json). No GPU driver, system configuration, device or model was changed for this report.

### 12.2 Software environments and an immediate reproduction caveat

The project package is`male-optic-frontend`0.1.0; its core dependency is NumPy and Python≥3.11, with separate optional scientific/source dependencies. Scientific execution commonly uses the sibling environment at`../mech_male_fly_cns/.venv/bin/python` with`PYTHONPATH=src:scripts` and one BLAS thread. The sibling repository is a preserved baseline/dependency, not the destination for new edits.

Current inspected scientific versions are Python3.14.10, NumPy2.5.3, SciPy1.18.1 and Matplotlib3.11.2. C++ is GCC16.2.1; Octave10.3.0 is available. These current versions are not a substitute for per-study archived environment records; versions have drifted since earlier runs.

The T4 worker used isolated Python3.11 / NEURON8.2.7 / NumPy1.26.4. **Its former `<TEMP>/t4-cable-matched-v1-venv` environment is absent today.** Saved code, model sources, raw data and outputs are retained, but a new full neural rerun requires restoring that pinned temporary environment or an equivalent separately recorded one. No package installation was performed for this report. [Runtime probe](results/project_technical_status_2026_11_08_v1/runtime_versions.json).

FlyVis and HDF5/source-processing environments are separate again; do not assume the minimal core installation reproduces every branch. Archived requirements, checkpoints and source hashes are the intended reproduction references.

### 12.3 What deployment work achieved

A portable CPU camera runtime and standalone packages exist. They process synthetic calibrated binocular fixtures through projection, frontend, recurrent graph and readout, with independent numerical parity. V8 preserves recurrent history through complete delayed frames while withholding expired outputs. Missing/corrupt/reordered frames remain faults; delayed data are not silently invented.

Historical CPU camera timing shows improved throughput but not zero missed deadlines: a four-thread active-wait configuration has median8.757ms, p95 11.505ms and213/1,200 paired updates over10ms. A sustained CUDA replay exceeds100 updates/s on average but still has1,096 individual misses of its10-ms budget. Those experiments exclude some acquisition/rendering/transport costs and use repeated/synthetic fixtures. They are not hard-real-time or physical-camera guarantees. [CPU V3](docs/PORTABLE_CPU_CAMERA_REPORT_V3.md), [continuing V8](docs/PORTABLE_CPU_CONTINUATION_REPORT_V8.md), [sustained CUDA](docs/SUSTAINED_CUDA_REPLAY_REPORT_V1.md).

V9 protocol/scripts are present as untracked work; the reviewed record does not establish a completed V9 deployment qualification. They were left untouched. There is no verified live robot, calibrated camera pair or motor-control loop in this handoff. The requested deployment target is portable Linux CPU first.

## 13. Data, storage and reproducibility

### 13.1 Why the folder became enormous

The project retained many complete rendered binocular movies, retinal grids, source arrays and neural histories across successive studies. A single401-frame pair of float32 173×173 retinal arrays is about96MB in decimal units before other fields/compression. Repeated image retention across hundreds or thousands of episodes readily dominates storage; it is not the minimal size of the connectome or executable model.

The user-authorized cleanup on1 November deletes2,823 old generated movies:159,674,482,886 nominal bytes(148.71GiB), recovering about149.6GB of measured filesystem space. Models, biological recordings, result arrays, original indexes, seeds, recipes and selected representative movies are retained. This follows an initial smaller cleanup of redundant material. [Retirement report](docs/LEGACY_MOVIE_RETIREMENT_REPORT_V2.md), [earlier recovery](docs/STORAGE_RECOVERY_REPORT_2026-11-01.md).

This is deliberate deletion, not an off-device backup. Historical full-index availability checks now fail for those ledgered movie paths. Do not call that new corruption or claim every original archive passes. Selected regeneration has been demonstrated; universal bitwise regeneration of all retired movies has not. Do not refill the disk by automatically rebuilding them during an audit.

### 13.2 Retained evidence and source locations

| Location | Purpose |
|---|---|
| `src/male_optic_frontend/` | Frontends, samplers, circuit/runtime adapters and readout components |
| `scripts/` | Versioned experiment, acquisition, independent-review and completion entry points |
| `configs/` | Study conditions, assumptions and frozen criteria |
| `tests/` | Unit/interface/numerical checks; not a biological-validation percentage |
| `data/raw/` | Retrieved external source code, anatomy and physiological data |
| `results/<study>/` | Generated observations, predictions, receipts, failures and seals |
| `docs/` | Scientific reports, protocols, corrections, deployment notes and progress |
| `results/raw_local_calibration_repair_v1/` | Qualified neural-only decoder, operating point and finite-room outcomes |
| `results/t4_reserved_transfer_v1/` | Latest reserved T4 physiology inputs, predictions, reviews and completion proof |

Early Git history is incomplete: the retrospective tracking audit found untracked source before later snapshots began. Scientific artifact manifests supply additional provenance but cannot reconstruct every historical edit. Git commits and SHA256 seals detect/version changes; they do not constitute an off-device backup. Source/data directories intentionally appear untracked/ignored in places; that alone does not mean the numerical evidence is absent.

### 13.3 Fresh selected integrity check for this report

All indexed files in the six selected intact archives below were rehashed on8 November. These are entry checks, not counts of unique animals/experiments; indexes can overlap conceptually or contain snapshots.

| Selected archive | Indexed files | Indexed bytes | Fresh result |
|---|---:|---:|---|
| Neural-only cutoff-repair benchmark |1,747|31,929,968|Pass|
| T4c static indicator transfer |45|791,855|Pass|
| Full T4 cable matched comparison |466|6,556,163|Pass|
| T4 flash transfer, including failed numerical versions |4,267|225,417,435|Pass|
| T4 geometry-identifiability diagnostic |234|3,810,483|Pass|
| Reserved T4 transfer |1,911|312,426,762|Pass|

This fresh check does not re-solve the neural equations or re-score the whole project. It establishes retained bytes in selected archives and must not be generalized to all retired-movie indexes. [Per-index hashes and checks](results/project_technical_status_2026_11_08_v1/selected_study_integrity.json).

### 13.4 Costs of representative recent work

| Study | Recorded computational work | Main retained result / cost boundary |
|---|---|---|
| Neural-only cutoff repair | About4,818.5CPU seconds; peak263MB worker RSS | Four one-thread workers; compact features/scores, no bulk movies; excludes assistant usage |
| Fixed72-model physiology search | About7,960CPU seconds; peak1.84GiB worker RAM | Finite failed candidate family; about119MiB output before final corrections |
| T4 flash transfer/corrections |248 new solves;45.01 childCPU seconds | Raw files dominate roughly225MB archive; preprocessing/acquisition/review excluded |
| T4 geometry diagnostic |40 new solves;11.42 childCPU seconds | About3.81MB indexed archive; no raw download |
| Reserved T4 transfer |228 solves;42.22 childCPU seconds; peak887MB worker RSS | About312.43MB indexed archive, mostly298.11MB raw; network retrieval dominated wall time |

CPU time, elapsed time, retained storage and assistant/model usage are different quantities. These measurements do not recover the total historical assistant usage or monetary cost; no complete cost ledger is claimed.

## 14. What has already been tried, and what remains untried

### 14.1 Already tried; do not propose these as brand-new fixes

- Multiple frozen/pretrained FlyVis comparisons, including a full native decoder and two camera geometries.
- Fixed-neighbor motion computation and explicit ON/OFF/cardinal routing.
- More scenes, new splits, different readouts, spatial features, additional averaging and cutoff calibration.
- Published direction-field projection and controlled retinal/input/solver refinements.
- uLPTCrn/H2rn reconstruction, family silencing, bIPS output cuts and normalization controls.
- Horizontal LPi reconstruction, existing LPi feedback and a separately labeled functional-opponent diagnostic.
- Known-recording gain/contrast/temporal hypotheses, a72-model finite physiology grid and adaptive Mi1 integration.
- T4/T5 source-stage physiology screens, original T4/T5 author-code reproduction and various population embeddings.
- Full T4 cable voltage comparison, flash-only registration/delay calibration, exact timing and finite2D uncertainty averaging.
- Image-only and image/neural hybrid engineering references.
- CPU/GPU optimization, standalone replay and camera-clock/fault interfaces.

These attempts have different controls and limits; “everything possible was tried” would be false. “Nothing useful worked” would also be false.

### 14.2 Distinct outstanding options

| Option | Actual remaining question | Evidence/budget prerequisite |
|---|---|---|
| Integrate the newly qualified T4 candidate | Does this specific physical-mV/registration version improve circuit physiology and walking detection? | Explicit spatial/contrast extension and voltage-to-drive contract; preserve old baseline; no automatic transfer of old decoder qualification |
| Matched T5 companion | Does a comparably qualified OFF-pathway component transfer under matched recordings and stimuli? | Existing T5 source reproduction is not this new held-out integration test; identity, timing and population split need admission |
| Validate the coupling bridge | How does predicted somatic voltage relate to drive/release entering the rate network? | Measurements or explicit functional assumptions; a T4c fluorescence gain does not identify this bridge |
| Broader fixed-detector reliability | Does the already successful neural-only detector retain its operating point over more independent negatives and scene families? | No threshold retuning; predeclared uncertainty and noise/scene distributions |
| Genuine out-of-distribution inputs | Effects of camera/photon/neural noise, moving objects, gait/head movements, lateral translation, pitch/roll and varying onsets/speeds | One controlled perturbation family at a time; do not start with an unrestricted giant sweep |
| Evidence-constrained electrical coupling | Can measured electrical parameters improve HS/H2/central responses? | Conductances/receptor/compartment constraints; no fabricated gap weights |
| Spatially/compartmentally resolved downstream physiology | Can a common model predict matched HS/H2/bIPS/DNp15 recordings and perturbations? | Exact stimulus and identified neurite/indicator mapping, development/test separation |
| Full native Ammer reference comparison | What does the published multilevel opponent model predict under its proper native assay? | Source has been recovered; it has not thereby become a validated horizontal walking model |
| New task-trained visual encoder | Can a separately trained connectome-constrained representation improve motion coding? | Distinct training project, diverse development motion, separate physiology test; not equivalent to rerunning old FlyVis checkpoints |
| Live camera deployment | Does calibrated acquisition plus the complete runtime meet latency/freshness requirements? | Working driver, actual sensor/clock calibration and a named target; synthetic fixtures are insufficient |
| Closed-loop locomotion / intention | Can perception support stable steering, and distinguish intended from unintended turns? | Validated open-loop interface plus motor/intention signals and a separate control study |

“Untried” here means no completed equivalent experiment was established in the reviewed record. It does not imply that no related pilot, source audit or legacy implementation exists.

## 15. Recommended finite next milestone

**Move from the qualified T4 component to an explicit, separately versioned integration test. Keep the working functional frontend and qualified neural-only readout as comparators.**

1. **Interface admission first.** Write the input/output units, causal timing, optical sampling, spatial embedding, state initialization, ON/OFF coverage and voltage-to-network coupling. Identify which are measurements and which are assumptions. Restore the pinned worker environment only when a rerun is needed. If a biological bridge cannot be identified, label an engineering bridge as such rather than inventing a release calibration.
2. **One small integration control batch.** Test static, bright/dark, preferred/null, contrast and frequency controls, including a few matched recorded cases. Check both the qualified cable's voltage and the downstream drive separately. Require unchanged-source replay and numerical guards before any new behavioral score.
3. **Freeze the candidate and decoder policy.** A new encoder changes feature distributions. Define whether the old decoder is transferred unchanged or a development-only new decoder is fit; keep the two comparisons separate.
4. **One held-out walking comparison.** Use identical test images for old and new models, three walking speeds, straight controls and±2/±5°/s. Prefer compact traces/features, streaming images and a fixed computation/storage budget. Count endpoint and whole-control-episode alarms; retain the old-cohort counterexample.
5. **Then a targeted mechanism question.** If the integrated candidate qualifies, test a predeclared bIPS/LPi manipulation and the relevant normalization/retraining controls. Do not infer biological necessity from a decoder pass.

Stop or pivot if the interface is unsupported, numerical parity fails, physiological controls regress materially or the fixed behavioral criterion fails. A stopped candidate is a reportable result. Another broad search on already inspected recordings is not the default next step.

Suggested budget policy: perform the interface/evidence audit before another whole-network sweep; estimate full-run storage before launching; keep at least20GiB free; use one bounded pilot before committing to a fresh final test. These are recommendations for the next protocol, not retroactive changes to completed studies.

## 16. Experimental predictions worth discussing with the professor

- Record bilateral responses to straight versus small-yaw optic flow while varying scene depth and asymmetric texture. The model predicts that some straight-flow asymmetries mimic turning; robust biological responses in those cases would constrain a missing computation.
- Compare bIPS perturbation effects on forward-only baseline balance as well as yaw response magnitude. A raised false-alarm tendency can coexist with retained yaw information.
- Test horizontal LPi perturbations with preferred, null, forward and regressive stimuli together. The model predicts opponent suppression but also attenuation of desired responses.
- Measure the same compartments and indicators under matched stimuli across animals; constrain measurement transfer separately from neural dynamics.
- Use stationary stimuli with more than one informative spatial orientation if the goal is2D RF registration. A single flash geometry can leave motion-relevant positions indistinguishable.

These are testable model-derived hypotheses, not claims that the corresponding biological causal effects have already been established.

## 17. Main references and how they were used

Bibliographic links are primary papers, author repositories or official datasets. Online access was checked where available on8 November; some publisher pages redirected or blocked automated access. Existing pinned local sources and project receipts remain the basis for exact computational provenance. No newly advertised dataset release was substituted into a frozen graph.

1. **Erginkaya et al.(2025), “A competitive disinhibitory network for robust optic flow processing in Drosophila,” Nature Neuroscience.** Central HS/bIPS/DNp15 motivation and known physiological/perturbation comparisons. It does not directly validate this3D walking simulator or every dynamic observer. [Paper](https://doi.org/10.1038/s41593-025-01948-9); [author code/data](https://github.com/ChiappeLab/Erginkaya_et_al_2025).
2. **Gruntman, Romani & Reiser(2018), “Simple integration of fast excitation and offset, delayed inhibition computes directional selectivity in Drosophila,” Nature Neuroscience21,250–257.** Fixed T4 model and whole-cell stimuli underlying the recent matched-voltage route. [Paper](https://doi.org/10.1038/s41593-017-0046-4); [PubMed](https://pubmed.ncbi.nlm.nih.gov/29311742/); [model source](https://github.com/ModelDBRepository/239435); [recording collection](https://doi.org/10.25378/janelia.c.3955843).
3. **Gruntman, Romani & Reiser(2019), “The computation of directional selectivity in the Drosophila OFF motion pathway,” eLife8:e50706.** T5 physiological equations and author references; port fidelity and biological transfer remain distinct. [Paper](https://doi.org/10.7554/eLife.50706); [author code](https://github.com/reiserlab/T5ConductanceModel); [data](https://doi.org/10.25378/janelia.c.4771805.v1).
4. **Lappalainen et al.(2024), “Connectome-constrained networks predict neural activity across the fly visual system,” Nature634,1132–1140.** Published task-optimized visual network and checkpoint comparison reference. It demonstrates an approach, not automatic validation of our adapter or downstream graph. [Paper](https://doi.org/10.1038/s41586-024-07939-3); [FlyVis](https://github.com/TuragaLab/flyvis).
5. **Ammer et al.(2023), “Multilevel visual motion opponency in Drosophila,” Nature Neuroscience26,1894–1905.** Opponency context, T4c indicator data and a separate native model reference. Vertical-circuit parameters cannot be silently relabeled horizontal. [Paper](https://doi.org/10.1038/s41593-023-01443-z); [PubMed](https://pubmed.ncbi.nlm.nih.gov/37783895/); [pinned author source](https://gin.g-node.org/gammer/Ammer_et_al_2023/src/db1f8089b697d1b19da1394ef94450bbec24f32b).
6. **Mauss et al.(2015), “Neural Circuit to Integrate Opposing Motions in the Visual Field,” Cell162,351–362.** Experimental opponent-inhibition motivation; not a source of measured horizontal MaleCNS conductances. [Paper](https://doi.org/10.1016/j.cell.2015.06.035); [PubMed](https://pubmed.ncbi.nlm.nih.gov/26186189/).
7. **Pokusaeva et al.(2024), “Bilateral interactions of optic-flow sensitive neurons coordinate course control in flies,” Nature Communications.** Electrical/bilateral interaction evidence and a limitation of the chemical-only model. [Paper](https://doi.org/10.1038/s41467-024-53173-w); [institutional author copy](https://research-explorer.ista.ac.at/record/18444).
8. **Suver et al.(2016), “An Array of Descending Visual Interneurons Encoding Self-Motion in Drosophila,” Journal of Neuroscience36,11768–11780.** External descending-neuron voltage/steady-state comparison context; raw matched small-yaw data were not established by the bounded source search. [Paper](https://www.jneurosci.org/content/36/46/11768).
9. **Drews et al.(2020), “Dynamic Signal Compression for Robust Motion Vision in Flies,” Current Biology30,209–221.e8.** Motivation for contrast compression, not a complete validation of the implemented normalization. [Paper](https://doi.org/10.1016/j.cub.2019.10.035); [PubMed](https://pubmed.ncbi.nlm.nih.gov/31928873/).
10. **Zhao et al.(2025), “Eye structure shapes neuron function in Drosophila motion vision,” Nature646,135–142.** Anatomical direction fields, coordinate transforms and H2 direction-curve source material used in the corresponding audits. [Paper](https://doi.org/10.1038/s41586-025-09276-5); [H2 dataset v2](https://doi.org/10.25378/janelia.28462100.v2); [pinned transformation code](https://github.com/reiserlab/eyemap_T4/blob/99d2a43123db636cedb55af9ff31a59657e7d17e/eyemap_func.R).
11. **Henning et al., “Inhibitory columnar feedback neurons are involved in motion processing in Drosophila,” version of record2026.** Mi1/C2/C3 and motion-response source data. Some old project documents cite the2025 reviewed-preprint date; the source version/commit must remain explicit. [Version of record](https://doi.org/10.7554/eLife.108529.3); [pinned data/code](https://github.com/silieslab/C2C3_feedback_Henning/tree/745c6114b72a61dabc9389a1f024dbe22f679edf).
12. **MaleCNS consortium / Berg et al., “Sexual dimorphism in the complete Drosophila male central nervous system connectome,” Cell(2026).** Anatomical ecosystem. The official portal now listsv1.0; the project's frozen local source hashes/curated export remain its actual data provenance. [Paper](https://doi.org/10.1016/j.cell.2026.08.015); [official portal](https://male-cns.janelia.org/); [official downloads](https://male-cns.janelia.org/download/).
13. **Fujiwara et al.(2017)** and **Chiappe et al.(2010).** Walking-related nonvisual signals and behavioral-state effects motivate limitations of a fixed, visual-only gain model. [Fujiwara paper record](https://pubmed.ncbi.nlm.nih.gov/27798632/); [Chiappe article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4435946/).
14. **Borst(2025), “Differential temporal filtering in the fly optic lobe,” Journal of Computational Neuroscience53,507–520.** Source context for the adaptive temporal proxy. Its normalized physiology-to-voltage scaling is not an independently measured synaptic calibration for our integration. [Paper](https://doi.org/10.1007/s10827-025-00914-5); [author code](https://github.com/axelborst/temporal_filtering).

This bibliography identifies foundations and actual data sources; it does not claim that every published model/dataset was reproduced completely or that papers validate the project's final integrated model by association.

## 18. Reproduction entry points and handoff guidance

Start with this report and the relevant study-specific protocol, corrected entry point and completion index. Do not run fixed-path producers into sealed result directories; many intentionally reject overwrites. Use a fresh output namespace/worktree with the required recorded dependencies.

| Question | Main entry points / evidence |
|---|---|
| What is the functional baseline? | [Professor technical report](docs/PROFESSOR_FUNCTIONAL_FRONTEND_TECHNICAL_REPORT_V1.md), [fixed-neighbor reproduction](docs/FIXED_NEIGHBOR_MOTION_REPRODUCTION_V1.md) |
| What did the original walking task show? | [Walking report](docs/VIRTUAL_WALKING_OPENLOOP_REPORT_V1.md), [Study A](docs/YAW_SENSITIVITY_ABLATION_REPORT_V1.md), [Study B](docs/ANATOMICAL_STRENGTHENING_REPORT_V1.md) |
| Where is the actual bounded2°/s pass? | [Readout report](docs/RAW_LOCAL_CALIBRATION_REPAIR_REPORT_V1.md), [model](results/raw_local_calibration_repair_v1/model.json), [cutoff](results/raw_local_calibration_repair_v1/cutoff.json), [results](results/raw_local_calibration_repair_v1/test_results.json) |
| Which physiological candidate most recently passed? | [Reserved T4 report](docs/T4_RESERVED_TRANSFER_REPORT_V1.md), [driver](scripts/t4_reserved_transfer_v1.py), [reviewer](scripts/review_t4_reserved_transfer_v1.py), [decision](results/t4_reserved_transfer_v1/decision.json) |
| How were the recent T4 data retrieved? | [Acquisition script](scripts/t4_reserved_acquire_v1.py), [member freeze](results/t4_reserved_transfer_v1/before_acquisition.json), per-member receipts in its sources directory |
| What failed downstream? | [LPi report](docs/HORIZONTAL_OPPONENCY_REPORT_V1.md), [HS physiology search](docs/PHYSIOLOGICAL_FACTORIAL_SEARCH_CONCLUSION_R2.md), [Mi1 integration](docs/MI1_HS_INTEGRATION_REPORT_V1.md) |
| What can run on CPU? | [CPU report](docs/PORTABLE_CPU_CAMERA_REPORT_V3.md), [V8 package report](docs/PORTABLE_CPU_CONTINUATION_REPORT_V8.md) |
| What was deleted intentionally? | [Movie retirement](docs/LEGACY_MOVIE_RETIREMENT_REPORT_V2.md), [exact ledger](results/legacy_movie_retirement_v2/retirement.jsonl) |
| What was checked for this synthesis? | [Audit code](scripts/project_technical_status_audit_20261108_v1.py), [selected integrity](results/project_technical_status_2026_11_08_v1/selected_study_integrity.json), [hardware](results/project_technical_status_2026_11_08_v1/hardware_and_repository.json) |

For a second-opinion reviewer: evaluate each claim against its actual model version, units, stimulus, split and measurement model. Do not merge different candidates' passing assays into one imaginary validated model. An uncertainty ledger or failed protocol is not evidence that the underlying biological problem is impossible.

## 19. Professor-ready situation statement

We built a reproducible image-to-neural open-loop platform around a frozen MaleCNS subnetwork and completed yaw-sensitivity, generalization and circuit-ablation studies. The original downstream-only readouts have important weak-yaw/false-alarm limitations; bIPS changes gain and bilateral balance but its biological necessity is not established. A later artificial neural-only readout passes a predefined2°/s benchmark in24 fresh simulated rooms, although an older cohort still supplies false-alarm counterexamples. Independently, a fixed published T4 cable with a prospectively specified registration-uncertainty method passes a reserved moving-response comparison, reducing pooled error33% against a direction-blind reference. These are defensible computational and restricted physiological milestones, respectively. They have not yet been combined into one qualified whole-pathway model; voltage-to-circuit coupling, T5/downstream physiology, broader robustness and walking requalification are the next specific research gaps.

## 20. Short explanation for an undergraduate

We want to understand how a fly notices a gentle turn while it walks forward. We have a virtual fly, a vision algorithm and a connectome-based neural model. Some early versions confused fast straight walking with turning. We now have one way of reading the simulated neurons that passes a limited small-turn test, and a separate early visual-neuron model that predicts some new real recordings. These are real pieces of progress. The missing step is showing that they work together for biologically justified reasons, under more varied conditions. The project is neither finished nor empty: the useful next task is a carefully checked integration, not another unrestricted search on the same data.
