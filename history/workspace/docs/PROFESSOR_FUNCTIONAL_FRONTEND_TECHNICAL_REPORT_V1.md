# An image-to-neural motion frontend for a frozen MaleCNS circuit

## Technical report and evidence handoff, V1

Prepared **13 October 2026**, America/Belem. Execution records use UTC. This is a retrospective synthesis of completed, versioned studies; it is not a new experiment or a new prospective protocol. The numerical results below come from saved evidence. No new benchmark simulations, parameter searches, recordings, or biological fits were performed to prepare this report. Packaging replays the existing illustrative demo solely to verify portability.

Repository: `male_optic_frontend`. Main completed study: `fixed_neighbor_motion_v1`.

### TLDR

**We have a working, computationally validated image-to-neural frontend.** Physical movies are sampled as local brightness, an explicit circuit computes motion from fixed neighboring positions and temporal delays, and its outputs drive the frozen MaleCNS network. All 13,579 source targets are covered. Four random textures pass every horizontal group criterion, supplemental speeds and cardinal gratings pass, and all ten HS/H2 targets have the expected measurable global preference in every texture: **40/40 comparisons**. Separate numerical implementations reproduce the source and downstream calculations. **This is a functional motion surrogate, not a validated reproduction of real T4/T5 physiology.** Subtype output routing and eye geometry contain declared assumptions, vertical channels retain some horizontal-texture responses, and biological degeneracy has not been established. The professor's original diagnostic was completed earlier with a weak result; the present positive artifact addresses the subsequently authorized, narrower engineering objective.

### Suggested statement to the supervisor

> We implemented and computationally validated a label-free image-to-neural pathway using an explicit fixed-connectivity motion surrogate and an unchanged downstream MaleCNS circuit. It passes a prospectively specified functional benchmark. We are presenting it as a reproducible engineering baseline; anatomical output routing and quantitative physiological prediction remain separate validation questions.

“Label-free” here means the numerical motion computation receives no intended movie velocity, condition label, or target preferred-angle field. It does **not** mean the architecture was learned without prior knowledge: the channel-to-subtype output assignment is explicitly specified.

## 1. Original question, current scope, and completion status

The initial smoke test passed image-derived drive into T4/T5 and obtained downstream HS/H2 responses. However, it chose an image neighbor using each target's prescribed `preferred_direction_deg`, and it lacked a sufficiently documented bilateral coordinate transformation. That established software propagation, not emergent biological direction selectivity.

The professor's follow-up requested:

1. An explicit mirror relationship between world coordinates and the two eye charts, determined from source definitions rather than downstream responses.
2. Nondirectional local image encoding, with no preferred-angle sampling, velocity labels, sign-specific normalization, or fitting to desired responses.
3. An audit of upstream circuitry. If absent, a separate explicit pre-T4/T5 spatiotemporal module (“Route B”) with fixed spatial interactions.
4. The seven seed-42 horizontal/static/unilateral conditions; analysis of every T4/T5 subtype and side and all eight HS/two H2 targets; negative controls; fourteen named artifacts; separate geometry and motion decisions, preserving negative findings.

The full original instructions are preserved in [original_professor_instructions.txt](../results/t5_evidence_audit_v1/original_professor_instructions.txt). The selected MaleCNS network contains T4/T5 and downstream cells but lacks the relevant Mi/Tm presynaptic visual stages. This is a statement about the **selected reduced model**, not the complete fly connectome. A separate motion module is therefore necessary for this integration.

The first complete corrected Route-B diagnostic used a frozen FlyVis upstream model. It produced `VISUAL_GEOMETRY_VALIDATED` **under declared source-chart conventions**, and `DIRECTION_SELECTIVITY_WEAK_OR_INCOMPLETE`. Its required artifacts and negative findings remain intact. Later investigations tested initialization, physiological model ports, image transfer, and restricted parameter compensation. The user subsequently authorized a simpler functional surrogate to obtain a defensible working frontend. The positive result reported here belongs to that new scope.

| Requirement or claim | Current evidence | Status / boundary |
|---|---|---|
| Physical images become numerical neural drive | Complete source and downstream runs, including label replay | Achieved for the specified surrogate |
| Renderer and local sampler receive no target preferred angles | Numeric contracts, source inspection, allowlist removal, analytic tests | Achieved on the executed path |
| Neighbor offsets arise from fixed module wiring | Same eight channels computed at every lattice site before routing | Achieved for the surrogate |
| Independent emergence of biological subtype preferences | Routing maps +H/−H/+V/−V to a/b/c/d in advance | **Not established**; output naming is an assumption |
| Bilateral eye charts and full spatial support | Source-defined mirrored charts; all 13,579 targets have complete interpolation support | Achieved under conventions; specimen optics unmeasured |
| Original seven-condition diagnostic and fourteen artifacts | Earlier postfix bundle and completion audit | Completed earlier with a weak/incomplete motion result |
| Strong horizontal a/b source response in the new benchmark | Every primary seed: 8/8 groups pass | Achieved in normalized model units |
| c/d weak for horizontal translation in a full biological sense | Smaller amplitudes, but 85–87% selective under the project's binary rule | **Not established** |
| Expected HS/H2 direction through the frozen circuit | 40/40 global comparisons and 40/40 ipsilateral contrast signs | Achieved as computational plausibility checks |
| Quantitative T4/T5 or HS/H2 recording agreement | No matched recording comparison for this new surrogate | **Not run** |
| Biologically distinct circuits with equivalent function | No such experiment for the new frontend | **Not established** |
| Publication novelty or acceptance | No external review or acceptance | **Not assessed** |

Thus the narrower engineering task is complete. A claim that every anatomical/mechanistic inference intended by the initial professor instructions has been demonstrated would exceed the evidence. The professor can assess whether the declared surrogate is an acceptable Route-B baseline for the next scientific study.

## 2. Relevant development history and why the approach changed

This chronology describes findings that affect interpretation. Older plans and superseded variants remain in the repository; their existence is not evidence that they succeeded. Tracking was introduced partway through development: early artifact hashes and execution records exist, but Git cannot reconstruct every earlier edit. Source Git tracking began at `e430690a7f263e3243e9ba71ea33ad1c7f98e448`. See [development trail](PROJECT_DEVELOPMENT_AUDIT_TRAIL_V2.md) and [append-only progress report](PROJECT_PROGRESS_REPORT.md).

| Stage | Main result | Implication for the current work |
|---|---|---|
| Direction-coded smoke frontend | Software propagation passed; target preferred-angle sampling constructed selectivity | Archived as diagnostic; excluded from the new call path |
| Frozen FlyVis postfix diagnostic | Complete 13,579-target coverage; only 1/8 horizontal groups met the 75% criterion; STATIC neural drift remained | Correct software/geometry conventions did not ensure the desired source response |
| Initialization investigation | Five seconds of adaptation at each stage yielded 100% STATIC stability; seeds 42/43/44 still gave 1/8, 0/8, 0/8 horizontal groups and 0/10 HS/H2 passes per seed | Startup drift was a real issue, but did not explain all weak selectivity |
| Published physiological model/source audit | T5 author equations checked across 168 protocols; released-archive compatibility discrepancy up to 0.330540 mV remained | Equation fidelity and reproduction of a historical numerical archive are different checks |
| Physiological population prototype | 80/80 local controls passed; full seven-condition run completed; expected downstream signs could occur while the strict individual source criterion remained 0/8 | A positive downstream sign alone is insufficient source validation |
| Texture replication | 624 cases, 12 new textures plus anchor; 0/8 horizontal templates robust, 5/8 after spatial pooling | No evidence of a broadly robust physiological texture frontend |
| Causal image-clamp repair | Future-dependent T4 baseline bug removed: output-prefix discrepancy 0.150695 mV → 0; 662 cases; long trajectories converged; horizontal grating mean criterion still only 16/32 | A real implementation bug was fixed, but that fix did not establish full biological transfer |
| Matched native T5 grating comparison | One published cell/example: amplitude direction 4/4 in model and recordings; model mean 0/4, recordings 3/4 expected plus 1 opposite; scored-window waveform RMSE 4.020545 mV | Weak means already occur under native input, before image or downstream conversion |
| Image-to-native grating transfer | All 64 main responses, 32 pairs preserved; amplitude error ≤0.24%; 280 runs and 19 tests | The pixel sampler can faithfully reproduce the native model on this controlled family |
| Image-to-native moving-bar transfer | All 144 main responses, 72 pairs preserved; peak error ≤0.19%; recorded/model peak and mean signs 9/9; 612 runs and 14 tests | A second positive transfer control argues against rebuilding the renderer from scratch |
| Finite T5 parameter pilot | 80 candidates; 2,210 trajectories including baseline/controls; one material timing alternative preserved all declared features | Bounded mathematical compensation exists; not proof of biological degeneracy |
| Prospective compensation challenge | Same timing alternative passed all 52 new inputs and sampling checks; 312 trajectories | Positive finite input generalization of that compensation, while preserving the weak-mean limitation |
| Active local sensitivity search | 6,552 trajectories; 12/40 new alternatives material; 0 material alternatives preserved every output; 11 changed both E/I ≥10%, none passed | Negative finite search, not global impossibility or uniqueness |
| Evidence audit | 12,480 predecessor entries and original 35-file assignment bundle intact; 16 tests; hard-coded configurable-threshold reuse defect found, frozen results unchanged | Separately checking equations, arithmetic, configuration use, and biology is essential |
| New fixed-neighbor surrogate | 47 source executions, 28 network trials; complete frozen functional gates pass | Provides the requested positive engineering baseline with a narrower claim |

The related detailed reports are included in the handoff package and linked in Appendix D. This history does **not** support the statement “the investigation found no useful cause.” It found several specific software, numerical, initialization, and readout limitations. It also does **not** isolate a single biophysical cause of every texture sign reversal, or prove that the previous physiological architecture cannot be improved.

### 2.1 What the older one-cell physiological evidence actually says

The matched T5 work used the published **cell 7 / iteration 52** example. Its raw eleven-parameter vector was:

```text
[13.878787185331442, 9.061384089454625, 15.62874562463774,
 0.3493954648308555, 16.592236462992943, 0.3325338482041943,
 2.9768208686252273, 0.10339859627994465, 2.85827584930246,
 1.9503301468924572, 1.1000499343945063]
```

These are **author parameter units**, not the new surrogate's constants. The unused first parameter and exact pole permutations are trivial redundancies and were excluded from scientific compensation counts. Four native temporal parameters convert using ×10 ms. The historical model uses spatially weighted excitation/inhibition, four cascade states, and relative membrane voltage

\[
\Delta V=\frac{-65-74g_I}{1+g_E+g_I}+65\quad\text{mV}.
\]

The audited fitting objective uses 24 width-two single-bar traces (3,748 samples). Forty-four archived fitting traces match the full data archive bitwise; only the width-two subset enters that objective. Gratings are held out **relative to that objective**. The author selected this illustrative example before our new scoring; the complete example-selection history is unknown, so it is not an independently selected biological test cell.

For eight native grating traces (four direction pairs), temporal frequencies were 3.125 and 0.78125 Hz, phases 1 and 5, evaluated at the actual fractional-start 2.5-ms recording clocks. Readouts used cycles 2–3 after each trace's [−100,0)-ms baseline subtraction. Mean model DSIs were −0.003690, 0.023469, 0.091497, 0.091518; recorded mean DSIs were −0.110111, 0.219109, 0.181728, 0.224513. The two slow model values are close to the project's 0.1 cutoff. It would be misleading to report only “0/4” without these magnitudes. Amplitude direction succeeded in all four, but full waveforms did not match quantitatively. Nine moving-bar pairs also had correct model/recording peak and mean signs, with stimulus-window waveform RMSE 2.629398 mV.

The positive compensation candidate `i_poles_spread` changes inhibitory decay **156.287456 → 117.215592 ms** and rise **165.922365 → 207.402956 ms**, holding other parameters fixed. On the 52-input challenge, worst peak/amplitude error was 3.5141%, mean error 2.0603%, waveform error 3.4797%, and final conductance error 2.5959%, under declared 5% output margins. Combined with the original 26 inputs, that is a **78-input, finite mathematical compensation example**. It preserves the original model's limitations. The active Jacobian had numerical rank 10/10 under a machine-epsilon rule; its weakest direction was mostly timing under the chosen coordinate scaling. This is not a rigorous proof of biological identifiability or of absent global compensation.

These earlier successes and failures belong to a different model, different units, and different assays. They are not physiological validation of the new surrogate and should not be merged into its success counts.

### 2.2 Available anatomy and the missing spatial constraint

Absence of upstream visual cells in the selected 13,593-node graph does not mean no upstream anatomical data are available. A separate larger structural export was audited: **65,799 neurons, 1,967,771 edges, 1,771 columns**, with 73,282 target/input-type offset records. It includes 13,580 T4/T5 cells; one T5a lacks a column assignment and was not given an invented position in the retained 13,579-target experiment. Relevant same-eye mapped inputs cover 6,861/6,861 T4 for Mi1, 6,855 for Tm3, 6,818 for Mi4, and 6,831 for Mi9; T5 coverage is 6,718/6,719 for Tm1/Tm2, 6,702 for Tm4, and 6,716 for Tm9.

The filtered export omits CT1, but the original annotation/edge table contains two CT1 cells, IDs 10009 and 10157. A separate read-only stream over 151,856,684 raw edge rows recovered 13,537 CT1→T4/T5 contacts, totaling 230,681 synapses. Those weights establish contacts, **not local synapse/branch positions or inhibitory temporal dynamics**. A global CT1 cell spans many columns; assigning its soma a single coordinate cannot identify each local input. This is one concrete reason a strictly anatomical physiological replacement remains incomplete. The new surrogate does not solve that missing constraint. See the preserved [anatomy/source audit](PHYSIOLOGY_INTEGRATION_SOURCE_GATE_REPORT_V1.md).

## 3. Current implementation: exact data flow and interfaces

