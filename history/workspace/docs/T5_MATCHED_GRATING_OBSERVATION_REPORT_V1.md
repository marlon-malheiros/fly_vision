# Matched T5 grating observation report, V1

Completed 11 October 2026 local time (12 October UTC). Study decision:
**`MATCHED_COMPARISON_COMPLETE_SCOPE_LIMITED`**. Detailed completion/checkpoint metadata are in
[completion.json](../results/t5_matched_grating_observation_v1/completion.json).

## TLDR

The fixed published T5 example gets the **direction of oscillation amplitude
right in all four recorded comparisons**, but its **mean direction strength
falls below our project criterion in all four**. The recordings have an
expected-direction mean in three comparisons and an opposite-direction mean
in one. Thus weak model means cannot generally be explained by saying the
recorded neuron carries direction information only in its oscillation amplitude.
The discrepancy is present under the native author stimulus, before image
sampling or downstream readout. Numerical execution was independently checked.
This is a useful limitation of this fixed model/readout, not proof that all T5
models fail or that the project is impossible. No degeneracy result is claimed.

## What changed and what was tested

The previous [image-clamp repair](PHYSIOLOGICAL_IMAGE_CLAMP_REPAIR_REPORT_V1.md)
removed a causal baseline bug and obtained convergence, but horizontal mean
criteria passed only 16/32 image conditions. This study adds a direct comparison
between **actual physiological observations** and the unchanged native T5 model.
It does not rerun T4, the population or HS/H2, nor change fitted parameters.

All eight measured grating traces from cell 7 are retained, comprising 9,248
samples and four paired conditions (two speeds × two starting phases). Samples
within traces are not independent biological replicates. The exact forward
model is evaluated at each actual 2.5-ms observation clock; clocks retain their
fractional starting times. Recordings are indexed by trial metadata and their
own one-based inclusive bounds, avoiding the known author `err_all` family-order
concatenation error.

The [prospective protocol](T5_MATCHED_GRATING_OBSERVATION_PROTOCOL_V1.md) and
21 method/input files were frozen at **2026-10-12T01:04:45.089559+00:00**, before new
grating mean/amplitude scores. The archive and historical model errors had been
examined earlier; this is a prospective new scoring protocol, not a claim that
the entire development was blind. Full source/configuration hashes are in
[the manifest](../results/t5_matched_grating_observation_v1/prospective_manifest.json).

## Training and parameter-selection provenance

The author's fitting script loads the single-bar `*_spfr.mat` dataset and masks
width-two bars. The 44 fitting traces and clocks are bitwise copies of traces in
the full single-bar archive; only 24 width-two traces, 3,748 samples, enter the
optimization objective. The archived model reproduces the saved objective:
1.603445030028503 versus
1.603445030028504 mV². Its all-fitting-trace error also
reproduces: 3.018001749227704 mV². With exact
event-aware integration, the training objective is
1.609316975149141 mV²; the small difference is retained,
not removed through refitting.

**No grating observations enter this audited objective.** Our fixed cell-7 /
iteration-52 example is the one explicitly named in the published plotting
script, acquired before this new scoring. The author's reasons for selecting
that particular example and the complete optimization/model-report history
have not been reconstructed. The population plotting script ranks models by
an `e0` field, but the producer's definition was not locally verified; this
study does not treat that ranking as additional proof. Consequently this is
stimulus-held-out relative to the audited bar objective, **not a fully blind
archive-selection experiment or independent-cell validation**.

