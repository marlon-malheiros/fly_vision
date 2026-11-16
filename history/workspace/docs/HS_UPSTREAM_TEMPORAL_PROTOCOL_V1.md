# One fixed upstream temporal-filter experiment V1

2026-11-03. Development experiment only. Existing HS contrast/frequency recordings
and all qualitative failures are already inspected. No fresh animal-level or
blind biological-validation claim. Preserve every original model/result.

## One hypothesis and source constraints

Test a common upstream bandpass signal before the existing local motion
computation. ON uses the Mi1-like low/high-pass time constants 54/318 ms; OFF
uses the Tm1-like constants 44/296 ms. These are extracted before simulation
from the first entries of the author's `lp_tau`/`hp_tau` arrays in the
`calc_data_T4`/`calc_data_T5` functions of FigureCode/Borst_Fig1.py, pinned
commit `2e277fef43139230fafc598c93301bf7b27645dd` of
https://github.com/axelborst/temporal_filtering. Its comment specifies units of
10 ms. [Borst 2025](https://doi.org/10.1007/s10827-025-00914-5) republishes
temporal fits to earlier upstream physiology; this is a source-backed functional
hypothesis, not four newly measured intrinsic membrane constants. The separate
50 ms observation filter in the author's simulation-library target generation
is not adopted as an additional neural stage. No raw upstream recordings or
independent acceptance dataset were acquired here.

For normalized rectified image contrast u, propagate h'=(u-h)/tau_lp,
g'=(h-g)/tau_hp and d'=(h-g-d)/tau_delay. Current visual deviation is h-g;
the inherited detector-delay signal is d. Exact matrix exponential propagation
uses the previously held image, never a future frame. Equilibrium for the first
stationary image is h=g=u and d=0. The signed bandpass signal represents a
deviation, not a negative absolute firing rate. Opponent multiplication, spatial
pooling and final channel rectification/routing remain unchanged.

Using these two cell-type temporal proxies over the whole eye and retaining a
separate 30 ms detector delay are explicit coupling assumptions. This does not
reconstruct those neurons, their heterogeneous receptive fields or an anatomical
three-arm motion detector. Do not infer a unique biological mechanism from
success/failure of this approximation. The fixed LPi graph, neural parameters,
sigma=0.121902687872575, spatial footprint and all decoder files are unchanged.
No sign reversal, time-constant sweep, gain fit or yaw-label optimization.

## Fixed cases and analysis

Twenty-two shared image slots. Primary: four frequencies 0.5/1/2.5/15 Hz at
full contrast, both directions (8); remaining contrasts 0.1/0.25/0.5/0.75 at
1 Hz, both directions (8). Frequency1 supplies contrast1 endpoints without
duplicate simulations. Numerical refinements: four preferred-direction
frequencies plus contrast0.5 in both directions (6). Phase zero, methods85,
60 Hz/four-bit square-wave grating, static/moving/static 2/2/1 seconds. This
small panel is not the complete frequency bank or phase-average benchmark.

Primary image/source clocks 1.25/2.5 ms; refined 0.625/1.25 ms. Solver 0.25 ms
throughout, preserving absolute 1 ms forcing ramp. Reuse gain-only baseline
arrays at the four PD frequencies for each clock from the sealed numerical
study after checking identical retinal/source hashes. Two primary cached cases
(0.5/15 Hz) replay bitwise at the identical solver step, including final state
and checkpoints. At primary PD2.5 additionally halve solver step to 0.125 ms for
both models with identical input. Save these outputs and all failures.

New network solves: 22 candidate +14 baseline +2 cached baseline replays
+2 solver checks =40. Baseline/candidate get identical images. No permanent
movies or full source drives. Retain 100 Hz wide-cell rates, hashes and compact
responses. Pre-motion rates must be <=1e-12, and clipping must be reported.

Primary response remains right HSN/HSE/HSS equal-mean atanh(rate), [2,4) minus
[1,2). Keep each subtype and signed-rate summaries; do not substitute favorable
ones. Contrast curves normalize by own PD100, frequency curves by own PD1 Hz.
Use existing fixed recording targets/bands; do not rebootstrap a narrow favorable
band. Frequency scoring takes the seven coordinates of this panel from the
pre-existing fifteen-coordinate joint band. Contrast scoring keeps seven prior
coordinates (PD50/75 and all ND contrasts). All targets are development evidence.

Numerics: 12 time-refinement +2 solver comparisons, each with its own model's
fixed primary PD1/PD100 reference. Preserve dual criteria: error <=
0.05*max(abs(primary),abs(reference))+1e-7 and error/abs(reference)<=0.05.
No new spatial-convergence claim. Independent log1p observations, literal scoring
arithmetic, rational display clock checks and source-parameter extraction checks.

## Frozen decisions and stop

The practical development-improvement flag requires all numerical checks,
frequency-panel normalized RMSE <=75% of matched baseline, contrast RMSE increase
<=0.02, no increase in contrast band violations, both PD50/75 inside band, and
zero clipping. These are prospective engineering triage margins, not biological
equivalence or statistical significance. Also report absolute band violations
and whether all seven frequency/contrast coordinates agree, separately. A better
RMSE cannot establish biological validity. Biological-validation and walking-
advancement flags remain false in this partial, inspected-data experiment.

Complete the entire panel whether improved or worse. No second candidate or
post-outcome repair belongs to this round. Record negative findings. If no
improvement, distinguish failure of this source-inspired approximation from
impossibility of a neural solution. Next alternatives may use better constrained
branch-specific filters or better matched recording/stimulus evidence; neither
is implemented implicitly after seeing outcomes.

## Resources and preservation

Whole-run estimate 32 MiB, cap 64 MiB, reserve20 GiB, two workers, peak2 GiB
each, 4200 new observation/replay CPU seconds. Stop submitting on failure/cap;
in-flight work may finish. Source acquisition only two scripts (20,995 bytes),
no repository clone, raw-data bulk archive or source ZIP duplicate. Run three
focused checks before freeze: exact state propagation against independent ODE
integration, causal-prefix/reset/stationary controls, and preservation of the
full recording joint band's coordinates in the small panel. Freeze all source and
targets before neural outcomes. Version code/protocol; append dated progress,
save an actual-date progress snapshot with completion sources/report, seal and
independently rehash after writer exit. Keep live progress/AGENTS outside indexes.
