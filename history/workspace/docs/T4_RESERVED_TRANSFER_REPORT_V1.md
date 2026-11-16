# Reserved T4 stationary-to-motion transfer V1

Completed2026-11-06. Prospectively defined project-reserved component test; original-author stationary-fit cohort overlap remains explicit.

## Outcome and stopping decision

**The frozen physical-mV geometry ensemble passes the predefined waveform rule on the reserved motion responses.** Its pooled mean squared prediction error is33.13% below the early-only direction-blind reference, with zero skill0.726160, reference skill0.331340 and joint bootstrap lower statistic0.102679. No later motion response fitted a gain, delay, registration, neuron parameter or candidate choice. This is useful new, restricted physiological prediction evidence for the published T4 component. It qualifies this candidate for further integration work; it is not whole-circuit biological validation or a successful small-yaw walking experiment.

The result is uneven: cell6 is0.68% worse than the direction-blind reference, while cells7/8 improve69.55%/57.23%. All three remain included, and the frozen criterion did not require positive reference skill in every cell. With three cells, the discrete27-bootstrap statistic is an admission rule, not a precise population confidence interval. Cell8's flash registration selects the grid boundary. Inhibition remains unqualified. No claim that the candidate is accurate for all motion conditions or all flies follows.

The [protocol](T4_RESERVED_TRANSFER_PROTOCOL_V1.md) fixes this candidate as primary before new response use, following its secondary success in the [geometry diagnostic](T4_GEOMETRY_IDENTIFIABILITY_REPORT_V1.md). Had it failed, this registration-only candidate route would stop without another tuning round on these cells. It passes, so the supported next milestone is explicit, separately versioned frontend integration followed by walking requalification.

## Recordings and exposure boundary

The source is the existing public Gruntman2017 archive, Figshare file9691765. The author assignment identifies original cells6/7/8 by dates20160504/20160505/20160510. All three were reserved by the project before this round. Cell6's author-assigned motion files split40/80ms and20/160ms dwell conditions; both are included based on that pre-outcome metadata. This new protocol intentionally uses both, rather than silently changing the earlier conditional earliest-file selection. These are bar-motion dwell values, not walking speeds.

Seven selected MAT members total298,112,788bytes; no full2.84GB archive, earlier raw copy or generated movie was acquired. Every member passes exact HTTP byte-range/length checks, original decompressed size/CRC32 and SHA256 receipts. An initial sandbox DNS failure is preserved; the authorized network retry succeeds. [Acquisition freeze and member records](../results/t4_reserved_transfer_v1/before_acquisition.json).

| Author cell | Flash trials / conditions | Motion trials | Early motion localization | Later scored PD/ND trials |
|---|---:|---:|---:|---:|
|6|220 /44|96 across two files|32|16|
|7|260 /52|96|32|16|
|8|340 /68|96|32|16|
|Total|820 /164|288|96|48|

First3 flash repetitions calibrate492 trials; last2 assess328 repeat trials. The48 later motion repetitions produce24 PD/ND×dwell condition means. The remaining144 later repetitions in other directions are not scored. All raw arrays necessarily load with the MAT file, but late response amplitudes are not processed or used for model selection before the numerical gates and calibration/prediction locks.

The published cable was fitted by its authors to population stationary responses from this experiment. The new test is therefore prospective with respect to this project's reserved moving responses, not independent of the author's stationary-fit cohort or laboratory. Per-cell early moving responses localize direction, and stationary responses calibrate registration/timing. This is stimulus-transfer testing with permitted calibration, not zero-calibration independent-animal prediction. Four C2/C3 animals remain unscored.

## Frozen candidate and execution

Pre-outcome code/protocol commit`11582a4`. The [method lock](../results/t4_reserved_transfer_v1/method_lock.json) precedes localization/calibration and hashes sources, scientific code and configuration. Preserve the original344-section cable,12 parameters, seed300,99 excitatory/55 inhibitory sites, eleven2.25deg-spaced inputs and actual-image/event sampler. The original delivered frontend, MaleCNS graph and network parameters are not changed.

Each earliest orientation/dwell repeat supplies the existing99.5th-percentile PD localizer; first-three stationary repeats fit the same five offsets,51 causal delays and analytic nonnegative scalar gain. Primary voltage gain remains1; the fitted gain is used for registration selection and the diagnostic only. All765 grid fits are saved. All25 two-dimensional integer shifts are evaluated from stationary images; equally average every exact input alias of the selected shift. The ensemble represents unresolved input geometry, not a newly inferred anatomical circuit or measured distribution of RF positions.

