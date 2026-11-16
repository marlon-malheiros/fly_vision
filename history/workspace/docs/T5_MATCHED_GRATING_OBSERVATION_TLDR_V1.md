# Matched T5 observation comparison — simple summary

We compared a real recorded T5 neuron's eight grating responses with the fixed
published model, using the same stimuli, times and measurement rules.

- **The oscillations:** both recordings and model prefer the expected direction
  in all four comparisons.
- **The average voltage:** recordings prefer the expected direction in three
  comparisons and the opposite direction in one. The model's direction strength
  falls below our chosen criterion in all four; the two slow cases are close to
  the cutoff, not devoid of directional information.
- **The implementation:** 14 tests passed, and a separate author solver matches
  our model to about 0.0000000002 mV. The recorded/model waveform mismatch is about
  4 mV over the scored windows, so direction agreement alone is not full accuracy.

This helps locate the problem: it is already present in the native model's
prediction of average voltage. We cannot explain it just by our image frontend,
or say that real neurons always have weak average responses. We still do not
know which biological mechanism or model change would resolve it.

We have a reportable, limited result for one recorded cell. We have not validated
a population or demonstrated neural degeneracy. A sensible next task is to test
image transfer against the native amplitude benchmark with unchanged parameters.
That task is proposed, not yet run.

Development, decisions and limitations are now recorded continuously in
[the progress report](PROJECT_PROGRESS_REPORT.md).
The full evidence is in [the technical report](T5_MATCHED_GRATING_OBSERVATION_REPORT_V1.md).
