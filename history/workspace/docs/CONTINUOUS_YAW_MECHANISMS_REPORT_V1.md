# Continuous yaw responses, symmetry and normalization controls V1

24 October 2026. **The finite numerical study and corrected independent
verification are complete.** No reliable small-turn threshold or
physiological validation has been established. Turning-dependent activity
survives, but scene-dependent offsets interfere with reading out small yaw.
[Protocol](CONTINUOUS_YAW_MECHANISMS_PROTOCOL_V1.md),
[reproduction](CONTINUOUS_YAW_MECHANISMS_REPRODUCTION_V1.md).

## Scope and evidence status

The study measures continuous model responses before interpreting detection
decisions: local yaw sensitivity, straight-walking offset, temporal information
and controlled input transfer. Original classification criteria and previous
failed results remain unchanged. It tests hypotheses from the independent
feedback rather than assuming a benchmark mismatch, a correct circuit or
saturation explains the errors. The neural graph is recurrent; the body's
prescribed motion remains open loop. It contains no motor-intention signal.

Primary inputs use the original 173×173 receptor grid, 0.3-mm eye baseline,
functional frontend, original MaleCNS equations/parameters and exact SE(2)
poses. Direct point rays remove panorama interpolation; they do not establish
biological optics, receptor-grid convergence or universal temporal accuracy.
The movement epoch is 0.5–1.5 s in a 2-s episode. Primary image/source/solver
clocks are 5/10/1 ms. Responses are mean signed model activity during
[0.70,1.40), with separate fixed early/late/decay summaries. q means left minus
right, using the existing graph-side labels and HS four-cell means.

The fixed main design comprises 280 controlled inputs and 240 fresh-room inputs,
two original graph copies per input, 26 source probes through six graph copies,
36 selected inputs through four expanded/control copies, and three temporal
plus three solver-only refinements. A separately frozen matrix-specific check
adds 12 half-step probe trajectories because the restored-weight control does
not inherit the old simple contraction bound. All original gates are retained.
[Supplementary check](CONTINUOUS_YAW_CONTROL_VALIDATION_ADDENDUM_V1.md).

## Controlled worlds and raw yaw response

Two known rooms receive original A, fully reflected M, symmetric-geometry G,
symmetric-texture T and fully symmetric S constructions. Each receives forward
speed 0/5.5/11/16.5 mm/s and yaw 0/±1/±2/±5°/s. Geometry symmetry adds mirrored
spheres; texture symmetry averages the original material field with its
reflection. This changes contrast and can change occlusions/object counts.
These manipulations are precisely defined counterfactual worlds, not pure
contrast-preserving or biologically measured interventions.

All 280 controlled inputs and 560 original intact/bIPS-silenced trajectories
completed without recorded execution failures. The frozen analysis retains
8,960 mean rows and 3,840 finite-difference gain rows. For original intact DNp15,
the central h=1°/s yaw gains in the original A worlds are:

| Forward speed (mm/s) | s07 gain | s12 gain |
|---:|---:|---:|
| 0 | 1.03367×10⁻⁴ | 9.77447×10⁻⁵ |
| 5.5 | 1.26448×10⁻⁴ | 1.25354×10⁻⁴ |
| 11 | 1.06737×10⁻⁴ | 1.12573×10⁻⁴ |
| 16.5 | 9.02105×10⁻⁵ | 9.43746×10⁻⁵ |

Units are model activity per °/s. The gain is [q(+h)−q(−h)]/(2h), not a
physiological firing-rate sensitivity. It includes the image and curved-path
changes produced by the yaw parameter, not an isolated neuronal transfer
function. All h=1/2/5 estimates, roles, graph copies and windows are retained;
neither speed invariance nor local linearity is assumed.
[All gains](../results/continuous_yaw_mechanisms_v1/core_analysis/yaw_gains.csv),
[all means/contrasts](../results/continuous_yaw_mechanisms_v1/core_analysis).

