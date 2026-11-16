# Fixed-neighbor functional frontend — technical report V1

Client date: 13 October 2026 (America/Belem); evidence timestamps use UTC.

**Decision: `FUNCTIONAL_END_TO_END_PASS`.** Source decision: `FUNCTIONAL_FRONTEND_PASS`.
This result concerns an explicit algorithmic motion surrogate. It does not establish
accurate biological T4/T5 membrane responses, independent specimen optics or degeneracy.

The user requested a working frontend supported by positive functional evidence.
We retained the physical renderer, label-free pixel sampler and declared bilateral
chart, and implemented a new circuit on a fixed retinal lattice. Every site computes
all eight ON/OFF × signed horizontal/vertical channels using the same delayed
neighbor products and spatial averaging. Target types route already computed
outputs. Sampling and circuit dynamics never query a target preferred angle or
the intended movie velocity. The declared surrogate subtype routing is part of
the architecture; its agreement with subtype labels is not independent biological
validation. This is a model-scope alternative, not a correction of the old published
conductance equations or restoration of the deprecated per-target sampler.

[Frozen protocol](FIXED_NEIGHBOR_MOTION_PROTOCOL_V1.md),
[methods/source hashes](../results/fixed_neighbor_motion_v1/prospective_manifest.json),
[configuration](../results/fixed_neighbor_motion_v1/config.json),
[all movie plans](../results/fixed_neighbor_motion_v1/plans.json).

**Functional tests.** Four textures each supplied the original seven physical
conditions, with ±60°/s motion and a stationary opposite field in unilateral movies.
Seed 42 is historical; three seeds were frozen before their new responses. Another
new texture supplied ±30/±90°/s and its own STATIC. Four cardinal gratings, seven
fine-clock counterparts and three runtime controls complete 47 source executions.
All 13,579 mapped targets have complete grid/pooling support. We retained the old
0.001 amplitude/difference floors, DSI 0.1 and 75% per-horizontal-group criterion.
Trials, retinal positions and seeds are not independent biological animals.

| Texture | Horizontal groups passing | Minimum expected fraction |
|---|---:|---:|
| 42 | 8/8 | 99.88% |
| 78201 | 8/8 | 100.00% |
| 78202 | 8/8 | 100.00% |
| 78203 | 8/8 | 99.88% |

Supplemental speed groups passing: **16/16**.
Cardinal grating eye/family comparisons: **16/16**.
Stationary maximum source activity: **0** normalized units.
Maximum group/pool sampling-refinement relative change: **4.1009%**
under the frozen 10% engineering gate. Sampling outcomes and individual/c/d scores
remain in [source analysis](../results/fixed_neighbor_motion_v1/source_analysis.json),
[group table](../results/fixed_neighbor_motion_v1/source_groups.csv) and
[all individual results](../results/fixed_neighbor_motion_v1/source_individual.csv).

![Texture results](../results/fixed_neighbor_motion_v1/figures/source_texture_results.png)

![Cardinal channels](../results/fixed_neighbor_motion_v1/figures/cardinal_motion_channels.png)

**Controls and numerical validation.** Same-input replay is bitwise equal:
**True**. Preferred-direction fields are removed before the
numeric interface; the geometry/routing allowlist produces an identical target
map. Mirrored inputs exchange eyes bitwise: **True**;
maximum probe/pool output discrepancy **0**.
Frame-scrambled signed-response ratios: **[0.006855868580990111, 0.006369840882641257, 0.006078674698956365, 0.006590399155025654]**, judged
against the fixed 0.5 ceiling. STATIC and causality have analytic test coverage.
Twenty-eight focused tests passed before freezing. All 47 executed channel sets
match a separate lfilter / summed-area-pooling / bilinear-readout reference to
**2.55e-08** normalized units; final filter states agree
within **5.55e-16**. Independently regenerated physical
pixel probes and retinal interpolation were also checked. Group decisions agree
with independently accumulated response means.
[Independent source review](../results/fixed_neighbor_motion_v1/source_independent_review.json).

![Inputs and eye registration](../results/fixed_neighbor_motion_v1/figures/physical_and_retinal_inputs.png)

**Frozen downstream integration.** All 28 primary drives entered the frozen 13,593-node MaleCNS
circuit, with unchanged parameters and 1-ms RK4. Only the 13,579 source targets
receive direct input. Activity uses one common unit scale; no sign-specific gain
or HS/H2 fitting. The source STATIC equilibrium is zero motion, so every trial
starts from the same zero downstream state. All-circuit STATIC stable:
**True**. Expected measurable global HS/H2 comparisons:
**40/40**; expected ipsilateral unilateral contrasts:
**40/40**. H2 comparisons remain qualitative model
plausibility checks. All ten exact body IDs and all seven conditions are retained
in [target results](../results/fixed_neighbor_motion_v1/hs_h2_results_v2.csv) and
[downstream analysis](../results/fixed_neighbor_motion_v1/downstream_analysis_v2.json).

