# Mi1 calcium benchmark V1, development-stop completion R2

Completed 2026-11-05. **No new biological validation was established.** All five
fixed candidates calibrated to zero gain on development animals. The six reserved
flies remain unscored: a zero-output candidate cannot pass the frozen strict
positive-skill criteria on any response. This is a development failure, not a
held-out biological failure or evidence that neural yaw detection is impossible.

## What was done and frozen

The [V1 protocol](MI1_CALCIUM_BENCHMARK_PROTOCOL_V1.md), code/configuration and
three synthetic alignment/gain/causality tests were frozen at commit `40e4c92`
before response inspection. The earlier metadata-only animal split was retained.
Development contains six control/four C2-silenced flies and 113 ROIs; 64 ROIs
from three control/three C2-silenced flies remain reserved. All fluorescence
processing checks metadata partition first, although MATLAB loading necessarily
reads entire files into memory. No movie or full MaleCNS simulation was needed.

Sources: [Henning et al., eLife](https://doi.org/10.7554/eLife.108529.3),
`silieslab/C2C3_feedback_Henning` commit
`745c6114b72a61dabc9389a1f024dbe22f679edf`; existing measured Mi1 kernel from
[Gonzalez-Suarez et al. 2022](https://doi.org/10.1016/j.cub.2022.06.075),
`ClarkLabCode/TimingModels` commit `100bb2f52cb9628477c3883e4b17774b0b244e67`.
Exact input/source hashes are retained in
[before_execution.json](../results/mi1_calcium_benchmark_v1/before_execution.json).
Published qualitative findings were known; only animal-level quantitative
responses had been reserved. Original models, parameters and results are unchanged.

## Models and measurements

Primary is the existing half-wave-rectified measured Mi1 branch: one-second
causal kernel with existing Laguerre/PCHIP interpolation, already deconvolved at
250 ms, followed by an explicit linear 250 ms calcium observer. There is no
second deconvolution or T4-style voltage squaring. Predeclared diagnostics use
paired 200/300 ms assumptions, a signed 250 ms branch, and the fixed 54 ms Mi1
low-pass surrogate with 250 ms observer. All are fixed except one nonnegative
global gain per candidate, fit on the six control development animal means.

Logged binary 10 Hz stimuli drive 240 Hz prediction, sampled at recorded instants.
Recordings use source `idSignal1 / mean(idSignal1) − 1`; model traces are centered
over their complete duration. Falling-edge epochs last 130 samples (13 seconds).
ROI means are averaged within fly before equal-fly calibration. No fitted offset,
latency, observer kinetics, amplitude-based exclusion or sign inversion was allowed.
Absolute luminance/retinal coverage and exact GCaMP6f calibration are unavailable.

## Development findings and explicit early stop

**All five nonnegative gains are exactly zero.** Every calibration numerator
sum(prediction × recording) is negative; denominators are positive. The algebra
is independently recalculated in
[zero_gain_algebra_r2.json](../results/mi1_calcium_benchmark_v1/zero_gain_algebra_r2.json).
Each locked candidate therefore has development skill exactly zero relative to
the zero-response baseline. On any finite nonzero test response, its skill must
also equal zero, and it ties the zero-gain simple baseline. Thus it cannot pass
the unchanged requirements of positive pooled skill, positive individual skills
and lower error than the simple baseline. No test score has been estimated from
an actual test response.

The [R2 continuation](MI1_CALCIUM_BENCHMARK_CONTINUATION_R2.md) explicitly stops
before test processing, an execution-plan deviation that preserves independent
data rather than relaxing scientific criteria. Original V1 test/review/report
stages were not run. Original V1 source, arrays, coefficient lock and hashes remain
unchanged. R2 review covers development only, never all 177 ROI responses.

## What the diagnostic reveals, and what it does not

Development inspection shows a mixture of positive and negative stimulus-related
responses across animals. The authors' plotted Mi1 comparison selects positive
stimulus-correlated ROIs; our prospectively fixed all-ROI criterion targets a
different measurement cohort. The following shape cosines use the UNCALIBRATED
primary prediction and do not hide its zero calibrated gain:

| Development animal | All ROIs | Q>0.5 | Q<−0.5 | Unscaled shape cosine |
|---|---:|---:|---:|---:|
| C2Sil / 200302_Fly2 | 11 | 7 | 0 | 0.5506 |
| C2Sil / 200302_Fly6 | 13 | 0 | 5 | -0.7062 |
| C2Sil / 200302_Fly7 | 12 | 0 | 7 | -0.7451 |
| C2Sil / 200302_Fly9 | 10 | 0 | 3 | -0.5689 |
| Control / 200217_Fly3 | 16 | 7 | 0 | 0.6349 |
| Control / 200217_Fly4 | 14 | 0 | 1 | -0.4185 |
| Control / 200218_Fly2 | 10 | 2 | 1 | -0.3663 |
| Control / 200218_Fly4 | 8 | 0 | 5 | -0.8387 |
| Control / 200302_Fly5 | 10 | 3 | 1 | -0.0961 |
| Control / 200302_Fly8 | 9 | 5 | 0 | 0.4373 |

The Q>0.5 selection is response-dependent. Its descriptive curves are retained,
but no fresh gains are fitted on that selection and no selected result rescues
primary acceptance. The primary unscaled shape cosine in the positively selected
control subsets ranges from0.631 to0.883 across four development flies. These
are selection-conditioned descriptive similarities, not calibrated predictions
or independent validation. The sign mixture is a concrete reason why a single positive
gain cannot represent this all-ROI cohort. It does not prove the measured Mi1
kernel is wrong, that inverted ROIs are artifacts, or that a specific biological
feedback pathway caused the failure. Unequal compartment signals, recording/
selection choices and the approximate observation model remain possible issues.
Separately, transient-versus-sustained waveform differences in development plots
remain descriptive and cannot uniquely identify defective circuit kinetics.

See [figure](../results/mi1_calcium_benchmark_v1/development_diagnostic_r2.png),
[all animal/model metrics](../results/mi1_calcium_benchmark_v1/development_diagnostics_r2.csv),
[summary](../results/mi1_calcium_benchmark_v1/development_summary_r2.json), and
`development_roi.npz` for every observed/unscaled-predicted curve, stimulus,
animal/fly/cell identity, epoch count and Q value. These are DEVELOPMENT evidence.

## Independent checks and resource cost

The untouched author preprocessing helper runs in Octave on only the ten
development flyIDs, using an exact-byte filename compatibility copy. All 113 ROI
epoch curves agree with Python, maximum absolute discrepancy
7.99e-15.
Independent scalar recalculation verifies 75 metric rows.
Direct convolution plus explicit observer recurrence agrees with the FFT/filter
implementation in 50 representative animal/model cases. Maximum 240/480 Hz
relative epoch RMS is 0.135796%; the unchanged 2%
guard passes: True. Three pre-execution synthetic tests also pass.
Original C2/C3 and factorial immutable indexes rehash unchanged. These checks
establish implementation consistency, not physiological correctness.

Completed development and successful analysis/verification stages used 1.58 recorded CPU seconds
before presentation; final per-stage JSON resources include presentation cost
after writer exit. Budget remains 600 CPU seconds/16 MiB new outputs/20 GiB
free reserve. No recordings or movie arrays are duplicated. One R2 independent-review exception occurred: uint8 stimulus differences
failed to detect falling edges in the verifier. Original science explicitly
used floating-point stimuli, and all113 saved epochs match the author oracle.
The failed traceback, original reviewer and oracle are preserved. The
[R3 correction](MI1_CALCIUM_BENCHMARK_REVIEW_CORRECTION_R3.md) casts only
review inputs and changes no model/result. Failed R2 review CPU was not
recorded, so successful-stage totals are a lower bound for the full attempt.
The scientific zero-gain failure remains unchanged. The unused V1 held-out driver remains reproducible source,
not executed evidence. No unsupported C2 connections were invented.

## Recommended next choices

1. Establish the intended measurement cohort using response-independent anatomy,
   ROI/compartment identity and recording quality metadata, and check why source
   animals have opposite signs. Use development data for this audit. If adequate
   independent identity criteria exist, freeze that revised component/measurement
   hypothesis before using any of the six reserved flies.
2. If such metadata cannot resolve the cohort, reproduce the authors' positive-
   correlation selection explicitly as a selection-conditioned development
   analysis. It can test reported response shapes, but cannot support an unbiased
   all-Mi1 validation claim. New recordings with independent ROI identification
   are the stronger alternative.
3. Only after the measurement target is defined, test whether independently
   constrained calcium kinetics or a different measured branch predicts its
   waveform. Do not add feedback, reverse signs per test animal, or tune a model
   against reserved responses to manufacture agreement.

The intact model was not a C2 lesion model; C2 development curves are descriptive
transfer evidence only. Recordings are female, and transfer into MaleCNS also
requires a sex/preparation qualification. Uniform-flash component agreement would
not establish T4/T5 direction tuning, HS/H2/bIPS/DNp15 physiology, fast walking or
2 deg/s reliability. Existing functional small-turn results and their physiological
limitations remain unchanged. Full biological validation is still incomplete.

## Reproduction

Use project scientific Python, `PYTHONDONTWRITEBYTECODE=1`,
`OPENBLAS_NUM_THREADS=1`, and `PYTHONPATH=src`. In a fresh versioned replay
location execute V1 `freeze`, then `development`; DO NOT execute V1 `test`.
Then execute R2 `freeze`, `analyze`, `review` (the preserved dtype failure);
execute `scripts/complete_mi1_calcium_benchmark_r3.py` stages `freeze`, `review`,
`report` and `seal`; finally execute R2 `verify` in a separate process. R3
`seal` includes the exact R3 correction sources in the archive. The original runner
uses a fixed study path; for a replay change only the output path in a separately
versioned copy, preserving sources, model and criteria. Outputs use exclusive
creation. Octave is required. Copies of code/config/protocols and a dated progress
snapshot enter the final seal after writers exit; the live progress/AGENTS files
remain outside the immutable index. No sealed old evidence is rewritten.

## Undergraduate explanation

We checked one upstream visual neuron before claiming the whole neural model is
biologically correct. Its predicted signal did not match the average of all
development recordings: some real signals changed in the opposite direction.
The best permitted fit therefore turned the model's volume to zero. Testing
that silent model on more flies could not make it pass, so we kept six test flies
unused. The next useful step is to establish which recorded signals represent
the biological response we mean to model, rather than adding arbitrary neural
wiring. This is a clearer diagnosis and preserves a fair future test, but it
does not yet complete biological validation or improve small-turn reliability.