At fast walking, original-world straight offsets divided by those local gains
are −3.580°/s in s07 and +2.862°/s in s12. These are local linear equivalent
offsets, not decoder estimates, actual rotations, false-alarm probabilities or
biological thresholds. They show that a nonzero baseline can be large relative
to the ±2°/s question even while yaw-dependent neural signals remain present.
These two direct-ray scenes are not interchangeable with the earlier 40-room
legacy-profile detection results.

## Symmetry separates stages, without uniquely assigning every error

All 56 complete original/reflected image comparisons are exact. The fully
symmetric straight/static movies have identical left/right images and pooled
motion fields in all eight room/speed combinations. All 56 empty-room A/G and
T/S duplicate cases also give identical source and neural arrays.

Despite this matched retinal input, forward walking in S produces nonzero
routed-channel means and neural differences. For fast walking, the maximum
recorded side difference among routed channel means is 9.06×10⁻⁵ in s07 and
5.46×10⁻⁵ in s12. The source populations have unequal counts/retinotopy, so
equal local fields do not imply equal delivered population summaries. The
network also has asymmetric weights. This identifies a stage distinction;
it does not isolate target sampling from connectivity or demonstrate that
either biological asymmetry is erroneous.

Fast-walking DNp15 equivalent offsets in S are −1.531 and −1.172°/s. Their
reduction relative to A accompanies changed image contrast and yaw gain;
it is not proof that symmetrization fixes detection. Original/reflected neural
even and odd components are retained. An odd response could include a
reflection-equivariant numerical artifact; mirror reversal alone does not
prove a signal is entirely physical scene parallax.
[Image/field/source symmetry checks](../results/continuous_yaw_mechanisms_v1/core_analysis/symmetry.csv),
[neural parity](../results/continuous_yaw_mechanisms_v1/core_analysis/neural_parity.csv).

Maximum recorded absolute downstream activity across the controlled original
copies is 0.00616847. For active outputs, the inferred local tanh derivatives
are above 0.9999619; the zero-rate silencing clamp has its own zero output
derivative and is not included in that saturation inference. These active
recorded downstream operating points are close to the linear origin. This
does not support downstream tanh saturation as the explanation in this subset;
it does not exclude frontend nonlinearities, source-cell effects or behavior
outside the tested conditions. Zero is a signed model baseline, not a clipping
boundary. No nonlinear/divisive adaptation claim follows from gain changes.

## Normalization and bounded-input controls

All 26 bounded probe inputs and 36 selected visual inputs completed. At common
normalized input c=0.05 and differential perturbation h=0.001, primary-window
DNp15 transfer is:

| Graph copy | Differential gain | Common leakage gain | Absolute gain ratio |
|---|---:|---:|---:|
| Original intact | 0.64425 | −0.031645 | 20.36 |
| Original bIPS silent | 0.51729 | −0.028652 | 18.05 |
| Expanded intact | 0.43950 | −0.000807 | 544.46 |
| Expanded new families silent | 0.46451 | −0.005750 | 80.79 |
| Original weights restored, intact | 0.60752 | −0.027363 | 22.20 |
| Original weights restored, new families silent | 0.64425 | −0.031645 | 20.36 |

Gains use model activity per normalized perturbation; q=L−R. The large expanded
ratio depends strongly on weight normalization and a small leakage denominator.
Restoring the original block reduces it to 22.20 even with the added neurons
active. Added activity changes transfer within each fixed graph, but this is
not evidence of a broadly robust physiological improvement. Across c=0.01,
0.05 and 0.1, original intact ratios are 19.84–21.99; bIPS-silent ratios are
17.63–19.41. The circuit therefore preferentially transmits the prescribed
differential probe, while retaining common-input leakage. Its transfer is
not identical to its response to spatially structured walking images.

