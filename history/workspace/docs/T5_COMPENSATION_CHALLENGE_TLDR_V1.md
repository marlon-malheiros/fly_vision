# Simple summary: the T5 compensation challenge

We tested the same alternative settings against **52 new bar/grating conditions**,
with no tuning. The inputs are synthetic: this tests the model, not new neurons.

Decision: **CHALLENGE_EQUIVALENCE_COMPLETE**. The fixed alternative meets all primary-feature, mean and waveform gates on this challenge. This strengthens limited parameter compensation over the predeclared native stimuli; it does not establish equivalence for arbitrary inputs or biologically distinct circuits.

Peaks/amplitudes stay within 5% in **52/52**
conditions; means in **52/52**;
full voltage traces in **52/52**.
All 312 calculations pass independent numerical verification. Sampling-provisional:
**False**.

Keep this candidate as a bounded example of temporal-parameter compensation. Before pursuing a stronger degeneracy claim, use a separately frozen local sensitivity/Jacobian analysis to ask whether compensation also permits changes in final excitation/inhibition contributions. A biological claim would need independent physiological cells/repeats; this study supplies none.

The alternative also preserves existing model weaknesses: two grating amplitude
pairs are unresolved, and all ten grating mean-direction pairs remain unresolved.

[Technical report](T5_COMPENSATION_CHALLENGE_REPORT_V1.md).
