# Fixed image-clamp repair and convergence: execution report V1

Generated 2026-10-11T22:34:22.834170+00:00. Decision: `CONVERGED_MEAN_HORIZONTAL_TRANSFER_INCOMPLETE`.

## TL;DR

The baseline repair and all 256/256 convergence checks pass. All 256 original trajectories reproduce (256 bitwise). The converged horizontal mean criterion passes 16/32 curves and all configurations in 0/8 cells.

Matched baselines and the fixed periodic tail do not establish complete temporal-mean transfer under the unchanged criteria. Classify weak scores separately from resolved opposite directions. No scoring threshold was lowered. Choosing a biological readout next requires a matched physiological observation protocol, rather than a transformation selected because it passes.

## What changed and what this tests

The [prospective protocol](PHYSIOLOGICAL_IMAGE_CLAMP_REPAIR_PROTOCOL_V1.md) fixes
the image-trial T4 clamp set to all 99 excitatory and 55 inhibitory sites. This
removes future-input-dependent activation while retaining the complete 344-section
cable, filters, all parameters, finite off-resistance, seed and numerical solver.
The legacy author-compatibility path and T5 equations are byte-identical to earlier
versions. The new wrapper is separately named; old records and the earlier
`TECHNICAL_COMPARISON_INVALID` decision remain preserved.

The batch contains 662 source cases: 256 old four-cycle gratings, 256 long gratings,
32 neutral records, 14 legacy/fixed causal controls and 104 compatibility checks.
All 16 cells, both scales/phases and four directions remain. No source gain, neural
parameter, geometry or score gate was fit. No population, random-square or HS/H2
simulation was repeated and no degeneracy search was conducted.

## Input extension, clocks and steady tail

The old native contrast records are not all exactly periodic: 194/256 have cycle
differences above 1e-12. We preserve all four recorded moving cycles exactly and
repeat the fourth sampled cycle 28 times, followed by the saved neutral tail.
This is an explicitly declared periodic replay of image-derived contrast. It is
not a fresh raster render and old-versus-long differences cannot be attributed
exclusively to duration. No observed best cycle was selected.

The fixed 32-cycle endpoint uses cycles 30–32: source-scale [40,120,43,960) ms,
assignment-scale [17,500,19,000) ms. Baseline is [2,500,3,000) ms. Nominal 1 ms
clock rounding is allowed only within 1e-5 ms; voltage samples are unchanged.
Convergence requires consecutive-period max voltage error <=0.001 mV and mean
error <=0.0001 mV, for every long trace. These are computational tolerances.

## Numerical repair evidence

| Check | Result |
| --- | --- |
| Legacy maximum silent-prefix discrepancy | 0.150695049 mV |
| Fixed maximum silent-prefix discrepancy | 0 mV |
| Neutral plateau checks | 32/32 |
| Grating versus neutral prefix error | 0 mV |
| Original four-cycle reproduction | 256/256; 256 bitwise |
| Compatibility reproduction | 104/104 |
| Native author-reference error | 5.01892641e-05 mV |
| Moving half-step error | 0.00289262666 mV |
| Original amplitude curves | 64/64 |
| Long versus original moving-prefix error | 6.39488462e-14 mV |
| Long convergence | 256/256 |
| Maximum long period voltage error | 8.41053804e-09 mV |
| Maximum long period mean error | 1.21431754e-11 mV |

The numerical audit reproduces the legacy control defect and measures the effect
of the prescribed policy change, rather than simply associating two saved traces.
Finite silent clamp current remains present in the new common baseline; this repair
does not implement exact-zero synaptic conductance or validate that floor biologically.

![Causal baseline controls](../results/physiological_image_clamp_repair_v1/figures/baseline_intervention.png)
![Cycle means](../results/physiological_image_clamp_repair_v1/figures/cycle_settling.png)

## Full readout results

Oscillation amplitude remains (q95−q05)/2, with the original amplitude/four-direction
gates. Mean preserves signed baseline-subtracted voltage; principal-pair response
and difference floors remain 0.065 mV and absolute DSI floor 0.1. Expected sign is
scoring-only. The secondary four-direction mean normalization remains distinct.

