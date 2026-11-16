# Soma-matched full-clock physiological diagnostic — V1

Completed numerical/data analysis 2026-10-21. This is a separately frozen conditional diagnostic; it is not full physiological validation of the visual model. Figure presentation review and the broader validation/hardware study remain separate.

The comparison replaces bilateral pooling and compressed epochs with explicit recorded soma-side matching and full 13-s protocols. It preserves both chemical graphs and every neural parameter. The same three historical signed analytic flow clamps drive both circuits; retinal images are bypassed.

## Data, calibration and independent checks

Metadata selected 82 sessions across eight class/reporter/background cohorts. Extraction saved 240 fluorescence trace summaries. Development uses 35 flies and testing uses 28, including 23 previously unused test flies; five earlier diagnostic test flies are explicitly reused. No neural-calibration fly enters the test partition. The current test set contains 95 observed trace summaries.

Each recorded trial/ROI is standardized using its own measured 1–2-s baseline. Measurement filter/gain candidates are fitted only on development data. This is an explicit phenomenological observation fit, not inferred neural dynamics or added neural noise. The primary comparison transfers the original circuit’s observation fit unchanged to the expanded circuit. Secondary per-circuit observation fits are retained.

Independent indexing and trial/ROI loops reproduced all 240 saved observed traces; maximum mean discrepancy 1.42e-14. All sixteen selected observation fits, source motion epochs and whole-fly splits passed review. The ledger retains 284 unusable/padded trial/ROI array units and their reasons. These checks establish numerical/data reproducibility, not biological validity.

## Primary held-out results

RMSE is in measured baseline-SD units. Each fly has equal weight within its cohort. Values are not directly comparable with the previous bounded discrimination-index RMSE, which used different data/readouts.

| Cohort | Test flies | Original RMSE | Expanded RMSE | Expanded − original MSE (95% fly-bootstrap interval) |
|---|---:|---:|---:|---|
| DNp15 / GC6f / dendrite / WT | 5 | 1.7550 | 1.7689 | +0.0492 [-0.1122, +0.3076] |
| DNp15 / GC7f / dendrite / native | 1 | 2.4784 | 2.5178 | +0.1969 [+0.1969, +0.1969] |
| H2 / sytGC7f / axon / native | 2 | 4.6197 | 4.6178 | -0.0176 [-0.0404, +0.0052] |
| HS / GC7f / axon / native | 3 | 5.6928 | 5.6945 | +0.0186 [+0.0034, +0.0377] |
| HS / sytGC7f / axon / native | 3 | 4.7710 | 4.7754 | +0.0416 [-0.1991, +0.4696] |
| bIPS / GC6f / axon / WT | 9 | 8.2119 | 8.6381 | +7.1812 [+1.3448, +14.1553] |
| bIPS / GC7f / axon / native | 1 | 2.9386 | 3.1691 | +1.4077 [+1.4077, +1.4077] |
| bIPS / sytGC7f / axon / native | 4 | 2.3872 | 3.1186 | +4.0267 [-0.9572, +10.0840] |

The anatomical additions do not show a consistent improvement across these cohorts. Test cohorts of one or two flies cannot establish population-level agreement. The saved zero-baseline skill, motion-only errors, temporal correlations and signed epoch contrasts expose additional failures; improvement of one metric does not substitute for agreement across measurement conditions.

![Primary error comparison](../results/validation_hardware_v1/soma_matched_physiology_v1/figures/cohort_error_comparison.png)

## Limitations and interpretation

Soma-side metadata resolves which modeled hemisphere is read, under a single-compartment population assumption. It does not prove that a model rate reproduces an imaged axon or dendrite. HS recordings are class-level rather than a verified one-to-one mapping to each selected MaleCNS subtype. Wild-type genetic-control backgrounds and reporter variants remain separate cohorts.

The input is a signed analytic clamp inherited from the earlier diagnostic, not the nonnegative image frontend. Exact retinal movie statistics, per-fly optics/head alignment, reporter transfer and missing electrical circuitry remain unresolved. The source recordings are from immobilized flies, so they do not validate active-walking state modulation. Filtering/calibrating an observation model cannot remove those gaps.

The normalized protocol contrast uses first-minus-second epoch responses without class-specific sign flips. It is explicitly not a reproduction of the published Figure 3e discrimination index; zero-denominator values remain undefined. No neural gain or connection was tuned for these outcomes.

## Undergraduate explanation

We improved the fairness of the comparison by reading the correct side of the model and using the recordings’ actual time course. We learned the recording-to-model scaling from one set of flies and tested it on different flies. Adding more anatomical neurons did not consistently make the predictions better. This tells us that correcting the comparison is useful, but the circuit still needs stronger biological constraints before we can claim it reproduces a real fly’s physiology.

[Frozen protocol](SOMA_MATCHED_PHYSIOLOGY_PROTOCOL_V1.md) · [Independent review](../results/validation_hardware_v1/soma_matched_physiology_v1/independent_review.json) · [All fly metrics](../results/validation_hardware_v1/soma_matched_physiology_v1/test_fly_metrics.csv) · [Observation candidates](../results/validation_hardware_v1/soma_matched_physiology_v1/observation_candidates.json)
