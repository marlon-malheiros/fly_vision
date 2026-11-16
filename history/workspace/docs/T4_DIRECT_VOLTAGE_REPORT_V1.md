# T4 image-to-direct-voltage component test V1

Started2026-11-05, finalized2026-11-06. Scientific-method freeze `a294b52`; source-admission freeze
`1a58318`; subsequent numerical-review correction freeze `8239f27`.

The unchanged T4 source mechanism **does not pass this restricted predictive
test**. Its current delivered output improves on zero response but performs
worse than a direction-blind physiological reference. Retaining the signed
internal branch signal improves prediction error in all three test cells, but
also fails that reference and the frozen uncertainty criterion. This round
does not establish biological validation or new small-turn reliability.

The important advance is a stimulus-matched, direct-electrical benchmark:
actual LED images and native display-event logs are now linked to individual
T4 voltage trials. It removes calcium-conversion uncertainty from this test.
Numerical reproduction succeeds after an explicitly preserved audit correction;
this is distinct from the negative biological prediction result.

## Question and scope

Does the existing published-source T4 mechanism, evaluated on the experiment's
actual images and timing, predict later electrical responses in other cells?
Does preserving its signed internal signal fix the loss associated with the
current rectifying output interface?

This is a **canonical preferred-direction-axis source-component assay**.
`delivered_drive` is an external input representation, not a simulated MaleCNS
T4 membrane state. `signed_branch` is the potential-like quantity inside its
source circuit, not an identified voltage-to-release interface. A single
development-only gain maps each representation to baseline-subtracted recorded
mV for prediction. Neither gain is physiological conductance calibration.

No original graph, frontend parameter, synapse, neuronal routing or walking
decoder changed. No full MaleCNS solve or new walking experiment was run.

## Source and prospectively fixed split

