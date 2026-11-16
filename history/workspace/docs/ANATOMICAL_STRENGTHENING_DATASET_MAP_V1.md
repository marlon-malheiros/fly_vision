# Study B physiological datasets and measurement map, V1

Recorded 2026-10-19. This is an evidence inventory and interpretation guide. It
adds no neural fit, decoder criterion or replacement physiological readout.

| Cells | Published source and data | Available comparison | Scope and unresolved constraint |
|---|---|---|---|
| T4 | [Gruntman, Romani and Reiser (2018)](https://doi.org/10.1038/s41593-017-0046-4); [public data](https://doi.org/10.25378/janelia.5576101) | Whole-cell voltage recordings, flashed/moving ON bars and a morphology-based conductance model. Existing matched comparison uses all eight published motion peaks, four speeds × PD/ND, with the published response statistic. | Recording-peak RMSE 0.831981 mV; author-figure simulation RMSE 0.043807 mV. Same-study, figure-derived motion summaries; full raw pooling reconstruction and independent-cell acceptance are not established. |
| T5 | [Gruntman, Romani and Reiser (2019)](https://elifesciences.org/articles/50706); [public collection](https://doi.org/10.25378/janelia.c.4771805.v1); [author model/code](https://github.com/reiserlab/T5ConductanceModel) | Whole-cell voltage, flashes, moving bars and gratings. Existing native model audit covers 168 protocols; matched published example is cell 7, iteration 52. | Grating stimuli were absent from the audited flash-fitting objective, but the example is not independent-cell validation. Retained-window waveform RMSE 4.020545 mV; model mean-direction criterion 0/4 versus 3/4 recorded. Moving-bar peak/mean directions agree in 9/9 pairs, while mean absolute peak error is 1.89575 mV. |
| HS/H2/bIPS/DNp15 | [Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9); [Zenodo data](https://doi.org/10.5281/zenodo.14967806); [analysis code](https://github.com/ChiappeLab/Erginkaya_et_al_2025) | Published calcium recordings and source tables. Local targeted preprocessed MAT files and the prior narrowed Figure 3e fly-level endpoints are available. | Forty-seven endpoints: 38 calibration endpoints from 22 flies; nine validation endpoints from five flies. No overlap of validation flies with original neural-gain calibration. Published-method analytic flow and signed epoch statistic are reproduced; frame-exact retinal movies, a validated neurite readout map and source-specific fluorescence/baseline transfer are unresolved. |
| uLPTCrn/H2rn | Same Erginkaya data/code archive; local targeted MAT directories exist for both families | Published calcium data support the recurrent-cell hypotheses and can inform a future explicitly calibrated observation model. | MaleCNS additions are candidate family homologs, not the individually recorded neurons. No cell-specific physiological pole or conductance was inferred from labels, nor fitted for yaw accuracy. These families were not added to the frozen four-class endpoint contract. |
| HS–H2 electrical interactions | [Pokusaeva et al. (2024)](https://doi.org/10.1038/s41467-024-53173-w) | Experimental evidence that electrical interactions matter for course control. | The MaleCNS chemical tables do not supply conductances in this model’s units or specimen-specific electrical edges. Zero modeled gap entries express this missing constraint. |
| Walking-dependent context | [Fujiwara et al. (2017)](https://doi.org/10.1038/nn.4435) | Nonvisual/locomotor modulation provides context for visual responses during walking. | Rigid visual motion replay supplies optic flow without a measured locomotion-dependent gain or efference-copy signal. |

The T4/T5 numerical ports are separate from the functional fixed-neighbor frontend.
Reproducing an author model, matching a native stimulus, matching a recording and
validating a full-eye downstream model are different evidence levels. None is
silently substituted for another.

The Erginkaya source protocol includes still/motion/still/reversed-motion/still
intervals of 2/2/5/2/2 seconds. The existing legacy benchmark compresses its two
motion epochs into a two-second signed input-clamp diagnostic. Its rate-based
signed epoch ratio is not a frame-exact or fluorescence-time-course reproduction.
Per-epoch recorded z-scoring needs a measured baseline distribution; a deterministic
zero-baseline model cannot supply that distribution without additional assumptions.
We do not add artificial variance or generic reporter kinetics to force z-scores.

There is also a readout-alignment gap. The legacy calculation pools both model
hemispheres, while source recordings are individual, hemisphere-aligned neurites.
Soma side is not a verified mapping to the imaged axonal/dendritic compartment.
The yaw decoders retain separate left/right features; the pooling issue concerns
this legacy physiological diagnostic. The post hoc L/R/pooled-component audit
exposes this dependency; it does not select
a favorable side or replace the frozen endpoint comparison.

For these reasons the current physiological comparison is a conditional diagnostic.
It does not establish quantitative validation of HS, H2, bIPS or DNp15 physiology,
and the observed numerical errors alone do not locate the biological cause of a
mismatch. A defensible future comparison must fix the actual stimulus/display,
neurite identity, response window and measurement model before validation, then
retain independent flies and matched recording conditions.

Local provenance, source hashes and complete conditional errors are retained in
[the source gate](../results/anatomical_strengthening_v1/physiological_source_gate.json),
[split audit](../results/anatomical_strengthening_v1/physiology_split_audit.json),
[benchmark](../results/anatomical_strengthening_v1/physiology_benchmark.json),
[readout audit](../results/anatomical_strengthening_v1/physiology_readout_audit.json),
and [the separate Study B report](ANATOMICAL_STRENGTHENING_REPORT_V1.md).
The old external manifest’s incorrect article title is corrected in new provenance;
its original bytes remain unchanged.
