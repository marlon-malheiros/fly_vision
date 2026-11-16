# Technical handoff: neural detection of small yaw during simulated fly walking

**Date:** 1 November 2026. **Purpose:** an independent technical review, including
Gemini, before committing to further expensive experiments. This document
consolidates existing evidence; it does not report a new simulation or biological
experiment. The latest completed scientific source/report checkpoint is `3e4efc9`;
its post-seal progress checkpoint is `667c7b2`.

**Project root:** `<WORKSPACE>`.
All paths below are relative to this root unless stated otherwise. Older reports
are intentionally preserved: their statements about what was still unexecuted
may have been superseded. Use the newest reports and saved arrays for current status.

## 1. Executive assessment

We want an image-driven neural model to detect small body rotations during forward
walking, with low straight-walking false alarms, and ultimately explain the
HS/H2–bIPS–DNp15 pathway in a way supported by physiology.

| Claim | Current evidence/status |
|---|---|
| Physically prescribed binocular walking movies | Implemented, with analytical geometry and numerical checks; biological optics remain approximated |
| Neural-only detection at +/-5 degrees/s | A bounded secondary result passes behavior and declared numerical checks in 24 held-out simulated rooms |
| Neural-only detection at +/-2 degrees/s across all three walking speeds | Not achieved under the complete current criteria |
| External image-based/hybrid detection at +/-2 degrees/s | Achieved in a separate bounded engineering benchmark; this does not complete the neural-only objective |
| Complete physiological validation | Not achieved; several limited comparisons are available, with mixed outcomes |
| Demonstrated biological bIPS contribution to reliable small-turn detection | Not established |
| Closed-loop control/robot deployment | Not part of these studies |

The latest round tested **16 fitted readers and 44 reader/operating-policy
combinations**. None qualifies, including on the small-turn-only subset of the
gates. Its most informative observation is that three new MaleCNS-derived readers
give the correct raw left/right sign on **32/32 small turns at every speed** in
calibration, yet still confuse some straight-walking activity with turns.

This supports the presence of useful directional information in these observations.
It does **not** establish reliable turn-versus-straight discrimination, prove that
the encoder is the bottleneck, or justify an unlimited search for better decoders.
Training a new walking-specific encoder is an untested hypothesis, not an
evidence-backed solution already selected for execution.

## 2. What “small turn” and “reliable” mean here

### Physical task

Yaw velocity is body-heading angular velocity, not a direct measure of retinal
image drift. Forward walking also produces retinal motion. The task is to
distinguish yaw superimposed on translation from translation alone.

The current focused conditions are:

- Forward speed: **5.5, 11, 16.5 mm/s**.
- Yaw: **0, +/-2, +/-5 degrees/s**, plus stationary controls.
- Walking begins at **0.5 s**; imposed yaw begins at **1.0 s**.
- Primary decision callback: **1.19 s**, approximately 190 ms after yaw onset.
- Straight/stationary alarm monitoring: **[1.0, 3.0) s**, 200 callbacks at 100 Hz.
- The reduced-model secondary endpoints are **1.49 and 1.99 s**: 490/990-ms
  capability tests that cannot pass the original 190-ms objective.

At 2 degrees/s, accumulated body rotation over 190 ms is **0.38 degrees**; at
5 degrees/s it is **0.95 degrees**. This comparison alone cannot establish a
sensory limit from pixel spacing: sampling, continuous luminance changes,
temporal integration and neural processing all matter. The 2-degree/s target and
190-ms deadline are engineering specifications, not experimentally established
thresholds for real flies in this project.

### Detection criteria

At each walking speed, require:

1. At least **80% jointly detected and correctly signed** turns.
2. At least **80% separately in each yaw direction**.
3. At most **10% straight-walking and stationary episodes with any alarm** over
   the full monitoring interval.
4. Retain performance at +/-5 degrees/s as the larger-magnitude control.
5. Meet the separately frozen numerical-refinement criteria.

For a signed scalar score q and common cutoff c, an alarm is |q|>c. A correct
turn detection also requires sign(q)=sign(true yaw). Raw sign accuracy counts
every turn, including those below the alarm threshold. These metrics must not
be substituted for one another.

For 24 rooms, each magnitude has 48 signed turns per speed: the gates require
at least 39/48 overall, 20/24 per sign and at most 2/24 false-alarm episodes.
For the latest 16-room calibration, there are 32 turns and 16 straight episodes
per speed: at least 26/32, 13/16 per sign and at most one false-alarm episode.

The fixed-onset positive endpoint is compared with an entire two-second negative
monitoring interval. This is intentional but stricter than matching single-frame
positive/negative errors. Review whether the specification fits the intended
biological/application question; do not silently weaken it to obtain a pass.

These are finite observed rates, not population guarantees. The same rooms occur
across speeds and signs. Correlated callbacks, speed conditions and reused rooms
must not be counted as independent animals or independent replications. For
example, zero alarms in 24 rooms still has an approximately 13.8% upper 95% Wilson
bound. A correct visual yaw estimate cannot establish whether the turn was intended.

