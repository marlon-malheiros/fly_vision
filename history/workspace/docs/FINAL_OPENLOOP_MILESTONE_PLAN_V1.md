# Final open-loop research milestone: one bounded end-to-end answer

2026-10-29. **Status: plan prepared; this final experiment has not run.**
This document proposes the remaining work and prospective criteria. It does
not alter any sealed study, reclassify earlier failures, or claim that the
neural small-turn goal is already achieved.

## The milestone in one sentence

Deliver one reproducible Linux CPU pipeline from binocular images through the
frozen visual frontend and LPi-strengthened MaleCNS circuit to a causal turn-onset
decision, and establish on fresh environments **whether it detects small turns,
how bIPS changes that performance, and which physiological claims are supported**.

The desired positive result is reliable neural-output small-turn detection.
The final research release must also be finishable if that desired result fails.
A completed negative study is a completed deliverable; it is not achievement of
the detector capability. Independent physiological validation is a separate
evidence status, not something inferred from a successful simulator score.

The scope is open-loop **yaw onset during established forward walking**. It
does not promise sustained-yaw tracking, inference of movement intention, a
walking gait model, robot steering, camera deployment or real-time wall-clock
performance. Those can be future milestones after this one closes.

## What is already available

| Component | Present status | Evidence |
|---|---|---|
| Binocular 3D renderer, functional frontend, frozen chemical graph | Implemented and numerically checked | [Walking study](VIRTUAL_WALKING_OPENLOOP_REPORT_V1.md) |
| Original yaw/bIPS ablations and candidate recurrent families | Completed; no reliable general small-yaw benefit established | [Evidence synthesis](YAW_BIPS_EVIDENCE_SYNTHESIS_V1.md), [anatomical study](ANATOMICAL_STRENGTHENING_REPORT_V1.md) |
| Working causal image/neural hybrid | Passed its finite simulated benchmark; external engineering readout with known speed | [Agreement study](AGREEMENT_YAW_REPORT_V1.md), [portable monitor](HYBRID_YAW_MONITOR_V1.md) |
| Recorded horizontal LPi reconstruction | Corrects mean DNp15 null-yaw sign in known 45 degree/s dot assay | [LPi study](HORIZONTAL_OPPONENCY_REPORT_V1.md) |
| Observation-scale calibration | Improves bIPS; DNp15 remains mixed; no complete scale-only repair | [Gain study](OPPONENCY_GAIN_CALIBRATION_REPORT_V1.md) |
| LPi candidate on fresh small-turn walking inputs | Not yet established | Planned here |
| Independent quantitative voltage comparison | Not yet executed; raw matched data availability unresolved | [Source constraints](../results/biological_family_dissection_v1/source_constraints_review.json) |

We will reuse these implementations and evidence. The working engineering
reference is a comparator and fallback, not a substitute for a neural result.
The LPi circuit remains a candidate; its previous advancement failures remain
recorded. No more gain/filter sweeps are part of this milestone.

## Six stages, with a concrete exit from each

| Stage | Work | Required output and exit |
|---|---|---|
| 1. Lock scope and inputs | Audit exact graph/source identities, old seals, seed history, ablation definitions and storage feasibility | Versioned execution protocol, complete input/seed ledger and known-data pilot; no fresh test results inspected |
| 2. Bound the physiology question | Audit eligible independent voltage evidence and freeze matched stimuli/endpoints | Either a feasible benchmark with uncertainty and an analysis freeze, or a source-gap ledger with explicitly limited biological status |
| 3. Connect the frozen system | Replay identical images through controls/LPi/lesions, implement the existing causal feature recipe, train only the external readouts | One command-line simulation/replay path, parity and leakage checks, frozen coefficients; no neural tuning |
| 4. Run the final held-out study | Execute the fixed speed/yaw grid in untouched rooms and score all models | Complete detection/direction/alarm curves, raw neural responses, bIPS effects, numerical checks and external comparison if feasible |
| 5. Audit once | Independently reconstruct metrics, uncertainty, key neural trajectories and input provenance | Pass/fail/source-limited evidence for every claim; software corrections versioned separately |
| 6. Close the release | Package code, model/configuration files, replays, figures and conclusions | Final technical report, one-page professor brief, undergraduate explanation, archived progress snapshot and verified immutable index |

