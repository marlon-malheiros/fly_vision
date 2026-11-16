# Stationary-flash registration and motion prediction V1

2026-11-06. This follows the user-authorized, metadata-selected source admission.
The first file has44 stationary conditions×5 repeats. Admit cells3–5 only with
five repeats per position/dwell and actual stored images/native20kHz clocks.
No flash response has yet been scored at this scientific freeze.

## Scientific scope and model

Keep the full Gruntman2018 cable,12 neural parameters, morphology,99/55 synapses,
seed300 and original MaleCNS/frontend fixed. Learn only **per-cell spatial
registration, causal input delay and a common voltage amplitude factor** from
stationary flashes. The source RF/temporal shape is tested, not freely refitted.
This is a limited calibration of image-to-source registration; it is not a new
connectomic reconstruction or identified physiological voltage-to-release rule.

All three cells' moving responses are already inspected and remain a
retrospective transfer comparison. Flash late repetitions are withheld from
this project's registration fits, but original author population-parameter
fitting used this experimental cohort; they are not wholly independent of the
published source fit. No additional moving cohort or C2/C3 animal is opened.

## Flash extraction and chronological separation

Determine each flash's centroid and duration from its stored32×96 LED frames.
Express position in physical LED pitches along/perpendicular to the previously
fixed canonical PD axis, relative to its moving-session image RF center. Do not
use voltage to infer axes. Cells4 and5 have stationary series diagonal to that axis;
its half-pixel centroids cannot be treated as one native-bin input. This was
found from metadata before any flash voltage scoring. An unused single-bin
method draft is retained, but never scientifically frozen or executed.
Every position and every20/40/80/160ms duration remains included, including
patterns missing the model's eleven sampling sites. An empty sampled pattern
predicts zero under the fixed source support; do not drop weak/far-position trials.

Within each condition sort all five repetitions by native start timestamp.
The **first three** supply the calibration mean; the **last two** supply an
untouched repeat-test mean. Freeze raw file IDs, chronology and conditions
before voltage transforms. Use voltage channel3×10mV, exact integer microsecond
half-open2ms bins, baseline[-250,−50)ms, score[0,duration+350ms). Keep individual
traces and the two means. Source event logs determine onset; never align to a
response peak. This fits within the recorded400ms post-flash display interval.

## Finite flash-only calibration

Build a fixed forward-response bank from actual static bright-frame patterns.
For every condition and offset δ, sample the eleven native positions through
the shifted center, with the preceding piecewise-constant LED rule, and map
grey3/white7 to0/1. Keep all simultaneous input positions. Deduplicate identical
11-channel patterns and dwell times. Reuse a previously reproduced native
flash only for an exactly matching one-hot pattern; use exact zero for an empty
pattern; simulate every other unique pattern through the unchanged full cable.
Never linearly sum voltage templates to approximate multiple inputs. Freeze
the complete pattern-to-condition mapping before voltage scoring.

Source pulse at time0 has baseline−65mV. New bank traces record0.1ms through
650ms. Interpolate at observed bin centers; for delay d≥0 evaluate at t−d,
returning zero before onset. This is a delay of input to the unchanged
autonomous cable, not an acausal output filter or calcium observer. Templates
use nominal recorded pulse duration; actual-frame/timing numerical controls
below check that this approximation is adequate.

Predeclare five integer offsets δ∈{−2,−1,0,1,2} LED pitches and51 delays
d∈{0,2,...,100}ms:255 registrations per cell. ±4.5deg registration and0–100ms
delay are bounded modeling allowances, not measured biological parameter
ranges. Report edge selections; never expand the grid after outcomes. For
each pair fit one nonnegative zero-intercept gain on the calibration means,
equally weighting all position/dwell conditions. Minimize this same mean MSE;
ties prefer smallest absolute offset, shortest delay, then signed offset.
No scored moving/late-flash response chooses a parameter, exclusion or variant.
Archive all255 fits/cell and lock the three primary registrations before any
late-flash voltage transform or new moving prediction.

Three fixed candidates: **flash-calibrated primary** (δ,d,g), diagnostic with
the same learned δ,d but physical-voltage gain1, and unchanged cable baseline
(δ=0,d=0,g=1). Compare all three; do not select another candidate after scoring.
No RF width, E/I strength, cable time constant, direction reversal or
condition-specific amplitude is optimized. Gain0 or invalid source geometry
prevents advancement to motion; preserve the failed calibration.

## Flash repeat test, motion transfer and criteria

For stationary repeat testing compare with zero and a spatially blind reference:
the calibration mean averaged across positions separately at each dwell in
the same cell. Give each condition then each cell equal weight. Enumerate all27
three-cell bootstraps with fixed registrations. The primary waveform criterion
requires positive pooled skills against both references, positive zero skill
in each cell and positive5th percentile of joint minimum bootstrap skill.
This is a predictive rule, not a physiological equivalence margin.

After locking and scoring flash repetitions, simulate both previously scored
later motion repetitions for all PD/ND×dwell conditions in cells3–5. Shift the
image RF center by δ along its canonical axis, delay the actual controller
events by d with initial/final grey holds, and apply the flash-derived voltage
gain. No refit. Compute physical-gain diagnostic from the same Vm. Reuse the
unchanged cable baseline's sealed motion traces, never regenerate old movies.
Motion scoring/zero/direction-blind references, masks and27-resample waveform
rule are identical to the preceding full-cable study. Lack of qualifying
inhibition masks remains unqualified, not a pass.

Flash accuracy failures are retained and **do not suppress the planned
retrospective motion comparison** when geometry, gains and numerical checks
are valid. This permits a complete transfer test without exposing fresh moving
data. A restricted flash-to-motion waveform success requires both primary
flash and motion criteria; even that would not validate the whole walking
circuit, independent animals or small yaw.

## Numerical/independent checks and limits

Before motion scoring, compare cached-template predictions with actual-image
NEURON output for four first-calibration flashes in cell3: positions0,+2 and
durations20,160ms. Apply that cell's locked registration/delay; compare unscaled
signed mV, tolerance0.005mV. If those source positions do not exist, stop and
document; do not choose better controls. Separately compare0.1 versus0.05ms
solver steps on cell3 PD/ND20/160ms first later motion repetitions, same0.005mV
maximum discrepancy. A failed numerical gate leaves scientific qualification
unestablished and does not authorize tuning a source parameter.

Independently check chronology, position geometry, native bin means, all765
grid MSEs/gains, selected minima, references, calibration locks and final
metrics/bootstraps. Preserve metadata-serialization failure and its separate R2
correction. Rehash the466 prior cable artifacts. Use compact11-channel inputs
and soma/observed traces; raw flashes total189,559,908bytes,256MiB permanent cap,
20GiB reserve,2GiB worker RSS and1200 scientific child-CPU seconds. Temporary
arrays are not movie archives. No bulk download, new image generation, full
MaleCNS solve or optimization against yaw classification.

Append progress and a report with undergraduate explanation. Copy dated progress
and methods before sealing, seal after all writers exit, verify in another
process. All old source/model/result files remain unchanged. Report failed
registrations, negative transfer and unidentifiable biology explicitly.
