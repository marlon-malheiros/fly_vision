# Fixed retrospective clock scenarios — V6

Declared 2026-10-22 before computing these new policy summaries. The full V5 scheduled timing results are already known. This analysis reuses all 300 preserved episodes and is retrospective; it is not a new timing benchmark or a held-out biological experiment.

Use the fixed V6 5-ms frame-response and 5-ms oldest-image-age bounds. Evaluate exactly two clock assumptions, without choosing a favorable one after scoring:

1. **Software reference:** exposure midpoint equals V5 scheduled availability, with zero mapping uncertainty. This reproduces the original frame-response gate.
2. **Synthetic capture offset:** exposure midpoint is 500,000 ns before scheduled availability, with 100-ns uncertainty. This matches the separately declared full-camera logic traces, approximating only a hypothetical 1-ms exposure/readout timing relationship. It is not a measurement of real camera transport, synchronization or exposure timing.

Use V5 scheduled/start/end timestamps without changing any frames or durations. Reconstruct a per-episode affine camera mapping of rate one, with exposure-midpoint anchor set by each assumption. Compute source lower/upper bounds and the stricter image-age/availability deadline with exact integer arithmetic. Count admission faults (start already late), completion faults (start admissible, end late), and original availability-only faults separately by mode. Keep all 120,300 frames, including episode-initial frames.

Also find the first violating frame of every episode. A latched wrapper would publish only the preceding prefix and withhold that frame and all subsequent frames until an explicit reset. Report prefix/withheld counts and episodes requiring reset, without silently resetting mid-episode or claiming that the preserved post-fault neural trajectory would still be available through the wrapper. Existing episode resets provide the only recovery boundaries in this calculation.

Save every per-frame deadline and fault flag, source input hashes and per-episode summaries. Independently reconstruct every classification using scalar arithmetic. Wrapper overhead and physical capture were not present in V5 timings; these summaries cannot certify guarded performance or replace the original reported gate.
