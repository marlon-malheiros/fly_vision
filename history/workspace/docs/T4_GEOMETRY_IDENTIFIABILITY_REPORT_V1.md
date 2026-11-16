# T4 geometry-identifiability diagnostic V1

Completed 2026-11-06. This is a bounded retrospective development study, separate from all sealed models and experiments.

## Outcome

Actual stationary images do not uniquely determine the two-dimensional registration of the fixed T4 input model. Accounting for that uncertainty improves motion prediction. The prospectively specified **secondary physical-mV ensemble passes the existing restricted waveform rule** on three already inspected cells. The **primary flash-gain ensemble still fails**. No candidate was selected using motion responses, no neural parameter was fitted, and this result does not establish independent biological validation, a repaired delivered MaleCNS frontend or reliable2deg/s walking-yaw detection.

This is useful progress: the earlier single-registration motion failure cannot be attributed solely to neural dynamics, because an unresolved input-registration choice materially changes the result. Geometry is not proven to be the sole error source. The voltage-gain transfer limitation remains, and a secondary result cannot replace the failed primary hypothesis after inspection.

## Frozen experiment and scope

The [protocol](T4_GEOMETRY_IDENTIFIABILITY_PROTOCOL_V1.md) and [configuration](../configs/t4_geometry_identifiability_v1.json) were hashed before this round's grid analysis and predictions. Cells3–5, canonical axes, flash-fitted delays/gains, all responses/references and waveform acceptance rule come unchanged from the [completed flash-transfer study](T4_FLASH_TRANSFER_REPORT_V1.md). There is no new data acquisition, source-parameter tuning, graph change, generated movie, whole-brain solve or conditional opening of reserved recordings.

For each cell, examine25 integer horizontal/vertical shifts in[-2,2]² LED pitches (2.25deg/pitch), using all164 flash conditions. All820 repetitions have matching stationary images within condition. Record complete eleven-channel input arrays and exact equality classes. Only registrations with exactly the same complete flash input as the previous selected registration enter prediction. Their already locked delay/gain remains unchanged; equal averaging across every such registration is specified before any new voltage simulation. This is an ensemble describing input uncertainty, not evidence that a real neuron averages positions or that these positions have equal biological probability.

The unchanged344-section Gruntman cable,99 excitatory/55 inhibitory sites and12 source parameters predict48 moving repetitions, averaged into24 conditions. Reuse prior input/output pairs only when complete event times and all contrast values match exactly. Compute a gain-preserving primary ensemble and a physical-mV secondary ensemble. Report both prior forecasts and every registration; never choose the best member by motion score.

## Geometry result

Coordinates below are shifts of the original center in stored-image horizontal/vertical LED pitches, not absolute anatomical locations.

| Cell | Distinct flash-input classes among25 shifts | Previous shift | All exactly equivalent shifts |
|---|---:|---|---|
|3|5|(0,0)|(0,−2),(0,−1),(0,0),(0,1),(0,2)|
|4|21|(0,+1)|(−1,0),(0,+1)|
|5|19|(0,−1)|(0,−1),(+1,0)|

Cell3's five alternatives also give identical moving inputs and reuse prior predictions. Cells4/5 have diagonal flash sequences: a horizontal displacement can be indistinguishable from the previous vertical displacement for the entire stationary stimulus set, while changing moving inputs. Finite image/bar boundaries exclude other potential aliases; no continuous2D identifiability claim follows from this finite grid. [Full audit](../results/t4_geometry_identifiability_v1/geometry_audit.json), [input arrays](../results/t4_geometry_identifiability_v1/cell04_flash_inputs.npz), [figure](../results/t4_geometry_identifiability_v1/figures/geometry_and_skill.png).

## Motion comparison

MSE is averaged over conditions within each cell and then equally over three cells. Skill is1−model_MSE/reference_MSE. A direction-blind reference predicts the same mean waveform for preferred and null motion at each speed, estimated from earlier repetitions. Positive skill means smaller prediction error than that reference. The unchanged pass rule requires positive pooled zero/reference skills, positive zero skill in every cell and a positive5th percentile of the joint minimum skill over all27 exact three-cell bootstrap resamples. That last quantity is the previously frozen decision statistic, not a precise population confidence interval from three cells.

| Candidate | RMSE (mV) | Zero skill | Direction-blind skill | Joint lower statistic | Rule |
|---|---:|---:|---:|---:|---|
|Previous primary, flash gain|4.925398|0.658928|−0.017603|−0.268560|Fail|
|**Primary: all aliases, flash gain**|4.761060|0.681308|0.049169|−0.079872|**Fail**|
|Previous registration, physical mV|4.480536|0.717757|0.157915|−0.087888|Fail|
|**Secondary: all aliases, physical mV**|4.221343|0.749467|0.252524|0.133000|**Pass**|

The secondary has25.25% less pooled MSE than the direction-blind reference. Per-cell reference skills are+0.406199,+0.040977,+0.329326. Cell4 remains marginal, and cell5's physical forecast worsens relative to its previous registration (+0.418917→+0.329326); both remain included. The primary gains1.370363/0.781753/0.678331 were fitted only to flashes. Primary cell4 remains worse than its reference (−0.165895). This demonstrates that a good stationary calibration need not transfer to motion.