[Gruntman, Romani and Reiser (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5967973/)
provides whole-cell T4 recordings and moving-bar experiments. The
[public deposit](https://doi.org/10.25378/janelia.5576101) contains author cell
assignments, protocol structures, actual display movies and voltage timestamps.
Author extraction/stimulus code establishes channel and image conventions.

Five cells were selected by the first five published assignments/dates before
individual voltage-response scoring; response quality never selected cells.
Only the five required MAT members were fetched from a2.84GB ZIP, using exact
HTTP ranges, length/CRC32 checks and SHA256 receipts. Raw storage is
176,689,947bytes, retained once. No full archive or generated movie was stored.

| Cell | Date | Partition | Early-localizer PD label | Canonical axis in stored image coordinates |
| --- | --- | --- | --- | --- |
| 1 | 2016-04-20 | Development | 6 | (0,−1) |
| 2 | 2016-04-26 | Development | 5 | (−1/√2,−1/√2) |
| 3 | 2016-04-27 | Test | 0 | (1,0) |
| 4 | 2016-04-28 | Test | 6 | (0,−1) |
| 5 | 2016-05-02 | Test | 6 | (0,−1) |

Each cell has96 trials:8 orientations×4 dwell times×3 repetitions. First
chronological repetitions localize the PD axis; the later two repetitions of
PD and ND provide the scored responses. Thus160 early localizer traces and80
later trials yield40 mean conditions,24 in test cells. No scored response sets
axis, gain, RF center, exclusions, lag or filter. Test-cell localizers were
processed only after development gains and numerical controls were locked.

Earlier project work had inspected pooled figures and author assignments;
these raw individual waveforms/scores were new at the experiment freeze. This
is a prospectively separated prediction test with partial prior source exposure,
not a wholly untouched literature benchmark. All five cells are now inspected
data for future model development. Four previously reserved C2/C3 animals
remain unscored.

## Input and measurement reconstruction

Every admitted file contains32×96,3-bit LED images, recorded frame events and
20kHz voltage samples. Display patterns advance nominally at50Hz; event logs,
including jitter and the frame0 reset, determine each simulated frame. The
recorded degree spacing is2.25deg/LED. Bar dwell times are20/40/80/160ms.
Movie centroids determine physical trajectory; diagonal movies retain the
author's longer pixel paths rather than being replaced by cardinal motion.

Stored rows require a vertical coordinate conversion:
`[gridCenter.x−1, nrows−gridCenter.y]`. All five movie centers match that
source convention. The response-localized axis is transported to a canonical
one-dimensional T4 mechanism; it is not absolute anatomical T4a/b/c/d validation.
Linear LED luminance, local Cartesian angular geometry, the longitudinal RF
and unreconstructed transverse integration remain modeling assumptions.

The fixed source mechanism uses its existing5.7deg Gaussian, measured Mi9,
Mi1, Tm3, Mi4 and CT1 temporal filters,5deg offsets, relative conductances and
reversal values. Physical7×7 contrast-energy normalization retains the existing
sigma. Piecewise-constant pixels use symmetric boundary weights; outside-panel
padding stays grey. These operations do not add anatomically unverified edges.

Native voltage is author channel3×10mV, baseline[-250,−50)ms. Outputs and
observations are compared in2ms bins, from motion onset through nominal motion
duration+250ms. Each representation subtracts its own pre-motion baseline.
Equal condition/cell weights prevent longer slow-motion trials dominating the
gain and MSE. Both gains are nonnegative, zero-intercept fits from cells1–2;
there is no time shift, offset fit, direction reversal or architecture search.

## Frozen comparisons and outcomes

Reference0 predicts no voltage change. The stronger reference is direction-blind:
at each dwell it averages that cell's early PD and ND traces, then predicts the
later repetitions. It is an empirical, cell-specific comparator with privileged
early response information, not an image-to-neuron circuit. Passing it would
show useful prediction beyond that simple early-trial reference.

Skill is `1−model_MSE/reference_MSE`; zero means equal performance, negative
means worse. Report pooled error across equally weighted cells, all per-cell
scores, and all27 exact three-cell bootstrap resamples. A waveform pass requires
positive skills against both references, positive zero skill in every test cell
and a positive5th percentile of the joint minimum bootstrap skill. This is a
restricted prediction rule, not an equivalence margin for biological validity.

| V1 metric | Current delivered output, primary | Signed internal branch, diagnostic |
| --- | ---: | ---: |
| Locked development gain | 59.902050 | 0.20107736 |
| Test RMSE, mV | 8.013764 | 7.272245 |
| Skill against zero | +0.097106 | +0.256466 |
| Skill against direction-blind reference | −1.693805 | −1.218350 |
| Joint bootstrap lower5th percentile | −1.945120 | −1.504460 |
| Waveform criterion | Fail | Fail |
| Qualifying confirmed inhibition masks | 0/3 | 0/3 |
| Restricted component criterion | Not met | Not met |

Keeping the signed branch lowers pooled MSE by17.65% relative to the current
output. This is a within-assay computational benefit, insufficient to qualify
the component and not evidence that direct signed injection is a biological fix.

| Test cell | Primary zero skill | Signed zero skill | Primary direction-blind skill | Signed direction-blind skill |
| --- | ---: | ---: | ---: | ---: |
| 3 | +0.128439 | +0.334582 | −1.573280 | −0.964643 |
| 4 | +0.099176 | +0.204588 | −2.113956 | −1.749566 |
| 5 | +0.058342 | +0.243662 | −1.362368 | −0.897450 |

The predicted responses do not capture the measured amplitudes and complete
waveforms across dwell times under the locked calibration. Both current and
signed representations are worse than the empirical comparator in every test
cell. These discrepancies cannot be attributed solely to calcium kinetics:
this test uses electrical voltage. They also do not identify one unique missing
synapse or show that every possible T4 implementation must fail.

The independent inhibition requirement sought≥20ms below−3 baseline-bin SD in
the160ms-ND early trial, confirmed negative in later repetitions, in at least
two test cells. **None qualifies**. Visible negative excursions in some traces
do not override this rule. Thus the inhibition gate is unqualified by this
sample, not evidence that a model predicted the wrong inhibitory sign. The
waveform criterion independently fails, so missing inhibition evidence cannot
explain away the overall rejection. No cell, time window or threshold was
changed to obtain a different result.

Figures: [all held-out waveforms](../results/t4_direct_voltage_v1/figures/heldout_waveforms.png),
[per-cell skills](../results/t4_direct_voltage_v1/figures/heldout_skills.png).
PDF copies are alongside them. Complete scores:
[V1 decision](../results/t4_direct_voltage_v1/decision.json),
[80 condition-output rows](../results/t4_direct_voltage_v1/condition_metrics.csv).

## Numerical results, failures and correction

Three focused synthetic tests pass: signed/rectified source parity, pixel-edge
sampling and binning/localizer-mask independence. All16 temporal/spatial checks
pass the frozen5% normalized-RMS bound. Maximum change is0.00942086, or0.9421%.
Temporal and spatial refinements were separate, on development cell1 PD/ND at
20/160ms, not universal convergence proof for every possible stimulus.

The scalar input audit independently checks87,150 pixel evaluations and119,400
frame-edge queries, the native50us sampling interval on all480 trials, geometry
and decision gates. Maximum normalized pixel discrepancy is1.11e-15.
[Input/gate evidence](../results/t4_direct_voltage_v1/input_and_gate_review.json).

The following failures are preserved:

1. Before voltage scoring, the first schema helper expected a terminal frameN.
   Actual controller logs reset to0. Its assertion and initial helper remain
   archived; the correction preceded the scientific freeze. It did not corrupt
   source files or change acceptance criteria.
2. After outcomes, the first independent response reviewer failed its1e-8mV
   tolerance. Producer microseconds×1e-6 and reviewer microseconds÷1e6 differ in
   floating-point edge membership when a native sample lies exactly on a bin.
   Three of80 later repetitions differed above roundoff; maximum0.0249542mV.
   This was a real boundary-convention discrepancy, not cumulative-sum error.
   Original reviewer, failure and primary V1 results remain unchanged.
3. The first completion utility rejected older artifact-index records before
   any snapshot or seal was written: old indexes use `size_bytes`, newer ones
   use `bytes`. Whole-dictionary equality falsely reported differences despite
   identical hashes and sizes. The initial utility and diagnostic are archived;
   the corrected completion utility explicitly compares SHA256 and either size
   field. No old artifact was modified or scientific outcome recomputed.

The separately frozen [R2 correction](T4_DIRECT_VOLTAGE_REVIEW_CORRECTION_R2.md)
first reproduces V1 with the literal producer conversion and independent direct
sums. All160 localizers,40 scored means, gains and54 bootstrap pairs agree:
max bin discrepancy9.11e-11mV; metric/bootstrap discrepancy1.42e-14.
[Review evidence](../results/t4_direct_voltage_v1/independent_review_r2.json).
All175 indexed artifacts from the preceding source/observation studies rehash
unchanged.

R2 also independently re-bins exact integer microseconds into half-open2000us
bins, retaining all model forecasts. PD axes stay identical in all five cells.
Three scored repetitions change; maximum single-bin change0.0383089mV versus
V1, maximum localizer-bin change0.0345696mV. It recomputes the same development
gains and every outcome without scientific retuning:

| Exact-tick R2 sensitivity | Current output | Signed diagnostic |
| --- | ---: | ---: |
| Skill against zero | +0.09710603 | +0.25646668 |
| Skill against direction-blind reference | −1.69382186 | −1.21836270 |
| Joint bootstrap lower bound | −1.94515571 | −1.50448928 |
| Restricted criterion | Not met | Not met |

[R2 full outcomes](../results/t4_direct_voltage_v1/clock_sensitivity_r2/decision.json)
and separate corrected response archives preserve numerical evidence. This is
a post-outcome numerical sensitivity on inspected cells, not another fresh
biological experiment. It leaves the scientific verdict unchanged. Future
native-clock analyses should use exact tick bins from the start.

## Supported conclusions and next decision

Supported: direct-voltage data with usable actual stimuli exist; a matched
source-component benchmark is feasible; a signed internal signal retains useful
predictive information, yet neither current interface meets the frozen test.
Numerical consistency is established within the stated checks. The previous
static T4c indicator-transfer result remains a separate limited success; it
does not validate image-to-T4 dynamics tested here.

Not established: full T4/T5 physiological validity; inhibitory equivalence;
absolute subtype/retinotopic validity; HS/H2/bIPS/DNp15 validation; reliable2deg/s
yaw in walking; biological causality; or impossibility of a successful model.
The three-cell test and same-experiment canonical-axis transport limit breadth.
Direct voltage itself is not a substitute for an identified synaptic release
model or the downstream circuit.

The next justified development choice is a separately versioned **T4 dynamics
reconstruction**, using these now-inspected matched data as development evidence.
First reproduce an author-supplied T4 circuit and its native stimulation/voltage
analysis, then identify which image normalization, RF integration or dynamics
assumption causes the remaining mismatch. These are candidate explanations,
not diagnosed causes. Do not add a new calcium observer or tune the whole graph
to rescue this electrical test. Any candidate should be frozen before a
different, independent validation cohort is scored; the reserved C2/C3 calcium
animals address a different component and are not automatically a suitable
direct-voltage validation set. Reconnect a qualifying component to MaleCNS
before repeating small-turn qualification.

## Reproduction, storage and archived evidence

Environment: repository Python environment
`<HOME>/Lab/mech_male_fly_cns/.venv/bin/python`, `PYTHONPATH=src`,
`PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`. Raw author methods are
referenced by hashes in the source records. Source and experiment protocols:
[admission](T4_DIRECT_VOLTAGE_ADMISSION_PROTOCOL_V1.md),
[dynamics](T4_DIRECT_VOLTAGE_PROTOCOL_V1.md). Execute acquisition only in a fresh
output directory, then metadata admission, `freeze`, `development`, `test` in
`scripts/t4_direct_voltage_v1.py`. Successful stages intentionally refuse to
overwrite outputs. The freeze stage must precede any response transforms.

Run `scripts/review_t4_direct_voltage_inputs_v1.py`, then the preserved first
reviewer to reproduce its expected boundary failure. Run
`scripts/review_t4_direct_voltage_r2.py freeze` and `run` for the successful
continuation and integer-clock sensitivity. Generate figures with
`scripts/plot_t4_direct_voltage_v1.py`. Run the three tests in
`tests/test_t4_direct_voltage_v1.py`. No new movie creation or full graph solve
is necessary. The completion utility snapshots methods/progress, seals after
all writers exit, and verifies in another process.

Scientific stages consume178.998CPU seconds in total; peak recorded process
RSS is1,259,872,256bytes. These counters exclude source acquisition, plotting,
independent reviews, failed reviewer and other startup work; they are not total
project CPU. Archive size before method/progress copies is about183MB decimal,
well below320MiB; no source data were duplicated. All sealed old results and
the four C2/C3 holdout animals are preserved. Numerical guards, failed checks,
metadata, localizers, individual trial forecasts, mean traces and bootstrap
arrays are retained in `results/t4_direct_voltage_v1/`.

## Undergraduate explanation: what we want, what we did, why

We want a neural model that explains how a fly notices a small turn while
walking. T4 cells are an early stage that detects image motion. This round
showed the model the actual images used in a real experiment and compared its
predictions with electrical recordings, so calcium indicators could not hide
the problem. Keeping the model's negative as well as positive signal helped,
but its predictions were still less accurate than a simple reference built
from early recordings. We therefore have a better test and a clearer early
stage to improve; we do not yet have biological validation of the walking
circuit. We should repair and independently test that stage before spending
more computation on the full walking model.
