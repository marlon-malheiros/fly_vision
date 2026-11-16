# Biological validation status — 2026-11-02

**Goal:** a neural model that detects small turns and reproduces measured fly-neuron responses.

**What works computationally:** the frozen neural-only readout passes its predefined fresh 24-room simulation test for +/-2 degrees/s (48/48,48/48,42/48 detections across speeds; zero observed straight alarms). An older room set still gives 3/24 fast straight alarms. The readout is artificial and reads T4/T5 directly; it is not evidence for biological bIPS causality.

**What we tested biologically today:** HS responses to moving stripes at five contrasts, with all recorded rows and three fixed circuit versions. Current LPi HS has 4/8 lower-contrast endpoints outside the descriptive simultaneous recording-row band. At 50% contrast, recorded PD reaches 91.4% of full-contrast response, versus 21.8% in the primary model. The circuit and detector were unchanged. 27/27 numerical sensitivity checks pass; complete results and source/display uncertainty remain explicit.

**Important correction:** the worksheet's contrast labels conflict with author export order and the published figure. We preserved the earlier report and recorded a source-supported correction. The prior claim about a true-full-contrast scalar comparison cannot be retained unchanged.

**What remains:** full physiological validation, matched downstream recordings/stimuli, broader false-alarm reliability and a biological small-turn threshold. H2/bIPS/DNp15 comparisons already exist, with mixed results; they are not fresh validation data.

**Next:** address the specified neuronal contrast-response discrepancy in a separate biologically constrained version, or obtain stronger independent matched physiological constraints. Keep the current working detector and all evidence intact. No further classifier optimization in this validation study.

[Detailed report](HS_CONTRAST_VALIDATION_REPORT_V1.md), [source correction](HS_VOLTAGE_SOURCE_CORRECTION_R2.md), [frozen rules](HS_CONTRAST_VALIDATION_PROTOCOL_V1.md).

**TL;DR:** small-turn decoding works on a bounded simulation test. Today's biological test identifies a concrete neuronal mismatch; biological validation has not yet succeeded.