## 3. Simulation and optical geometry

“Walking” here means a prescribed camera/body trajectory through a static virtual
scene, not an articulated leg simulation or a neural controller.

The body translates along its instantaneous heading and follows an exact circular
arc once constant yaw begins. With q=max(t-1,0), omega in radians/s and walking
speed v, the post-yaw displacement is:

```text
heading = omega*q
x = v*max(min(t,1)-0.5,0) + v*sin(omega*q)/omega
y = v*(1-cos(omega*q))/omega
z = 2 mm
```

The zero-yaw limit is implemented separately, and the y expression uses a stable
half-angle form. Source: `src/male_optic_frontend/ongoing_walking_yaw_v1.py`.

The two eye origins rotate with the body. `eye_origin()` uses an inherited
0.3-mm binocular baseline. The procedural scenes contain enclosing boxes,
textured surfaces and optional opaque spheres; ray casting preserves physical
perspective, occlusion and depth. Geometry intersection clearance is checked.
The environment family is restricted; new rooms are new instances, not evidence
of robustness to natural scenes or arbitrary environment families.

Important optical distinctions:

- The original functional model samples a **173x173, 1-degree retinal chart**
  spanning +/-86 degrees per eye. The fine raster is a computational sampling
  choice, not a literal reconstruction of every photoreceptor's optics.
- Inherited eye-chart references are -80/+80 degrees with a left-eye horizontal
  reflection. Anatomical chart construction includes imposed calibration
  conventions and is not an independently measured specimen-wide visual map.
- The full published network uses its own 721-site hexagonal lattice and
  approximate 180/31-degree coordinate pitch. Spherical and perspective camera
  hypotheses were both executed; they generate different retinal images.
- The reduced Ammer-derived model uses a 30x30 spherical chart at 6-degree
  centers, with 5x5 subray aperture integration. This is a declared transfer
  assumption, not the same image input as either earlier pipeline.

The rigid eyes/body lack natural head compensation, pitch/roll, neural/photonic
noise and locomotor-state modulation. Those omissions constrain interpretation.

Main geometry code:

```text
src/male_optic_frontend/virtual_walking_v1.py
src/male_optic_frontend/continuous_yaw_worlds_v1.py
src/male_optic_frontend/visual_coordinates.py
scripts/neural_model_perspective_repair_v1.py
```

## 4. Model families: these must remain distinct

### A. Functional motion frontend plus selected MaleCNS graph

This is the main anatomical downstream project, with a functional visual surrogate
providing imposed T4/T5 direction channels. It is not a fully reconstructed retina
through T4/T5 physiological model.

The frontend uses local contrast, delayed correlation/opponency, rectification
and pooling. Its inherited delay is **30 ms**, neighbor offset is **1 raster
step** and pooling radius is **3 steps** on the primary 1-degree grid. Eight
channels route to T4a/b/c/d and T5a/b/c/d targets. Direction routing is imposed;
successful motion responses do not validate the upstream biological mechanism.

The current LPi-expanded graph contains **13,624 modeled cells**:

| Role | Count |
|---|---:|
| T4/T5 | 13,579 |
| HS | 8 |
| H2 | 2 |
| bIPS | 2 |
| DNp15 | 2 |
| uLPTCrn candidates | 17 |
| H2rn homology candidates | 8 |
| Selected LPi12/LPi21 cells | 6 |

The 45 non-T4/T5 cells are available individually to external learned readers.
Candidate identity/provenance and chemical connectivity are not interchangeable
with measured physiological parameters or experimentally confirmed homologies.

The inherited intact chemical dynamics are:

```text
tau * dx/dt = -x + chemical_gain * W*tanh(x) + drive_gain*D(t)
tau = 0.02 s
chemical_gain = 0.873579331825114
drive_gain = 0.21936608020509474
```

W is the inherited normalized signed chemical matrix, with postsynaptic rows and
presynaptic columns. State/rate units are model units, not calibrated membrane
voltage or spikes/s. The primary solver is 1-ms RK4 with 10-ms input/observation
clocks and the inherited last-1-ms forcing ramp. Half-step controls must preserve
that ramp in physical time; otherwise they change forcing as well as integration.
The implementation has a checked tanh approximation for small states. There are
**zero electrical edges**. A stored gap gain of 1 does not create missing gap junctions.

LPi feedback is already present:

| Directed connection class | Included graph edges |
|---|---:|
| LPi -> T4/T5 | 7,493 |
| T4/T5 -> LPi | 14,799 |
| LPi -> HS | 15 |
| LPi -> H2 | 6 |
| LPi -> LPi | 9 |

These are edge counts, not individual synapse counts. The selected horizontal
MaleCNS LPi12/21 cells have inhibitory GABA predictions under the inherited sign
rule. They must not be equated automatically with the vertical glutamatergic
LPi3-4/4-3 circuit or similarly numbered types in another connectome.

Read:

