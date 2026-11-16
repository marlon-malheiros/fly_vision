# Mi1 validation resolution V2 — audit and finite alternatives

2026-11-05. New study, preserving the complete V1 archive. Before this freeze,
V1 development responses and Q counts are known. The metadata audit confirmed
all development quality fields are zero, driver/compartment labels do not explain
sign, native fluorescence means are positive, and raw/interpolated stimuli have
the expected polarity. No reserved fluorescence has been processed. Known paper
and V1 results motivate these new hypotheses; they are not preregistered V1 rules.

## Fixed questions and finite alternatives

1. Verify all V1 indexed bytes, zero-gain algebra, saved epochs, source-matching
   preprocessing and float/uint8 handling. V1 all-ROI failure does not establish
   failure of the authors' positive-response cohort. Record that correction.
2. Audit response-independent metadata and native-vs-interpolated traces on
   development only. No threshold based on a reserved response.
3. Reproduce author-like Q>0.5 selection descriptively on development data.
4. Qualify ROIs on EARLY repetitions only and predict LATER repetitions. Preserve
   six animal partitions unchanged. No late repetition influences selection,
   fluorescence normalization, coefficient fitting or candidate choice.
5. Compare six existing fixed dynamics: V1 five candidates and the already
   source-supported 54 ms low-pass/318 ms high-pass Mi1 proxy with rectification
   and 250 ms observer. No altered connectivity or physiological parameter.
6. Test two clearly labeled measurement/reference alternatives: all-ROI prediction
   with polarity determined on early repetitions, and a per-ROI early-response
   template predicting later repetitions. Neither is an anatomical neural model
   or a biological noise ceiling theorem. They diagnose repeatability/cohort
   mismatch; success cannot rescue biological acceptance.

## Independent repetitions and normalization

Use falling edges of FLOAT stimulus arrays. Complete cycles must have the next
falling edge; score the first98 samples (0–9.7s) only. Require every cycle interval
>=99 samples. This avoids the previous13s windows' overlapping repetitions.
Use the first floor(Ncycles/2) cycles as localizer, omit the next whole cycle as
guard, and use all remaining complete cycles for evaluation (at least3 each).
F0 is the mean of early localizer samples only; observed early/late curves equal
F/F0−1. A common frozen normalization lets late drift appear as error rather
than fitting it away. Model traces are centered on the same early indices.

Positive-responsive qualification is corr(early response mean, early stimulus
mean)>0.5, using the authors' threshold but different repetitions for scoring.
No response-amplitude exclusion. For the polarity diagnostic, use sign of that
same early correlation for every ROI; no ROI exclusions or late sign flips.
The early-response template uses no late data and has no fitted amplitude.
All raw floats, masks, cycle indices, fluorescence F0, early/late stimuli/curves,
predictions and animal IDs are saved. Complete MAT containers load in memory,
but fluorescence access is restricted to the current partition/phase.

## Development, locking, test and scope

Fit one nonnegative global amplitude per dynamics/selection analysis from early
control development animal means. No offset or latency fit. For positive-ROI
models, choose ONE candidate among the five nonbaseline dynamics using
leave-one-development-animal-out prediction of late repetitions. Rank by pooled
CV MSE, break ties by listed order (measured250 rectified,200,300,signed,adapted54).
All six models' diagnostics are retained. Baseline54 gain is fitted separately.
No hyperparameter grids. The chosen model, gains, CV results and code are locked
before processing any reserved fluorescence.

Reserved animals: process early cycles ONLY, save masks/F0/indices and hash-lock
them before accessing late fluorescence. Then evaluate all fixed candidates
once on late repetitions; no tuning or repeat testing. Report animals with no
qualified ROI as noncoverage, not a biological model failure. Predeclared limited
positive-Mi1 component acceptance requires at least2/3 qualified control test
animals; all qualified control animal skills>0; pooled skill>0; lower pooled MSE
than the development-calibrated54ms baseline; numerical checks pass. This is
experiment-specific predictive agreement, not full biological validity. Three
test animals cannot establish a robust population threshold or equivalent
physiology. No new yaw or full-circuit claim regardless of outcome.

C2-silenced animals use the intact calibration as a cross-condition challenge;
no invented C2 efficacy. Report perturbation mismatch without treating it as a
simulated lesion. The all-ROI polarity diagnostic reports separate predictive
skill and its unsupported observation-sign assumption, never neural validation.
The repeat-template reference diagnoses temporal repeatability, not a maximum
possible biological accuracy. Quantify all failures and noncovered animals.

## Independent verification and closure

Before outcomes test unsigned falling edges, strict repetition non-overlap,
late-response noninterference with masks/F0, and causal observer. Independently
reconstruct stored curves from native/resampled source and retained cycle lists;
verify all scalar gains/errors without the metrics helper. Check 240/480Hz
unscaled predictions for one ROI per each of16 flies, all6 models, <=2% relative
epoch RMS; direct convolution/explicit recurrence for measured models and
independent exact adaptation recurrences. Preserve any exceptions with resources.

Maximum180 CPU seconds (including subprocess children),32MiB new outputs,
20GiB free reserve, one worker. No raw recordings/movies copied. Create a final
evidence matrix for Mi1, T4/T5, HS, H2, bIPS, DNp15 and walking using existing
reports, distinguishing observed contradiction, missing evidence and restricted
agreement. A finite model/data search can exclude these candidates under these
tests; it cannot prove every biological model impossible. State explicitly
whether full validation can be completed with current artifacts and why.
Append live progress, preserve all old evidence, save dated progress and methods,
seal after writers exit and rehash in a separate process. No further open-ended
iteration after this finite test: deliver the supported result and exact next
evidence needed.