See [provenance.json](../results/t5_matched_grating_observation_v1/provenance.json)
and [all training memberships](../results/t5_matched_grating_observation_v1/training_membership.csv).
The existing published observations suffice for this comparison; a new recording
was not required. The underlying model and data are from Gruntman, Romani and
Reiser, [the original T5 paper](https://elifesciences.org/articles/50706),
[published data collection](https://doi.org/10.25378/janelia.c.4771805.v1) and
[author model repository](https://github.com/reiserlab/T5ConductanceModel).
Local released scripts and hashed archives, rather than a recreated optimization,
provide the provenance evidence above.

The [paper's optimization methods](https://elifesciences.org/articles/50706.pdf)
also state that the top ten of 1,000 fits were selected by width-two bar error.
Its grating comparison emphasizes fitted oscillation amplitude and phase
([Figure 5](https://elifesciences.org/articles/50706)). This supports an
amplitude-direction benchmark as a next bounded target. Our one-example,
two-cycle quantile/mean comparison is not a reproduction of the paper's full
population validation, and does not refute that published result.

## Stimulus and readout definitions

Native gratings have eight phase steps per cycle and 40- or 160-ms dwell:
periods **320 and 1,280 ms**, or **3.125 and 0.78125 Hz**. Starting phases are
1 and 5. Expected direction is defined from the published phase/displacement
metadata, before inspecting voltages. Native spatial columns are not assigned
a new degree conversion. The fast stimulus differs from the earlier 500-ms /
2-Hz image condition; direct numerical equivalence is not assumed.

For each trace, subtract its own [-100,0)-ms mean, then analyze complete cycles
2–3: [345,985) ms for the fast stimulus, [1,305,3,865) ms for the slow one.
These contain 256 and 1,024 samples respectively. The initial cycle and extra
final native hold remain in saved full waveforms, excluded from these fixed
scores. The observations contain only three cycles, so this comparison is a
matched **finite-window response**, not established physiological steady state.

Primary mean is the signed arithmetic average; primary amplitude is
(q95−q05)/2 with linear sample quantiles. Both paired readouts use signed
DSI = (Rpositive−Rnegative)/(abs(Rpositive)+abs(Rnegative)). Expected direction
passes our fixed engineering criteria only when maximum absolute pair response
>=0.065 mV, absolute
direction difference >=0.065 mV and abs(DSI)>=0.1, with positive sign. A negative
resolved sign is reported rather than relabelled as a preferred direction.
These thresholds support continuity with prior project decisions; **they are
not physiological confidence limits or an author validation criterion**.

## Complete paired results

| Hz | Starting phase | Observed mean DSI | Model mean DSI | Observed amplitude DSI | Model amplitude DSI | Prospective flags |
| --- | --- | --- | --- | --- | --- | --- |
| 3.125 | 1 | -0.110111 | -0.003690 | 0.470189 | 0.349346 | RESOLVED_WRONG_SIGN_PRESENT |
| 3.125 | 5 | 0.219109 | 0.023469 | 0.120112 | 0.103703 | OBSERVED_MEAN_MODEL_INCOMPLETE |
| 0.78125 | 1 | 0.181728 | 0.091497 | 0.399052 | 0.265166 | OBSERVED_MEAN_MODEL_INCOMPLETE |
| 0.78125 | 5 | 0.224513 | 0.091518 | 0.366903 | 0.264641 | OBSERVED_MEAN_MODEL_INCOMPLETE |

Recorded primary amplitude passes 4/4 and exact-model amplitude passes 4/4.
Recorded means pass expected direction in 3/4; the other pair has resolved
opposite sign under project thresholds. Model means pass 0/4: the fast phase-1
pair fails both the difference and DSI floors; the other three fail the DSI
floor. The two slow model DSIs (~0.0915) are close to the 0.1 cutoff, so a
binary 0/4 alone exaggerates the severity. The actual magnitudes remain the
principal evidence:

| Hz | Starting phase | Observed mean Δ (mV) | Model mean Δ (mV) | Observed amplitude Δ (mV) | Model amplitude Δ (mV) |
| --- | --- | --- | --- | --- | --- |
| 3.125 | 1 | -1.588119 | -0.031036 | 3.279915 | 1.910727 |
| 3.125 | 5 | 2.202534 | 0.204629 | 0.890822 | 0.691261 |
| 0.78125 | 1 | 1.057533 | 0.765161 | 5.673509 | 3.774470 |
| 0.78125 | 5 | 1.578240 | 0.765401 | 5.186254 | 3.768979 |

The first fast recorded pair has mean preference opposite to its amplitude
preference (mean DSI −0.1101, amplitude DSI +0.4702). Retaining it prevents an
unsupported claim that the measured mean always has the expected direction.
For the other three pairs, observed mean direction strength exceeds the
fixed-model value: approximately 0.219 vs 0.0235, 0.182 vs 0.0915, and 0.225
vs 0.0915. Neither a general "mean carries no direction information" explanation
nor complete reproduction of measured direction strength is supported.

Direction agreement for amplitude does **not** establish full waveform accuracy.
Pooled model-to-observation waveform RMSE is
**4.305291 mV** over all recorded samples
and **4.020545 mV** over scored samples.
Both RMSE values use the author's relative voltage units without the new
per-trace baseline subtraction. The readout scores and plotted waveforms use
the declared per-trace baseline convention. Both recordings and predictions
are retained.

![All eight waveforms](../results/t5_matched_grating_observation_v1/matched_waveforms.png)

![Paired direction strengths](../results/t5_matched_grating_observation_v1/matched_direction_strength.png)

## Baseline, amplitude-estimator and cycle sensitivity

The largest absolute newly measured prestimulus baseline is 0.807234
mV. Repeating the mean score without the new baseline subtraction gives observed
DSIs, in the same four-pair order: **-0.115981, 0.133062, 0.303287, 0.113997**. Expected/opposite direction
classifications remain 3/4 and 1/4, and model means remain 0/4 passing; numerical
DSIs do change, so the baseline convention must accompany any reported score.

Robust amplitudes can include recording noise and non-sinusoidal harmonics.
As a separately declared secondary readout, fixed-frequency constant+sine+cosine
least squares gives observed amplitude DSIs **0.653887, 0.254201, 0.397966, 0.345620**, versus model
**0.502083, 0.192182, 0.268113, 0.267748**. All four retain expected direction under the same
engineering criteria. This supports the amplitude direction finding across
these two estimators, without supplying uncertainty or reproducing the authors'
unavailable sinusoidal-fitting function. Only a readout was fitted; circuit
parameters were unchanged.

The two retained cycle means, in mV, make drift visible without choosing a new
window after seeing results:

| Grating index | Observed cycle 2 mean | Observed cycle 3 mean | Model cycle 2 mean | Model cycle 3 mean |
| --- | --- | --- | --- | --- |
| 0 | 7.986785 | 4.848001 | 4.955091 | 3.424443 |
| 1 | 8.368490 | 7.642534 | 5.063479 | 3.378127 |
| 2 | 6.977168 | 5.277608 | 5.428821 | 3.494727 |
| 3 | 5.200960 | 2.648749 | 5.127218 | 3.387073 |
| 4 | 3.681262 | 3.195602 | 4.565793 | 4.562074 |
| 5 | 2.584263 | 2.177535 | 3.800485 | 3.797060 |
| 6 | 4.620879 | 3.986984 | 4.566717 | 4.562074 |
| 7 | 2.772738 | 2.678645 | 3.800930 | 3.797060 |

These cycles are repeated stimulus presentations within archived condition
traces, not independent experimental animals or identified trial repeats.
Do not calculate population p-values from their sample counts.

![Absolute pair differences and secondary checks](../results/t5_matched_grating_observation_v1/matched_response_differences.png)

## Technical validation and limits of the audit

- **14 focused tests passed**, covering native dynamics and
  recording alignment plus fractional clocks, incomplete recordings, baseline
  offsets, phase wrapping, signed inhibition, zero denominators and conflicting
  mean/amplitude preferences.
- All eight recordings and clocks match direct extraction from their original
  raw bounds bitwise; the 11 parameters match the source archive bitwise.
- A separate numerical review compares all eight exact waveforms with the
  previously saved tight, event-split author RHS solver. Maximum error is
  **2.10796713418e-10 mV**, below the frozen
  1e-8-mV tolerance.
- Independent sums, sorted-quantile interpolation and harmonic normal equations
  differ by at most **1.06581410364e-14**.
  All 48 primary/secondary pair scores and failure flags agree with independent
  arithmetic. The review is a separate implementation run by this agent, not a
  blinded external scientific reviewer.
- The released numerical archive itself differs from the exact model by at
  most 0.083527272 mV across these gratings. Its primary direction pass
  counts are the same as the exact model: amplitude 4/4, mean 0/4. Thus this
  interpretation is also present in the released archive, not introduced by
  our exact integration.
- All four predecessor indexes and 10,048 indexed entries
  passed verification before new scoring; completion metadata records the
  corresponding final verification. Counts overlap between indexes and are
  not numbers of unique biological observations.

See [technical review](../results/t5_matched_grating_observation_v1/independent_review.json),
[test record](../results/t5_matched_grating_observation_v1/focused_tests.json),
[complete trace metrics](../results/t5_matched_grating_observation_v1/trace_metrics.csv),
[all pair metrics and failures](../results/t5_matched_grating_observation_v1/pair_metrics.csv),
and [per-cycle/readout values](../results/t5_matched_grating_observation_v1/trace_metrics.json).
These checks establish reliable computation for this assay; they do not provide
new neurons, physiological noise bounds or validation of image transfer/T4/HS/H2.

## Scientific conclusion and next step

**The weak-mean issue is already visible in this fixed published T5 example
under its native grating protocol.** It cannot generally be attributed solely
to our image sampling or to absent mean selectivity in the measured neuron.
Numerical implementation agrees with the author RHS and the archive reproduces
the same primary classifications. This identifies a limitation in prediction
of this readout by this fixed parameterization; it does not isolate which
biophysical mechanism or additional parameter would resolve it.

The project now has a defensible narrower result: causal software repair,
convergence, and a matched physiological comparison that separates amplitude
direction success from mean-response discrepancies. Biological population
validity and neural degeneracy remain unestablished. Texture sign reversals
remain unexplained by this experiment.

The next bounded task should use amplitude direction as the supported native
T5 benchmark and compare a metadata-matched OFF grating passed through the image
frontend with the exact native schedule, holding parameters fixed. Such a
comparison tests image transfer without demanding that a mean criterion already
missed by the native example suddenly pass. It must preserve both mean and
amplitude diagnostics and prospectively state the spatial mapping. If the
scientific objective requires quantitative mean-voltage prediction, a separate
model-development and held-out validation plan is needed; changing thresholds
or choosing successful phases would not establish that accuracy. This new task
has not been executed here.

## Development tracking and reproducibility

User-requested ongoing progress is in
[the live progress report](PROJECT_PROGRESS_REPORT.md); its dated completion copy
is [the study snapshot](../results/t5_matched_grating_observation_v1/project_progress_snapshot.md).
The live report and `AGENTS.md` remain outside immutable artifact indexes so
future updates can be recorded without breaking completed-study seals. Git
tracks source/configuration/tests/docs; study artifacts remain linked by hashes
in [the new index](../results/t5_matched_grating_observation_v1/artifact_index.json).
Git checkpoints are in [git_snapshots.json](../results/t5_matched_grating_observation_v1/git_snapshots.json).
These local records support an auditable report; they do not provide off-device backup.

Reproduction entrypoints (from repository root, with NumPy/SciPy/Matplotlib/pytest
available) are the `provenance`, `prepare`, `analyze`, `review` actions in
`scripts/run_t5_matched_grating_observation_v1.py`, then this report generator and
`scripts/seal_t5_matched_grating_observation_v1.py`. Run each study in a fresh
copy with a new output directory/version; the completed V1 directory must remain
immutable. The source simulator is reused unchanged; no optimizer is called.
