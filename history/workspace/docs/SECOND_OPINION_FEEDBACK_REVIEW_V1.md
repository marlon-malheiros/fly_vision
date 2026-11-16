# Assessment of the independent feedback and proposed plan revision

24 October 2026. Critical review of user-supplied feedback, not a newly frozen
experiment. Existing reports, models, readouts and acceptance criteria remain
unchanged. [Situation overview](SECOND_OPINION_PROJECT_OVERVIEW_V1.md).

**The feedback changes the order and emphasis of the next study. It does not
establish the cause of our errors.** Treat formulation mismatch, scene leakage
and normalization effects as hypotheses with different existing support.
Normalization scaling and sampling effects have already been demonstrated in
their specified comparisons; the entire generalization failure has not been
uniquely attributed to either. The assertion that the circuit is fundamentally
sound is no more established than the opposite assertion.

## Changes worth adopting

- Characterize graded neural responses before another threshold search:
  small-yaw response slope, straight-walking bilateral offset, dependence on
  forward speed, and temporal responses. Retain the existing classification
  results as secondary evidence; do not replace a failed frozen criterion
  retrospectively with a new favorable metric.
- Use reflected and symmetric visual controls to separate contributions from
  geometry, texture, retinal sampling/routing and network imbalance. Verify
  the complete image/coordinate/channel reflection, including eye origins and
  yaw conventions, before interpreting source or neural differences.
- Add an explicitly baseline-weight-preserving control if expanding anatomy
  again. Study B already audited the scaling identity and compared the
  expanded circuit with both new families silenced, retaining normalization.
  That isolates scaling and transmitted activity within its comparison.
  Holding the old block fixed is an additional useful counterfactual; it is
  not evidence that a new arbitrary coupling gain is biologically correct.
- Treat exact author-code reproduction as necessary for a claim of exact
  reproduction, **not a prerequisite for further diagnostic or physiological
  work**. Source/stimulus inquiries can proceed in parallel with useful tests.
- Develop one matched physiological benchmark with a source-supported
  observation model, calibrated separately from independent validation.

## Corrections needed before using the proposed ladder

1. **The network is recurrent.** The project includes T4/T5 recurrence and
   feedback, as well as downstream interactions. The frontend also has temporal
   memory. Open loop describes the absent neural-to-body feedback; it does not
   imply a feedforward or memoryless neural network. Our readout uses two
   bilateral mean features and already yields a continuous yaw score before
   thresholding. It compresses information but is not the entire computation.

2. **Mirror reversal does not prove a purely physical cause.** A numerical or
   feature-extraction artifact can itself respect reflection symmetry. Reversal
   helps decompose responses but needs independent geometry/sampling checks.
   Symmetric rooms must include correctly reflected textures and poses. Unequal
   T4/T5 counts, retinotopic positions or routing can also make aggregate source
   values unequal without an error in the local motion-filter equations.

3. **Contrast and optical geometry are different quantities.** Scene depth
   affects angular flow; contrast affects the image-derived detector response.
   The supplied azimuth equation is a useful simplified planar/central-camera
   description, not the complete finite-baseline binocular renderer. Ambiguity
   after population/window compression does not prove exact optical equivalence
   of arbitrary full image sequences. Deterministic scene false alarms were
   already reported as scene counts, not spontaneous neural error probabilities.

4. **Analytic injection is a circuit probe.** A uniform alpha*v +/- beta*yaw
   drive would ignore directional channel identities and may violate the
   inherited [0,1] drive bounds. Define channel-aware bounded perturbations in
   declared diagnostic units. Success under that probe would not uniquely
   establish the frontend as the only bottleneck in natural scenes.

5. **A failed scalar rescaling does not prove nonlinear or divisive control.**
   Linear multi-input mixing, recurrent temporal filtering and unequal pathways
   can defeat one gain/offset fit. Compare nested linear/static/temporal controls
   before claiming adaptation or nonlinearity. Our printed reference is a linear
   simultaneous steady-state reconstruction, not author-provided middle-layer
   ODE code. Its bIPS effects already illustrate a linear mechanism.

6. **Define comparable gains.** Yaw gain per degree/s and translation gain per
   mm/s cannot simply be divided and called a dimensionless dB rejection ratio.
   Specify normalized channel perturbations or physical reference amplitudes.
   An AUROC over environments measures scene discrimination under that sampling;
   it is not a neural-noise or behavioral psychometric threshold. Any new
   threshold criterion belongs to a separate prospective study.

7. **Symmetrization is a synthetic control.** It requires verified homolog and
   retinotopic correspondences and must not overwrite the anatomical baseline
   or be labeled a biological requirement. Likewise, correct stimulus polarity
   requires verified soma/axon/eye conventions rather than assumed H2 labels.

8. **Do not assume saturation or a universal calcium filter.** Our rates are
   signed tanh deviations, so zero is not a lower clipping boundary. A
   retrospective audit of the 44 saved intact direct-ray cases finds maximal
   absolute downstream rates of 0.0083265 (HS), 0.0026181 (H2), 0.0036105 (bIPS)
   and 0.0024910 (DNp15). The corresponding smallest recorded activation slope
   exceeds 0.99993. Thus these saved downstream points are near the linear
   origin; they do not support downstream tanh saturation as the explanation
   in this subset. This says nothing definitive about frontend nonlinearities,
   all source cells, unsampled solver times or all 40 rooms.
   [Saved-data audit](../results/second_opinion_feedback_review_v1/operating_points.json).

The [paper's Methods](https://www.nature.com/articles/s41593-025-01948-9#Sec15)
describe different indicators across preparations and use calcium convolution
for visualization of a steady-state model. A universal 0.5-s decay is not an
established observation model for our data. Reporter/compartment dynamics,
baseline, scaling and measurement rectification need evidence and a separate
calibration/validation split. The reported measurements also cannot be assumed
to be interchangeable raw delta-F/F traces.

The proposed drone, haltere fusion and obstacle-centering interpretations remain
outside the present walking study. A straight-walking model output might have
another behavioral interpretation, but a centering benefit or DNp15-specific
sensor-fusion mechanism has not been demonstrated here. Do not reinterpret
failed yaw classification as demonstrated successful steering. Closed-loop
control remains deferred under the existing scope.

## Recommended sequence, pending a new execution instruction

1. Freeze a finite operating-point and continuous-response study with an explicit
   optical sampling rule. Measure raw neural yaw gain, straight offset and
   normalized input-to-output transfer; analyze temporal information separately.
   Check local linearity and numerical error rather than assuming saturation.
2. Perform controlled reflection and symmetry tests, tracing images, motion
   fields, routed source drives and network responses. Use bounded circuit-input
   probes as complementary tests; require multiple controls for attribution.
3. In parallel, specify one recording-matched physiological benchmark. Exact
   walking-agent reconstruction is optional for this bounded question; the
   stimulus and measurement definitions used must still be explicit.
4. Only then test justified counterfactual circuit controls and a richer readout.
   Calibrate on development data and evaluate on fresh environments, since the
   existing diagnostic rooms and 40-room outcomes have already been inspected.
   Fit no circuit parameter merely to improve yaw classification.

These are recommendations, not a newly authorized full experiment or a claim
that the feedback's proposed diagnosis has been verified. The undergraduate
reason for the change is simple: **first understand how strongly the circuit
responds to turning and to uneven forward motion; then decide whether the
problem lies in the visual signal, the circuit, or how we read its output.**
