# Image-to-native T5 transfer — simple summary

The image frontend works for the matched grating control. We drew the exact
native dark/background stripes, passed the pixels through the existing sampler,
and kept the published neuron model unchanged.

- All 64 main responses preserve oscillation amplitude, with at most 0.24% error.
- All 32 direction comparisons pass. Finer pixels reproduce native voltage to
  about 0.000000000001 mV.
- 19 tests passed; a separate solver checked all 280 runs. Its audit needed a
  documented integer-type correction, and the failed attempt was preserved.

This is a positive computational result: we have a dependable image-to-native
benchmark and no evidence here that we need to rebuild the whole frontend.
It does not fix the published model's average-voltage mismatch with recordings,
explain random-texture problems, or prove biological validity or degeneracy.
The eight geometry templates reuse one recorded-cell model, so they are not
eight independent experimental neurons.

Next proposed check: matching moving-bar data, a second stimulus family, with
fixed parameters. That check has not yet been run.

[Full report](T5_IMAGE_NATIVE_TRANSFER_REPORT_V1.md) ·
[Ongoing progress](PROJECT_PROGRESS_REPORT.md)