| Cell | Early-only PD orientation / axis | Flash offset (LED pitches) | Delay (ms) | Diagnostic flash gain | Exact2D aliases(dx,dy) |
|---|---|---:|---:|---:|---|
|6|6 /(0,−1)|+1|28|1.552090269|(−2,−1),(−1,−1),(0,−1),(1,−1),(2,−1)|
|7|4 /(−1,0)|+1|24|1.189632381|(−1,0),(0,−1)|
|8|0 /(+1,0)|−2|38|1.360531743|(−2,0)|

Cell8 reaches the prespecified spatial boundary; the grid was not widened after inspection. Cell6's aliases also give identical moving inputs, so caching avoids redundant solves. All fits and aliases are locked before the motion prediction list, and all later observations are scored after the numerical guard. [Calibration lock](../results/t4_reserved_transfer_v1/calibration_lock.json), [alias lock](../results/t4_reserved_transfer_v1/alias_lock.json), [prediction lock](../results/t4_reserved_transfer_v1/prediction_lock.json).

## Quantitative result

Native20kHz voltage is converted to mV and baseline-subtracted on[−250,−50)ms. Compare half-open2ms means over[0,nominal motion duration+250ms), preserving the earlier endpoint convention. Average repetitions, equal conditions within each cell and then equal cells. Reference skill is1−MSE/referenceMSE; the direction-blind reference averages early PD/ND responses at each dwell. The existing rule requires positive pooled zero/reference skills, positive zero skill per cell and positive5th percentile joint minimum skill across all27 exact cell-bootstrap resamples. Neither pass thresholds nor endpoints were relaxed.

| Readout | RMSE(mV) | Zero skill | Direction-blind skill | Joint lower statistic | Waveform rule |
|---|---:|---:|---:|---:|---|
|**Frozen primary: physical-mV ensemble**|4.872612|0.726160|0.331340|0.102679|**Pass**|
|Diagnostic: same ensemble×flash gain|4.662535|0.749263|0.387755|0.226646|Pass|

| Cell | Primary zero skill | Primary direction-blind skill | Diagnostic direction-blind skill |
|---|---:|---:|---:|
|6|0.715247|−0.006834|0.462344|
|7|0.796698|0.695480|0.550609|
|8|0.683413|0.572348|0.011275|

The diagnostic does better in aggregate but is not promoted after inspection. Physical primary predictions already clear the rule. These scores measure complete time-course error, not just matching a peak or choosing the correct direction. They do not establish exact biophysical equivalence, a behavioral detection threshold or robust out-of-distribution performance.

Stationary reserved repeats also pass: physical-mV readout RMSE3.068731mV, zero/spatial-blind skills0.625520/0.321202, joint lower0.199906. The gain-fitted diagnostic has skills0.670102/0.402014, lower0.194352. The unchanged no-registration cable also passes this repeat criterion; stationary success alone does not demonstrate that new registration is necessary. The present motion test qualifies the candidate, but without a new intact-versus-no-ensemble motion ablation it does not establish that averaging caused the reserved-data improvement.

[Final decision](../results/t4_reserved_transfer_v1/decision.json), [48 motion condition-output scores](../results/t4_reserved_transfer_v1/condition_metrics.csv), [waveforms](../results/t4_reserved_transfer_v1/figures/reserved_waveforms.png), [per-cell comparison](../results/t4_reserved_transfer_v1/figures/reserved_skill.png). Full compact predictions, individual observed repeats, all flash trials/grids and exact bootstrap arrays are retained.

## Inhibition and model limitations

The unchanged early160ms ND masks contain0/362/63 bins in cells6/7/8. The later scored mean is positive within both nonempty masks: cell7 recorded+2.965795mV versus predicted+2.333537; cell8 recorded+2.730186 versus predicted+2.248477. No cell confirms sustained negative voltage in those later windows; inhibition is therefore unqualified, not validated. The early-to-later disagreement is preserved rather than used to exclude cells or redefine the mask. [Signed means](../results/t4_reserved_transfer_v1/inhibition_review.json).

