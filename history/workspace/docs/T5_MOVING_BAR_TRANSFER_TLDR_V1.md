# Moving-bar comparison — simple summary

The second motion test passed without changing the neuron parameters.

- All 144 main image responses preserve the original model's peaks, with at
  most 0.19% error; all 72 direction comparisons agree.
- Recorded and model peaks prefer the expected direction in all nine bar
  width/speed comparisons. Average voltage also does so in all nine pairs.
- 14 tests passed and a separate solver verified all 612 runs.

We now have reliable image-to-native controls for both gratings and moving bars.
The model's weak grating averages depend on the stimulus/window. They remain
in the report, alongside model/recording waveform errors of about 2.6 mV during
bar motion. Getting direction right does not mean predicting every voltage well.

The eight geometry templates share one recorded-cell model. Population validity,
random-texture reliability and neural degeneracy are still unproven.

This bounded transfer stage is complete. The next proposed stage is a small,
predeclared parameter-sensitivity pilot on a mixed bar/grating benchmark,
excluding trivial parameter redundancies. That pilot has not been run.

[Technical report](T5_MOVING_BAR_TRANSFER_REPORT_V1.md) ·
[Progress report](PROJECT_PROGRESS_REPORT.md)