| Long-tail measurement | Horizontal a/b | Vertical c/d |
| --- | --- | --- |
| Amplitude curves passing | 32/32 | 32/32 |
| Principal mean curves passing | 16/32 | 10/32 |
| Raw expected mean sign | 32/32 | 32/32 |
| Resolved opposite mean sign | 0 | 0 |
| Cells passing all mean configurations | 0/8 | 0/8 |
| Four-direction mean passed | 0/32 | 0/32 |
| Four-direction mean angle within 45° | 32/32 | 32/32 |

| Cell | Cycles | Axis | Amplitude pass | Principal mean pass | Four-direction mean pass |
| --- | --- | --- | --- | --- | --- |
| T4a_L | 4 | horizontal | 4/4 | 1/4 | 0/4 |
| T4a_R | 4 | horizontal | 4/4 | 1/4 | 0/4 |
| T4b_L | 4 | horizontal | 4/4 | 1/4 | 0/4 |
| T4b_R | 4 | horizontal | 4/4 | 2/4 | 0/4 |
| T4c_L | 4 | vertical | 4/4 | 1/4 | 0/4 |
| T4c_R | 4 | vertical | 4/4 | 2/4 | 0/4 |
| T4d_L | 4 | vertical | 4/4 | 1/4 | 0/4 |
| T4d_R | 4 | vertical | 4/4 | 0/4 | 0/4 |
| T5a_L | 4 | horizontal | 4/4 | 1/4 | 0/4 |
| T5a_R | 4 | horizontal | 4/4 | 1/4 | 0/4 |
| T5b_L | 4 | horizontal | 4/4 | 1/4 | 0/4 |
| T5b_R | 4 | horizontal | 4/4 | 1/4 | 0/4 |
| T5c_L | 4 | vertical | 4/4 | 1/4 | 0/4 |
| T5c_R | 4 | vertical | 4/4 | 1/4 | 0/4 |
| T5d_L | 4 | vertical | 4/4 | 0/4 | 0/4 |
| T5d_R | 4 | vertical | 4/4 | 0/4 | 0/4 |
| T4a_L | 32 | horizontal | 4/4 | 2/4 | 0/4 |
| T4a_R | 32 | horizontal | 4/4 | 2/4 | 0/4 |
| T4b_L | 32 | horizontal | 4/4 | 2/4 | 0/4 |
| T4b_R | 32 | horizontal | 4/4 | 2/4 | 0/4 |
| T4c_L | 32 | vertical | 4/4 | 2/4 | 0/4 |
| T4c_R | 32 | vertical | 4/4 | 2/4 | 0/4 |
| T4d_L | 32 | vertical | 4/4 | 2/4 | 0/4 |
| T4d_R | 32 | vertical | 4/4 | 0/4 | 0/4 |
| T5a_L | 32 | horizontal | 4/4 | 2/4 | 0/4 |
| T5a_R | 32 | horizontal | 4/4 | 2/4 | 0/4 |
| T5b_L | 32 | horizontal | 4/4 | 2/4 | 0/4 |
| T5b_R | 32 | horizontal | 4/4 | 2/4 | 0/4 |
| T5c_L | 32 | vertical | 4/4 | 2/4 | 0/4 |
| T5c_R | 32 | vertical | 4/4 | 2/4 | 0/4 |
| T5d_L | 32 | vertical | 4/4 | 0/4 | 0/4 |
| T5d_R | 32 | vertical | 4/4 | 0/4 | 0/4 |

Long principal failures, with overlapping reason counts: {'dsi_floor': 38}.
All failed and successful curves remain in the complete tables. A converged
trajectory does not automatically pass a tuning test. If any convergence prerequisite
failed, the plotted scores remain descriptive rather than eligible steady-state findings.

![All long mean curves](../results/physiological_image_clamp_repair_v1/figures/long_mean_tuning.png)
![Readout comparison](../results/physiological_image_clamp_repair_v1/figures/readout_comparison.png)

The remaining long-window mean failures are all `dsi_floor` failures, with
correct raw direction signs. Horizontal principal mean passes 0/16 curves for
18°/0.78125 Hz and 16/16 for 30°/2 Hz. Both wavelength and temporal frequency
change together, so this comparison does not isolate a frequency effect. No
horizontal cell passes all four scale/phase configurations; the weaker configuration
is retained. The numerical baseline defect and incomplete settling are excluded
as sufficient explanations of the persistent weak mean scores in this repaired,
converged assay. The original random-square sign reversals remain a separate problem.

