# Adaptive Mi1 integration: exploratory interface diagnosis

2026-11-05. This is POST-OUTCOME interpretation of existing frozen test inputs,
not a new acceptance criterion, model fit, synaptic lesion or biological result.
The main candidate already fails its frequency-violation and null-suppression
guards. All core numerical checks pass. No additional neural solve is performed.

For each eye/type, take the unweighted mean external drive during motion[2,4)s
in direction0 and180. Define D=(mean0−mean180)/(mean0+mean180). This is a
direction contrast between pooled injected signals, NOT a preferred/null DSI
of recorded or simulated T4 cell activity. Both nominal1Hz and fast15Hz, both
eyes and both source types are retained. No direction is relabeled to improve D.

| Right-eye 15Hz external pool | Comparator D | Adaptive D | Reduction in absolute direction difference |
|---|---:|---:|---:|
| T4a | +0.135546 | +0.002557 | 95.16% |
| T4b | -0.081858 | -0.001326 | 97.15% |

The absolute difference between opposite-direction pool means drops by about
95–97% in the right-eye15Hz T4 external-drive pools under this bridge. The
adaptive source supplies positive motion-minus-static increments to BOTH pools
for BOTH directions. This helps explain why fixing the HS preferred-motion sign
does not guarantee preserved direction discrimination. It identifies a weakness
already visible in these external input summaries, not only in the HS output
measurement. It does not uniquely establish the cause of the full HS mismatch.

Separately, preferred15Hz HS static/moving means change from0.002876/0.002124
in the comparator to0.001267/0.003015 in the adaptive model. For null motion the
adaptive moving mean is0.002675. Thus the sign change involves both a lower
static baseline and a higher motion response; it is not evidence for a uniquely
selective preferred-direction gain. Values are arbitrary graded-state units.

These pool means are not synaptically weighted HS currents, cellwise source
tuning, actual recurrent T4 firing, membrane voltage or calcium. Spatially
heterogeneous changes can cancel in a pool. Inherited spatial embedding,
Mi1/Tm3 relative coupling and downstream interactions remain qualified. Do not
claim that real T4 neurons lose95–97% of direction selectivity or that adding
one inhibitory synapse is a demonstrated fix.

The actionable next constraint is the intermediate motion representation:
compare T4 preferred/null spatial and temporal tuning before asking the whole
graph to match HS. The current Mi1 flash component result constrains temporal
responses alone. Reusing these HS outcomes to select another arbitrary coupling
would remain development, not independent validation.

[All pool contrasts](../results/mi1_hs_integration_v1/T4_input_direction_contrasts_exploratory.csv),
[exact derived comparisons](../results/mi1_hs_integration_v1/interface_interpretation_exploratory.json),
[HS static/moving means](../results/mi1_hs_integration_v1/HS_epoch_means.csv),
[main technical report](MI1_HS_INTEGRATION_REPORT_V1.md).