For cell4, the two flash-indistinguishable registrations have primary motion skills+0.033201 and−0.440254; for cell5,+0.310042 and+0.057661. These differences demonstrate material input uncertainty. Reporting the better member as a validated solution would be outcome-based selection, which was not done.

[Decision and all member scores](../results/t4_geometry_identifiability_v1/decision.json); [240 condition-output scores](../results/t4_geometry_identifiability_v1/condition_metrics.csv); [complete prediction list frozen from images](../results/t4_geometry_identifiability_v1/prediction_lock.json); [motion waveforms](../results/t4_geometry_identifiability_v1/figures/motion_waveforms.png). Stationary forecasts are exactly inherited from their flash-equivalent inputs, so the prior physical-mV flash-repeat pass also remains; no additional stationary neuron simulations are necessary.

## Numerical evidence, failures and resources

Forty new full-cable solves comprise32 moving repetitions and8 temporal refinements. All eight0.1→0.05ms checks pass the unchanged0.005mV maximum-error guard; worst error0.002866684mV. Forty-eight unique prior repetitions are reused, with cell3 aliases requiring no new solves. The72 alias-condition means contain144 prediction references; repetitions may share exact inputs/outputs. Source parameters, sites, axes and observation arrays remain unchanged.

The independent R2 reviewer reconstructs all75 registrations and144 moving input sequences, covering144,804 integer-pixel samples. Event clocks match exactly, readout error≤3.91e−14mV, metric/bootstrap error≤8.89e−16. All4267 indexed prior flash-study artifacts rehash unchanged. [Independent evidence](../results/t4_geometry_identifiability_v1/independent_review_r2.json).

The initial reviewer fails because subtracting onset from unsigned source timestamps underflows for pre-onset events. The production sampler already converts clocks before subtraction and is unaffected. The failed reviewer/log are preserved; the [R2 correction](T4_GEOMETRY_REVIEW_CORRECTION_R2.md) uses signed native ticks and repeats the complete review. No prediction, threshold or model output is altered. Figure label layout was corrected before sealing without changing numerical results.

Worker scientific CPU11.418364s, peak RSS59,527,168bytes; excludes parent preprocessing, independent review, plotting and provenance hashing. One worker, no bulk downloads, no copied raw recordings or regenerated movies. New-study storage remains under32MiB; archive counts/bytes and post-exit hash proof are recorded in `results/t4_geometry_identifiability_v1/completion_v1/`. The live progress file and AGENTS remain outside the immutable index; a dated progress copy is included.

## What is solid, and what remains

Solid computational evidence: unchanged cable parameters/source geometry, exact stationary input equivalences, material motion differences from those equivalences, converged voltage solves and independently reproduced scores. Solid but restricted physiological evidence: prior stationary-repeat prediction and this secondary motion prediction on recorded T4 voltage. The static population observation-transfer result is also retained in its [separate report](T4_OBSERVATION_TRANSFER_REPORT_V1.md); it is a different assay and does not validate neural dynamics.

Not established: independent-animal image-to-voltage prediction, sustained null-direction inhibition (prior qualifying masks0/3), absolute RF geometry, T5/downstream HS/H2/bIPS/DNp15 physiology, generalization to arbitrary visual inputs, improved original delivered frontend, or reliable2deg/s detection during fast walking. The original author's stationary-fit cohort overlaps these cells, and the project has repeatedly inspected their moving responses. No retrospectively obtained pass erases that exposure. The three additional moving files and four C2/C3 animals remain unopened/unscored.

Next finite milestone: prospectively freeze the physical-mV geometry-uncertainty comparator, admit suitable reserved matched recordings using metadata, and test once without fitting their moving voltages. Registration calibration must use stationary data or independent metadata under a predeclared rule. Keep the failed primary as a reported comparison; do not add another gain/offset sweep on these three cells. A successful independent component test would justify reconnection and separate walking-yaw requalification. If that test fails, move to constrained dynamics/model comparison rather than claiming that another pass on these same cells is independent validation.

## Undergraduate explanation

We want a neural model that explains how a fly sees a small turn while walking. Before trusting that large model, we test a motion-sensitive neuron called T4 against real voltage recordings. A stationary bar can leave a location ambiguous, like seeing one stripe without knowing exactly where a sensor sits along it. We found that two equally compatible locations can predict different responses when the bar moves. Averaging those unresolved possibilities, while keeping the published neuron's voltage scale, now gives a useful match on our three familiar cells. The flash-fitted gain version still fails. We have a concrete source of uncertainty and a promising component candidate; we still need unfamiliar recordings and later walking tests before calling the whole model biologically validated.

## Reproduction

Set `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH=src:scripts` and use `<HOME>/Lab/mech_male_fly_cns/.venv/bin/python`. The frozen script stages are `freeze`, `audit`, `prepare`, `run`, `score`; they create a new archive and refuse overwriting scientific inputs. Use a fresh versioned destination for a complete rerun; do not rerun these writers into the sealed archive. The worker requires the pinned Python3.11/NEURON8.2.7/NumPy1.26.4 environment specified in the configuration. Run `scripts/review_t4_geometry_identifiability_r2.py` against an unsealed rerun, then `scripts/plot_t4_geometry_identifiability_v1.py`. The completion utility's `check` stage only verifies the sealed evidence and writes its completion-side proof. Scientific methods and dependencies are copied into the archive before sealing.