Whole-network label replay is bitwise identical. Independent graph-equation/RK4
replay covers all 28 network trials, maximum float32 all-cell record error
**7.45e-09**, float64 HS/H2 error
**1.39e-17**. This verifies this discretized network;
it does not establish measurement-unit calibration or physiological accuracy.

![Wide-field outputs](../results/fixed_neighbor_motion_v1/figures/hs_h2_seed42_traces.png)

**What is defensible.** A positive decision establishes a reproducible functional
motion frontend on the frozen spatial/temporal/stimulus benchmark, with image-only
numeric input and explicit circuit wiring. It is useful for software integration
and controlled model experiments. The eye chart, filter time, grid, pooling and
output-slot mapping are declared conventions. Their success cannot demonstrate
the detailed biological computation, independently learned subtype preferences
or recovery of the old physiological model's texture/grating weaknesses. Earlier
failed studies remain archived. No recordings were added or refitted.

For a supervisor, present this as a functional prototype and its complete test
evidence. Broader physiological claims require matched recordings and an appropriate
observation model. Next work should be a declared use of this baseline or biological
comparison; passing a prototype is not publication acceptance or degeneracy.

**Reproduction and preservation.** Source runtime versions, legacy-source hashes,
commands/logs and frozen input/method inventories are saved inside the result bundle.
Run a fresh workspace/version; the completed directory refuses overwrites. Source
actions use `run_fixed_neighbor_motion_v1.py`: freeze, launch_source, analyze_source.
The independent reviewer uses source, source_decisions, downstream actions. Gate
passing permits launch_downstream, followed by downstream_analysis and report in
the report script. The legacy environment is read only. Portable dependencies are
listed in the two versioned requirement files. The numerical arrays stay outside
Git and are hash-sealed; this is not an off-device backup. All earlier seals were
verified before/after; the live progress report remains append-only.

**Retained tuning limitation.** Vertical c/d-like slots also show horizontal random-texture selectivity under the same binary criterion: the mean selective fractions are 85.63%, 85.97%, 86.71%, 85.42% for the four seeds. Their mean response strengths are 13.64%, 13.23%, 13.53%, 13.57% of the horizontal groups. This is texture-dependent cross-axis activity, not evidence of complete biological subtype tuning. It does not change the frozen functional decision, whose horizontal and cardinal-control gates all pass. The output-slot naming is a declared surrogate assignment. Compared models have different output units/architectures; the new pass is not a calibrated biological amplitude improvement over the older failed model. [Descriptive context](../results/fixed_neighbor_motion_v1/off_axis_descriptive_context.json).

**Technical interruptions and corrections.** The original source worker stopped under the zero-swap/memory guard after 38 completed executions. A hashed memory-only wrapper releases transient eye arrays and isolates remaining cases; its full-array replay is bitwise identical. The first independent-review attempt failed at final-pixel adjacent indexing; the endpoint-safe reference correction preserves physical source support and numerical tolerances. The frozen downstream worker stopped at the same resource guard after 25 completed trials; its unchanged routine completed the last three in a fresh process. All original logs, successful batches, failed supervisor records, pre-response amendments and validation tests remain in the bundle. No scientific gate or neuron parameter changed.

**Final statistics audit and export correction.** All 81,474 individual source classifications and 40 wide-field decisions were verified. A post-analysis comparison amplified ~1e-18 rounding in 72 silent vertical slots into tiny DSI differences; no class changed. Score arithmetic is independently checked on the identical saved float32 traces, while the physical model reference keeps the declared 1e-7 tolerance. Wide-field V1 condition means used float32 accumulation; the versioned V2 export uses unchanged float64 HS/H2 traces and compensated means. Maximum mean correction 1.328e-8, with every global/unilateral verdict unchanged. All failed audit logs, diagnoses and V1 exports remain preserved. Validation tolerances and source/model parameters were not relaxed. [Final checks](../results/fixed_neighbor_motion_v1/final_checks.json), [full-precision export](../results/fixed_neighbor_motion_v1/downstream_analysis_v2.json).

The [supervisor brief](FIXED_NEIGHBOR_MOTION_SUPERVISOR_BRIEF_V1.md) and [standalone runnable demo](../examples/fixed_neighbor_motion_demo_v1.py) provide a compact entry point. The full-precision statistics export and final arithmetic corrections are recorded in the versioned amendments; all earlier failed checks remain available.
