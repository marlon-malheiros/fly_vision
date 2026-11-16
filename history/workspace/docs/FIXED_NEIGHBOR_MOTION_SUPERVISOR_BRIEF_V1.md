# Functional frontend result for supervisor review — 13 October 2026

**We now have a tested functional image-to-motion-to-HS/H2 prototype.**
The result is `FUNCTIONAL_END_TO_END_PASS` under the frozen benchmark.

A new fixed retinotopic circuit computes all eight ON/OFF and axis-opponent
channels from neighboring luminance samples and one fixed delay. It receives no
movie direction or target preferred-angle labels. Completed channels are routed
to declared T4/T5-like output slots and the frozen MaleCNS network.

All eight horizontal groups pass on each of four textures, including three new
seeds: the lowest expected-and-selective fraction is 99.88%. Supplemental 30/90°/s
checks and all 16 cardinal grating eye/family comparisons pass. STATIC motion
output is zero. Pixel mirrors and label replays pass. Temporal scrambling reduces
the signed motion response below 0.7% of the ordered response.

All ten HS/H2 targets show measurable expected global direction on all four
textures (40/40); ipsilateral unilateral contrasts also agree (40/40). Every
recorded network cell passes STATIC stability. Twenty-eight initial tests,
independent checks of all 47 source executions, independent replay of all 28
network trials and the final individual-score audit pass.

This is an algorithmic surrogate with explicit chart, spatial, temporal and
output-routing conventions. T4/T5-like names are assigned output slots. It does
not establish individual T4/T5 physiological accuracy or independently measured
specimen optics. Vertical-like slots also show horizontal texture selectivity
(85–87% under the binary criterion), at about 13–14% of horizontal response
strength. That limitation is retained. No biological degeneracy is claimed.

Memory/swap interruptions, a reference pixel-endpoint bug and post-analysis
arithmetic/mean-export precision corrections are documented with original logs.
Circuit parameters, trajectories, acceptance thresholds and scientific decisions
were never tuned after the benchmark. The original biological-model failures
remain archived as separate evidence.

The reusable component and standalone demo can be run without biological
recordings. The compact review package contains reports, tables, code and figures;
full numerical evidence is indexed in the workspace. This is a useful baseline
for controlled integration work and a concrete artifact to review with the
supervisor. Broader biological claims require separate matched-data validation.

[Technical report](FIXED_NEIGHBOR_MOTION_REPORT_V1.md) ·
[Architecture](FIXED_NEIGHBOR_MOTION_ARCHITECTURE_V1.md) ·
[Reproduction](FIXED_NEIGHBOR_MOTION_REPRODUCTION_V1.md).