For visual h=2°/s gains across the twelve room × A/S × nonzero-speed settings,
bIPS silencing retains 85.33–85.77% of original intact DNp15 gain. Expanded
intact retains 71.30–72.29%; expanded new-family silence retains 73.69–74.33%.
Restoring the original weights with new families active retains 96.19–96.69%;
silencing those families in the restored graph reproduces the original intact
trace. Thus the reduction in visual gain after expansion is largely associated
with how the graph was normalized, with a smaller additional activity-dependent
effect. Neither intervention demonstrates biological causality or a detection
repair. Signed offsets, including increases under some conditions, are retained.
[Full probe transfer](../results/continuous_yaw_mechanisms_v1/control_analysis/probe_transfer.csv),
[normalization means](../results/continuous_yaw_mechanisms_v1/control_analysis/normalization_means.csv),
[descriptive report tables](../results/continuous_yaw_mechanisms_v1/report_tables).
These report tables summarize completed outcomes; they introduce no new
prospective acceptance criteria.

The expanded/control comparison restores all 203,861 original block weights
exactly in a separate graph, keeps added pathway weights fixed and compares
intact versus dual-new-family suppression under both normalizations. This
factorial control complements Study B's earlier scaling audit. It is not a
new physiological reconstruction, and no coupling was optimized for detection.

Probe inputs preserve channel identities and [0,1] bounds. Their common and
differential perturbations share normalized input units, making their gain
ratio dimensionally defined. Those units have no fitted conversion to real
walking speed or firing rate. Probe success cannot by itself identify the
frontend as the sole bottleneck; the probe also changes spatial/channel
structure compared with real 3D walking images.

## Fresh-room readout comparison

All 240 fresh-room inputs and 480 intact/bIPS-silenced trajectories completed.
The selected penalties were 0.001 for DNp15 means, 0.1 for all cell means and
0.01 for means plus slopes, each selected across the three speeds using only
calibration rooms. All 36 candidate fits, nine selected speed-specific models
and 720 held-out predictions are retained. No neural parameter was fitted.

Intact results across the eight held-out rooms are:

| Readout | Speed (mm/s) | Overall yaw RMSE (°/s) | Straight-score RMS (°/s) | ±2°/s sign accuracy | ±2°/s scene AUROC |
|---|---:|---:|---:|---:|---:|
| DNp15 means | 5.5 | 1.098 | 0.986 | 16/16 | 0.758 |
| DNp15 means | 11 | 2.281 | 2.069 | 12/16 | 0.570 |
| DNp15 means | 16.5 | 2.627 | 2.117 | 10/16 | 0.531 |
| All cell means | 5.5 | 1.326 | 1.160 | 15/16 | 0.664 |
| All cell means | 11 | 2.237 | 2.076 | 13/16 | 0.578 |
| All cell means | 16.5 | 3.316 | 3.112 | 10/16 | 0.547 |
| Means + slopes | 5.5 | 1.358 | 1.188 | 14/16 | 0.703 |
| Means + slopes | 11 | 2.936 | 2.785 | 11/16 | 0.477 |
| Means + slopes | 16.5 | 3.583 | 3.349 | 11/16 | 0.516 |

Overall RMSE pools yaw 0, ±2 and ±5°/s, rather than only the small-turn cases.
AUROC compares absolute scores from sixteen signed turn cases with eight
straight cases, across rooms; 0.5 is the ranking chance reference. At slow
walking the ±5°/s AUROC is 1.0 for all three intact readouts, but the corresponding
fast values fall to 0.656, 0.688 and 0.594. The test set is small and finite;
these descriptive comparisons do not establish population-level significance.
Adding cell means or these temporal slopes does not consistently improve
held-out performance. More complex readout features are not automatically a fix;
this does not exclude information in other time-dependent representations.

Applying intact-trained readouts to bIPS-silenced outputs causes a distribution
shift. DNp15-mean RMSE becomes 2.034, 7.887 and 8.080°/s at the three speeds;
small-turn AUROC becomes 0.563, 0.484 and 0.508. These are fixed-readout lesion
effects, not information-loss estimates after lesion-specific retraining or
biological perturbation predictions. Original-decoder secondary scores are
retained without changing its sealed thresholds. No new detection or false-
positive threshold was selected from these test outcomes.
[All summaries](../results/continuous_yaw_mechanisms_v1/held_out/summary.csv),
[all predictions](../results/continuous_yaw_mechanisms_v1/held_out/predictions.csv),
[pre-test model/split freeze](../results/continuous_yaw_mechanisms_v1/readouts/before_held_out.json).