Stages 2 and 3 may proceed independently after the model identities are locked.
Missing physiology files must not indefinitely block the computational test.
However, they do prevent a physiological-validation claim. Any newly discovered
biological evidence can motivate a later model version, not a quiet modification
of this candidate during its final test.

## Fixed experimental system

Primary chain:

```text
3D scene and trajectory → binocular retinal images → existing functional T4/T5 surrogate
→ frozen MaleCNS graph → bilateral DNp15 activity/history → external causal readout
→ left-turn onset / straight / right-turn onset
```

Simulator truth generates the trajectory and supplies training/scoring labels.
It must not enter the primary inference path as true speed, yaw, depth, onset,
scene identity, future frames or a matched straight-control trajectory.
The functional surrogate and external readout are modeling components, not
claims that every biological neuron or motor computation has been reconstructed.

Keep 1-degree retinal sampling, 5 ms image updates, 10 ms neural inputs,
the 1 ms solver, eye geometry, frontend and all inherited neural parameters.
Walking starts at 0.5 s and yaw at 1.0 s, with no state reset at the event.
Turn episodes run through 1.3 s; straight/stationary controls through 3.0 s.
Monitor straight walking over [1.0, 3.0) s. Validate camera/sphere/wall clearance
for the whole longer trajectory before responses are computed. Geometrically
invalid scenes follow a predeclared, outcome-independent exclusion/replacement
rule with every exclusion retained.

Use ten separately identified copies on identical images:

1. Original frozen circuit.
2. Expanded circuit before LPi.
3. Recorded LPi intact: primary anatomical candidate.
4. Same LPi graph, added LPi silent: normalization control.
5. LPi graph with bIPS silenced.
6. LPi graph with all bIPS outgoing connections removed.
7. LPi graph with only bIPS-to-DNp15 connections removed.
8. LPi graph with HS silenced.
9. LPi graph with H2 silenced.
10. LPi sham: identical intact computation.

Freeze exact body-ID/matrix masks; do not renormalize after lesions. Existing
chemical edges are the only anatomical edges. No electrical conductance,
unverified identity or physiological time constant is invented. Verify sham
parity and equivalence of bIPS silencing versus removing all its outputs in
the remaining cells. Retain the identity qualifications of recurrent families.

Keep the causal image detector and already frozen hybrid as engineering
comparators. The legacy hybrid explicitly receives the known constant walking
speed condition. That is a declared experimental input for that comparator,
not evidence of speed-independent visual inference. Primary neural inference
uses one readout pooled across speeds and does not receive true speed.

## Training, untouched testing and readout

Planned allocation, fixed in a seed manifest before rendering new outcomes:

| Split | Independent rooms | Conditions per room | Image episodes |
|---|---:|---:|---:|
| Readout training | 12 | 16 | 192 |
| Calibration/audit | 12 | 16 | 192 |
| Final untouched test | 60 | 34 | 2,040 |
| Total | 84 | — | 2,424 |

Training/calibration conditions are three speeds (5.5, 11, 16.5 mm/s) crossed
with yaw 0, ±2, ±5 degrees/s, plus stationary. Final testing adds ±10, ±20,
±40 degrees/s as secondary sensitivity-grid points, preserving the original
assignment's range. Each speed/magnitude has 120 signed turns and 60 straight
controls. The same rooms and straight controls are reused across conditions;
they are not new independent animals or extra independent straight trials.

Rooms are seed-disjoint from every previous study and from other splits,
balanced between empty and three-sphere scenes in the existing textured-room
family. This tests new instances of that family, not unrestricted natural scenes.
Fresh test images are generated only after coefficients and code are frozen.

Use the existing two-feature causal recipe: each side's current 100 ms mean
minus its own 100 ms mean 200 ms earlier. Fit a standardized linear ridge
readout with penalty 0.001 and unpenalized intercept on training rooms only,
pooling all three speeds. Training uses the primary conditions, including
stationary controls; no true speed enters inference. HS/H2/bIPS responses and
the same specified readout recipe are secondary descriptions of the circuit.