```text
results/fixed_neighbor_motion_v1/config.json
results/horizontal_opponency_v1/graphs/lpi/graph.json
results/neural_model_options_r2/analysis/existing_lpi_feedback_audit.json
src/male_optic_frontend/streaming_v1.py
src/male_optic_frontend/neural_population_readout_v1.py
src/male_optic_frontend/final_openloop_core_v1.cpp
```

### B. Full published FlyVis visual model

The native FlyVis1.2.0 reference has **45,669 neurons, 1,513,231 chemical edges,
64 cell types and 734 trained neural parameters**. Its pretrained motion decoder
uses all **34 actual output populations** in the original order. The earlier
eight-type T4/T5 adapter did not run that complete decoder; the later full-network
study did. Adding zeros for the other populations is not an equivalent reproduction.

This model does **not** contain the named HS/H2/bIPS/DNp15 pathway. Both eyes are
mirrored copies of the published right-eye model, an explicit computational
assumption rather than measured bilateral anatomy.

Checkpoint:

```text
data/derived/flyvis_r3/results/flow/0000/000/best_chkpt
SHA-256 d8a57a022aa18ca338599be713af9db29b89cde4b00098ffe42b78f0d583e46a
```

The native decoder's training units are not directly degrees/s. Fixed field
readers used a two-by-two observation conversion fitted to eight +/-60-degree/s
canonical means; +/-2 controls were excluded. Native Euler integration, sampling
clock conventions and post-update outputs require their own checks.

Read `docs/NEURAL_MODEL_OPTIONS_REPORT_V1.md`,
`docs/PUBLISHED_POPULATION_YAW_REPORT_V1.md` and
`src/male_optic_frontend/published_flow_probe_v1.py`.

### C. Released reduced Ammer2023 opponent model

The latest round actually executes the Figure7a model code, rather than merely
recommending it. It uses the source three-input motion detector, ON/OFF pathways,
local/recurrent LPi inhibition and conductance output. Its source system is
vertical-motion T4/T5–LPi–VS circuitry. Our horizontal application is exploratory;
its states are not reconstructed MaleCNS HS/H2/bIPS/DNp15 cells.

Fixed source values are low/high-pass time constants **50/250 ms**, detector DC
**0.02**, LPi-to-T4/T5 gain **0.5**, other source link gains **1**, all neural
time constants **20 ms**, and output excitatory/inhibitory driving potentials
**+40/-20 mV relative to rest**. The author's `rect(x,threshold)` floors at the
threshold; it does not subtract the threshold. The implementation follows the
released code and checks literal author functions.

The primary transfer uses 5-ms steps and 2.5-s first-image adaptation. Local
30x28 drives pool into 6x6 patches, preserving the source's narrower final edge
patch. Four recurrent populations plus two global conductance outputs per eye
produce **292 recorded values**. A causal level/change representation gives
**584 features**. Output baseline subtraction uses only stationary adaptation.

The paired feedback block removes LPi-to-T4/T5 and reciprocal LPi links while
retaining feedforward inhibition. Each copy receives the same movie. Because
separate readers are fitted to each copy, differences between fitted decoder
scores are not an isolated causal effect of feedback alone.

Read:

```text
data/raw/neural_completion_options_v1/ammer_model/source_manifest.json
data/raw/neural_completion_options_v1/ammer_model/Modelling_Figure7a_Tuning_curves.ipynb
src/male_optic_frontend/small_turn_round_v1.py
```

## 5. What has worked computationally

### Bounded neural-only result at 5 degrees/s

One predefined secondary external linear reader of the 45 simulated downstream
cells uses the functional frontend and frozen LPi-expanded MaleCNS circuit.
The reader and a **2.337116267814088** negative-control cutoff were frozen before
the shared 24-room test images.

| Forward speed | Correct signed +/-5 turns | Straight alarms | Correct signed +/-2 turns |
|---:|---:|---:|---:|
| 5.5 mm/s | 48/48 | 0/24 | 14/48 |
| 11 mm/s | 48/48 | 0/24 | 8/48 |
| 16.5 mm/s | 47/48 | 0/24 | 2/48 |

Stationary alarms are 0/24. The secondary 5-degree/s result passes all **135
declared numerical comparisons**, including a separately frozen follow-up after
the 5-degree behavior was inspected. It is a bounded task-trained observer, not
a newly identified biological neuron. No intermediate yaw rate establishes an
exact continuous detection threshold. The study's original all-magnitude target
and primary readout remain failed.

Sources: `docs/NEURAL_POPULATION_CUTOFF_REPORT_R2.md`,
`docs/NEURAL_POPULATION_FIVE_DEGREE_NUMERICS_ADDENDUM_V1.md`.

### Separate image-based/hybrid 2-degree/s result

The later dense image/neural hybrid was frozen before 60 new rooms, 960 episodes.
It uses causal image motion at finer 0.5-degree sampling and geometric assumptions.
At the 190-ms endpoint, +/-2 correct counts are **120/120, 120/120, 115/120**;
straight alarms are **0/60 at every speed**, stationary 0/60. All 81 selected
numerical comparisons pass, maximum score difference **0.1336**, below 0.2.