The new readouts use four training, four calibration and eight held-out rooms
with seeds and feature families fixed before simulation. Models receive known
walking speed. Compare bilateral DNp15 means, all 14 cell means, and means
plus within-window temporal slopes. Ridge penalties are selected on calibration
data only; every selected family is tested. Held-out RMSE, sign accuracy,
straight offsets and scene AUROC are finite-environment diagnostics, not
neural-noise or behavioral thresholds. Intact-trained transfer to bIPS
silencing and the original sealed decoder remain secondary comparisons.

## Numerical review and reproduction

The fixed temporal checks pass: all 48 mean and 16 gain comparisons remain
within their original 5% tolerances with the specified floors. Maximum relative
errors are 3.763% for means and 3.712% for gains. These concern the three fixed
fine-time/solver cases, not every movie or arbitrarily smaller yaw.

Independent V2 review verifies 588 execution receipts and 1,660 output hashes,
recomputes every primary core mean exactly, and checks all 36 restored-muted
visual traces against the original intact model with zero recorded error.
All 36 ridge candidates match independent augmented least-squares solutions
within 1.52×10⁻¹² in coefficients. All 720 held-out scores match independent
recomputation within 4.63×10⁻¹³°/s.

The additional half-step probe check passes all 64 mean and 32 gain comparisons;
maximum relative errors are 0.0221% and 0.0370%. Six full original-Python neural
replays (two visual and four probe/copy combinations) agree with the strict
kernel within 6.94×10⁻¹⁸ in rates and 4.34×10⁻¹⁹ in final states.
[Independent review](../results/continuous_yaw_mechanisms_v1/independent_review_v2/complete.json),
[supplementary convergence rows](../results/continuous_yaw_mechanisms_v1/independent_review_v2/counterfactual_solver_checks.csv).
There are 1,364 planned simulation/control trajectories, excluding preflight,
reproduction smoke and the six independent Python replays.

The first verifier failed its small-yaw landmark reprojection check. Its
two-point finite difference at h=10⁻⁵ s incurred truncation error near vertical
rays: maximum error 5.36×10⁻⁵ rad/s against the fixed 10⁻⁵ tolerance. A separately
versioned five-point, fourth-order stencil at the same h gives 1.11×10⁻⁸ rad/s
across 80 fixed landmarks, without changing the tolerance, renderer, analytic
flow or neural results. The original source/failure and precheck remain saved.
This is a corrected verification method, not a retrospectively relaxed gate.
[Correction V2](CONTINUOUS_YAW_VERIFICATION_CORRECTION_V2.md),
[original failure](../results/continuous_yaw_independent_review_v1.log).

Historical preflight reproduces direct-ray images, source drive and neural
outputs exactly. The variable-material renderer matches independent NumPy
luminance exactly on the fixed checks, with maximum depth error 4.98×10⁻¹⁴ mm.
The source-built fresh-namespace reproduction smoke test passed preparation,
preflight and both freezes. It does not repeat the full 520-input sweep.
Original source/model identities remain frozen. No previously sealed report,
artifact or baseline parameter was overwritten.

Seven PNG/PDF figure pairs accompany the report:
[retinal images](../results/continuous_yaw_mechanisms_v1/presentation_v2/controlled_retinal_images.png),
[gains and offsets](../results/continuous_yaw_mechanisms_v1/presentation_v2/yaw_gain_and_straight_bias.png),
[symmetric input stages](../results/continuous_yaw_mechanisms_v1/presentation_v2/symmetric_input_stages.png),
[probe transfer](../results/continuous_yaw_mechanisms_v1/presentation_v2/normalized_probe_transfer.png),
[normalization](../results/continuous_yaw_mechanisms_v1/presentation_v2/normalization_control.png),
[time courses](../results/continuous_yaw_mechanisms_v1/presentation_v2/dnp15_time_courses.png),
[fresh readouts](../results/continuous_yaw_mechanisms_v1/presentation_v2/fresh_readout_comparison.png).
The original layouts are preserved; V2 separates two overlapping legend/footer
areas and simplifies time ticks without changing data.

