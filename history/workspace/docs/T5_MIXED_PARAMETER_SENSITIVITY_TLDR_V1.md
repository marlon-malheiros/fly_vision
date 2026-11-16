# Simple summary: native T5 parameter pilot

We wanted to know whether different model settings could give nearly the same
responses, a first computational step toward studying degeneracy.

We tested **80 fixed alternatives** on **26 bar/grating inputs**. **53**
kept every direction classification; **6** kept all quantitative
feature gates; **1** did so while meeting our substantial-change definition.
One materially changed parameter set preserves all 26 features and 13 pair gates.

All 2,210 calculations passed independent numerical review. No settings were
fitted to the recordings. This is evidence about one model under a limited
benchmark; it does not establish degeneracy in real neurons.

The successful alternative changes inhibitory decay from 156.3 to 117.2 ms and
rise from 165.9 to 207.4 ms. The two changes almost compensate: output features
change at most 3.57%, and all direction comparisons stay intact. The model still
uses nearly the same final inhibitory conductance. Weak grating means remain.

Freeze a separate challenge set before evaluating these candidates: new native bar speeds/widths and grating frequencies/phases, with full-waveform/mean readouts. This would test whether the limited equivalence generalizes; existing physiological validation remains confined to one cell.

[Technical report](T5_MIXED_PARAMETER_SENSITIVITY_REPORT_V1.md).