Image-only also obtains 120/120 at every speed with zero observed straight alarms;
adding the neural branch has no demonstrated reliability advantage in that study.
This shows feasibility for that image-based computational system and assumptions.
It does not prove that every neural representation retains the same information,
that it is a physiological computation, or that different sampling is a fair
matched-input comparison. Earlier matched original-resolution image controls
also provide useful evidence; their exact time support/future allowance differs.

Read `docs/DENSE_IMAGE_HYBRID_REPORT_R3.md` and
`docs/SEQUENTIAL_SMALL_TURN_REPAIRS_REPORT_V1.md` before proposing the already
implemented hybrid as a new neural-only solution.

## 6. Previous full-published-network round

The immediately preceding investigation ran 384 declared conditions: 14 canonical,
64 two-camera walking-development episodes, 18 numerical refinements and 288
training/calibration episodes. Some additional observer/replay checks also ran.

- Canonical +/-2-degree/s image motion produces correctly signed native decoded
  responses in both declared textures. This is a functional control, not small-yaw
  walking reliability or a physiological threshold measurement.
- Three fixed field readers fail in both spherical and perspective interfaces.
  Cutoffs eliminating observed straight alarms remove all +/-2 detections in
  their two-room development sample.
- A 1,632-feature spatial-population MLP and 96-feature decoder-field linear reader
  use 12 training/6 calibration rooms. The MLP attains training MSE **0.001214**,
  yet at its conservative cutoff both original readers detect **0/12 small turns
  at every speed**.
- Separately frozen reflection-consistent cross entropy and antisymmetric
  unit-direction regression also fail; the former gives **0/12, 0/12, 1/12**.
- Native decoder arithmetic agrees within approximately 6.77e-7; independent
  neuron steps within 2.92e-7, both within frozen 2e-5 limits. Some walking-reader
  numerical refinements fail. Arithmetic agreement is not a scientific pass.
- The reserved fresh test rooms are not rendered because calibration fails.

These results must be considered before recommending the same pretrained decoder,
camera correction, symmetry constraint or generic MLP readout again. They do not
exclude every neural reader or demonstrate that encoder retraining is necessary.

## 7. Latest round: training, policies and all major results

### Features and fitting

Existing MaleCNS observations use 24 p training rooms and 16 w calibration rooms,
already inspected in earlier studies. Spatial T4/T5 activity is pooled into
6x4 bins per eye/subtype: **384 levels**, or **768 level/change features**.
The 45 individual downstream changes are also available. The native network uses
12/6 rooms and its own 4x3 bins, **1,632 features**.

For a 100-Hz neural vector a[t]:

```text
level[t]  = mean(a[t-9 : t+1])
change[t] = level[t] - mean(a[t-29 : t-19])
```

Only zero and +/-2 training examples enter the new fits. +/-5 is evaluation-only.
Negatives contribute every monitored callback; turns contribute their specified
endpoint. The three sign classes receive equal total weight, and episodes have
equal weight within class. Latest MaleCNS/reduced fits have **19,344 samples**;
the native fit has **9,672**. These are correlated fitting rows, not independent
experimental observations. Normalization uses training-only moments, SD floor 1e-12.

The four existing-model alternatives are:

1. 45 downstream changes -> three-class linear softmax.
2. Rectified T4/T5 ON/OFF opponent ratios plus downstream changes -> linear softmax,
   **237 features**. Each axis ratio is (positive-negative)/(positive+negative+floor),
   with floor 0.1 times the training median positive local energy. History is causal.
3. 768 spatial MaleCNS features -> nuisance-penalized ridge.
4. 1,632 full-published-population features -> nuisance-penalized ridge.

Softmax uses float64 Adam, 600 fixed steps, learning rate .003 and weight decay
.001. Its score is P(+)-P(-); this output is not established as a calibrated
probability under distribution shift. Nuisance ridge minimizes class/episode-weighted
MSE to sign(yaw), plus .01 standardized slope penalty and **10 times additional
weighted squared zero-yaw predictions**. The intercept is not ridge-penalized.

Reduced-model intact/blocked copies each receive nuisance and softmax readers at
190/490/990 ms, producing 12 additional fits. Its 640 walking episodes contain
all 16 conditions in the same 24/16 training/calibration rooms.

### Negative-only cutoffs and temporal follow-up

Before calibration score files existed, two operating policies were frozen:

- Conservative: max(.5, maximum absolute negative episode peak).
- Budgeted: for each stationary/speed group of N negatives, sort peaks descending
  and take index floor(.1*N), zero based; choose the largest group value and .5
  as one global cutoff. At N=16 this permits one observed alarm; N=6 permits none.

Neither policy uses positive trials to select a cutoff or true speed at inference.
The .5 floor is inactive for the reported latest cutoffs. Budgeted thresholds are
the lowest common ones satisfying the observed group budgets for these scores.
Threshold certificates are restricted to this scalar-policy family and sample.