## Physiological benchmark and remaining scientific limits

The supported parallel audit/specification is complete. Eleven eligible native
bIPS/sytGCaMP7f axonal sessions involve eight already inspected flies. Exact
trial images, modified G3 generator/parameters and verified frame/side mapping
were not located in the bounded source audit. Public Motion Maker G4 code was
verified at a fixed commit, but it does not establish the paper's modified G3
stimuli. No generic calcium decay, synthetic noise or neural/observation fit
was inserted. New recording-matched scoring and physiological validation remain
unavailable. [Benchmark specification and evidence gates](CONTINUOUS_YAW_PHYSIOLOGY_BENCHMARK_V1.md).

After the user requested a public-source solution, an additional search
downloaded all three published example movies and both supplementary PDFs,
audited every commit of the paper repository and preserved full public G4 and
fork histories. The archive currently exposes one version. These sources
support an approximate stimulus-family benchmark without relying on a private
professor handoff; exact per-trial stimulus identity remains unverified.
[Retrieval and feasible next benchmark](ERGINKAYA_PUBLIC_STIMULUS_FOLLOWUP_V1.md).

The functional frontend/routing, specimen-specific normalized chemical weights,
single-node rate model, common time constant and unmodeled electrical coupling
remain biological assumptions/gaps. Candidate recurrent homologies retain their
qualifications. There is no walking-related nonvisual input, biological trial
noise or calibrated fluorescence. Raw source probes exclude the spatial/vertical
structure present in walking input. Symmetry controls and small fresh-room
counts do not establish broad natural-scene robustness or a unique mechanism.
This study adds no motor controller or physical deployment result.

## Supported predictions and the next evidence

Within this model, small yaw changes DNp15 activity while forward walking and
scene content introduce offsets comparable with the target turn. bIPS contributes
to differential transfer; suppressing it reduces visual yaw gain and shifts a
fixed intact readout. Those two effects must be measured separately. Added
pathways alter transfer, but their apparent advantage is strongly confounded
with weight normalization. A more flexible readout alone did not establish
robust small-turn discrimination in fresh environments.

Experimentally testable hypotheses are: (1) a straight-walking baseline varies
with visual texture even at fixed nominal speed; (2) bIPS perturbation changes
both baseline and local DNp15 yaw gain, with stronger downstream than upstream
effects under the specified stimuli; (3) scene-dependent baseline variation
can limit small-yaw discriminability despite nonzero mean yaw gain. Test these
with matched scenes, speed, side/compartment registration and repeated trials.
Their magnitudes in model units are not quantitative recording predictions.

The next supported development is a separate, prospectively specified
stimulus/physiology benchmark and source-mapping audit. Any proposed mapping
or normalization change needs an independently justified definition and fresh
tests, rather than selection to erase these offsets. Public example movies or
method-matched random-dot reconstructions can support explicitly approximate
comparisons when exact trial frames are unavailable; they cannot be silently
treated as the recorded inputs. No new circuit tuning is justified by these
diagnostics alone.

## Undergraduate explanation: what we did, what we want, and why

We want to understand why the model can respond to a turn yet still report
turning during straight walking. We tested carefully controlled pictures and
followed the signal through the visual filters, their mapping onto neurons and
the circuit. Even symmetric pictures produced unequal neural signals because
the modeled sides receive and process inputs differently. Scene texture adds
another imbalance. Different readouts still struggled with small turns in new
scenes, and adding neurons changed the result partly because of weight scaling.
We want the next changes to address these measured problems and compare with
real recordings. This matters because a strong response to turning does not
guarantee that straight walking and turning can be told apart. Reproducible
calculations alone do not establish that
the model matches a real fly or that a reliable detector has been achieved.