Other limits: only three project-reserved cells, original-author population training overlap, per-cell stationary/early-motion calibration, finite RF grid, one boundary selection, unmeasured distribution over geometric aliases and no evaluation of T5 or downstream HS/H2/bIPS/DNp15 physiology. A somatic-voltage prediction is not automatically a quantitatively identified transmitter-release signal. Any bridge into the existing connectome drive must be explicit and separately tested; integration cannot be claimed from this component assay alone.

## Numerical checks, independent review and corrections

All guards retain0.005mV maximum error. Eight pulse-duration midpoint checks pass(max7.672222e−5mV),12 actual-image/template checks pass(max0.000315871mV), and12 motion0.1→0.05ms solver refinements pass(max0.003022693mV). A final independent calculation reproduces all24 actual-image/solver errors. These are numerical reproducibility evidence, distinct from physiological prediction.

The independent reviewer reconstructs820 flash traces,96 early localizers,765 registration fits, all75 image registration stacks, motion image/event inputs,48 scored repetitions,24 motion means, references and bootstrap metrics. Max native-bin difference7.11e−14mV, grid difference1.78e−14, readout difference9.77e−14, metric difference1.46e−13. It checks571,956 scalar pixel evaluations and four identical source-parameter/site audits; all234 immediately preceding indexed geometry-study files remain unchanged. [Review](../results/t4_reserved_transfer_v1/independent_review.json), [final numerical checks](../results/t4_reserved_transfer_v1/final_numerical_review.json).

The initial cell6 schema combiner double-offsets original stimulus labels in its second file, causing an IndexError before response amplitudes are used. Initial script/diagnostic are preserved; [R2 metadata correction](T4_RESERVED_METADATA_CORRECTION_R2.md) maps original labels to local arrays and validates assigned movie lengths without changing raw bytes or science rules.

A reused flash helper retains legacy descriptive fields:`primary=flash_calibrated` names its gain-fitted flash output, while `new_moving_data_opened=false` is literally inaccurate if read as saying no early motion localizers were processed in this new study. The scientific protocol's primary is physical-mV; early moving repeats were processed and later test voltages were still unscored at that flash stage. Preserve the helper output and use the explicit [scope correction](../results/t4_reserved_transfer_v1/flash_scope_correction_r2.json). No score, source split, primary motion decision or acceptance criterion changes.

## Resources, preservation and reproduction

228 new NEURON solves:132 flash-duration templates,8 midpoint checks,12 actual-image parity checks and76 motion/refinement solves. Scientific worker CPU42.218520s; peak worker RSS887,058,432bytes. These counters exclude acquisition wall time, parent fitting/preparation, independent review, figures and hashing. Network retrieval was the main wall-clock delay. Raw298,112,788bytes are kept once; permanent384MiB cap and20GiB free reserve remain. No new movies, whole-brain solve, closed-loop action or old-model update.

Use `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH=src:scripts` with the existing project Python. Source stages in `scripts/t4_reserved_acquire_v1.py`:freeze/acquire selected member IDs. Scientific stages in `scripts/t4_reserved_transfer_v1.py`:metadata,freeze,localize,plan_bank,bank,fit,flash_test,numerical,aliases,prepare_motion,run_motion,score. These writers use exclusive files; rerun only in a separately versioned destination, never into the sealed study. Worker environment is pinned Python3.11/NEURON8.2.7/NumPy1.26.4. Independent reviewer and completion utility reproduce scores, generate figures and snapshot/seal results. A dated progress copy and method sources precede sealing; `completion_v1/post_exit_integrity.json` records a separate-process rehash after all writers exit. Live AGENTS/progress remain outside the immutable index.

## Undergraduate explanation and next milestone

We want a neural model that helps explain how a fly notices a small turn while walking. T4 is an early motion-sensitive neuron, so we first ask whether its model predicts real electrical recordings. Previously we found that stationary pictures can leave its retinal location ambiguous. We froze a method that averages those unresolved locations and tested new reserved motion responses without adjusting the model to their answers. It passes our limited rule and predicts better overall than a reference that ignores motion direction, although one cell is slightly worse. That is a concrete biological prediction result worth keeping. It does not yet show that the complete fly circuit detects tiny turns reliably.

Next: build a separately versioned integration of this qualified T4 reference with an explicit voltage-to-network-input bridge, preserve the functional frontend as baseline, and rerun the frozen walking comparisons. Treat T5, downstream physiology, inhibitory behavior and the2deg/s walking criterion as separate outstanding tests. Do not spend another round fitting these now-inspected three cells or claim full biological validation from their passing waveform score.
