# Neural-only milestone: 5°/s works in the benchmark; 2°/s remains open

31 October 2026.

We want a neural model that notices small body turns while a fly is already walking. We kept the existing visual frontend and MaleCNS circuit fixed, trained readers of simulated neural activity, and tested them in 24 new virtual rooms. No image-motion estimator is used by these readers.

One predefined secondary reader passes the behavioral criteria at **5°/s** across all three walking speeds:

| Walking speed | Correct signed 5°/s detections | Straight-walking alarms |
|---:|---:|---:|
| 5.5 mm/s | 48/48 | 0/24 |
| 11 mm/s | 48/48 | 0/24 |
| 16.5 mm/s | 47/48 | 0/24 |

It also passes all **135 declared numerical comparisons**. Four full replays and independent calculations check the implementation. These are finite simulation results, not guarantees for all environments.

**Our original 2°/s goal is still unmet.** The same conservative reader detects only 14/48, 8/48 and 2/48 such turns across speeds. Lowering the cutoff catches more turns but brings back false alarms. Spatial readers also failed the complete target; their negative results are preserved.

This is progress toward a neural solution: useful turn information can be read from the model without the image estimator. It is an artificial supervised readout of 45 simulated neurons, not a newly validated biological circuit. The frontend remains a functional surrogate; physiological validation and a demonstrated bIPS advantage remain open. No closed loop was added.

Next alternatives are a direct test of the published full FlyVis neural pipeline with its existing pretrained flow decoder, or new physiological constraints on motion encoding and spatial integration. We verified that the decoder weights exist; that pipeline has not yet been tested on our walking scenes.

[Population study and failures](NEURAL_POPULATION_READOUT_REPORT_V1.md), [cutoff study and supported 5°/s result](NEURAL_POPULATION_CUTOFF_REPORT_R2.md), [five-degree numerical protocol](NEURAL_POPULATION_FIVE_DEGREE_NUMERICS_ADDENDUM_V1.md), [reproduction instructions](NEURAL_POPULATION_REPRODUCTION_V1.md).