Use the fixed 1 degree/s decoder-equivalent boundary between straight and
the ±2 degree/s project target, preferring straight on a tie. This operating
point is an engineering choice already used in the project, not a biological
sensory threshold. It is not fitted to test rooms. Calibration rooms audit
generalization and readiness; they do not select a decoder family, alter the
cutoff, or trigger another gain search. Retain the calibration result even if
it is poor. Physical yaw-velocity estimation from arbitrary neural units is not
claimed by the decoder's degree/s-equivalent scale.

Primary lesion comparisons apply the unchanged intact LPi readout. A declared
secondary analysis retrains the same fixed recipe for each lesion using only
training rooms. This distinguishes disruption of an operating point from loss
of decodable information; neither result establishes biological necessity.

## Prospective capability criteria

At **every walking speed**, for ±2 degree/s and maintained at ±5 degree/s:

- At least 80% detected turns.
- At least 80% correct raw direction across all turns, including misses.
- At least 80% both detected **and** correctly directed by 200 ms after onset.
- At most 10% straight controls alarming at the endpoint.
- At most 10% straight episodes having any alarm during the full two-second
  monitoring interval. Count episodes, not callbacks.

Thus require at least 96/120 joint successes and at most 6/60 straight alarms
per speed. Also require at least 48/60 joint successes for each signed yaw,
so a strong right-turn result cannot hide a weak left-turn result. Stationary
episodes must have at most 6/60 any-alarm cases; verify their raw neural states
remain at the expected zero-drive equilibrium. Report readiness/undefined
outputs and all larger-yaw results. Missing/undefined outputs in a required
ready interval count as failures. The joint criterion, separate signed-yaw
requirements and explicit monitoring controls are prospective requirements.
The joint measure was recommended by the earlier
[acceptance review](SMALL_TURN_ACCEPTANCE_REVIEW_V1.md); these rules do not
retroactively change old 80/80/10 classifications.

The 200 ms criterion is simulated signal time, not camera-to-actuator or host
wall-clock latency. This is an onset detector; the own-history feature does
not by itself establish sustained-yaw tracking. Passing engineering reference
or hybrid gates does not constitute a neural-circuit pass.

Report paired room-bootstrap intervals, per-speed errors and denominators.
Cluster both signs/repeated speeds by room; use an appropriate room-level
interval for false alarms. Sixty rooms is a finite benchmark allocation, not
a claimed statistical-power calculation. Observed 80%/10% passage does not
establish population bounds; any stronger reliability statement needs its own
predeclared uncertainty criterion. No pooled result may hide a failed speed.
Report a smallest qualifying tested yaw magnitude only if its criteria and
those at every larger tested magnitude hold. Otherwise retain isolated or
nonmonotonic results without inventing a continuous threshold or sensitivity
below the minimum tested 2 degree/s.

## Physiological evidence stage

Start with the previously identified Suver et al. (2016) DNHS1 material and its
author-linked sources, plus at most two additional predeclared source families
chosen for relevant cell identity/stimulus evidence. Perform one bounded audit
of article, supplement, data-availability statement and linked repository for
each. Record searches and stop after that pass. Existing source searches are
reused; no indefinite repeat search for the missing Erginkaya G3 arrays.

Choose eligible targets from methods/cell identities and stimulus match, not
from whichever model predictions look favorable. Disclose that Suver has
already been inspected qualitatively; do not call the whole source blind.
Freeze the candidate circuits and matching/digitization protocol before new
numeric target extraction and model scoring.

Prefer signed preferred/null and rotation/translation steady-response ratios
that cancel an arbitrary common scale. A model state is not automatically a
voltage; specify the observation assumptions. Match retinal geometry, cell
subtype/side, stimulus direction/speed/contrast and averaging window as far as
the source supports. Near-zero denominators are unresolved ratios, not zeros.
Do not interpret digitization error alone as biological variability or confuse
SEM with between-animal spread. Numeric tolerances cannot be responsibly chosen
until the source's sampling/error definitions are audited; freeze them then,
before scoring new endpoints, rather than inventing them in this plan.

Possible exits are explicit:

- Eligible independent recordings: execute a matched quantitative comparison.
- Only suitable published curves: digitize with uncertainty and report a
  limited external consistency benchmark, with inspection history disclosed.
