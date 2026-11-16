# Independent geometry-review clock correction R2

2026-11-06, after model outcomes. The initial independent reviewer subtracts the onset directly from the source event array, which has unsigned integer dtype. Pre-onset events underflow to huge positive timestamps; its subsequent search for an event at or before time0 fails with IndexError. The production sampler explicitly converts events to float before subtraction and is unaffected.

Preserve `scripts/review_t4_geometry_identifiability_v1.py` and the study's `failed_review_v1.log`. The separate R2 reviewer converts native integer timestamps to signed int64 before subtracting onset. All integer pixels, event order, source parameters, predictions, scores and acceptance rules remain unchanged. R2 must compare all saved input arrays and rederive all scores rather than assume that correcting the reviewer establishes biological validity. This is an audit implementation correction, not a new biological test or a model repair.