```text
Physical world-coordinate movie
    ↓ AngularMovie(time_s, frames, azimuth_deg, elevation_deg)
Two source-defined eye coordinate transforms
    ↓ identical bilinear sampling on a fixed grid
Local luminance L(t, eye, elevation, horizontal), in [0,1]
    ↓ nondirectional ON/OFF encoding
Fixed delay states and symmetric neighboring product branches
    ↓ signed axis opponency, 7×7 signed spatial averaging
Eight rectified motion channels at every site
    ↓ bilinear readout of ALL channels at every target position
Declared fixed channel-to-T4/T5-like output routing
    ↓ common unit-scale body-ID-matched drive
Frozen MaleCNS graph and original 1-ms RK4 solver
    ↓ source-cell network rates and all eight HS/two H2 trajectories
```

The computational grid sites are virtual sensors/circuit locations, **not newly reconstructed biological neurons**. T4/T5-like source outputs are features of this surrogate. The downstream T4/T5 rate is a different quantity: it also reflects frozen network dynamics. The report and arrays distinguish these stages.

### 3.1 Contracts and location of permitted metadata

The physical renderer legitimately uses speed, direction, seed, and moving-field metadata to construct pixels. These variables terminate at the movie object. `AngularMovie` owns read-only arrays and has no experiment-condition, intended-velocity, or target-tuning field.

`local_luminance(movie, world_xy)` uses only movie pixels/axes and coordinates. The reusable motion interface is:

```python
simulate_retina(
    luminance, time_s, grid, locations_eye_deg,
    config=None, *, probe_locations=None,
)
```

Its arguments do not include body ID, subtype, preferred direction, condition, expected output, or velocity. It returns `time_s`, `all_channels`, `pooled_channels`, optional `probes`, `initial_delay_state`, and `final_delay_state`.

The wrapper separately reads target `body_id`, `layer`, `azimuth_deg`, and `elevation_deg`. Layer supplies side and **output routing**, after all channels are computed. All other metadata is ignored. Removing the preferred-direction fields gives an identical target map in the recorded preflight. This tests metadata independence; it does not remove the anatomical assumptions encoded in the fixed routing table.

Relevant source:

- [fixed_neighbor_motion.py](../src/male_optic_frontend/fixed_neighbor_motion.py): complete motion core, reproduced verbatim in Appendix A.
- [fixed_motion_stimuli.py](../src/male_optic_frontend/fixed_motion_stimuli.py): physical test movie constructors.
- [retinal_input.py](../src/male_optic_frontend/retinal_input.py), [visual_coordinates.py](../src/male_optic_frontend/visual_coordinates.py): nondirectional sampler and transforms.
- [run_fixed_neighbor_motion_v1.py](../scripts/run_fixed_neighbor_motion_v1.py): preflight/freeze, movie execution, routing, scoring, downstream bridge.
- [review_fixed_neighbor_motion_v1.py](../scripts/review_fixed_neighbor_motion_v1.py): separately coded reference equations/readouts.
- [test_fixed_neighbor_motion.py](../tests/test_fixed_neighbor_motion.py): analytic/causal/support fixtures.

The original preferred-angle correlator is retained historically and is not invoked by this path. The new module is an explicit algorithmic substitute; its agreement with a declared directional architecture must not be presented as discovery of that architecture from anatomy.

### 3.2 Saved numerical schemas

NPZ records are read with `allow_pickle=False`; identities use string arrays. For a coarse source execution, `T=401`, `N=13,579`. Fine-clock executions have `T=801`.

| File / array | Shape | Stored type / interpretation |
|---|---|---|
| Source movie `frames` | T×180×360 | float32 physical luminance |
| Movie `time_s`, angular axes | T, 360, 180 | Clock and world pixel-center coordinates |
| Source `all_channels` | T×8×N | float32; every feature at every target position, before routing |
| Source `routed_activity` | T×N | float32; the specified feature selected for each output slot |
| Source `retinal_L`, `retinal_R` | Each T×173×173 | float32 local nondirectional luminance |
| Source `delay_final_L/R` | Each 2×173×173 | float64; ON/OFF final low-pass states |
| Source `pooled_channels` | T×2×8 | float64; means over complete-support grid sites, left/right |
| Source `probes` | T×2×8×5 | float32; locations (0,0), (−20,0), (20,0), (0,−20), (0,20) degrees in each eye |
| Source identity fields | N | Body IDs, cell types, sides, channel indices; movie digest also saved |
| Network `source_drive` | 201×13,579 | float32 saved 10-ms input, with exact source ID order |
| Network `state`, `rate` | 201×13,593 | float32 all-node records at 10 ms |
| Network `hs_h2_state/rate` | 201×10 | Separate float64 wide-field records |
| Network `initial_state`, `final_state` | 13,593 each | Full-precision state endpoints |

The module computes fields on all sensor sites at each step but the study stores complete channel traces at target positions, pooled/probe traces, retinal inputs, and final filter states; it does not save every intermediate sensor field at every time. Those fields can be regenerated from the retained retinal input and equations. Raw array schemas, identities, clocks, and complete file hashes are available through the source/downstream registries.

## 4. Coordinate conventions and spatial support

Let `wrap` map angular differences to [−180°,180°). World positive azimuth means increasing raster azimuth; world positive elevation means upward. Define:

\[
h_L=-\operatorname{wrap}(a+80^\circ),\qquad
h_R=\operatorname{wrap}(a-80^\circ),\qquad e_L=e_R=e.
\]

Positive eye-horizontal is declared anterior-to-posterior/front-to-back (FTB). Thus global +azimuth is FTB for the right chart and back-to-front (BTF) for the left; global −azimuth reverses those assignments. The inverse transforms return physical world sampling positions. Image rows are stored from +89.5° to −89.5° elevation, while the local grid elevation increases; axes, rather than array-row assumptions, determine sampling.

| Quantity | Left eye | Right eye |
|---|---|---|
| World reference | (−80°,0°) | (+80°,0°) |
| World-to-eye linear basis | diag(−1,+1) | diag(+1,+1) |
| Global sign for FTB | − | + |
| Global sign for BTF | + | − |
| Retained target count | 6,786 | 6,793 |
| Grid | 173×173; both axes −86°…+86°, 1° pitch | Same |
| Complete-support grid sites | 27,225 = 165² | Same |

A pair spans ±1 site, and pooling adds radius 3; therefore the outer four rows/columns are invalid for readout. Every target's **four bilinear vertices** must lie in the valid mask. All 13,579 target positions satisfy that rule. Weight sums differ from one by at most 1.1102230246251565e−16. No target is dropped, extrapolated, or filled with zero because of absent support. The entire new sensor grid lies within the actual movie pixel-center bounds, azimuth ±179.5°, elevation ±89.5°.

The previous FlyVis crosswalk used axial coordinates with

```text
s = 180/31 degrees
eye_horizontal = -s*v
eye_elevation  = -s*(u + v/2)
```

That basis remains recorded as provenance but the **new regular sensor grid does not run a FlyVis hex lattice or checkpoint**. The chart sources use T4a/T4c as functional orientation anchors. The MaleCNS exporter assigns eye centers ±80°, 5° column spacing, and elevation clipping at ±80°; the FlyVis renderer uses its own 180/31° pitch. These are model definitions, not measured optical calibration. See [coordinate evidence V2](POSTFIX_COORDINATE_EVIDENCE_V2.md), [source manifest](../results/fixed_neighbor_motion_v1/prospective_manifest.json), and [geometry audit](../results/fixed_neighbor_motion_v1/geometry.json).

**A mirror-consistency pass cannot establish independently registered specimen optics.** It verifies the declared transform and physical input symmetry. Neither left/right signs nor eye references were changed after inspecting current neural outputs.

![Physical panorama and registered local luminance](../results/fixed_neighbor_motion_v1/figures/physical_and_retinal_inputs.png)

## 5. Motion equations, initialization, and output wiring

All luminance values are finite in [0,1]. At each site and for both eyes, construct

\[
c_{\rm ON}=\max(2L-1,0),\qquad
c_{\rm OFF}=\max(1-2L,0).
\]

These depend only on local brightness and contain no motion direction. Each family has its own delay state at every site:

\[
\tau\dot d=c-d,\qquad \tau=0.03\;\mathrm{s},\qquad d_0=c_0.
\]

Initialization assumes the first image existed for a stationary equilibrium prehistory. It is not a fitted estimate of a real neuron's resting state. For samples at times \(t_n\), propagate the **previous sample's hold**:

\[
\alpha_n=1-\exp[-(t_n-t_{n-1})/\tau],\quad
d_n=d_{n-1}+\alpha_n(c_{n-1}-d_{n-1}).
\]

The production implementation uses `-expm1(-dt/tau)` for numerical accuracy. It then computes the current contrast from frame \(n\), without updating any past state using a future frame.

For each ON/OFF family, centered at a site \((h,e)\):

\[
s_H=d(h-1,e)c(h+1,e)-d(h+1,e)c(h-1,e),
\]
\[
s_V=d(h,e-1)c(h,e+1)-d(h,e+1)c(h,e-1).
\]

The offsets are **one grid step**, corresponding to 1° on this grid and a total neighbor-pair span of 2°. Both branches exist everywhere. Direction discrimination arises because the ordered activation of adjacent positions changes these delayed products.

Average each signed field with a uniform 7×7 window, **before rectification**:

\[
\bar s(h,e)=\frac1{49}\sum_{i=-3}^{3}\sum_{j=-3}^{3}s(h+i,e+j).
\]

For each family create the four channels

\[
[\max(\bar s_H,0),\max(-\bar s_H,0),
  \max(\bar s_V,0),\max(-\bar s_V,0)].
\]

Constant-zero padding exists in the numerical filter at the outer grid edge, but no accepted target or pooled-valid-site readout uses incomplete support. The signed result can be recovered as the positive channel minus its opponent.

States/contrasts lie in [0,1], signed pair differences in [−1,1], and convex averaging/positive rectification yields channels in [0,1]. There is no trial-dependent normalization, fitted directional gain, or clipping to obtain a pass. Internal filter/pooling arithmetic is float64; target activity is stored as float32.

At each target coordinate, bilinear weights sample **all eight channels**. Only afterward does fixed output wiring choose:

| Channel index | Computed feature | Declared output slot |
|---:|---|---|
| 0 | ON +H | T4a-like |
| 1 | ON −H | T4b-like |
| 2 | ON +V | T4c-like |
| 3 | ON −V | T4d-like |
| 4 | OFF +H | T5a-like |
| 5 | OFF −H | T5b-like |
| 6 | OFF +V | T5c-like |
| 7 | OFF −V | T5d-like |

This table is a **specified model connectivity assumption**. It is permissible evidence of a direction-sensitive fixed circuit operating on pixels, but not independent evidence that each anatomical T4/T5 subtype acquires its observed preference from reconstructed biological wiring. The successful a/b sign comparison is conditional on this table. No target subtype chooses an image sample offset.

### 5.1 Parameter provenance

| Parameter | Value | Origin / meaning |
|---|---|---|
| Luminance baseline | 0.5 | Declared normalization convention |
| Delay pole | 30 ms | Fixed exploratory value; not estimated from current recordings |
| Grid pitch | 1° | Fixed computational discretization |
| Neighbor displacement | ±1 site | Fixed explicit connectivity |
| Pair span | 2° | Derived from grid/displacement |
| Signed pooling | Uniform 7×7 | Fixed exploratory spatial smoothing |
| Eye reference/basis | ±80°, mirrored horizontal axes | Inherited source-chart convention |
| Routing | Table above | Declared surrogate anatomy assignment |
| Drive scale | 1 for every output | Common normalized-unit conversion |
| Scoring thresholds/window | Section 7 | Predeclared exploratory engineering criteria |