- Inadequate stimulus, identity, measurement or uncertainty information: record
  the gap, finish the computational study, and mark physiological validation
  **not established**. The milestone cannot be relabeled biologically validated.

No message to authors/professor is sent automatically. A data request can be
prepared later, but an external response is not a completion dependency here.

## bIPS interpretation and numerical audit

Quantify paired changes in DNp15 responses, bilateral asymmetry, joint detection
and straight alarms at each speed. Report fixed-readout and recalibrated-readout
lesion effects separately. A uniform bIPS benefit is not a required outcome;
if effects reverse with speed/readout or intervals include zero, report a
conditional or unresolved contribution. Model interventions are causal within
the equations, not proof of biological causality.

Use analytical optic-flow controls, exact trajectory checks, source-ID/sign
audits, prefix causality and no-reset checks. Predeclare three known pilot rooms
crossed with three speeds and yaw 0/±2: 27 primary refinement cases. Compare
image/input time steps, spatial sampling and solver refinement while preserving
physical frontend supports and the inherited 1 ms forcing ramp. If a refinement
changes the physical detector rather than its numerical approximation, label
it a different model instead of calling it convergence.

Require solver-state discrepancy below 1e-7 and readout-equivalent discrepancy
below 0.2 degree/s on this subset, with no decision flips for an unqualified
capability claim. Failed numerical gates remain failures. Independently
recompute every reported metric, bootstrap and ablation ledger; replay a
preselected subset of fresh cases from saved scene/input recipes. These
checks establish bounded numerical reproducibility, not physiology.

## Resources, stop rules and final package

Approximately 5.9 GiB is currently free in the project filesystem, so existing
drivers requesting 15–25 GB must not be launched unchanged. First measure
runtime and storage on known pilot inputs, without new scientific optimization.
Use existing streaming/replay machinery; preserve all observed neural outputs,
scores, coefficients, scene parameters, hashes and failures. Retain full images
and full hidden-state checkpoints for a predeclared replay/numerical subset;
otherwise preserve deterministic regeneration recipes and incremental image/
drive hashes rather than silently lossy movies. Document this retention policy.
Check projected capacity before generating the final set. Do not delete old
evidence or unrelated V9 work. If capacity is insufficient, record the concrete
requirement and settle storage before rendering; do not reduce the final sample
after inspecting its outcomes. Do not promise wall-clock duration before pilot
measurement. Physical camera/hardware optimization stays outside this scope.

After the final held-out results, stop. No gain, filter, connection, feature
family, cutoff or scene-exclusion adjustment to rescue the result. Correct
software bugs in separately versioned records; scientific changes require a
new project version, not another round hidden inside this milestone.

The final package contains:

1. A versioned image-to-decision CLI and label-free replay example, with separate
   raw neural, neural-decoder, image-reference and hybrid outputs.
2. Frozen models/decoders, source and seed manifests, lesion masks and exact
   environment/software versions.
3. Complete quantitative primary/secondary results, uncertainty, all failures
   and numerical-reproduction evidence.
4. Independent physiological comparison **or** a specific source-gap status.
5. One integrated technical report, one-page professor summary and undergraduate
   explanation of what we wanted, what we did, what worked and why it matters.
6. Dated project progress, its pre-seal snapshot, immutable artifact index and
   separate post-exit integrity verification.

The report must finish with three separate statements: **research package
complete/incomplete; neural capability passed/failed/numerically unresolved;
physiological evidence supported/limited/not established.** A working engineering
fallback may be delivered even if the neural capability fails, with that
distinction visible. Closed-loop robotic control is a subsequent milestone.

## Undergraduate explanation

We already have a tool that can detect turns from simulated pictures, and a
brain model with an improved inhibitory pathway. Now we need one final fair
comparison. We will show both systems new virtual rooms, check missed turns and
false alarms, and remove bIPS in model copies to see what changes. Separately,
we will compare with real neuron measurements if the available data support it.
Then we stop and deliver one clear result. We can finish the research package
honestly even if the brain model still needs work; calling the detector solved
requires it to pass the tests.

[Machine-readable plan](../configs/final_openloop_milestone_plan_v1.json).