After inspecting the four existing readers' failures, a separately frozen final
follow-up applies two rules to the three MaleCNS score streams without refitting:
100-ms mean minus its 200-ms-lagged mean, and five same-sign consecutive callbacks
retaining the minimum absolute score. Those six scores under two policies add
12 combinations. Total: **16 fitted models, 32 base policies, 12 temporal policies**.
The research program is adaptive development, not one original preregistration.

### Primary-endpoint results

Budgeted policy, except where explicitly stated. Counts are joint correct detection.

| Reader | +/-2: slow / medium / fast | Straight alarms |
|---|---:|---:|
| Downstream softmax | 6 / 9 / 6 of 32 | 0 / 0 / 1 of 16 |
| Opponent-ratio softmax | 32 / 17 / 9 of 32 | 0 / 0 / 1 of 16 |
| Spatial MaleCNS nuisance ridge | 20 / 15 / 14 of 32 | 0 / 0 / 1 of 16 |
| Native-population nuisance ridge | 0 / 0 / 0 of 12 | 0 / 0 / 0 of 6 |
| Reduced intact nuisance | 0 / 0 / 0 of 32 | 0 / 0 / 1 of 16 |
| Reduced intact softmax | 0 / 0 / 0 of 32 | 0 / 0 / 1 of 16 |
| Reduced feedback-blocked nuisance | 1 / 0 / 1 of 32 | 0 / 0 / 1 of 16 |
| Reduced feedback-blocked softmax | 1 / 1 / 1 of 32 | 0 / 1 / 1 of 16 |

The three MaleCNS-derived base readers have **32/32 raw-sign accuracy at each
speed**. Spatial nuisance ridge has the highest worst-speed rate, only 43.75%.
The ratio reader is strongest at slow speed, but falls to 28.125% at fast speed.
Its conservative cutoff gives 32/16/9 detections; the budgeted policy gives 32/17/9.
The shared cutoff is approximately .989742; nuisance ridge uses .942384.

All 12 temporal policies fail. No reduced reader qualifies at either later
endpoint; budgeted detections there range from zero to two of 32 per speed.
This does not demonstrate that every possible longer integration scheme fails.

The latest 24 reserved `st00`–`st23` rooms remain **unrendered** under the go/no-go
rule. These failures concern known-room calibration, not a new-room test result.
Do not use reserved test rooms for development or call earlier repeatedly inspected
recordings/rooms newly blind because a new script was run.

### Numerical and independent evidence

- Literal author filters: maximum discrepancy **9.06e-16**; intact and blocked
  recurrence checks: **exact equality**.
- Causal and pre-yaw image-prefix checks: bitwise equality.
- Fresh full walking replay through literal source functions, every patch, both
  copies: image hash matches; all three stored feature vectors agree exactly
  after declared float32 storage.
- **108 numerical runs**: three rooms x three speeds x yaw0/+/-2 x four profiles.
  Profiles are primary, 9x9 aperture, 2.5-ms image/neural step and finer neural
  integration under identical visual holds.
- Per reduced reader: 81 actual refinement comparisons, evaluated under two
  policies, giving 162 rows. Three feedback-blocked nuisance readers pass all
  rows, maximum score errors **.17123, .18592, .14512**, below .2. They still fail
  behavior. All other reduced readers fail at least one numerical gate; largest
  discrepancy **1.21553**. No tolerance was waived.
- Independent original/temporal predictions: **199,752 / 77,952**, maximum errors
  **1.09e-14 / 9.33e-15**. All **264** policy summaries and **1,944** numerical-policy
  rows are independently checked. **640** reduced artifact receipts and **976**
  frozen prior inputs are rehashed. Nine focused tests pass.

There are zero scale-floor features in the reduced fits, so constant-feature
extrapolation is unsupported as their failure explanation. Earlier native checks
also ruled out that proposed explanation in their specific data. Do not generalize
either audit to every possible implementation without examining its arrays.

The latest study seals **1,663 files / 126,246,589 bytes**; this is an artifact
count, not an experiment count. Its index SHA-256 is
`d14696c25dfbbf1ef55933ec5753fe0a0a64e90c39a3253717e14664ba6ea376`.

## 8. Biological evidence: partial, sometimes conflicting

### Erginkaya-related bIPS/DNp15 comparisons

The project has inspected public recordings and connectomic identities, with
reporter/compartment mapping checks and several computational dissections. Exact
modified G3 stimulus arrays/generator remain unavailable in the audited materials;
image-to-recording comparisons use explicit approximations. This limits exact
quantitative reproduction; it does not make every narrower comparison impossible.

Adding the selected horizontal LPi cells corrects a model null-yaw response sign
in the audited dot assay, but physiological metrics are mixed. Example existing
full-waveform summaries:

| Existing cohort/metric | Expanded pre-LPi | LPi intact |
|---|---:|---:|
| DNp15 GC6f WT: mean per-fly skill | -.25730 | +.09978 |
| DNp15: median per-fly skill | +.34686 | +.37853 |
| DNp15: pooled skill | +.33117 | +.27114 |
| bIPS sytGC7f axon: mean per-fly skill | +.45738 | +.32544 |

Skill uses a zero-response comparison; per-fly normalization can be unstable for
low-response animals. Mean, median, pooled error and individual traces must be
kept together. Excluding a quiet fly because its normalized skill is unfavorable
would not be a justified repair. These recordings have already been inspected;
they cannot be relabeled fresh independent validation.

The LPi anatomical addition and its sign improvement do not establish that missing
LPi is the unique cause of current small-turn failures. Current LPi feedback exists,
and the standalone full-published visual route fails walking transfer without the
named downstream MaleCNS pathway.

### HS comparison

A published voltage source-data assay gives ND/PD ratio **.19333**, with descriptive
unpaired recording-row interval **[-.17017, .90160]**. Pairing/animal IDs are not
verified. Original, expanded and LPi model predictions all lie within that broad
interval. This is weak compatibility with one scalar constraint, not complete
validation or evidence selecting the LPi model. The original prediction is closer
to the mean point than the LPi prediction in this assay.

### H2 and cellular frontends

The audited H2 model mean preferred-direction error is **16.72 degrees**, versus
**13.76 degrees** for the body-horizontal reference. This does not establish an
advantage over that reference. Published T4/T5 physiological implementations and
local anatomy have also been reproduced/audited; numerically corrected versions
still show incomplete mean-response transfer in the image assays.

Important unresolved constraints include:

- Local CT1/input spatial assignments: aggregate body-to-body synapse counts do
  not locate the contacts of a broad multicolumnar neuron.
- Independently measured retinal/anatomical registration and receptive-field maps.
- Physiological voltage/rate-to-MaleCNS drive conversion and measurement models.
- Receptor-specific effective strengths, heterogeneous dynamics and electrical coupling.
- Reliable identities/functions for candidate recurrent neuron groups.
- Eligible independent recording tests after extensive development-data reuse.

Do not invent missing anatomical contacts, gap conductances or biological gains
to make a classifier pass. A labeled modeling assumption can support an exploratory
study, but cannot be reported as measured physiology.

Biological source reports:

```text
docs/HORIZONTAL_OPPONENCY_REPORT_V1.md
docs/BIOLOGICAL_FAMILY_DISSECTION_REPORT_V1.md
docs/OPPONENCY_GAIN_CALIBRATION_REPORT_V1.md
docs/HS_VOLTAGE_BENCHMARK_REPORT_V1.md
docs/H2_FROZEN_MODEL_BENCHMARK_REPORT_V2.md
docs/PHYSIOLOGY_INTEGRATION_SOURCE_GATE_REPORT_V1.md
docs/PHYSIOLOGICAL_IMAGE_CLAMP_REPAIR_REPORT_V1.md
results/neural_model_options_r2/analysis/biological_constraints.json
```

## 9. What is established, inferred and unknown

**Established within the saved computational studies:** bounded 5-degree/s
neural-only performance; separate image/hybrid 2-degree/s performance; failure of
the latest 44 combinations in calibration; high raw sign accuracy for three latest
MaleCNS readers; scalar-score overlap with negative episode peaks; failure persisting
in three numerically qualified reduced readers; mixed physiological comparisons.

**Reasonable hypotheses:** coarse pooling, encoding dynamics, background-sensitive
features, training coverage, confidence calibration, sensory-state assumptions or
spatial integration may contribute. More diverse walking-domain training could
help. None is established as the unique cause or a guaranteed repair.

**Not established:** absence of yaw information from full neural activity;
necessity of encoder retraining; sufficiency of an RNN/CNN/transformer; biological
impossibility at 2 degrees/s; biological causality of model lesion effects; complete
physiological validation; biological benefit of bIPS; physical deployment reliability.

The latest straight/turn confidence overlap proves a restricted cutoff limitation
for each tested score, not a limit on every decoder of the original observations.
Likewise, correct sign on actual turns does not prove that the same observations
can distinguish zero from nonzero yaw robustly over all monitored times.

## 10. Approaches already tried: avoid proposing them as untouched fixes

