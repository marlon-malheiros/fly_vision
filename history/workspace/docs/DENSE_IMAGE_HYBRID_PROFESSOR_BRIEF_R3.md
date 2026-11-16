# Small-turn detection: professor brief, R3

2026-10-30. We obtained a working **external image/neural hybrid** for small-yaw onset during simulated forward walking. The tested neural-only readouts still produce excessive straight-walking alarms; biological validation remains incomplete.

The selected detector is `dense_hybrid/full_dnp_change`. It combines the unchanged LPi-expanded MaleCNS output with a dense 0.5-degree image-motion estimator, using current/past observations and no true speed or yaw. It was selected before testing 60 untouched rooms (960 episodes), with unchanged ≥80% correct-turn and ≤10% any-straight-alarm criteria at every speed and yaw magnitude. The decision endpoint is 190 ms after yaw onset.

| Speed mm/s | Correct ±2 turns | Each sign | Correct ±5 turns | Straight any alarms |
|---|---:|---|---:|---:|
| 5.5 | 120/120 | 60/60, 60/60 | 120/120 | 0/60 |
| 11 | 120/120 | 60/60, 60/60 | 120/120 | 0/60 |
| 16.5 | 115/120 | 58/60, 57/60 | 120/120 | 0/60 |

Stationary alarms: 0/60. All 81 selected numerical comparisons pass (largest score difference 0.1336, limit 0.2); independent score/count/bootstrap checks and four end-to-end replays pass. All previous failed repairs remain reported and sealed. No graph, neural parameter or cutoff was tuned for this result.

This completes a bounded open-loop engineering milestone. The image branch supplies extra resolution and geometric assumptions. Image-only also detects 120/120 small turns at every speed with zero straight alarms; adding the neural branch has no demonstrated reliability benefit here. We have not demonstrated a neural repair, a bIPS advantage, real-fly physiology or physical-robot performance. The defensible next biological question is what additional measured circuitry/encoding could recover this reliable visual information without the external estimator.

[Full report, figures and limitations](DENSE_IMAGE_HYBRID_REPORT_R3.md). [Complete final counts](../results/dense_image_hybrid_r3/analysis/test_curves.csv).