Correlation-sensitive T4/T5 responses provide biological motivation, including fast temporal effects; they do not identify these exact constants. Salazar-Gatzimas et al. also reported observations inconsistent with a particular classic model, so that paper is **not validation of this exact Reichardt-style surrogate**. [Primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5097865/). The ON/OFF and cardinal-channel organization is motivated by measured T4/T5 populations; it remains an imposed output organization here. [Maisak et al.](https://www.nature.com/articles/nature12320).

## 6. Frozen experiment and complete stimulus inventory

The protocol, code, tests, configuration, target identities/routing, geometry, movie plans, and source dependencies were hash-frozen at **2026-10-13T03:49:35.257350+00:00**, before new benchmark response inspection. The manifest lists **26 method/input files**, plus external source hashes. Analytic/synthetic fixture tests preceded the freeze. Seed 42 is historical; seeds 78201/78202/78203 are new stimulus textures for this study. No parameter search, best-seed selection, or failed-group rescue by pooling seeds occurred.

| Source subset | Contents | Saved executions |
|---|---|---:|
| Primary textures | Seeds 42, 78201, 78202, 78203 × seven conditions | 28 |
| Supplemental speeds | Seed 78204: STATIC, global ±30 and ±90°/s | 5 |
| Cardinal gratings | 0°, 90°, 180°, 270° | 4 |
| Fine-clock textures | Seed 78201: STATIC, global ±60°/s at 2.5 ms | 3 |
| Fine-clock gratings | Four cardinal gratings at 2.5 ms | 4 |
| Runtime controls | Same-input replay, physical mirror, temporal scramble | 3 |
| **Total source executions** | All retained; no dropped cases | **47** |

Only the **28 primary trials** were run through the frozen downstream circuit. Grating/speed/fine-clock counts are source results, not additional network or biological replications.

### 6.1 Primary random-square movies

The random world texture uses 6°×6° black/white squares with luminance 0/1, generated by `numpy.random.default_rng(seed)`. The source world is 480° azimuth ×180° elevation; the visible panorama is 360°×180°, at 1° pixel pitch (180 rows ×360 columns). Pixel-center axes are azimuth −179.5°…+179.5°, elevation +89.5°…−89.5°. Translation is bilinearly sampled from the physical source texture. Consequently, **rendered pixels can be gray at translated square boundaries even though source squares are binary**.

Clock: \(t_n=n\times0.005\) s for \(n=0,...,400\), duration 2 s, motion from 0.5 to 1.5 s. Response analysis uses saved samples satisfying 0.7≤t≤1.4 s. The code's actual comparison mask, not a reconstructed nominal sample count, defines endpoint inclusion.

Let \(q(t)=\operatorname{clip}(t-0.5,0,1)\). For a moving pixel, the source texture is evaluated at world coordinate \(a-vq(t)\), so positive \(v\) moves the pattern toward increasing world azimuth. Negative movies are physical translations with negative \(v\); no neural-input sign is flipped.

| Condition index | Name | Physical velocity | Moving field |
|---:|---|---:|---|
| 0 | STATIC | 0 | Neither |
| 1 | HORIZONTAL_GLOBAL_POSITIVE | +60°/s | Both |
| 2 | HORIZONTAL_GLOBAL_NEGATIVE | −60°/s | Both |
| 3 | LEFT_FIELD_POSITIVE | +60°/s | World azimuth <−5° |
| 4 | LEFT_FIELD_NEGATIVE | −60°/s | World azimuth <−5° |
| 5 | RIGHT_FIELD_POSITIVE | +60°/s | World azimuth >+5° |
| 6 | RIGHT_FIELD_NEGATIVE | −60°/s | World azimuth >+5° |

For unilateral movies, the inactive field and 5° guard remain the **initial stationary texture**, not a blank field. The final audit verifies complete STATIC/unilateral rasters for all four primary seeds: 20 checks. The two modeled eye grids extend somewhat across the world midline; hemisphere-isolated world motion does not imply zero sampled motion at every site in the opposite modeled eye.

### 6.2 Supplemental, grating, and control details

Supplemental ±30/±90°/s movies use seed 78204 and a **600° source world**, including their own STATIC. A different source width changes the RNG texture layout; these movies must not be paired against a primary 480° STATIC, or interpreted as identical-texture speed sweeps across all three speeds.

Cardinal gratings use

\[
L(a,e,t)=0.5+0.5\cos\left[\frac{2\pi}{24^\circ}
\left(a\cos\theta+e\sin\theta-60^\circ\mathrm{/s}\;q(t)\right)\right],
\]

with θ=0/90/180/270°. Temporal frequency during translation is 2.5 Hz. These are algorithmic axis/polarity controls, not stimulus-matched recordings. Fine-clock runs use 2.5-ms steps and 801 frames, otherwise the same corresponding parameters.

Runtime controls use `primary_s78201_c1`. Mirror reverses raster azimuth columns, preserving physical axes/times, then checks that sampled retinal inputs exchange eyes before checking responses. Scramble permutes frames strictly inside 0.5<t<1.5 s using RNG seed **917**, preserving onset/end frames. The ordered and scrambled pooled signed H signals are compared in each eye/contrast family. Exact replay reconstructs the same numerical movie without giving the detector a label; a separate complete network replay changes the textual stimulus name.

Every primary/supplemental pair and every individual target remains available, including vertical slots and weak/silent positions. Tables have not been filtered to favorable cases.

## 7. Definitions and acceptance gates

### 7.1 Source responses

For every mapped target, take the mean response difference against that texture's matching STATIC in the fixed response window:

\[
R_+=\operatorname{mean}(y_+-y_0),\qquad
R_-=\operatorname{mean}(y_--y_0),
\]
\[
\mathrm{DSI}=\frac{R_+-R_-}{|R_+|+|R_-|+10^{-12}}.
\]

The sign is in **global physical coordinates**. It is computed before anatomical comparison; the anatomical label is not used to select a favorable numerator. An empirical larger response can be recovered from the sign. A cell is resolved/selective only if **all** three conditions hold:

```text
max(abs(R+), abs(R−)) >= 0.001
abs(R+ − R−)         >= 0.001
abs(DSI)             >= 0.1
```

For each a/b subtype, each eye, and each primary texture separately, at least **75% of cells** must both meet those conditions and have the specified physical sign. Expected global signs are Right-a +, Left-a −, Right-b −, Left-b +, for both ON/T4-like and OFF/T5-like families. This yields eight required horizontal groups per seed, **32 primary groups**. Supplemental speeds add **16** required groups. Group `dsi_mean` is the average of individual DSIs; it is **not** the DSI calculated from group-average responses.

For c/d slots the complete individual/group scores are retained, but no expected horizontal sign or c/d-suppression gate was imposed for the new functional decision. Null fields in their group table mean **not an acceptance test**, not a pass. `expected_horizontal=False` for c/d individual rows means no horizontal expectation was defined; it is not evidence of wrong anatomy.

### 7.2 Other source gates

| Test | Frozen criterion |
|---|---|
| Geometry | Every target's four vertices have complete neighbor/pool support |
| STATIC source | Maximum activity ≤1e−10 |
| Cardinal grating | Correct dominant channel, expected-vs-opponent DSI ≥0.1, activity ≥0.001 in both eyes/families: 16 comparisons |
| Sampling refinement | Horizontal group R+/R− relative changes ≤10%, denominator floor 0.001; mean individual-DSI change ≤0.02; same group verdict |
| Grating refinement | Pooled channel mean relative changes ≤10%; opponent-DSI change ≤0.02; same physical dominance verdict |
| Same-input replay | Every saved source array bitwise equal |
| Metadata removal | Allowlisted target map equal; no preferred-angle arguments in core |
| Mirror | Retinal input eye exchange bitwise equal; pooled/probe output discrepancy ≤1e−7 |
| Temporal scramble | Absolute pooled signed H response ratio ≤0.5 in each eye/family |
| Independent source implementation | Absolute channel error ≤1e−7; final filter state error ≤1e−10 |

Fine-clock tests address this **source discretization and selected group readouts**, not a proof of continuous-time convergence for every input, every individual decision, or the entire downstream network. Their 10% margin is an engineering tolerance, not a biological error bar.

### 7.3 Downstream gates

The same 0.001 amplitude/difference and 0.1 DSI floors apply to global network response comparisons. For all ten HS/H2 targets, every primary texture must yield a resolved response in the expected global sign. HS is compared as ipsilateral FTB; H2 as BTF in the body-ID-specific reference eye.

All network cells must have STATIC response-window vs pre-motion [0.3,0.5]-s mean change ≤0.001 and within-response-window range ≤0.001. All ten targets additionally require the expected sign of ipsilateral unilateral + minus − response. That unilateral criterion is a **sign check**, not another amplitude/selectivity threshold or a complete contralateral physiological validation.

`FUNCTIONAL_FRONTEND_PASS` requires all source gates plus reference checks. `FUNCTIONAL_END_TO_END_PASS` adds complete frozen-network execution, numerical verification, STATIC stability, all global target gates, and ipsilateral sign checks. These names designate the frozen engineering contract only.

## 8. Source results

**Decision: `FUNCTIONAL_FRONTEND_PASS`.** All 47 executions and 81,474 individual direction rows are retained. The latter are 13,579 targets ×six benchmarks (four primary textures plus two supplemental speeds), not 81,474 neurons or biological trials.

| Texture seed | Horizontal groups passing | Minimum expected-selective fraction | Mean group fraction |
|---|---|---|---|
| 42 | 8/8 | 99.881797% | 99.985225% |
| 78201 | 8/8 | 100.000000% | 100.000000% |
| 78202 | 8/8 | 100.000000% | 100.000000% |
| 78203 | 8/8 | 99.881517% | 99.985190% |

All **16/16 supplemental horizontal groups** pass: minimum expected fraction at 30°/s is **99.6364%**, at 90°/s **100%**. All **16/16 cardinal eye/family comparisons** pass. STATIC maximum across the checked source conditions is **exactly zero**. This follows from the equilibrium initialization and opponent product equality; it does not predict zero tonic firing in a real stationary-image neuron.

Exact source replay is bitwise equal. Mirrored retinal inputs exchange eyes bitwise, with maximum pooled/probe discrepancy **0**. Scramble ratios, ordered Left-ON, Left-OFF, Right-ON, Right-OFF, are:

```text
[0.006855868580990111, 0.006369840882641257,
 0.006078674698956365, 0.006590399155025654]
```

Thus the scrambled pooled signed contrast is at most **0.686%** of its ordered value, versus the 50% ceiling. This supports temporal-order dependence for that control; it is not a biological mechanism identification or a guarantee for all shuffled inputs.

Maximum sampling-refinement relative response error is **4.100949%**, below 10%. Maximum horizontal group DSI change is **6.6092473e−5**; maximum grating opponent DSI change is **1.9083471e−6**. All declared group/grating refinement verdicts agree.

![Primary texture group results](../results/fixed_neighbor_motion_v1/figures/source_texture_results.png)

![Four cardinal grating outputs](../results/fixed_neighbor_motion_v1/figures/cardinal_motion_channels.png)

### 8.1 Retained cross-axis limitation

| Seed | Mean a/b expected-selective fraction | Mean c/d selective fraction | c/d : a/b mean response strength |
|---|---|---|---|
| 42 | 99.9852% | 85.6267% | 13.6353% |
| 78201 | 100.0000% | 85.9726% | 13.2260% |
| 78202 | 100.0000% | 86.7055% | 13.5315% |
| 78203 | 99.9852% | 85.4153% | 13.5690% |

These are unweighted averages across the eight subtype/eye groups. Response strength is each group's `max(abs(mean R+), abs(mean R−))`, averaged within a/b or c/d, then divided c/d by a/b. It is not the fraction of total synaptic energy or a measured physiological ratio. This descriptive calculation was added after analysis; it changed no acceptance rule.

The vertical slots have smaller horizontal-texture responses, but many exceed the binary selectivity floor. A high DSI can occur for a small response; amplitude and direction must be assessed together. **A cause has not been established.** Correlated texture edges interacting with fixed pair geometry and finite pooling are a plausible computational explanation to test, not an experimentally demonstrated causal conclusion. Pure cardinal gratings pass axis controls, but that does not establish complete tuning under textured scenes.

The complete 96 group rows, with all c/d results, appear in Appendix B. The per-cell CSV retains empirical global preferences and response values. Cardinal comparisons appear in Appendix C.

## 9. Frozen downstream model and results

### 9.1 Exact circuit and equations

The selected graph has **13,593 nodes**: 13,579 T4/T5, eight HS, two H2, two PS321/BIPS, and two DNp15. All nodes are active in the saved graph. Chemical weights are a float64 CSR matrix with **203,861 nonzero entries**; gap weights have **zero nonzero entries**. The recorded gap gain is one, but there are no gap edges in this model.

Chemical matrix rows are postsynaptic and columns presynaptic. The frozen construction uses strict annotated transmitter signs, a minimum synapse count of one, a linear count transform, and class multipliers all equal to one. Duplicate compatible edges are summed. Each chemical row is normalized by its sum of absolute signed weights (`post_abs_sum`); empty rows remain zero. Thus for a nonempty row, the matrix entry is signed synapse count divided by total accepted incoming count. These are reduced rate-model weights, not independently measured synaptic conductances. Gap inclusion is enabled in configuration but yields no edges in the selected snapshot. Saved matrices are authoritative for replay.

Let \(x\) be state, \(m\) the active mask, and \(r=\tanh(x)\odot m\). The original frozen rate model is:

\[
\dot x=\frac{-x+g_C W_C r+
g_G[W_Gx-\operatorname{rowsum}(W_G)\odot x]+
g_D(u\odot m)}{\tau_D}.
\]

| Frozen parameter | Actual value |
|---|---:|
| \(\tau_D\) | 0.02 s |
| Chemical gain \(g_C\) | 0.873579331825114 |
| Drive gain \(g_D\) | 0.21936608020509474 |
| Gap gain \(g_G\) | 1.0 |
| Solver step | 0.001 s |
| Initial state for each trial | All zeros |

These gains were inherited from a pre-existing frozen parameter checkpoint; “no fitting” means **no refitting in this study**, not that no historical calibration ever occurred. Actual values, versions, and all external legacy input hashes are in [graph.json](../results/fixed_neighbor_motion_v1/downstream/graph.json).

The legacy configuration also retains descriptive metadata from its previous calibration stimulus. Those historical display/starfield settings are not the movies used here: the new run supplies explicit image-derived external drive and zero legacy velocity vectors. Reusing the frozen graph/parameters does not reproduce or revalidate that earlier calibration protocol.

Only the exact 13,579 source body IDs receive direct input. Every non-T4/T5 direct-drive column is zero, including HS/H2. The common conversion is normalized routed activity with unit scale; there is no type-specific or sign-specific amplitude adjustment. The network rate is a dimensionless `tanh` output, not spikes/s, membrane voltage, calcium, or current calibrated to recordings. It can be negative.

The source movie is sampled at 5 ms. The bridge takes every second routed sample (201 samples at 10 ms), casts to float64, maps by body ID, and repeats each input over ten 1-ms solver nodes. The original RK4 solver uses input at both endpoints and their arithmetic mean at the midpoint. Accordingly, transitions include that endpoint/midpoint convention; this is not an exact continuous-time zero-order-hold integration. No intended yaw or translation velocity is supplied: those legacy vectors are zero.

Each trial integrates 2,001 solver-time states from 0 to 2 s. Initial zero state is the common equilibrium of this model under the zero stationary motion drive. Saved all-cell state/rate arrays are every tenth solver sample, float32; full initial/final states and separate HS/H2 state/rate records are float64. The independent numerical reviewer checks the **same declared discrete solver and drive schedule**, not a separate finer-step convergence result. Downstream timestep refinement was not newly benchmarked in this surrogate study.

### 9.2 Target identities and anatomical comparison

| Body ID | Type | Side / reference eye | Expected eye direction | Expected global sign |
|---|---|---|---|---|
| 10015 | HSN | R / R | FTB | + |
| 10016 | HSE | R / R | FTB | + |
| 10023 | HSS | R / R | FTB | + |
| 10034 | HSE | L / L | FTB | − |
| 10181 | HSN | L / L | FTB | − |
| 10419 | HSS | L / L | FTB | − |
| 11793 | HST | L / L | FTB | − |
| 12521 | HST | R / R | FTB | + |
| 10019 | H2 | L / L | BTF | + |
| 10025 | H2 | R / R | BTF | − |

Reference eyes are supported by direct T4/T5 afferent body-ID joins. In the preserved coordinate evidence, H2 10019 has 1,560 such left afferent edges and zero right; H2 10025 has 1,592 right and zero left. H2 is a wide-field modeled target with no matched individual retinotopic recording position. Its BTF test is a qualitative plausibility check. The graph and literature do not supply a new quantitative recording validation here.

### 9.3 Results for all seeds

**Decision: `FUNCTIONAL_END_TO_END_PASS`.** All **28/28** primary network trials completed. All **40/40** expected measurable global HS/H2 comparisons and **40/40** ipsilateral unilateral contrast signs pass. All-circuit STATIC stability passes; its zero-input zero-state trajectories remain zero. A whole-network textual label replay matches every internal state and rate **bitwise**.

| Texture seed | Global targets passing | Ipsilateral signs passing | Absolute global DSI range | Minimum expected-signed ipsilateral contrast |
|---|---|---|---|---|
| 42 | 10/10 | 10/10 | 0.560511–0.620786 | 0.058241614 |
| 78201 | 10/10 | 10/10 | 0.551698–0.625634 | 0.057311256 |
| 78202 | 10/10 | 10/10 | 0.541787–0.630508 | 0.054998585 |
| 78203 | 10/10 | 10/10 | 0.556003–0.622223 | 0.056399698 |

The response units and models differ from the older failed studies. This pass is not a calibrated biological amplitude improvement over FlyVis or the published conductance models. The exact full-precision means for every target/seed and all seven conditions appear in Appendix E, from **V2** exports. No target or seed has been omitted.

![All ten seed-42 HS/H2 trajectories](../results/fixed_neighbor_motion_v1/figures/hs_h2_seed42_traces.png)

## 10. Validation: what was independently checked

The source/reference/scoring code is separately implemented within this project and run by the same coding workflow. “Independent” means a different numerical implementation that avoids calling the production calculation for its verdict; it does **not** mean independent investigators, blinded external replication, or biological validation.

| Check | Extent | Measured result | What it establishes |
|---|---|---|---|
| Analytic/contract tests before freeze | 28 focused cases across motion, existing raster sampler, drive adapter | 28 passed | Selected mathematical identities, causality, support, malformed-input handling |
| Delay reference | All 47 source cases; streamed `scipy.signal.lfilter` vs production recurrence | Final state error ≤5.551115123125783e−16 | Implemented temporal filter agreement |
| Spatial/channel reference | Summed-area rectangular averages instead of `uniform_filter`; independent readout weights | Channel error ≤2.5544847792602354e−8, tolerance 1e−7 | Declared source equations/readouts reproduced |
| Physical movie reference probes | Six independently regenerated pixel positions across all times of non-control physical movies | Error ≤2.972915313925739e−8 | Physical translation/grating probes agree; not an independent reconstruction of every moving pixel |
| Retinal interpolation | Full saved retinal samples vs separate bilinear reconstruction | Error ≤2.9802322387695312e−8 | Pixel-to-grid interpolation agrees |
| Batch vs streaming reference fixture | 45-frame, 2×11×11 synthetic contrast array, RNG 771 | Bitwise equal | Reference memory-layout change preserves that filter |
| Independent source decisions | 96 groups and 16 grating cases | Every decision agrees | Decision arithmetic from separately computed response means |
| All-cell source scalar audit | 81,474 rows from identical saved float32 traces using compensated sums | Max scalar discrepancy 5.828670879282072e−16 | Exported scores/classes agree with the saved numerical representation |
| Separate model-vs-saved means | Physical reference retained at original model tolerance | Max mean discrepancy 1.28347435457421e−9; zero class changes | Small source storage/reference differences do not change resolved conclusions |
| Physical STATIC/unilateral audit | 20 full-raster controls | Pass | Stationary opposite fields and STATIC maintained |
| Independent downstream replay | All 28 trials; separate RHS and reordered RK4 from saved matrices/drives | All-cell error ≤7.4505756564313685e−9 (tol 1e−7); HS/H2 error ≤1.3877787807814457e−17 (tol 1e−10) | Discrete graph-equation/solver agreement |
| Final wide-field arithmetic | All 40 decisions, float64 traces | Pass at original strict tolerances | Correct V2 means and direction/static/unilateral decisions |
| Integrity/format audit | 470 finite arrays, exact identities/clocks, prior study entries | Pass | Stored evidence consistency; does not establish biology |
| Figure inspection and compact-package test | Four figures, PNG/PDF; extracted standalone demo | Visual pass; archive CRC pass; demo arrays bitwise equal | Reviewable presentation and portable core execution |

Important analytic tests include an ordered-flash response with closed-form delay value, reversed spatial order, arbitrary stationary-pattern zero response, future-frame modification leaving the earlier output prefix identical, all channels existing before routing, complete-footprint rejection, exact bilinear interpolation of a linear field, physical image mirror before neural output, NaN luminance and nonmonotonic clock rejection.

These checks directly address known previous validation gaps. In particular, matching arithmetic alone did not detect an older future-dependent clamp bug; the new core has a causal-prefix test. Repeating hard-coded scoring literals could not detect a previous changed-config reuse defect; current results are reported with their exact frozen configuration and separately checked scalar outcomes. No validation procedure substitutes for recording comparison.

## 11. Failures, recovery, and statistics corrections

All first failures, partial successful batches, correction records, helper source snapshots, and successful retries are preserved. Recovery did not alter a biological/model parameter or loosen a scientific gate. The log chronology matters: a final PASS alone would hide real technical problems.

| Issue | Observed failure and retained evidence | Correction and check |
|---|---|---|
| Source memory/swap guard | Worker stopped after 38 saved cases; `execute_source_supervisor.json`: `MEMORY_LIMIT`, exit −15, elapsed 364.162 s, peak RSS 1,869,488,128 bytes | Release transient eye buffers and run each remaining movie in a fresh supervised process; full-array replay of a completed case bitwise identical; original 38 kept and final 47 completed |
| Reference memory layout | Batch reference needed a bounded layout | Stream the same `lfilter`; synthetic batch/stream test bitwise equal; source arrays unchanged |
| Pixel-reference endpoint bug | First source reference tried row 180 of a 180-row image; failed `source_reference_execution.log` retained | Bound adjacent interpolation indices at the final valid pixel center, after rejecting out-of-support coordinates; endpoint fixtures passed; corrected reference completed all 47 |
| Downstream memory/swap guard | Worker stopped after 25/28 trials; peak RSS 2,391,257,088 bytes, elapsed 134.153 s, exit −15 | Same frozen worker in a fresh supervised process skipped verified completed batches and completed the last three; no graph/input/solver change |
| Nearly silent source DSI audit | 72 source slots differed from the physical float64 reference above the strict scalar-comparison tolerance; max DSI discrepancy 1.0659999229824259e−5, **zero selective-class changes** | Tiny ~1e−18 outputs interact with the 1e−12 DSI denominator. Separately verify equations at the original model tolerance and arithmetic on the **identical saved float32 traces** using `math.fsum`; do not weaken either tolerance |
| Wide-field V1 mean precision | V1 means accumulated float32 all-cell records; checker used separate float64 HS/H2 records. 152 comparisons exceeded 1e−10; max condition-mean difference 1.328143058032527e−8 | Create versioned V2 export from unchanged float64 traces with compensated sums; assert all 40 scientific verdicts unchanged; preserve V1 and failed audit attempts |

The memory supervisors combine an RSS ceiling of 6,000,000,000 bytes with a **zero-swap clause**, two-hour wall-time limit, and ≥8,000,000,000 free disk bytes. Logged peak RSS is below the ceiling, so the records implicate the combined memory/swap guard; they do not record an exact `VmSwap` value. It would be unsupported to claim the process used more than 6 GB in these two interruptions. Buffer retention is a plausible resource explanation, not a separately measured allocator diagnosis.

The 72 nearly silent source slots are not all c/d; the retained diagnosis includes a horizontal T4b slot too. They are far below the amplitude gate. For a silent denominator-regularized ratio, tiny signed numerical residues should not be interpreted as meaningful direction. The resolved classifications remain unchanged.

The first final scalar check and two precision-recovery attempts failed; their logs are `final_checks_execution.log`, `final_checks_execution_r1.log`, and `final_checks_execution_r2.log`. The successful full-precision audit is `final_checks_execution_r3.log`. The initial progress entry's smaller mean-error estimate was corrected in a later append-only entry; the value used here is the measured **1.328143058032527e−8** diagnosis.

Specific amendments and evidence:

- [memory_recovery_amendment.json](../results/fixed_neighbor_motion_v1/memory_recovery_amendment.json), [memory_recovery_replay.json](../results/fixed_neighbor_motion_v1/memory_recovery_replay.json).
- [independent_memory_amendment.json](../results/fixed_neighbor_motion_v1/independent_memory_amendment.json), [reference_endpoint_amendment.json](../results/fixed_neighbor_motion_v1/reference_endpoint_amendment.json), [reference_endpoint_test.json](../results/fixed_neighbor_motion_v1/reference_endpoint_test.json).
- [downstream_resume_record.json](../results/fixed_neighbor_motion_v1/downstream_resume_record.json).
- [final_scalar_diagnosis.json](../results/fixed_neighbor_motion_v1/final_scalar_diagnosis.json), [final_arithmetic_amendment.json](../results/fixed_neighbor_motion_v1/final_arithmetic_amendment.json).
- [wide_field_precision_diagnosis.json](../results/fixed_neighbor_motion_v1/wide_field_precision_diagnosis.json), [mean_export_amendment.json](../results/fixed_neighbor_motion_v1/mean_export_amendment.json), [final_checks.json](../results/fixed_neighbor_motion_v1/final_checks.json).

The off-axis descriptive discussion was added after scoring and explicitly labeled post-analysis. It neither added a new acceptance criterion nor reclassified an old failed study. Report synthesis adds no new scientific pass.

## 12. Claim limits and information still needed

**Supported:** a causal, fixed-connectivity source computation from physical pixel movies; complete target mapping; the frozen functional benchmark; unchanged downstream integration with the recorded target preferences; numerical verification and recoverable local artifacts.

**Not demonstrated:** reconstructed upstream biological microcircuits, independently predicted subtype preferences, optical calibration of this specimen, quantitative voltage/rate/calcium prediction, physiological uncertainty, population validity, broad natural-scene robustness, unique model identification, neural degeneracy, or publication novelty.

Four textures are replications of a computational stimulus, not four flies. The thousands of positions share the same circuit equation and spatially overlapping pixels; they are not independent biological cells with independently measured parameters. No animal-level confidence intervals, p-values, or physiological equivalence margins follow from these counts. The 0.001/0.1/75% thresholds and 10% sampling margin are predeclared engineering choices.

The ON/OFF branches have the same temporal and spatial constants. Real T4 and T5 can differ. The detector retains eight motion feature channels, whereas assigning those features to anatomical targets uses the specified routing. Changing the routing does not change the core eight-channel calculation but would change the delivered target identities and downstream result. Therefore label-removal/replay alone cannot validate that routing biologically.

The benchmark samples three speed magnitudes across different textures/world widths, one square scale, one sinusoidal wavelength, cardinal directions, and two source sample clocks. It does not measure full speed/spatial-frequency tuning, eight-direction curves, contrast adaptation, response to flicker, natural images, or robustness to the whole admissible input space. Finite signed pooling reduces some noise but does not remove the reported texture-dependent cross-axis activity.

### 12.1 Do we need external data to keep using this artifact?

For generic detector use and the standalone demo: **no** biological recording data are needed. NumPy/SciPy suffice.

For exact full network reproduction: the portable source archive is insufficient by itself. It requires the recorded legacy MaleCNS source/configuration/input files or a new versioned runner reconstructed from the saved graph and equations. Those files exist locally and are hash-identified; the compact handoff does not pretend to include the entire original workspace.

For a claim that the surrogate reproduces real T4/T5: **yes, empirical constraints and a declared observation model are needed**. Published T5 data already exist and were used in the earlier one-cell comparison; “we have no data” would be false. What is missing is a matched, justified comparison for this surrogate and broader independent cells/conditions where available. Current dimensionless feature units cannot be directly compared to mV or calcium without a prospectively specified conversion and appropriate held-out evaluation.

The T5 author repository includes recordings/model results for seventeen cells; our prior matched analysis used one illustrative cell. [Author repository](https://github.com/reiserlab/T5ConductanceModel). Availability does not establish complete provenance, adequate trial repeats, correct stimulus/retinotopy matching, or population coverage. Those must be audited before treating the archive as an independent validation cohort.

## 13. Recommended next decisions

The completed artifact can be handed to the supervisor now. The next work should follow an explicit scientific use, rather than another unstructured search for a favorable response.

1. **Accept or reject the functional-baseline scope.** Review the fixed subtype routing, coordinate conventions, unit drive, and c/d cross-axis responses. If the original task requires reconstructed anatomical emergence, identify the specific missing evidence rather than treating this engineering pass as its completion.
2. **If the immediate goal is a reliable simulation input:** keep this version frozen and use it as the documented baseline. Define the new downstream question and its acceptance criteria before changing parameters or stimuli.
3. **If the goal is physiological prediction:** audit available recorded cells/protocols, specify what observable is predicted, establish alignment/units and an observation model, separate any calibration set from held-out conditions/cells, and compare both scalar responses and waveforms. A negative quantitative comparison remains informative.
4. **If cross-axis suppression is necessary:** first run a small new frozen diagnostic separating horizontal gratings, horizontal edges, and random textures, preserving signed H/V fields and spatial edge structure. Then use predeclared ablations of pooling or pair geometry. A hypothesized texture interaction must be demonstrated before changing the detector and claiming a causal fix.
5. **If degeneracy becomes the question again:** define outputs, material mechanism differences, symmetry exclusions, uncertainty/equivalence margins, and held-out inputs. The older timing-compensation result is a limited computational starting point; it does not certify distinct real circuits.

None of these follow-ups was executed for this report. They are proposals, not completed evidence. A publishable claim also requires literature/novelty assessment and scientific review; passing this software benchmark does not supply either.

## 14. Reproducibility and environments

### 14.1 Portable core demonstration

Extract the handoff ZIP into a new directory. With NumPy and SciPy installed:

```bash
PYTHONDONTWRITEBYTECODE=1 python examples/fixed_neighbor_motion_demo_v1.py --output <TEMP>/fixed-motion-demo.npz
```

The demo constructs a physical right-moving cosine raster and calls the same generic module. Its recorded means are ON +H 0.065779, ON −H 0.000005, OFF +H 0.078599, OFF −H 0.000003; vertical channels are zero. It is illustrative, **not an additional benchmark success**. The previously extracted V2 review archive's demo matched every saved array bitwise. The present handoff is checked separately as described in its manifest.

The generic module needs neither a FlyVis checkpoint nor the MaleCNS legacy environment nor biological recordings. A minimal local-luminance call is:

```python
import numpy as np
from male_optic_frontend.fixed_neighbor_motion import (
    RetinalGrid, MotionCircuitConfig, simulate_retina,
)

grid = RetinalGrid(np.arange(-10., 11.), np.arange(-10., 11.))
t = np.arange(201) * .005
pixels = np.full((len(t), *grid.shape), .5)
result = simulate_retina(pixels, t, grid, [[0., 0.]], MotionCircuitConfig())
assert np.all(result['all_channels'] == 0)
```

Here `pixels` are already samples on the local regular retinal grid; physical panorama use adds `local_luminance` and explicit eye-to-world coordinates first.

### 14.2 Actual recorded runtimes

| Runtime | Interpreter / packages |
|---|---|
| Source analysis/test | Python 3.11.16; NumPy 2.4.6; SciPy 1.17.1; Matplotlib 3.11.2; pytest 9.0.2 |
| Frozen downstream | Python 3.14.8; NumPy 2.5.3; SciPy 1.18.1; pandas 3.0.6; PyYAML 6.0.3 |

Source interpreter used: `<TEMP>/maleoptic-texture-analysis-venv/bin/python`. Downstream interpreter: `<HOME>/Lab/mech_male_fly_cns/.venv/bin/python`. The source environment lacks pandas/PyYAML; the existing legacy environment was read only. No old temporary FlyVis interpreter is required for this surrogate. Pins are in [source requirements](../requirements-fixed-motion-source-v1.txt) and [downstream requirements](../requirements-fixed-motion-downstream-v1.txt).

Common execution environment:

```bash
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=src:scripts
export OPENBLAS_NUM_THREADS=2
export OMP_NUM_THREADS=2
export MPLCONFIGDIR=<TEMP>/maleoptic-texture-mpl
```

### 14.3 Full study execution sequence and corrections

**The completed V1 study refuses overwrites. Do not execute these mutation actions in the sealed workspace.** Use a fresh restored workspace without this study's generated output directory, preserving required predecessor evidence and resolving the exact legacy inputs. A changed scientific configuration or relocated dependencies needs a new version and freeze. The compact ZIP supports the demo and audit of included evidence; it is not a turnkey full-workspace replication.

The original sequence was:

```text
1. Run the 28 focused motion/sampler/adapter tests and save log/XML.
2. run_fixed_neighbor_motion_v1.py freeze
3. run_fixed_neighbor_motion_v1.py launch_source
   Original worker stopped after 38 completed cases.
4. Freeze/hash memory_recovery_amendment.json.
   recover_fixed_neighbor_motion_memory_v1.py replay
   recover_fixed_neighbor_motion_memory_v1.py resume
   These preserve/hash-check existing cases and complete the remaining nine.
5. Freeze/hash the independent-memory and endpoint-reference amendments.
   Corrected source review: recover_fixed_neighbor_motion_reference_v1.py
   This imports the streaming reference, replacing only its endpoint probe helper.
6. run_fixed_neighbor_motion_v1.py analyze_source
7. review_fixed_neighbor_motion_v1.py source_decisions
8. run_fixed_neighbor_motion_v1.py launch_downstream
   Original worker stopped after 25 completed trials.
   Same downstream action in a fresh supervised process completes the remaining three.
9. review_fixed_neighbor_motion_v1.py downstream
10. report_fixed_neighbor_motion_v1.py downstream_analysis
11. report_fixed_neighbor_motion_v1.py report
12. Preserve original failed final audits; hash arithmetic/precision amendments.
    recover_fixed_neighbor_motion_mean_export_v1.py
    writes V2 statistics and runs the corrected final arithmetic checker.
13. Inspect figures; test extracted archive/demo; checkpoint source;
    snapshot progress; seal artifact_index.json.
```

The original `review_fixed_neighbor_motion_v1.py source` action failed at the raster endpoint and should not be described as the successful reviewer. The actual source checker is the corrected wrapper above. Recovery helpers require their recorded amendment JSONs; copying a command without those hashed prerequisites is not a complete reproduction procedure. All original/corrected sources and amendment records are included in the evidence handoff. The read-only frozen arrays plus separately coded reviewer support audit without rerunning the experiment; exact complete regeneration still requires the local external files.

## 15. Provenance, seals, and package contents

Current source/report checkpoint: **`6405a53330beef423f4e1049ad22505641dc1a50`**. Completion-ledger checkpoint before this report: **`b7ad4742b98cf0c6f3011fb803636c20f868aedf`**. Study completion: **2026-10-13T05:10:38.840975+00:00**. These are local checkpoints, not a remote backup.

Main [artifact index](../results/fixed_neighbor_motion_v1/artifact_index.json):

```text
SHA-256: 25d1390b8d96eb573d2f191df6faab95e52b4bd4402e8296abe9c2da7ef51c6a
Entries: 337
Sum of indexed file sizes: 2,803,993,570 bytes
```

These entry counts/bytes include overlapping copies/review packages and source files, not unique observations. Eleven predecessor indexes, **12,516 entry verifications**, were checked before/after the current experiment; overlap prevents interpreting the sum as unique files. The earlier evidence audit's 12,480 count predates addition of its own 36-entry index. Both counts are consistent with their respective scopes.

The old compact review ZIP V2 is 3,415,443 bytes, SHA-256 `e754d8be057e9b494fe4de189aba2e765236366a8b3cefb86996671d7dcce911`. It remains unchanged. This report has its own new handoff directory and manifest, preserving rather than updating the old seal.

| File | SHA-256 |
|---|---|
| `configs/fixed_neighbor_motion_v1.json` | `e04c6e652aa236852b7e208b8e1c19a725265d26bacef385f10699f01a7a4c12` |
| `src/male_optic_frontend/fixed_neighbor_motion.py` | `46d6434a6f8c188aa2228d227ba43bf7c2d8375d36d181fc78bd73d44b2f83ba` |
| `src/male_optic_frontend/retinal_input.py` | `10ce14adfce3cb273fda657b8ea0ea1e6ca1b9a8e2682b07832f49e91a760ab5` |
| `src/male_optic_frontend/visual_coordinates.py` | `cfbf2b1a45df1cb5f635a40703608d6c6fda27090a35f886c554dd7c71ef5914` |
| `scripts/run_fixed_neighbor_motion_v1.py` | `600e0529a9b7ca717ceb4f396d4c4c31af8fc52c5d5cc71d3a6e6adb78118301` |
| `scripts/recover_fixed_neighbor_motion_reference_v1.py` | `b8c52825e4cad17435a3ce95848aebf18ddaa8ee1992cbdc069b1a959a476356` |
| `results/fixed_neighbor_motion_v1/prospective_manifest.json` | `883db3bbc0e5c476d33495200ef305529f8c12ce020faf3d8fa2238e08ee9731` |
| `results/fixed_neighbor_motion_v1/source_groups.csv` | `b7ea0ee399c46f17d0444bcba7e652cde5f7f4d604b567c6d141604d81dfc0e3` |
| `results/fixed_neighbor_motion_v1/source_individual.csv` | `2a47e93775f7511573989a98b9dcec84a4a839bea6a747c0e87d525b4ef22400` |
| `results/fixed_neighbor_motion_v1/downstream_analysis_v2.json` | `96eb4825ee879064c19be65367816da7e1a57c5a13ef69da0fac0eacd5149c80` |
| `results/fixed_neighbor_motion_v1/hs_h2_results_v2.csv` | `3d78724b4c7eb7d818d37a519e1dff795b807bd6445fbb459dedf6e081e22c17` |
| `results/fixed_neighbor_motion_v1/downstream/graph.json` | `91b1f680f9533152480203d65f60f96739229ffe6e9d53dc2a61e2bb6c6c2da6` |
| `results/fixed_neighbor_motion_v1/downstream/chemical_weights.npz` | `035a97b22e4a88bce9a147e374628c0e59e79d006bc4e4177c99a136520f97b0` |
| `results/fixed_neighbor_motion_v1/downstream/graph_arrays.npz` | `a1294c651c7a111439cfc0d0363a9075db69edb8f1c814ae250e50e8dd0ba373` |
| `results/t5_evidence_audit_v1/original_professor_instructions.txt` | `025736da4a1e39b38cb2cce9ea23bf9a09285839abdc862729c3634b4f5be102` |

External eyemap SHA-256: `d127508041073ccb465f36db667f3091e17350f66d7cfd66ddde98ecee94def6`. Its original absolute path is in `config.json`; hashes identify its contents independently of location.

### 15.1 Evidence locator

All current paths below are relative to `results/fixed_neighbor_motion_v1/`:

| Record | Use |
|---|---|
| `config.json`, `plans.json`, `targets.json`, `geometry.json`, `retinal_wiring.npz` | Constants, 47 executions, exact body IDs/positions, wiring/support |
| `prospective_manifest.json`, `preservation_before.json` | Original freeze and predecessor/external hashes |
| `source_registry.json`, `source/*_movie.npz`, `source/*.npz` | Complete movie/source hashes and numerical inputs/outputs |
| `source_analysis.json`, `source_groups.csv`, `source_individual.csv` | Complete 96 groups and 81,474 source rows |
| `source_independent_review.json`, `independent_means.npz`, `source_decision_review.json` | Independent source equation/decision checks |
| `off_axis_descriptive_context.json` | Retained post-analysis c/d limitation |
| `downstream/graph.json`, `graph_arrays.npz`, `chemical_weights.npz`, `gap_weights.npz` | Frozen equations, matrix/node/active-mask identities and source hashes |
| `downstream_registry.json`, `downstream/primary_*.npz` | 28 complete network records |
| `downstream_analysis_v2.json`, `hs_h2_results_v2.csv` | Authoritative full-precision wide-field exports |
| `downstream_analysis.json`, `hs_h2_results.csv` | Preserved older float32-based statistics |
| `downstream_individual.csv` | 54,372 all-network direction rows: four seeds ×13,593 cells |
| `downstream_independent_review.json`, `downstream_label_control.json` | All-trial numerical replay and exact textual-label control |
| `final_checks.json`, `*_amendment.json`, diagnoses, failure/retry logs | Final audit and transparent correction history |
| `method_amendment_snapshots/`, source snapshot JSONs | Executed original/corrected method provenance |
| `tests_initial.log/.xml`, `figures/`, `visual_review.json` | Test/figure evidence |
| `git_checkpoint.json`, `completion.json`, `artifact_index.json` | Version/completion/seal |
| `project_progress_snapshot.md` | Completion-time progress copy; live ledger remains appendable |

The new **professor handoff ZIP** contains this report/TLDR, the full original prompt, relevant earlier reports, frozen configuration and code, corrected helper sources, scalar result tables and review/amendment records, figures, graph arrays/matrices, and a per-file hash manifest. Large raw movie/channel/network trajectories and the external legacy workspace are excluded. Its README names those omissions. A hash manifest detects alterations; it does not itself supply biological truth or off-device preservation.

## 16. Instructions for an LLM or human reviewing this handoff

The report provides sufficient equations, constants, stimulus plans, score definitions, numerical outcomes, and scope limits to critique the main inference without this conversation. Exact individual records, code, and correction evidence are supplied in the archive. Claims that require an omitted raw trajectory or external file should be marked unresolved rather than invented.

Suggested prompt:

```text
Act as a critical computational-neuroscience methods reviewer. Read the attached
technical report, TLDR, original professor instructions, and available source/
configuration/results. Separate (a) implemented facts with saved evidence,
(b) declared modeling assumptions, and (c) untested biological hypotheses.

1. Does the fixed-grid all-channel computation satisfy the label-free image
   interface requirement? Identify the exact data flow and any leakage.
2. Assess whether the specified a/b/c/d output routing and source-chart anchors
   make any subtype/anatomical validation circular. Distinguish a functional
   motion circuit from independent reconstruction of biological direction tuning.
3. Audit equations, initial states, units, boundary support, body-ID mapping,
   ON/OFF ordering, scoring masks/denominators, group vs cell DSI, and the
   5-ms → 10-ms drive → 1-ms RK4 endpoint/midpoint convention.
4. Determine what the numerical references actually verify. Do not treat
   arithmetic replay, repeated pixel positions, or texture seeds as independent
   biological evidence or as proof of downstream timestep convergence.
5. Review every failure/recovery and V1→V2 precision correction. Were source
   trajectories/gates preserved? Flag missing evidence rather than assuming it.
6. Explain the c/d horizontal-texture responses as an open causal question.
   Propose one small discriminating experiment, not an unbounded parameter sweep.
7. Map achievements against the professor's original Route-B task and the later
   narrower functional scope. Identify exactly which stronger claims remain open.
8. If physiological validation is proposed, specify the necessary recordings,
   stimulus/retinotopy alignment, observation model, calibration/held-out split,
   uncertainty treatment, and quantitative readouts. Existing one-cell T5 results
   belong to a different model; do not transfer their validation to this surrogate.
9. State the strongest defensible claim and one next step. A finite negative bank
   does not prove global impossibility; a functional PASS does not establish
   biological degeneracy, novelty, or publication acceptance.

Cite filenames/JSON fields or report sections for each finding. Clearly label
inferences and hypotheses. Do not claim to inspect files that were not supplied.
```

## Appendix A. Complete frozen numerical motion core

The following is the exact content of `src/male_optic_frontend/fixed_neighbor_motion.py`, included so an LLM receiving only this report can inspect initialization, offset construction, order of operations, interpolation, and routing. Its hash is in Section 15. Rendering, experiment scoring, and network loading are separate files in the handoff.

```python
"""Functional retinal motion circuit with explicit, target-independent wiring.

All ON/OFF and horizontal/vertical opponent channels exist at every grid site.
No target identity, tuning label or intended movie motion enters this module.
The model is an algorithmic surrogate, not a fitted T4/T5 membrane-potential model.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy.ndimage import uniform_filter

CHANNELS = ('ON_H_POS', 'ON_H_NEG', 'ON_V_POS', 'ON_V_NEG',
            'OFF_H_POS', 'OFF_H_NEG', 'OFF_V_POS', 'OFF_V_NEG')


@dataclass(frozen=True)
class MotionCircuitConfig:
    delay_tau_s: float = .03
    neighbor_steps: int = 1
    pooling_radius_steps: int = 3
    contrast_baseline: float = .5

    def __post_init__(self):
        if not np.isfinite(self.delay_tau_s) or self.delay_tau_s <= 0:
            raise ValueError('Delay time must be positive')
        for x in (self.neighbor_steps, self.pooling_radius_steps):
            if not isinstance(x, int) or x < 0:
                raise ValueError('Spatial steps must be nonnegative integers')
        if self.neighbor_steps < 1 or self.contrast_baseline != .5:
            raise ValueError('Require nonzero neighbor displacement and neutral .5 baseline')


@dataclass(frozen=True)
class RetinalGrid:
    horizontal_deg: np.ndarray
    elevation_deg: np.ndarray

    def __post_init__(self):
        for name in ('horizontal_deg', 'elevation_deg'):
            axis = np.array(getattr(self, name), dtype=float, copy=True)
            if axis.ndim != 1 or len(axis) < 3 or not np.isfinite(axis).all() or not np.all(np.diff(axis) > 0):
                raise ValueError('Retinal axes must be finite increasing vectors')
            if not np.allclose(np.diff(axis), np.diff(axis)[0], rtol=0, atol=1e-12):
                raise ValueError('Require a regular grid')
            axis.setflags(write=False)
            object.__setattr__(self, name, axis)

    @property
    def shape(self):
        return len(self.elevation_deg), len(self.horizontal_deg)

    @property
    def xy(self):
        h, e = np.meshgrid(self.horizontal_deg, self.elevation_deg)
        return np.column_stack((h.ravel(), e.ravel()))

    def valid_mask(self, config):
        border = config.neighbor_steps + config.pooling_radius_steps
        mask = np.zeros(self.shape, bool)
        if min(self.shape) <= 2*border:
            raise ValueError('Grid too small for complete neighbor/pooling support')
        mask[border:-border, border:-border] = True
        return mask


def contrasts(luminance):
    value = np.asarray(luminance, dtype=float)
    if not np.isfinite(value).all() or np.any((value < 0) | (value > 1)):
        raise ValueError('Luminance must be finite within [0,1]')
    return np.stack((np.maximum(2*value-1, 0), np.maximum(1-2*value, 0)))


def opponent_fields(current, delayed, config):
    """Multiplication and subtraction on fixed pairs centered at each site.

    Positive horizontal is increasing eye-horizontal; positive vertical is
    increasing eye-elevation. Symmetric branches differ only in fixed wiring.
    """
    if current.shape != delayed.shape or current.ndim != 3 or current.shape[0] != 2:
        raise ValueError('Require two contrast families on the same retinal grid')
    d = config.neighbor_steps
    result = np.zeros((2, 2, *current.shape[1:]), float)
    result[:, 0, :, d:-d] = (delayed[:, :, :-2*d]*current[:, :, 2*d:] -
                             delayed[:, :, 2*d:]*current[:, :, :-2*d])
    result[:, 1, d:-d, :] = (delayed[:, :-2*d, :]*current[:, 2*d:, :] -
                             delayed[:, 2*d:, :]*current[:, :-2*d, :])
    width = 2*config.pooling_radius_steps+1
    # Pool signed signals before rectification. No padding contributes at valid sites.
    return uniform_filter(result, size=(1, 1, width, width), mode='constant', cval=0.)


def rectified_channels(opponent):
    values = np.stack((np.maximum(opponent[:, 0], 0), np.maximum(-opponent[:, 0], 0),
                       np.maximum(opponent[:, 1], 0), np.maximum(-opponent[:, 1], 0)), axis=1)
    return values.reshape(8, *opponent.shape[2:])


@dataclass(frozen=True)
class GridReadout:
    """Spatial sampling of ALL channels, using coordinates only."""
    vertices: np.ndarray
    weights: np.ndarray

    @classmethod
    def at_locations(cls, grid, xy, config):
        xy = np.asarray(xy, dtype=float)
        if xy.ndim != 2 or xy.shape[1] != 2 or not np.isfinite(xy).all():
            raise ValueError('Locations must have shape (position,2)')
        x = (xy[:, 0]-grid.horizontal_deg[0])/np.diff(grid.horizontal_deg)[0]
        y = (xy[:, 1]-grid.elevation_deg[0])/np.diff(grid.elevation_deg)[0]
        ix, iy = np.floor(x).astype(int), np.floor(y).astype(int)
        nx, ny = len(grid.horizontal_deg), len(grid.elevation_deg)
        if np.any((ix < 0) | (ix >= nx-1) | (iy < 0) | (iy >= ny-1)):
            raise ValueError('Readout lies outside grid')
        vertices = np.stack((iy*nx+ix, iy*nx+ix+1, (iy+1)*nx+ix, (iy+1)*nx+ix+1), axis=1)
        if not np.all(grid.valid_mask(config).ravel()[vertices]):
            raise ValueError('Readout lacks complete spatial circuit support')
        ax, ay = x-ix, y-iy
        weights = np.stack(((1-ax)*(1-ay), ax*(1-ay), (1-ax)*ay, ax*ay), axis=1)
        vertices.setflags(write=False); weights.setflags(write=False)
        return cls(vertices, weights)

    def sample(self, fields):
        a = np.asarray(fields)
        return np.sum(a.reshape(*a.shape[:-2], -1)[..., self.vertices]*self.weights, axis=-1)


def simulate_retina(luminance, time_s, grid, locations_eye_deg, config=None, *, probe_locations=None):
    """Return every channel at every requested position, from unlabeled numbers.

    Initial filter state is the equilibrium for the first stationary image.
    A sample at t reads the filter state propagated over the preceding hold.
    The current sample is never used to update a past state.
    """
    config = config or MotionCircuitConfig()
    time = np.asarray(time_s, dtype=float)
    image = np.asarray(luminance)
    if image.shape != (len(time), *grid.shape) or not np.isfinite(time).all() or len(time) < 2 or np.any(np.diff(time) <= 0):
        raise ValueError('Input grid/time mismatch')
    readout = GridReadout.at_locations(grid, locations_eye_deg, config)
    probe = GridReadout.at_locations(grid, probe_locations, config) if probe_locations is not None else None
    activity = np.empty((len(time), 8, len(readout.vertices)), np.float32)
    probes = np.empty((len(time), 8, len(probe.vertices)), np.float32) if probe is not None else None
    pooled = np.empty((len(time), 8), float)
    state = contrasts(image[0])
    previous = state.copy()
    valid = grid.valid_mask(config)
    for n, frame in enumerate(image):
        if n:
            alpha = -np.expm1(-(time[n]-time[n-1])/config.delay_tau_s)
            state += alpha*(previous-state)
        current = contrasts(frame)
        channels = rectified_channels(opponent_fields(current, state, config))
        if np.any(channels > 1+1e-12) or not np.isfinite(channels).all():
            raise FloatingPointError('Invalid circuit activity')
        activity[n] = readout.sample(channels)
        if probe is not None: probes[n] = probe.sample(channels)
        pooled[n] = channels[:, valid].mean(axis=1)
        previous = current
    return dict(time_s=time.copy(), all_channels=activity, pooled_channels=pooled,
                probes=probes, final_delay_state=state, initial_delay_state=contrasts(image[0]))


def route_channels(all_channels, channel_indices):
    """Fixed output wiring, applied after every channel has been computed."""
    values = np.asarray(all_channels)
    indices = np.asarray(channel_indices)
    if values.ndim != 3 or values.shape[1] != 8 or indices.shape != (values.shape[2],) or indices.dtype.kind not in 'iu' or np.any((indices < 0) | (indices >= 8)):
        raise ValueError('Invalid channel routing')
    return values[:, indices, np.arange(len(indices))]
```

## Appendix B. All source group results

Values below are copied from the saved 96-row source group table and rounded only for presentation. “Expected %” applies to horizontal a/b groups. `n/a` for c/d is not an acceptance pass. Selective % counts the three numerical floors regardless of physical sign. Mean DSI averages per-cell signed global DSIs. Full-precision per-cell/group values remain in the CSV/JSON.

| Benchmark | Eye | Slot | n | Mean R+ | Mean R− | Mean DSI | Selective % | Expected % |
|---|---|---|---|---|---|---|---|---|
| seed_42 | L | T4a | 835 | 2.27750049e-05 | 0.0958853883 | -0.999506 | 100.0000 | 100.0000 |
| seed_42 | L | T4b | 844 | 0.0913311107 | 2.33392585e-05 | 0.999422 | 100.0000 | 100.0000 |
| seed_42 | L | T4c | 895 | 0.0123648874 | 0.0105216024 | 0.112370 | 83.9106 | n/a |
| seed_42 | L | T4d | 850 | 0.0106896071 | 0.0127219101 | -0.132281 | 85.6471 | n/a |
| seed_42 | L | T5a | 825 | 1.83816284e-05 | 0.0955228606 | -0.999600 | 100.0000 | 100.0000 |
| seed_42 | L | T5b | 863 | 0.0926535413 | 2.13355634e-05 | 0.999498 | 100.0000 | 100.0000 |
| seed_42 | L | T5c | 862 | 0.0127314659 | 0.0101236384 | 0.086464 | 87.5870 | n/a |
| seed_42 | L | T5d | 812 | 0.0116019666 | 0.0136905605 | -0.089758 | 87.8079 | n/a |
| seed_42 | R | T4a | 849 | 0.0921491753 | 2.0433743e-05 | 0.999476 | 100.0000 | 100.0000 |
| seed_42 | R | T4b | 846 | 2.59417621e-05 | 0.0906062828 | -0.999336 | 99.8818 | 99.8818 |
| seed_42 | R | T4c | 883 | 0.00995788377 | 0.0109849088 | -0.020215 | 85.2775 | n/a |
| seed_42 | R | T4d | 859 | 0.00790192587 | 0.00940224127 | -0.107491 | 83.9348 | n/a |
| seed_42 | R | T5a | 838 | 0.0980244274 | 1.94472117e-05 | 0.999571 | 100.0000 | 100.0000 |
| seed_42 | R | T5b | 852 | 2.22592038e-05 | 0.0941960266 | -0.999492 | 100.0000 | 100.0000 |
| seed_42 | R | T5c | 858 | 0.015848688 | 0.0122336642 | 0.127945 | 85.0816 | n/a |
| seed_42 | R | T5d | 808 | 0.012765821 | 0.0145700047 | -0.096138 | 85.7673 | n/a |
| seed_78201 | L | T4a | 835 | 2.15044536e-05 | 0.0928902025 | -0.999512 | 100.0000 | 100.0000 |
| seed_78201 | L | T4b | 844 | 0.0916620615 | 2.27196953e-05 | 0.999471 | 100.0000 | 100.0000 |
| seed_78201 | L | T4c | 895 | 0.013218193 | 0.0117639508 | 0.093750 | 87.0391 | n/a |
| seed_78201 | L | T4d | 850 | 0.0129570285 | 0.0136716515 | -0.009084 | 84.0000 | n/a |
| seed_78201 | L | T5a | 825 | 1.87282263e-05 | 0.0933369492 | -0.999564 | 100.0000 | 100.0000 |
| seed_78201 | L | T5b | 863 | 0.0898435243 | 2.25744714e-05 | 0.999455 | 100.0000 | 100.0000 |
| seed_78201 | L | T5c | 862 | 0.0114248895 | 0.0104056727 | 0.078210 | 86.3109 | n/a |
| seed_78201 | L | T5d | 812 | 0.00993080179 | 0.0123013686 | -0.072325 | 86.8227 | n/a |
| seed_78201 | R | T4a | 849 | 0.0999840385 | 2.15239527e-05 | 0.999523 | 100.0000 | 100.0000 |
| seed_78201 | R | T4b | 846 | 2.68940131e-05 | 0.094418681 | -0.999354 | 100.0000 | 100.0000 |
| seed_78201 | R | T4c | 883 | 0.0127390385 | 0.0140060051 | -0.074087 | 85.7305 | n/a |
| seed_78201 | R | T4d | 859 | 0.0121603517 | 0.0118245079 | -0.000464 | 84.7497 | n/a |
| seed_78201 | R | T5a | 838 | 0.0993485684 | 2.65547963e-05 | 0.999404 | 100.0000 | 100.0000 |
| seed_78201 | R | T5b | 852 | 2.79812898e-05 | 0.091612631 | -0.999280 | 100.0000 | 100.0000 |
| seed_78201 | R | T5c | 858 | 0.0110094024 | 0.0114430758 | 0.020922 | 86.2471 | n/a |
| seed_78201 | R | T5d | 808 | 0.0113793279 | 0.00846090762 | 0.122517 | 86.8812 | n/a |
| seed_78202 | L | T4a | 835 | 2.01435893e-05 | 0.091057287 | -0.999495 | 100.0000 | 100.0000 |
| seed_78202 | L | T4b | 844 | 0.0910131632 | 1.89140499e-05 | 0.999533 | 100.0000 | 100.0000 |
| seed_78202 | L | T4c | 895 | 0.00972799483 | 0.0116592328 | -0.099186 | 84.5810 | n/a |
| seed_78202 | L | T4d | 850 | 0.0122428721 | 0.010570012 | 0.071208 | 87.0588 | n/a |
| seed_78202 | L | T5a | 825 | 2.31958367e-05 | 0.0925809568 | -0.999421 | 100.0000 | 100.0000 |
| seed_78202 | L | T5b | 863 | 0.0931488982 | 2.41461441e-05 | 0.999442 | 100.0000 | 100.0000 |
| seed_78202 | L | T5c | 862 | 0.0118164658 | 0.0126293317 | -0.013099 | 87.1230 | n/a |
| seed_78202 | L | T5d | 812 | 0.0138015527 | 0.0115484423 | 0.082403 | 84.2365 | n/a |
| seed_78202 | R | T4a | 849 | 0.090821305 | 2.09777945e-05 | 0.999513 | 100.0000 | 100.0000 |
| seed_78202 | R | T4b | 846 | 2.08611021e-05 | 0.0887108167 | -0.999501 | 100.0000 | 100.0000 |
| seed_78202 | R | T4c | 883 | 0.0118377396 | 0.0119960638 | -0.009448 | 86.8630 | n/a |
| seed_78202 | R | T4d | 859 | 0.0119497073 | 0.0119761598 | -0.044687 | 87.1944 | n/a |
| seed_78202 | R | T5a | 838 | 0.0901401606 | 2.10901958e-05 | 0.999447 | 100.0000 | 100.0000 |
| seed_78202 | R | T5b | 852 | 2.21257409e-05 | 0.0890483389 | -0.999491 | 100.0000 | 100.0000 |
| seed_78202 | R | T5c | 858 | 0.0111713056 | 0.0119865478 | -0.057662 | 88.3450 | n/a |
| seed_78202 | R | T5d | 808 | 0.0105219193 | 0.0120175328 | -0.034504 | 88.2426 | n/a |
| seed_78203 | L | T4a | 835 | 2.38000813e-05 | 0.0928880234 | -0.999357 | 100.0000 | 100.0000 |
| seed_78203 | L | T4b | 844 | 0.0877582403 | 2.62224842e-05 | 0.999035 | 99.8815 | 99.8815 |
| seed_78203 | L | T4c | 895 | 0.011041371 | 0.0113091582 | -0.050965 | 89.1620 | n/a |
| seed_78203 | L | T4d | 850 | 0.0104886979 | 0.0105637354 | 0.002675 | 82.0000 | n/a |
| seed_78203 | L | T5a | 825 | 2.06697112e-05 | 0.0932929999 | -0.999508 | 100.0000 | 100.0000 |
| seed_78203 | L | T5b | 863 | 0.0906030763 | 2.54513308e-05 | 0.999391 | 100.0000 | 100.0000 |
| seed_78203 | L | T5c | 862 | 0.0125598722 | 0.0134595334 | -0.042111 | 85.6148 | n/a |
| seed_78203 | L | T5d | 812 | 0.0137848621 | 0.010295808 | 0.128345 | 83.9901 | n/a |
| seed_78203 | R | T4a | 849 | 0.0959899504 | 1.95958696e-05 | 0.999491 | 100.0000 | 100.0000 |
| seed_78203 | R | T4b | 846 | 2.4411724e-05 | 0.0898422099 | -0.999392 | 100.0000 | 100.0000 |
| seed_78203 | R | T4c | 883 | 0.0109637227 | 0.0120043565 | -0.057044 | 84.0317 | n/a |
| seed_78203 | R | T4d | 859 | 0.0111267182 | 0.0111228777 | -0.002464 | 89.6391 | n/a |
| seed_78203 | R | T5a | 838 | 0.0963107278 | 2.23105609e-05 | 0.999469 | 100.0000 | 100.0000 |
| seed_78203 | R | T5b | 852 | 2.5419021e-05 | 0.0899007814 | -0.999365 | 100.0000 | 100.0000 |
| seed_78203 | R | T5c | 858 | 0.0109356251 | 0.0138693471 | -0.074960 | 86.8298 | n/a |
| seed_78203 | R | T5d | 808 | 0.0138296503 | 0.0102563729 | 0.141194 | 82.0545 | n/a |
| speed_30 | L | T4a | 835 | 2.38126709e-07 | 0.0708806925 | -0.999991 | 100.0000 | 100.0000 |
| speed_30 | L | T4b | 844 | 0.0656136143 | 2.94314616e-07 | 0.998800 | 99.8815 | 99.8815 |
| speed_30 | L | T4c | 895 | 0.00525164051 | 0.00583592162 | -0.017225 | 77.2067 | n/a |
| speed_30 | L | T4d | 850 | 0.00600968202 | 0.00573255271 | -0.029195 | 75.0588 | n/a |
| speed_30 | L | T5a | 825 | 1.99313715e-07 | 0.0721663472 | -0.997571 | 99.6364 | 99.6364 |
| speed_30 | L | T5b | 863 | 0.0672899031 | 2.08849998e-07 | 0.999992 | 99.8841 | 99.8841 |
| speed_30 | L | T5c | 862 | 0.00662543641 | 0.00662161643 | 0.003386 | 77.2622 | n/a |
| speed_30 | L | T5d | 812 | 0.00739519257 | 0.00696088363 | -0.024316 | 79.1872 | n/a |
| speed_30 | R | T4a | 849 | 0.0681171128 | 2.43385546e-07 | 0.999991 | 100.0000 | 100.0000 |
| speed_30 | R | T4b | 846 | 2.72606012e-07 | 0.0673998326 | -0.999831 | 99.7636 | 99.7636 |
| speed_30 | R | T4c | 883 | 0.00581171056 | 0.00538113327 | 0.020126 | 77.5764 | n/a |
| speed_30 | R | T4d | 859 | 0.00477229206 | 0.00598419265 | -0.101647 | 77.2992 | n/a |
| speed_30 | R | T5a | 838 | 0.0690521987 | 2.28198789e-07 | 0.999991 | 100.0000 | 100.0000 |
| speed_30 | R | T5b | 852 | 2.30251123e-07 | 0.0695897898 | -0.999990 | 99.8826 | 99.8826 |
| speed_30 | R | T5c | 858 | 0.00700428893 | 0.00710222794 | 0.023066 | 84.4988 | n/a |
| speed_30 | R | T5d | 808 | 0.00666705204 | 0.00677078601 | -0.021916 | 79.0842 | n/a |
| speed_90 | L | T4a | 835 | 0.000176473023 | 0.0999794291 | -0.996255 | 100.0000 | 100.0000 |
| speed_90 | L | T4b | 844 | 0.0947714777 | 0.00020587981 | 0.995169 | 100.0000 | 100.0000 |
| speed_90 | L | T4c | 895 | 0.0129421178 | 0.0136043878 | -0.030444 | 84.6927 | n/a |
| speed_90 | L | T4d | 850 | 0.0133875605 | 0.0130732181 | -0.029605 | 85.2941 | n/a |
| speed_90 | L | T5a | 825 | 0.000148283897 | 0.100879871 | -0.996859 | 100.0000 | 100.0000 |
| speed_90 | L | T5b | 863 | 0.0966170341 | 0.000172395723 | 0.996297 | 100.0000 | 100.0000 |
| speed_90 | L | T5c | 862 | 0.0152503506 | 0.0160287468 | -0.008274 | 87.0070 | n/a |
| speed_90 | L | T5d | 812 | 0.0168629477 | 0.0151606075 | 0.042161 | 86.6995 | n/a |
| speed_90 | R | T4a | 849 | 0.0984747458 | 0.000185336827 | 0.996028 | 100.0000 | 100.0000 |
| speed_90 | R | T4b | 846 | 0.00019765594 | 0.100478127 | -0.995936 | 100.0000 | 100.0000 |
| speed_90 | R | T4c | 883 | 0.0128209864 | 0.0138615178 | -0.069779 | 85.1642 | n/a |
| speed_90 | R | T4d | 859 | 0.0120003627 | 0.0139784346 | -0.073541 | 84.9825 | n/a |
| speed_90 | R | T5a | 838 | 0.0999978419 | 0.000200121307 | 0.995776 | 100.0000 | 100.0000 |
| speed_90 | R | T5b | 852 | 0.000195629014 | 0.101439923 | -0.995956 | 100.0000 | 100.0000 |
| speed_90 | R | T5c | 858 | 0.0159128455 | 0.0161267862 | 0.015118 | 81.9347 | n/a |
| speed_90 | R | T5d | 808 | 0.0151353074 | 0.0149538425 | -0.011757 | 82.5495 | n/a |

## Appendix C. All cardinal grating comparisons and sampling checks

The four mean columns are +H, −H, +V, −V within the listed ON/OFF family, spatially averaged over valid retinal grid sites. The DSI compares the physically expected channel to its opponent. These pooled controls are not per-anatomical-cell four-direction tuning curves.

| World angle | Eye | Family | +H | −H | +V | −V | Opponent DSI | Pass |
|---|---|---|---|---|---|---|---|---|
| 0 | L | ON | 3.35226301e-06 | 0.0729431711 | 0 | 0 | 0.999908090 | True |
| 0 | L | OFF | 3.38577727e-06 | 0.0726683008 | 0 | 0 | 0.999906820 | True |
| 0 | R | ON | 0.0726212769 | 3.38151246e-06 | 0 | 0 | 0.999906877 | True |
| 0 | R | OFF | 0.0730581285 | 3.35255378e-06 | 0 | 0 | 0.999908226 | True |
| 90 | L | ON | 0 | 0 | 0.0728677616 | 3.35256219e-06 | 0.999907987 | True |
| 90 | L | OFF | 0 | 0 | 0.0726983757 | 3.35319045e-06 | 0.999907755 | True |
| 90 | R | ON | 0 | 0 | 0.0728677616 | 3.35256219e-06 | 0.999907987 | True |
| 90 | R | OFF | 0 | 0 | 0.0726983757 | 3.35319045e-06 | 0.999907755 | True |
| 180 | L | ON | 0.0726212769 | 3.38151246e-06 | 0 | 0 | 0.999906877 | True |
| 180 | L | OFF | 0.0730581285 | 3.35255378e-06 | 0 | 0 | 0.999908226 | True |
| 180 | R | ON | 3.35226301e-06 | 0.0729431711 | 0 | 0 | 0.999908090 | True |
| 180 | R | OFF | 3.38577727e-06 | 0.0726683008 | 0 | 0 | 0.999906820 | True |
| 270 | L | ON | 0 | 0 | 3.35256219e-06 | 0.0728677616 | 0.999907987 | True |
| 270 | L | OFF | 0 | 0 | 3.35319045e-06 | 0.0726983757 | 0.999907755 | True |
| 270 | R | ON | 0 | 0 | 3.35256219e-06 | 0.0728677616 | 0.999907987 | True |
| 270 | R | OFF | 0 | 0 | 3.35319045e-06 | 0.0726983757 | 0.999907755 | True |

| Eye | Compared group/control | Largest relative response change | DSI change | Pass |
|---|---|---|---|---|
| L | T4a | 4.055036% | 5.4216968e-05 | True |
| L | T4b | 4.070068% | 5.25676681e-05 | True |
| L | T5a | 4.058141% | 4.23630119e-05 | True |
| L | T5b | 4.071138% | 4.86191057e-05 | True |
| R | T4a | 4.078303% | 3.9807127e-05 | True |
| R | T4b | 4.077047% | 6.23923367e-05 | True |
| R | T5a | 4.065055% | 5.39993334e-05 | True |
| R | T5b | 4.092612% | 6.60924734e-05 | True |
| BOTH | grating_0 | 4.100949% | 1.9083471e-06 | True |
| BOTH | grating_90 | 4.098460% | 1.87477282e-06 | True |
| BOTH | grating_180 | 4.100949% | 1.9083471e-06 | True |
| BOTH | grating_270 | 4.098460% | 1.87477282e-06 | True |

## Appendix D. Original deliverables and predecessor evidence

The original fourteen named outputs reside in `results/postfix_horizontal_execution_v2/`. Their complete audit is [POSTFIX_COMPLETION_AUDIT_V1.md](POSTFIX_COMPLETION_AUDIT_V1.md), and their separate hash index is `results/postfix_completion_v3/final_bundle_index_v2.json`. All were retained by the later evidence audit:

```text
VISUAL_COORDINATE_REGISTRATION.md
MOTION_COMPUTATION_ARCHITECTURE.md
ANTI_DIRECTION_LEAKAGE_AUDIT.md
postfix_horizontal_config.json
postfix_horizontal_trajectories.npz
t4t5_direction_summary.csv
hs_h2_direction_summary.csv
side_resolved_summary.csv
coordinate_mapping.png
t4t5_direction_responses.png
hs_h2_direction_responses.png
stimulus_preview.png
run_manifest.json
POSTFIX_HORIZONTAL_REPORT.md
```

The archived smoke-test interpretation is: “The original frontend smoke experiment established software-level propagation from an image-derived direction-coded T4/T5 drive to HS/H2. It is superseded for mechanistic interpretation because direction selectivity was constructed in the frontend and bilateral visual coordinates had not yet been anatomically registered.” This wording is from the project assignment, not a quote from a published paper.

Important prior reports:

- [Horizontal random-square technical report](HORIZONTAL_RANDOM_SQUARES_TECHNICAL_REPORT_V1.md).
- [Postfix initialization completion audit](POSTFIX_INITIALIZATION_COMPLETION_AUDIT_V1.md).
- [Physiology integration source gate](PHYSIOLOGY_INTEGRATION_SOURCE_GATE_REPORT_V1.md), [T5 source error investigation](T5_REFERENCE_ERROR_INVESTIGATION_REPORT_V1.md).
- [Physiological population prototype](PHYSIOLOGICAL_PROTOTYPE_EXECUTION_REPORT_V1.md), [texture replication](PHYSIOLOGICAL_TEXTURE_REPLICATION_REPORT_V1.md), [causal clamp repair](PHYSIOLOGICAL_IMAGE_CLAMP_REPAIR_REPORT_V1.md).
- [Matched T5 grating observations](T5_MATCHED_GRATING_OBSERVATION_REPORT_V1.md), [image/native grating transfer](T5_IMAGE_NATIVE_TRANSFER_REPORT_V1.md), [moving-bar transfer](T5_MOVING_BAR_TRANSFER_REPORT_V1.md).
- [Parameter pilot](T5_MIXED_PARAMETER_SENSITIVITY_REPORT_V1.md), [compensation challenge](T5_COMPENSATION_CHALLENGE_REPORT_V1.md), [active sensitivity](T5_ACTIVE_SENSITIVITY_REPORT_V1.md), [evidence audit](T5_EVIDENCE_AUDIT_REPORT_V1.md).
- [Current frozen protocol](FIXED_NEIGHBOR_MOTION_PROTOCOL_V1.md), [architecture](FIXED_NEIGHBOR_MOTION_ARCHITECTURE_V1.md), [original current-study report](FIXED_NEIGHBOR_MOTION_REPORT_V1.md), [reproduction notes](FIXED_NEIGHBOR_MOTION_REPRODUCTION_V1.md).

| Preserved index | Entries verified | SHA-256 |
|---|---|---|
| `results/physiological_execution_artifact_index_v1.json` | 8418 | `c70985904cb48dcbd2260475a8f73897ba721592950dfc5e103c0a2c115e6235` |
| `results/physiological_texture_replication_v1/artifact_index.json` | 427 | `fe7b1841edea2af6782eadddbcba5ece0b91bc4acf826e02778143ab8db53597` |
| `results/physiological_grating_readout_comparison_v1/artifact_index.json` | 46 | `b95a441b83c36489ec5c99ad4cacc18e2d0147e03082a683727033393807a0a9` |
| `results/physiological_image_clamp_repair_v1/artifact_index.json` | 1157 | `efceaf13e7aa66514956bfc90c1c60def3b4174f0c19f3306b9bb735d55396a6` |
| `results/t5_matched_grating_observation_v1/artifact_index.json` | 57 | `74aec37ffe65659f94827e970cd814a33f711462e6e34c0e1c0e99f594c6fe91` |
| `results/t5_image_native_transfer_v1/artifact_index.json` | 653 | `3f82daafd9c73e3ce9b7eff2e6cfe07b69ec99e248b873176f5b9f6d0a1acace` |
| `results/t5_moving_bar_transfer_v1/artifact_index.json` | 1328 | `e941840acae4832704539a7e2c115dfba7d856172e62f3101222d7f6e525897e` |
| `results/t5_mixed_parameter_sensitivity_v1/artifact_index.json` | 171 | `4169e8dec771bb29ec3abfc0f3cec193bd9c014eed7ed0e9ce273e0e01c6c0b6` |
| `results/t5_compensation_challenge_v1/artifact_index.json` | 49 | `e7d5c50f0c5964347b5ec14848d57d65d5c1ea99c51c6b3beacba0332824b6be` |
| `results/t5_active_sensitivity_v1/artifact_index.json` | 174 | `842b1c9961555770a70fa164f85ae242f1c6be140f5861b75de40ca5e59ebb71` |
| `results/t5_evidence_audit_v1/artifact_index.json` | 36 | `1ce90857cfa8e2ae8d916dc960174d1b532cbd86151231faf4cc21381b28c2e0` |

## Appendix E. All HS/H2 condition means and direction comparisons

Authoritative source: `downstream_analysis_v2.json` / `hs_h2_results_v2.csv`, from unchanged float64 HS/H2 traces with compensated sums. All STATIC means are exactly zero. Columns G+/G−, L+/L−, R+/R− are **world-coordinate physical conditions**, not eye-coordinate directions. DSI is global signed DSI. All listed rows pass global selectivity/sign, ipsilateral contrast sign, and STATIC stability. Values are rounded for readability; CSV/JSON retain precision.

| Seed | Body ID | Type | Ref. eye | G+ | G− | L+ | L− | R+ | R− | Global DSI | Ipsilateral +−contrast |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 42 | 10019 | H2 | L | 0.0838633722 | 0.0218800552 | 0.0838618216 | 0.0218570135 | -9.40943279e-06 | -1.74468291e-05 | 0.586167 | 0.062004808 |
| 42 | 10025 | H2 | R | 0.0224210672 | 0.0882948131 | -1.06425902e-05 | 4.01111508e-06 | 0.0223840438 | 0.0882832733 | -0.594980 | -0.0658992295 |
| 42 | 10015 | HSN | R | 0.0929105424 | 0.0217382158 | -2.2393031e-05 | -8.32145409e-05 | 0.0928005264 | 0.0218211296 | 0.620786 | 0.0709793969 |
| 42 | 10016 | HSE | R | 0.0888901451 | 0.0227420679 | -2.68375658e-05 | -9.97478148e-05 | 0.0888075588 | 0.0228414161 | 0.592554 | 0.0659661427 |
| 42 | 10023 | HSS | R | 0.0888845126 | 0.021520582 | 5.11570784e-06 | 1.24065697e-06 | 0.0885355853 | 0.0215181627 | 0.610152 | 0.0670174226 |
| 42 | 10034 | HSE | L | 0.0229197624 | 0.0813820378 | 0.0229606484 | 0.0812022629 | -4.60126809e-05 | 1.83053894e-06 | -0.560511 | -0.0582416145 |
| 42 | 10181 | HSN | L | 0.0225511882 | 0.0819162707 | 0.0226382709 | 0.0818932838 | -8.93481045e-05 | -1.68077838e-05 | -0.568264 | -0.0592550129 |
| 42 | 10419 | HSS | L | 0.0229214362 | 0.087286987 | 0.0229147103 | 0.0869949479 | 2.66301069e-06 | 1.32074751e-05 | -0.584035 | -0.0640802376 |
| 42 | 11793 | HST | L | 0.0227179683 | 0.0832995299 | 0.0227047472 | 0.0831176557 | 9.52964053e-06 | 3.85239134e-05 | -0.571430 | -0.0604129085 |
| 42 | 12521 | HST | R | 0.0921859902 | 0.02216309 | 2.41386379e-05 | 6.00995264e-06 | 0.0920025729 | 0.0221564815 | 0.612361 | 0.0698460914 |
| 78201 | 10019 | H2 | L | 0.0839217109 | 0.0218125874 | 0.0839233144 | 0.0217908374 | -9.71437939e-06 | -1.77042872e-05 | 0.587408 | 0.062132477 |
| 78201 | 10025 | H2 | R | 0.0231830537 | 0.089388738 | -1.06200111e-05 | 3.87796071e-06 | 0.0231412002 | 0.0893817704 | -0.588120 | -0.0662405702 |
| 78201 | 10015 | HSN | R | 0.095385584 | 0.0219662743 | -2.2573299e-05 | -8.17895929e-05 | 0.095260564 | 0.0220485174 | 0.625634 | 0.0732120467 |
| 78201 | 10016 | HSE | R | 0.0897640017 | 0.0235223816 | -2.70536478e-05 | -9.80397025e-05 | 0.0896648499 | 0.0236205362 | 0.584727 | 0.0660443137 |
| 78201 | 10023 | HSS | R | 0.0921818565 | 0.0213710332 | 5.12006187e-06 | 1.2386024e-06 | 0.0917759313 | 0.0213701212 | 0.623593 | 0.0704058101 |
| 78201 | 10034 | HSE | L | 0.0233711323 | 0.0808939857 | 0.023415618 | 0.0807268744 | -4.670954e-05 | 1.72744767e-06 | -0.551698 | -0.0573112564 |
| 78201 | 10181 | HSN | L | 0.0230928266 | 0.0845366281 | 0.0231829103 | 0.0845138406 | -9.07971395e-05 | -1.72757391e-05 | -0.570883 | -0.0613309303 |
| 78201 | 10419 | HSS | L | 0.0222652553 | 0.0812352559 | 0.0222591561 | 0.0809630477 | 2.76778501e-06 | 1.33936376e-05 | -0.569756 | -0.0587038916 |
| 78201 | 11793 | HST | L | 0.0230860129 | 0.0826177954 | 0.0230741817 | 0.0824448799 | 9.86243513e-06 | 3.9061002e-05 | -0.563194 | -0.0593706981 |
| 78201 | 12521 | HST | R | 0.0931938292 | 0.0227885764 | 2.41594981e-05 | 5.99738083e-06 | 0.0929857518 | 0.0227827277 | 0.607034 | 0.0702030242 |
| 78202 | 10019 | H2 | L | 0.0833532826 | 0.0212769516 | 0.0833512782 | 0.0212573232 | -8.8445827e-06 | -1.63609396e-05 | 0.593292 | 0.062093955 |
| 78202 | 10025 | H2 | R | 0.0210311374 | 0.0831477529 | -1.05469593e-05 | 3.78898968e-06 | 0.0209999213 | 0.0831378315 | -0.596250 | -0.0621379102 |
| 78202 | 10015 | HSN | R | 0.0874685718 | 0.0198213621 | -2.25874994e-05 | -8.00677099e-05 | 0.0873799534 | 0.0199019899 | 0.630508 | 0.0674779636 |
| 78202 | 10016 | HSE | R | 0.0817157924 | 0.0217789509 | -2.7070675e-05 | -9.59764104e-05 | 0.0816489189 | 0.0218746921 | 0.579129 | 0.0597742269 |
| 78202 | 10023 | HSS | R | 0.081193001 | 0.0207425427 | 5.08217726e-06 | 1.20874844e-06 | 0.0808955771 | 0.020739801 | 0.593026 | 0.0601557761 |
| 78202 | 10034 | HSE | L | 0.0230095578 | 0.0792041794 | 0.0230464271 | 0.0790530743 | -4.25724527e-05 | 1.62812471e-06 | -0.549776 | -0.0560066472 |
| 78202 | 10181 | HSN | L | 0.0225842262 | 0.083604192 | 0.0226652374 | 0.0835854785 | -8.27350727e-05 | -1.59903797e-05 | -0.574639 | -0.0609202411 |
| 78202 | 10419 | HSS | L | 0.0233582463 | 0.0785954477 | 0.0233461363 | 0.0783447213 | 2.50919175e-06 | 1.24229019e-05 | -0.541787 | -0.054998585 |
| 78202 | 11793 | HST | L | 0.0229134689 | 0.0804618541 | 0.0228993571 | 0.0803056635 | 8.94900529e-06 | 3.62445442e-05 | -0.556694 | -0.0574063064 |
| 78202 | 12521 | HST | R | 0.0855755179 | 0.0210939992 | 2.39810632e-05 | 5.85437831e-06 | 0.0854151652 | 0.0210877148 | 0.604498 | 0.0643274504 |
| 78203 | 10019 | H2 | L | 0.0827559973 | 0.0215047969 | 0.0827563576 | 0.0214783345 | -9.05224657e-06 | -1.69450067e-05 | 0.587481 | 0.0612780231 |
| 78203 | 10025 | H2 | R | 0.0224052102 | 0.085648278 | -1.04836075e-05 | 4.42405633e-06 | 0.0223635011 | 0.0856378204 | -0.585294 | -0.0632743192 |
| 78203 | 10015 | HSN | R | 0.0858327019 | 0.0207475831 | -2.22249601e-05 | -8.39313744e-05 | 0.0857121798 | 0.0208322808 | 0.610668 | 0.0648798989 |
| 78203 | 10016 | HSE | R | 0.0872270773 | 0.0222515392 | -2.6636185e-05 | -0.000100607043 | 0.0871337449 | 0.0223514819 | 0.593500 | 0.0647822629 |
| 78203 | 10023 | HSS | R | 0.0953143228 | 0.0221964573 | 5.05225771e-06 | 1.21718823e-06 | 0.0949193575 | 0.0221921428 | 0.622223 | 0.0727272147 |
| 78203 | 10034 | HSE | L | 0.0230202829 | 0.0837076871 | 0.0230618646 | 0.083522938 | -4.49901928e-05 | 1.61590108e-06 | -0.568618 | -0.0604610734 |
| 78203 | 10181 | HSN | L | 0.0225613751 | 0.0790670459 | 0.0226475566 | 0.0790472543 | -8.74972223e-05 | -1.66190388e-05 | -0.556003 | -0.0563996977 |
| 78203 | 10419 | HSS | L | 0.0224706483 | 0.0898865247 | 0.0224630144 | 0.0895460389 | 2.67591314e-06 | 1.28242198e-05 | -0.600014 | -0.0670830246 |
| 78203 | 11793 | HST | L | 0.0225126022 | 0.0835685441 | 0.0224999316 | 0.0833820994 | 9.52856888e-06 | 3.74058743e-05 | -0.575559 | -0.0608821678 |
| 78203 | 12521 | HST | R | 0.0892798493 | 0.0217865205 | 2.38394731e-05 | 5.90049535e-06 | 0.0890808446 | 0.0217795671 | 0.607685 | 0.0673012775 |

## Selected primary literature and its role

- **Maisak et al. (2013), Nature 500:212–216**, [A directional tuning map of Drosophila elementary motion detectors](https://www.nature.com/articles/nature12320), DOI 10.1038/nature12320. Motivation for ON/OFF cardinal channel organization; not independent confirmation of our specified routing.
- **Salazar-Gatzimas et al. (2016), Neuron 92:227–239**, [Direct measurement of correlation responses in Drosophila elementary motion detectors reveals fast timescale tuning](https://pmc.ncbi.nlm.nih.gov/articles/PMC5097865/), DOI 10.1016/j.neuron.2016.09.017. Motivation for temporal correlation-sensitive computation; does not validate the chosen 30-ms pole or this exact detector.
- **Gruntman, Romani and Reiser (2019), eLife 8:e50706**, [The computation of directional selectivity in the Drosophila OFF motion pathway](https://elifesciences.org/articles/50706), DOI 10.7554/eLife.50706, [released code/data](https://github.com/reiserlab/T5ConductanceModel). Source of the earlier one-cell physiological model and recordings; a separate architecture from the present surrogate.
- **Lappalainen et al. (2024), Nature 634:1132–1140**, [Connectome-constrained networks predict neural activity across the fly visual system](https://www.nature.com/articles/s41586-024-07939-3), DOI 10.1038/s41586-024-07939-3. Context for the older frozen FlyVis pathway; no FlyVis checkpoint was used in the new motion core.
- **Eye structure shapes neuron function in Drosophila motion vision (2025)**, [primary article](https://www.nature.com/articles/s41586-025-09276-5), DOI 10.1038/s41586-025-09276-5. Context for the limits of wide-field direction comparisons and optical/position assumptions; not a matched recording test in this study.

All new-study numerical claims are grounded in the saved local files, not inferred from these papers. The strongest supported conclusion remains: **a reproducible functional image-to-neural baseline, with positive computational tests and explicitly unresolved biological claims**.
