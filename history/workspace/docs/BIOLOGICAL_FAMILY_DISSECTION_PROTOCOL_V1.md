# Biological family dissection and DNp15 audit V1

27 October 2026. Authorized follow-up to the completed biological failure-localization
study. Earlier data and intact/joint-clamp outcomes are known. Freeze this recipe
before computing single-family outcomes or new DNp15 diagnostic summaries. This
is retrospective development, not independent biological validation.

## Execution and controls

Use the same eight saved inputs: the first two original dot seeds, four motion
protocols, primary aligned_100 display, 13 seconds each. Preserve all graph,
frontend, numerical, channel-routing and measurement parameters. No rerendering,
new connection, conductance or closed-loop controller is introduced.

The complete 2×2 factorial design uses the same expanded graph and input-weight
normalization in every state:

- `expanded_intact`: both added families active, reuse all eight sealed cases.
- `expanded_ulptcrn_silent`: silence the 17 qualified uLPTCrn-family candidates.
- `expanded_h2rn_silent`: silence the eight qualified H2rn-family candidates.
- `expanded_new_silent`: both added families silent, reuse all eight sealed cases.

Silencing sets the existing activity mask to zero; it does not renormalize
remaining inputs or imply absence of any connection. Candidate identities remain
qualified homologies. Reproduce one complete expanded-intact trajectory exactly
before executing the sixteen new single-family cases. Verify copied baselines
against the previous immutable index. Independently check masks, source identity,
currents and a Python RK4 interval in all 32 factorial cases. Run fixed-forcing
half-step controls for both new single-family variants on the first yaw input.

Save full wide-field rates, final states, two whole-network checkpoints and
complete selected-graph chemical currents by source role, using the existing
execution method. The wrapper redirects only this process's output paths and
constructor; prior source files and directories are never edited.

## Analysis frozen before outcomes

Reuse all 234 known recording summaries and inherited calibration/test/walking
assignments. Preserve separate reporter, compartment and genotype cohorts.
Use the preceding study's three normalization choices, both contrast indices,
author soma mapping and all four motion protocols. The original biological
benchmark observation mapping is primary. Secondary own-model fits retain the
same 56 existing candidates, calibration bilateral data only and deterministic
ties. Hash fits before reused test scoring; do not choose a replacement circuit
or measurement method using these outcomes.

For each seed, side and role, retain raw last-500-ms epoch contrasts and
magnitude indices. For any scalar response f, compute the factorial interaction
`f(both active) - f(U silent) - f(H silent) + f(both silent)` and each family's
conditional effect with its partner active and silent. A nonlinear index
interaction is descriptive and is not itself proof of synaptic synergy. Retain
raw contrast interactions alongside it.

Classify bIPS sign dependence using all four seed/side raw indices with a 1e-12
contrast-resolution floor. Report all signs and magnitudes rather than selecting
a side or seed. If the intact sign is not positive everywhere, report failure
of robustness rather than declaring a family-specific rescue. If one single
clamp removes the positive sign everywhere and the other preserves it everywhere,
that family has the stronger conditional sign dependence in this model. If both
remove it, report joint dependence; if both preserve it while the joint clamp
removes it, report redundant sign support. Mixed outcomes are heterogeneous.
These are decision labels for this finite graph, not biological necessity claims.

Compare bIPS and DNp15 jointly using fixed observation transfer, including
unilateral and walking-preparation errors. Retain worse outcomes and differences
after secondary calibration. No candidate qualifies for biological validation
from a positive index or a better mean waveform score alone.

## DNp15 audit

Independently reread original metadata for all selected DNp15 sessions: neuron,
neurite, soma, imaging hemisphere, reporter/genotype, ROI indices, clocks and
stimulus names. Compare with inherited plans and exact selected arrays. Distinguish
an actual indexing/identity contradiction from an unverified single-compartment
measurement assumption. Do not choose a hemisphere because it fits better.

On every known DNp15 waveform, separate fixed-mapping squared errors into the
two baseline windows, motion epochs and post-motion periods. Report first/second
motion errors and signed response contrasts. Evaluate an explicit descriptive
shape ceiling: with the already frozen filtered model waveform x and recorded y,
compute the best nonnegative scalar projection gain max(0, <x,y>/<x,x>) and the
remaining MSE, plus signed cosine similarity. This uses each inspected trace
and is an oracle bound, not a fitted deployable measurement model or validation.
It asks whether scalar gain alone could account for each mismatch; no oracle
gain is adopted. Preserve the zero-input case and undefined cosine separately.
Also report within-fly stimulus differences and cross-cohort variability, without
pooling reporter/genotype groups or inventing physiological parameters.

Recheck primary source methods and publicly documented dataset availability for
stimulus/compartment constraints. Existing inspected recordings cannot become new
validation data. If independent matched recordings or exact stimulus arrays are
unavailable, preserve that result and distinguish data limitations from a
demonstrated model defect.

## Decisions and alternatives after this study

1. A clear family contribution supports a later, separately frozen pathway-level
   test in that family. Mixed/redundant outcomes support distributed-circuit
   analysis rather than deletion of one family.
2. A verified metadata/indexing error supports an evidence-based corrected version;
   otherwise preserve the original mapping. A shape mismatch motivates better
   physiological dynamics or matched inputs when constrained by evidence. A
   mainly amplitude mismatch motivates independent reporter/state calibration.
3. Only a justified candidate with an explicit fixed measurement/readout rule
   should proceed to fresh small-yaw environments. Earlier walking family lesions
   did not establish a general gain; do not repeat them as new evidence.

Stop after the declared factorial comparison and audit. Report supported and
unresolved mechanisms, propose alternatives, append progress, archive exact
sources and dated progress before sealing, and verify after sealing exits.
No outcome-driven parameter search or new small-turn success claim is authorized
by this protocol.