## Independent verification

Separate direct arithmetic checks 512 grating traces, 128 curves, 14 causal controls,
32 neutral records and all compatibility/reproduction comparisons. Status **PASS**;
maximum mean error 1.50990331e-14 mV. Four predeclared fresh full-cable
T4 replays are bitwise identical. Twelve scalar T5 replays agree to
7.81597009e-14 mV. 8 worker
audits match the original full morphology, sites, seed and parameters. 21
focused tests pass. This is separate numerical implementation, not an external
scientific replication. All three previous artifact indexes and their entries were verified.

## Existing physiological observations and the next scientific decision

The local T5 source package contains the cell-7 input protocols and observation
fields ['vm_all_sb', 'vm_all_mb', 'vm_all_mg', 'vm_all_sg', 'vm_all_mm']; moving/static grating schedules are
present alongside bar and minimal-motion schedules. The provided optimization workflow fits the single-bar `_spfr` dataset, then
predicts the `_all` protocols. Thus the eight measured moving-grating conditions
(9,248 samples) are candidates for a stimulus-held-out comparison. Audit the archived
parameter selection and exact training/test protocol membership before claiming
that status. A held-out stimulus test in one fitted cell is distinct from validation
in an independent cell or the complete MaleCNS population. These data are already
local and useful for checking the author's observable and timing convention.
The T4 package here is simulation code/morphology/parameters; its simulated
reference traces are implementation references, not experimental ground truth.

The [machine-readable inventory](../results/physiological_image_clamp_repair_v1/physiological_observation_inventory.json)
lists available fields and files. We have not computed a new physiological readout
comparison in this batch. Inventory existing measured data and the corresponding
author analysis first; request additional external observations only if the needed
matched or held-out data are absent. Exact subtype, stimulus, units, baseline and
scoring window must match the question. Do not select a transformation because it passes.

Matched baselines and the fixed periodic tail do not establish complete temporal-mean transfer under the unchanged criteria. Classify weak scores separately from resolved opposite directions. No scoring threshold was lowered. Choosing a biological readout next requires a matched physiological observation protocol, rather than a transformation selected because it passes.

The next bounded scientific comparison should use the eight existing T5 native
moving-grating voltage conditions: first audit parameter/split provenance, then
match stimulus, baseline and window and compare mean versus amplitude in both
measured and fixed-model traces. Declare the observation comparison before its
new scores, and keep the model parameters fixed. This can begin with existing
files; additional external observations are needed only if the provenance or
required independent test data are missing. That comparison is not executed here.

The full-circuit degeneracy route stays paused. The original random-texture sign
reversals remain unresolved; no population or downstream conclusion is updated by
this local grating repair. Biological validity, neural degeneracy and publication
novelty/acceptance remain unestablished.

## Development tracking and reproduction

The [consolidated development trail](PROJECT_DEVELOPMENT_AUDIT_TRAIL_V1.md) links
older milestones, failures and later interpretations. Git initially had no commits;
checkpoint `e430690a7f263e3243e9ba71ea33ad1c7f98e448` records the pre-repair source. The new
experiment separately freezes code, protocol and numeric inputs before simulation,
retains timestamped events/worker logs, and seals complete results with hashes.
A second local source checkpoint records this repair. Git history starts at these
snapshots; it does not reconstruct every earlier edit. Results/raw data are retained
as separately hashed artifacts rather than Git objects. These local records are
reportable evidence; an off-device backup remains a separate task.

[Config](../configs/physiological_image_clamp_repair_v1.json),
[run manifest](../results/physiological_image_clamp_repair_v1/run_manifest.json),
[complete curves](../results/physiological_image_clamp_repair_v1/analysis/all_curve_measurements.csv),
[all cells](../results/physiological_image_clamp_repair_v1/analysis/all_cell_outcomes.csv),
[decision](../results/physiological_image_clamp_repair_v1/analysis/analysis_summary.json),
[independent audit](../results/physiological_image_clamp_repair_v1/independent_review/independent_review.json),
[artifact index](../results/physiological_image_clamp_repair_v1/artifact_index.json).
Plots also have standalone PDFs. Reproduce in a newly versioned output directory:
prepare → execute → analyze → review → report → final checks → seal. Source clocks
and pinned analysis/NEURON runtime versions are recorded in `environment.json`.