| Approach | Where to verify | Current limitation |
|---|---|---|
| Functional input contrast normalization | `docs/SEQUENTIAL_SMALL_TURN_REPAIRS_REPORT_V1.md` | Improves some controls; no complete small-turn neural success |
| Local image-derived velocity injected into direction channels | Same report, matched motion-encoding control | Engineered input; downstream remains unreliable; some spatial readers fail fast false-alarm gates |
| Anatomical horizontal LPi addition / functional opponency | `docs/HORIZONTAL_OPPONENCY_REPORT_V1.md` | Mixed physiology; not a new missing edge in current graph |
| Published T4/T5 physiological ports, image-clamp corrections | Physiological source/transfer reports above | Source correctness does not complete spatial/physiological integration |
| Additional gain/electrical hypotheses | `docs/POKUSAEVA_GAP_REPRODUCTION_REPORT_V1.md`, earlier repair reports | Prior conditional failures; no justified arbitrary gap conductance |
| Richer MaleCNS population linear/MLP readers | `docs/NEURAL_POPULATION_READOUT_REPORT_V1.md` | Full 2-degree target fails; bounded secondary 5-degree success |
| Full pretrained native FlyVis decoder | `docs/NEURAL_MODEL_OPTIONS_REPORT_V1.md` | Canonical motion works; walking transfer fails |
| Spherical/perspective interface comparison | Same report | Both tested; different optical inputs, not identical-input ablations |
| Native spatial MLP, task-direction loss, reflection symmetry | `docs/PUBLISHED_POPULATION_YAW_REPORT_V1.md` | Training fit does not generalize to calibration |
| Small-turn-specific fitting, neural opponent ratios, hard-negative penalty | `docs/SMALL_TURN_ROUND_REPORT_V1.md` | Raw direction improves; reliable detection still fails |
| Released reduced opponent circuit / source feedback block | Same report | Horizontal transfer is assumed; all task candidates fail |
| Longer 490/990-ms endpoints, final score-change/persistence rules | Same report | The tested options fail; not a general exclusion of all temporal models |

A genuinely new proposal must identify what changes, what evidence motivates it,
and how its smallest test differs from these completed experiments.

## 11. Priority file map for an independent reviewer

Read in order; a recursive dump of all historical artifacts is unnecessary.

| Priority | Path | Purpose |
|---|---|---|
| 1 | `docs/SMALL_TURN_ROUND_REPORT_V1.md` | Latest complete study, distinctions and failure results |
| 2 | `configs/small_turn_round_v1.json` and `docs/SMALL_TURN_ROUND_PROTOCOL_V1.md` | Actual fixed conditions and primary criteria |
| 3 | `results/small_turn_round_v1/analysis/all_policy_summary.json` | 192 base-policy outcome rows |
| 4 | `results/small_turn_round_v1/analysis/temporal_summary.json` | 72 temporal-policy rows |
| 5 | `results/small_turn_round_v1/existing/calibration_predictions.npz` | Full existing-reader negative/turn score streams |
| 6 | `results/small_turn_round_v1/existing/models.json` | Exact latest readout fits |
| 7 | `src/male_optic_frontend/small_turn_round_v1.py` | Features, source model, losses and inference |
| 8 | `scripts/small_turn_round_v1.py` | Data selection, fitting and scoring implementation |
| 9 | `docs/NEURAL_POPULATION_CUTOFF_REPORT_R2.md` | Actual bounded 5-degree success and 2-degree tradeoff |
| 10 | `docs/NEURAL_MODEL_OPTIONS_REPORT_V1.md` | Full published model already executed |
| 11 | `docs/DENSE_IMAGE_HYBRID_REPORT_R3.md` | Existing successful external engineering reference |
| 12 | Biological reports in section 8 | Scope/measurement/provenance limitations |

Additional high-value numerical artifacts:

```text
results/small_turn_round_v1/analysis/score_overlap.json
results/small_turn_round_v1/analysis/scalar_threshold_certificates.json
results/small_turn_round_v1/analysis/full_curve_review.json
results/small_turn_round_v1/analysis/literal_full_path_replay.json
results/small_turn_round_v1/numerics/summary.json
results/small_turn_round_v1/numerics/comparisons.json
results/small_turn_round_v1/reduced/calibration_predictions.npz
results/small_turn_round_v1/reduced/models.json
results/small_turn_round_v1/analysis/operating_points.json
results/small_turn_round_v1/final_decision.json
results/small_turn_round_v1/post_exit_integrity_v1.json
```

Earlier actual neural observations, useful for information/readout audits:

```text
results/neural_population_readout_v1/observation_map.npz
results/neural_population_readout_v1/known/<scene>_v<speed>_y<signed_yaw>/observations.npz
results/neural_population_readout_v1/design_individual_linear.npz
results/published_population_yaw_r2/train/*.npz
results/published_population_yaw_r2/calibration/*.npz
```

The latest reduced features are in
`results/small_turn_round_v1/reduced/<scene>_v<speed>_y<signed_yaw>.npz`,
with `sample_index`, `intact` and `no_feedback` arrays and JSON receipts. Negatives
contain 200 monitoring rows; positives contain the three declared endpoints.
Those saved positive features cannot support arbitrary new time-history analyses
without reexecution. Some earlier MaleCNS positive traces end at 1.3 s: do not
pretend they contain longer-latency observations.

## 12. Reproducibility and resource limits

Reproduction instructions are in `docs/SMALL_TURN_ROUND_REPRODUCTION_V1.md` and
`docs/NEURAL_MODEL_OPTIONS_REPRODUCTION_V1.md`. The current project simulation
interpreter is Python3.14; the tested Torch/FlyVis bootstrap uses CPython3.11.16
with Torch2.13.0+cu130 executing on CPU and isolated dependencies under /tmp.
An alternate binary stack and physical deployment have not been tested.

