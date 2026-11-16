# Physiological search: conclusion and final integrity correction R2

2026-11-04. The finite search is complete; biological validation remains incomplete.

We want a neural visual model that detects small turns and agrees with real fly recordings. This round tested every combination in a fixed grid of 72 models, without fitting new parameters. Twenty-four were primary parallel-inhibition candidates; 48 were historical single-arm diagnostic comparisons. All prior models and results remain preserved.

The useful improvement is contrast handling. Reusing the existing fixed normalization moves the preferred half-contrast response from about 0.740 to 0.962 of full contrast, inside the retained data band of 0.827–1.000. The strongest balanced candidate is `g1_k250_parallel_T5_slowing_only`. It passes all of this round’s development guards except the preferred-response sign rule. It still misses 4 of 7 frequency coordinates, so this is a partial repair, not an otherwise fully validated model.

No primary candidate passes every frozen development guard. All three confirmed finalists predict a negative response at preferred 15 Hz, where the retained recording mean is positive. The leading candidate predicts −0.0755 of its 1 Hz response, versus the recorded +0.0764. Finer temporal sampling preserves its negative sign. Changing the solver is therefore not a supported fix for this finding.

An exploratory matched-input control localizes part of this effect within the model. At 15 Hz, omitting horizontal-T4 external drive leaves a positive HS response (0.00118724); adding that drive produces -0.00075214, a change of -0.00193938 in model units. At 1 Hz that same input contributes positively. The recurrent neurons remain active in this control: it is neither a biological cell lesion nor proof of a unique missing synapse. [Exact diagnostic](../results/physiological_factorial_search_v1/exploratory_input_contribution_r2.json).

All 160 screen/strict-step comparisons and all 18 finalist refinement checks pass. The independent checker reproduced 1,005 endpoints within 1.15×10⁻¹⁷. The original 228 pilot, 230 temporal-study and 59 source-study indexed files rehash unchanged. Scientific CPU use was 7,960 seconds; peak worker RAM was 1.84 GiB. Outputs occupy about 119 MiB before this small final correction, with no movie archive. Numerical reproducibility does not establish biological validation.

A distinct supported next direction is to audit the newly located L1/L2 and C2/C3 feedback datasets for stimulus-matched upstream constraints. Those data have not been used to choose this round’s models. Their file availability is established; their suitability, measurement model and connection to our network still require an audit. Simply placing another feedback filter before measured kernels may double-count feedback already present in those kernels. [Source audit](PHYSIOLOGICAL_FEEDBACK_EVIDENCE_AUDIT_V1.md).

Two software failures are preserved. V1 score writing failed on a NumPy boolean after all screens; the separately frozen R2 continuation corrected serialization without changing mathematics or repeating simulations. The first seal then included an open report log: its final 25-byte completion line invalidated that one indexed entry. The post-exit audit caught this. The original failed index remains unchanged; the corrected authoritative index is [completion_r2/artifact_index.json](../results/physiological_factorial_search_v1/completion_r2/artifact_index.json). All scientific arrays, targets, protocols and the original technical report are unchanged.

[Full technical report](PHYSIOLOGICAL_FACTORIAL_SEARCH_REPORT_V1.md), [all scores](../results/physiological_factorial_search_v1/complete_scores.csv), [strict confirmation](../results/physiological_factorial_search_v1/confirmation_scores.json).

For an undergraduate: we fixed one mismatch in how the model handles contrast, but it still responds incorrectly to some motion. We checked that this is reproducible behavior of these equations, rather than a coarse solver error. The next useful evidence concerns the upstream circuit and how its measurements connect to the model.
