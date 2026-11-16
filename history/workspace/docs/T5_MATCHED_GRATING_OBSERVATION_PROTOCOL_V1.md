# Matched T5 grating observation protocol, V1

## Question and scope

Does the fixed published T5 example reproduce the direction preference and
strength of measured grating responses under the author's exact native stimulus?
Does the measured mean itself carry less direction information than oscillation
amplitude? This is a bounded same-cell prediction comparison, not population
validation, an image-to-native equivalence test or a degeneracy experiment.

All eight grating observations from cell 7 and iteration-52 model parameters
are retained. No new response-based cell/model selection, circuit parameter
fitting, T4 simulation or downstream simulation is permitted. Rules below must
be hashed before calculating new grating scores. Prior analyses have already
examined model replay errors and image grating scores; this is not a claim of
complete historical blinding. Training-only error inspection is permitted before
freezing the new observation comparison.

## Provenance prerequisites

Verify the author acquisition hashes, published example selection in the plotting
script, single-bar-only fitting archive, width-two training mask, exact inclusion
of fitting recordings/clocks in the full dataset and archived fitting objective.
The published workflow fits bars and predicts gratings. The acquisition adopted
the author's explicitly designated example, not a new best grating response.
The author's reasons for selecting that example and the full optimization
history are unavailable; do not describe this as a fully blind validation set.
Stimulus-held-out relative to the audited objective and independent-cell
validation are different claims. Preserve the known author `err_all` family-order
bug by aligning observations from metadata, never by hardcoded family order.

## Exact native stimulus and clocks

Use `published_t5_forward.forward_trial` with the unchanged 11 archived parameters,
27 native positions and all published events. Native onset is 25 ms. Preserve
the extra final hold in the author's grating schedule in full waveforms, but
exclude it from complete-cycle scores. The eight phase steps per cycle have
40- or 160-ms dwell: periods 320 or 1,280 ms, frequencies 3.125 or 0.78125 Hz.
These are not identical to the earlier image assays; their native spatial units
must not be converted to degrees without additional evidence.

Retain the actual observation clocks, including their fractional starting times.
Require uniform 2.5-ms intervals; do not round or interpolate measured times.
Evaluate model voltage at exactly those clocks. Extract recordings with their
own MATLAB one-based inclusive bounds using the actual protocol order.

Pair grating family indices (0,1), (2,3), (4,5), (6,7). Each pair has one dwell
time and one starting phase (1 or 5). Positive phase increments correspond to
positive native displacement in the published stimulus. Use this metadata
orientation as expected preference, never the observed or predicted voltage.
Verify all phase increments and author orientation metadata before scoring.

## Matched measurements

Voltages are the author's relative mV. For each observed, exact-model and archived
model trace, subtract its own mean over [-100,0) ms, then score
[25+P,25+3P): discard the first complete cycle and retain cycles 2 and 3.
This contains 256 samples at P=320 and 1,024 at P=1,280. Full waveforms and all
baselines are saved. This finite observed window is not evidence of steady-state
convergence. Do not extend measured data or replace the window after inspection.

Primary readouts:

- Mean response: arithmetic average of baseline-subtracted samples.
- Robust amplitude: half the difference between the 95th and 5th percentiles,
  using NumPy's linear quantile definition. This matches the earlier project's
  amplitude estimator; it is not an exact recreation of the authors' sinusoid
  fit, and recording noise can inflate it.

For each readout and pair retain both responses, their signed difference and
DSI = (Rpositive - Rnegative) / (abs(Rpositive) + abs(Rnegative)). Never rectify
mean responses or normalize amplitude and mean differently. A zero denominator
returns DSI=0 with an unresolved flag. Also report full and retained-window
waveform RMSE, observed/model response differences, individual cycles 1–3 mean
and amplitude, and a fixed-frequency least-squares constant+sine+cosine amplitude
on the same retained window. The latter is a secondary measurement, not fitting
new circuit parameters or selecting a better model. It provides a check on the
noise sensitivity of the robust-amplitude estimate; it does not reproduce an
unavailable author fitting function.

## Interpretation rules frozen before new scores

Raw response differences and quantitative observation/model discrepancies are
the principal evidence. Report each of the four pairs separately. For continuity
with the earlier engineering criteria, classify both readouts with the same
fixed floors: maximum absolute response >=0.065 mV, absolute pair difference
>=0.065 mV and absolute DSI >=0.1. A resolved positive difference passes expected
direction; a resolved negative difference is a wrong-sign result; otherwise it
is unresolved, retaining every failed criterion. These are project criteria,
not measured confidence intervals or accepted physiological thresholds.

For each pair, label:

- `OBSERVED_AMPLITUDE_WITH_WEAK_MEAN` if observed amplitude passes and observed
  mean is unresolved; this supports a readout distinction for that condition.
- `OBSERVED_MEAN_MODEL_INCOMPLETE` if observed mean passes and model mean does
  not; the discrepancy exists already in the native model comparison.
- `NATIVE_MEAN_AGREEMENT` if observed and model means both pass; this establishes
  agreement of this direction classification only, not full biological validity.
- `RESOLVED_WRONG_SIGN_PRESENT` if either primary mean or amplitude readout is
  resolved in the opposite metadata direction; inspect all quantitative errors.
- `OTHER_OR_UNRESOLVED` otherwise.

Flags can coexist. All eight traces and four pairs remain in the conclusion,
including conflicting signs or different speeds/phases. Study-level decision is
`TECHNICAL_COMPARISON_INVALID` if any alignment/provenance/numerical prerequisite
fails; otherwise `MATCHED_COMPARISON_COMPLETE_SCOPE_LIMITED`. No arbitrary global
RMSE cutoff or success quota will convert this one-cell comparison into biological
validation. Report discrepancies even if direction labels agree.

No new hypothesis tests or biological uncertainty estimates: the available
vectors do not identify independent repeats, trial variance or new cells. Their
9,248 samples are not 9,248 independent biological observations. Independent
cells and repeat-level uncertainty would be required for a population validation
claim, but are not required to execute this bounded comparison.

## Validation and tracking

Meaningful tests cover fractional-clock boundaries, partial recordings, baseline
offsets, inhibition/zero denominators, phase wrapping and the distinction between
mean and amplitude. Review every recorded observation directly from raw bounds,
every model waveform against the previously saved event-split tight author RHS
solver (1e-8-mV tolerance), and primary arithmetic with independently implemented
sorted quantiles/sums. Verify the archived parameter vector remains unchanged.
Inspect all eight waveforms in a standalone figure; save complete tables and
technical review. Check all four predecessor artifact indexes and their entries
before and after execution. Append progress to the live report, take a completion
snapshot, commit source/docs/tests/configuration, then seal the new evidence.