```text
scripts/run_neural_completion_runtime_v1.py
results/neural_model_options_r2/analysis/resolved_runtime.json
```

Producers intentionally refuse existing output paths. Running them in the current
workspace can reproduce an expected failure or stop on existing files; use a new
version/workspace for new production. Prefer reading saved arrays for review.

Preserved operational corrections include JSON serialization of NumPy counts,
a reviewer launched before its dependent export existed, and a flat-methods
driver/module basename collision. Exact original sources are preserved by their
full relative paths and pre-outcome hashes in the completed archive. These issues
were corrected without changing the reported scientific thresholds/results.

The filesystem is nearly full. The latest study retained about 126 MB under a
240-MB evidence budget. Earlier numerical evidence/raw sources are retained outside
Git as indexed artifacts; code and live progress are Git-tracked. Disk size and
artifact count do not measure model/API usage. No reliable token or monetary
cost total is supplied here. The user specifically wants to avoid another large,
expensive round without a strong decision rationale.

Project rules are in `AGENTS.md`: append dated progress, preserve sealed results,
archive dated progress before sealing, distinguish reproducibility from biological
validation, and do not invent connectivity or claim unsupported biological success.
Unrelated measured-camera V9 files are pending work and should remain untouched.

## 13. Questions we want the independent reviewer to answer

Please give a critical diagnosis rather than encouragement or a large generic plan.

1. **Is the current failure localized?** Which observations support an encoding,
   spatial-pooling, decoder, confidence, temporal, sampling or specification problem?
   Distinguish demonstrated facts, plausible hypotheses and unknowns.
2. **Is encoder training justified?** Explain why preserved raw directional
   information does or does not justify that expense. What cheaper observation
   would change the decision? Do not infer necessity from failed scalar readers.
3. **Can existing arrays answer the next question?** Consider matched-condition
   signal/noise, temporal false-alarm structure, activity-space separability,
   training/calibration shift and nuisance sensitivity. A paired straight-control
   oracle is permissible as a labeled diagnostic, never as an inference input.
4. **Are the criteria appropriate?** Assess the 0.38-degree accumulated rotation,
   190-ms deadline, whole-episode false-alarm requirement, room sample sizes,
   missing sensory noise and the distinction between engineering and fly thresholds.
   If a different target is warranted, explain it as a new specification rather
   than retroactively declaring the old one passed.
5. **What has biology actually constrained?** Identify the minimum matched
   measurement/observation model needed next. Do not demand perfect biology before
   any useful experiment, or claim full validation from source-code agreement.
6. **Rank at most three distinct alternatives and choose one smallest next test.**
   Give exact data and code inputs, one controlled change, required assumptions,
   unchanged baseline, negative controls, decision criteria, explicit run/time/
   memory budget and a stopping rule. Prefer a read-only audit first. Do not launch
   another broad simulation/training sweep just to discover that it was unnecessary.
7. **If progress is currently blocked, state the precise constraint.** Explain
   what evidence could remove it and whether the limitation is missing data,
   implementation, identifiability, resource budget or task definition. Do not
   claim that real flies or all neural models cannot detect small turns.

If you lack local filesystem access, state that limitation and base your conclusions
on this handoff. Do not claim to have inspected files you cannot open. If you have
access, begin with a read-only audit of the priority list and cite exact evidence.
Do not modify sealed files, fit new biological parameters, consume reserved test
rooms, contact authors or launch expensive training during the initial review.

## 14. Primary literature already used in the project

These identify the existing source models and comparison context; this handoff
does not claim a new literature review or a ready-made biological 2-degree/s solution.

- [Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9),
  the central bIPS/DNp15 experimental comparison.
- [Lappalainen et al. (2024)](https://www.nature.com/articles/s41586-024-07939-3),
  the connectome-constrained/task-optimized visual network.
- [Official FlyVis optic-flow example](https://turagalab.github.io/flyvis/examples/02_flyvision_optic_flow_task/).
- [Ammer et al. (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620086/),
  multilevel motion opponency, and its [released model](https://doi.gin.g-node.org/10.12751/g-node.7v3pe6/).
- [Pokusaeva et al. (2024)](https://www.nature.com/articles/s41467-024-53173-w),
  source of the limited HS voltage comparison.
- [Published T5 physiological model](https://doi.org/10.7554/eLife.50706),
  used in earlier integration audits.

## Plain-language recap

We want a simulated fly brain to notice a tiny turn while walking and eventually
match real neuronal measurements. We have a bounded neural detector for larger
5-degree/s turns and a separate image-based system that detects 2-degree/s turns.
The tested neural-only systems still confuse some straight walks with small turns.
The latest round confirms that correct turn direction can survive even when reliable
turn detection fails. We need an independent, cost-conscious diagnosis of the next
decisive experiment; changing the encoder is one hypothesis, not a proven necessity.
