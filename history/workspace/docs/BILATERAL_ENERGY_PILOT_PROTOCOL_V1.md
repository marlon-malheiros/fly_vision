# Saved-array bilateral energy pilot V1 — 2026-11-01

Prospective implementation and selection rules for one bounded attempt prompted
by the user's attached independent review. Freeze this file, configuration and
implementation hashes before fitting or examining new scores. Previous studies
are immutable. The attached review is a hypothesis source, not verified evidence.

## Question and scope

Can a low-dimensional, antisymmetric neural readout with bilateral motion-energy
normalization meet the existing small-turn detection criteria? This changes an
artificial readout, not the frontend, synaptic graph or physiological parameters.
It cannot establish biological validation. It is a development experiment on
already-inspected rooms. No encoder training, images, neural simulations, old
test populations, or reserved st00–st23 environments are authorized by this pilot.

Use only stage `known` of `results/neural_population_readout_v1/plans.json`:
24 p training rooms (zero and +/-2 deg/s only) and all 16 w calibration rooms
(zero, +/-2 and +/-5). Verify each read observation against its existing receipt.
No +/-5 training outcomes enter selection. Positive arrays have 131 samples;
negative arrays have 301, at 100 Hz. Do not assume the review's 300-sample shape.

## Fixed inference and controls

Extract 19 fixed features: seven right-minus-left role means (HS, H2, bIPS,
DNp15, uLPTCrn candidates, H2rn candidates, LPi) and twelve right-minus-left
horizontal source features (two channel classes a/b, six eye-coordinate columns,
averaged over four elevations and T4/T5). Role means accommodate unequal cell
counts; this grouping does not assert one-to-one homology, anatomical symmetry,
or a mirror-symmetric graph. The antisymmetry is a constraint on the artificial
readout of these grouped observations. No added anatomical connection is implied.
Use the original causal ten-sample mean minus that mean 20 callbacks earlier.
No intercept or centering is allowed. Weighted RMS scaling is fit on training
data only. The 19-feature basis is fixed without examining outcomes.

Energy E is the causal 20-sample mean of nonnegative activity averaged across
both eyes and T4a/b,T5a/b bins, including empty bins as the observer stored them.
This bilateral sum is independent of local channel sign conventions. It is an
energy proxy, not a measured walking speed. Using both horizontal directions
avoids assuming the review correctly identifies the forward-motion channel in
each eye. Eref is the median training straight-walking E over callbacks 100..299.
Define D = floor + (E/Eref)^gamma. Test gamma in {1,2}, floor in {0.1,1}.
The matched raw control has D=1. No bilateral-discrepancy term is included: the
review mentions one but does not specify its formula.

Fit one raw antisymmetric ridge numerator per lambda, using zero and +/-2
training episodes, with equal total mass per sign and equal episodes within
sign. Negative episodes distribute their mass equally over callbacks 100..299;
positive episodes use callback 119 only. Multiply weights by the number of
training episodes: lambda {1,10,100,1000,10000} penalizes a sum of episode-equivalent
losses, not a mean loss. This convention is explicit to avoid an accidental
1,000-fold penalty change. Keep the fitted numerator identical across its four
normalizations. For every score, fit one nonnegative scalar gain on training
samples after division, minimizing weighted squared error to yaw labels. This
gain fixes score units as training-calibrated deg/s equivalents; it does not
affect relative detections under a calibrated cutoff or add a 20th linear DOF.
It is not a physiological calibration or proof that scores measure true yaw.

Leave one p room out, with scaling, Eref, numerator and final gain refit strictly
on the other 23. Pool out-of-fold predictions, then use a single negative-only
cutoff: the largest per-speed/static order statistic allowing floor(0.1*n) alarm
episodes, with strict |score|>cutoff. Choose by largest minimum signed detection
fraction over six speed/sign groups; then total correct +/-2 detections; then
lowest sign-balanced out-of-fold squared error; then declared config order.
Select the normalized model and raw control separately. These are training-only
hyperparameter comparisons, not unbiased nested-CV validation estimates.

Refit both selections on all p rooms, persist a hash freeze, then evaluate w once.
Also reproduce the unchanged 45-cell `episode90/individual_linear` baseline with
its original coefficients and original cutoff 1.6219391228674396. A fourth
diagnostic applies D=1 to the normalized model's selected numerator; this isolates
normalization at the same lambda without choosing another candidate. Baseline
must reproduce its previously saved calibration episode scores and 18/32 fast
small-turn detections. New candidates use the smallest common negative-only
cutoff allowing <=1/16 alarms at each walking speed and at rest. No positive w
episode selects a cutoff, feature, coefficient or hyperparameter.

## Gates, diagnostics, stop rule and resources

At callback 119 (190 ms after yaw onset), require >=26/32 correct signed detections
AND >=13/16 per sign at each speed, at BOTH +/-2 and +/-5 deg/s. Straight and static
episodes are monitored over [1.0,3.0) s, callbacks 100..299. Keep one common cutoff
and <=1/16 episode alarms per speed/static. Do not shorten negative monitoring.
Verify population and score prefixes are bitwise equal for matching straight and
turn episodes before yaw onset. Independently reproduce feature arithmetic and
linear scoring, report stationary scores, raw sign accuracy, energy by speed,
thresholds, per-room endpoints and negative peaks.

A paired-straight subtraction is an explicitly nondeployable diagnostic only:
report signed normalized turn increments and straight clutter SD by speed for the
fixed selected numerator. No paired straight episode is available to inference.
Do not label this an information-theoretic ceiling. Failure cannot prove that
the representation lacks all usable yaw information or that encoder training is
falsified. Do not fit an additional quadratic/oracle bank.

If no normalized model passes calibration, stop this pilot: no new room rendering,
no further policy bank and no encoder training. Propose a separately bounded
unbinned local-subunit prototype as the next option; do not silently execute it.
If calibration passes, stop model selection and apply the single selected model
to existing cached numerical observations for all original 81 spatial/temporal/
solver refinements. Require max score error <=0.2, unchanged endpoint decisions
and unchanged straight-episode alarm status. Do not substitute nine checks for
the existing 81. Fresh-room evaluation requires a separately frozen test plan
after numerical qualification. There is no positive validation claim in this
saved-array pilot alone.

Bound the fit/calibration process to one CPU, no GPU, 60 s wall time, 1 GB RSS,
and total persistent study artifacts <=2 MB including compact traces, code,
reports and the dated progress snapshot. Keep larger temporary data in /tmp.
If a budget is exceeded, preserve the failure and stop, rather than weakening
criteria or concealing the overrun. Source editing and independent review time
are reported separately from the bounded analysis invocation. Archive input
hashes, selected models, all training selection summaries, all calibration
endpoints/negative peaks, complete compact score curves and any failures.

## Review corrections accepted before outcomes

The old linear baseline is stronger than the latest readers and must be shown.
However, estimated Lucas–Kanade motion is not exact ground-truth flow; failure
of one pooling architecture does not disprove all learned encoders. A v-squared
clutter term is a conditional linear-flow approximation, not an established law
for this nonlinear neural model. Sparse and dense LK controls differ. The earlier
T5 recording archive has already been inspected. Absent electrical edges in this
selected model do not establish their absence in biology. Neither a low linear
SNR nor a failed pilot proves impossibility. No new physiological validation is
claimed or attempted here.
