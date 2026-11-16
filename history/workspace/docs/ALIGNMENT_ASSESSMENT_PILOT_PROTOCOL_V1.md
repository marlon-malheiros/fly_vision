# Stimulus alignment and model assessment pilot V1

16 November 2026. A bounded follow-up to an already observed finding, with a new
method frozen before the analyses below. The earlier T4 examples motivated this
study; they are development data, including cells previously reserved by this
project. There is no new biological holdout and no whole-circuit validation.

## Questions and interpretation

1. Do previously exact model-input aliases persist when the saved LED images
are sampled at fractional positions and through a specified optical blur?
2. In a controlled spatial-response example with known truth, how often does
selecting a single calibration-optimal alignment reject the generating model?
Does retaining a calibration-compatible set reduce those rejections by yielding
more unresolved decisions, and does it also retain incompatible mechanisms?

The original T4 study performed RF mapping before its selected bar protocols.
Nominal grid centres are recorded. We audit their coordinate convention and
archive metadata, but do not assume that the selected bar files constitute the
experiment's entire calibration record. An ambiguity in this reanalysis must
not be attributed to the authors' entire experiment or to neural degeneracy.

## Archived image analysis

Read in place the six already inspected author cells 3–8: SingleBar files for
20160427, 20160428, 20160502, 20160504, 20160505, 20160510. Verify their existing
acquisition receipts. Extract all distinct static bright images and confirm all
repeated flash frames. Verify all eleven model-input samples for the historical
25 integer shifts against cached cells 3–5. Preserve previous canonical axes,
source grid centres and previously chosen reference shifts; for cells 6–8 use
their archived selected alias lists. Do not select an alignment using new
recorded response outcomes.

Sample shifts in [-2,2]^2 LED pixels at 0.25-pixel increments. Use exact
piecewise-constant LED integration with symmetric boundary convention when
sigma=0. For sigma=0.5 and 1.0 LED pixels, convolve each LED's square area
analytically with an isotropic Gaussian using normal CDF differences; outside
the display is background. One LED pixel is 2.25 degrees. These blur scales are
sensitivity assumptions, not estimates of these animals' optics. Report exact
numerical equality (max difference <=1e-12 contrast), and descriptive RMS
differences at 0.01 and 0.05 contrast tolerances. The latter are not empirical
neural-discrimination thresholds. Report all blur scales and all six cells.
Quarter-pixel sampling is a finite subpixel sweep, not a continuous proof.

Stop claiming blur-robust exact ambiguity if the selected aliases separate
under either nonzero blur scale. Report small differences separately without
calling them biologically indistinguishable. This stage is an input analysis;
it does not generate new cable voltages or reinterpret prior physical-mV
forecasts as optically qualified.

## Controlled assessment with known truth

Use three frozen, unit-integral positive spatial filters: an isotropic Gaussian
with sigma 1 pixel; an elongated Gaussian with sigmas (1,1.6); and a symmetric
mixture of two isotropic Gaussians displaced by +/-1.5 pixels in y. Give each
model the same 25 candidate RF centres on the integer [-2,2]^2 grid. Add an
independent known Gaussian optical blur with sigma 0.5 pixels by adding
variances. This is a linear spatial toy model, not a T4 physiology simulation.

Calibration comprises eleven width-one vertical bars at x=-5,...,5 and height
nine pixels. Test comprises 25 single-LED patches on the fixed [-2,2]^2 grid.
Each condition has three repeats. Cross every generating model and every true
centre with independent additive normal measurement noise SD 0.02,0.05,0.10
of the model's unit-integral response, 200 replicates per setting. Seed 20261116.
All models, including wrong ones, receive the same stimuli, known noise,
candidate alignments, and observations. Uniform enumeration of truths is an
evaluation design, not a biological prior. No gains or noise parameters fit.

Choose one alignment by smallest calibration squared error; break ties in
fixed lexicographic centre order. Alternatively retain all alignments whose
calibration residual sum, divided by sigma^2/3, is at most the 97.5th percentile
of chi-square(11). This is an absolute known-noise compatibility test, not a
likelihood-ratio fit or a posterior. No nonempty set is forced. Score each
alignment on independent test data against chi-square(25)'s 97.5th percentile.
For a set: reject when empty or all its members fail; support only when every
member passes; otherwise report unresolved. Support here only means passing
this finite toy test, not recovering the true biological mechanism.

Report rejection of the actual generating family; support, unresolved, and
non-rejection of every other family; candidate-set size and true-centre
coverage; oracle-alignment results; and counts for all truth/noise combinations.
The known-noise set procedure has a union-bound false-rejection probability at
most 0.05 when the true model and alignment are included, by the two tests'
0.025 errors. Monte Carlo may fluctuate. Reduction in rejection alone is not a
method advantage: unresolved outcomes and wrong-family retention are required.
No new calibration design is claimed superior; that would require a separately
specified equal-budget comparison. All scientific outcomes, including null or
negative findings, enter the report and initial manuscript.

## Resources and preservation

One process; no new raw downloads, generated movie archive, NEURON solves or
reserved animal access. Estimate under 300 CPU seconds, under 1 GiB process
memory and under 128 MiB retained output; hard stop at 900 CPU seconds, 2 GiB
RSS, or 256 MiB output, with 20 GiB disk reserve. Load MAT files sequentially.
Freeze this protocol, code, tests, source receipts and selected predecessor
evidence before results. Independently check scalar optical integration and
selected synthetic decision arithmetic. Preserve failures and source versions.
Append progress, write a detailed report and initial manuscript with verified
references, snapshot methods and dated progress, then seal and separately
rehash the completed pilot. Live progress remains outside the index.
