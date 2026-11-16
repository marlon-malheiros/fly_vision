# HS temporal refinement V1

Started 2026-11-02; completed 2026-11-03 (America/Belem).
**All 20 planned numerical checks pass at the refined resolutions;
the physiological frequency-response discrepancy persists.** This completes the
bounded numerical follow-up, not biological validation. No neural parameters,
gain calibration, connectivity or decoder were changed.

## What we wanted and what we did

The [preceding gain-control study](HS_GAIN_TRANSFER_REPORT_V1.md) improved the
preferred-direction contrast response but failed its full physiological gates.
It also reported four temporal numerical failures: preferred-direction 2.5 and
15 Hz, in both the original and calibrated-gain frontends. We needed to establish
whether a sampling error could explain the physiological discrepancy before
revising another biological mechanism.

The [prospective protocol](HS_TEMPORAL_REFINEMENT_PROTOCOL_V1.md), configuration,
code and 169 dependencies were frozen before execution; Git checkpoint
`0fa29c0`. Fourteen image cases yielded 28 model solves and four additional
exact legacy replays. Both frontends used identical binocular images, the same
13,624-cell LPi-intact circuit, fixed sigma=0.121902687872575, existing delays
and graph parameters. Preferred direction, phase zero, methods85 field only.
No curve fitting, new neural connections or fresh biological targets.

| Profile | Image interval, ms | Source interval, ms | Frequencies, Hz |
|---|---:|---:|---|
| Old primary, retained | 5 | 10 | 0.5, 1, 2.5, 15 |
| Old temporal / new solver control | 2.5 | 5 | New control: 2.5, 15 |
| Image only | 1.25 | 5 | 2.5, 15 |
| Middle | 1.25 | 2.5 | 0.5, 1, 2.5, 15 |
| Fine image | 0.625 | 2.5 | 2.5, 15 |
| Fine | 0.625 | 1.25 | 0.5, 1, 2.5, 15 |

All new comparison solves use RK4 at 0.25 ms. The inherited absolute 1 ms forcing
ramp is preserved; every source/solver ratio is an integer and every source
interval exceeds the ramp duration. Images remain four-bit square-wave gratings
refreshed at 60 Hz, held between refreshes, with continuous moving phase from
2–4 s. Finer image sampling changes how accurately that held display is processed;
it does not turn the stimulus into a higher-refresh display. Temporal refinement
does not change retinal coordinates or the gain footprint.

## Numerical findings

The endpoint remains equal-mean right HSN/HSE/HSS atanh(rate), mean [2,4) minus
[1,2) s. Each numerical comparison retains its frontend's **old phase-zero PD1 Hz
primary endpoint** as the reference. Both original tolerance requirements apply:
absolute error <= .05*max(abs(base),abs(reference))+1e-7 and error/reference <= .05.

| Frozen primary comparison | Pass / total | Largest error / fixed reference |
|---|---:|---:|
| Middle → fine, all four frequencies | 8/8 | 2.2624% |
| Middle → fine-image, flagged frequencies | 4/4 | 1.1594% |
| Fine-image → fine, flagged frequencies | 4/4 | 1.1031% |
| Old temporal → new solver control | 4/4 | 5.8846e-7% |
| **Total** | **20/20** | |

All supporting new comparisons also pass: earlier joint refinement 6/6
(maximum 4.3485%), intermediate image-only 4/4 (2.3709%), intermediate source-only
4/4 (1.9776%). The four old coarse failures remain failures, maximum 9.0828%.
They are preserved rather than reclassified using the favorable fine grids.

The separated checks show measurable contributions from **both image and source
sampling**, with negligible solver contribution in these cases. They establish
agreement on the two finest tested grids and endpoints, not proof of asymptotic
convergence or a unique continuous-time ground truth. They do not certify every
frequency, direction, phase or the candidate's spatial convergence.

An explicitly **post-analysis descriptive diagnostic**, with no effect on the
frozen gates, compares fine endpoints with old primary endpoints. Fine responses
are 7.88–8.81% lower across the four frequencies and two frontends. Thus the old
coarse bank should not be retrospectively labeled converged. Refinement largely
shifts response amplitudes together, leaving the frequency-response shape
discrepancy. [Diagnostic](../results/hs_temporal_refinement_v1/coarse_fine_descriptive_diagnostic.json).

![Refinement with a fixed old reference](../results/hs_temporal_refinement_v1/temporal_refinement.png)

## Biological comparison after refinement

This is a descriptive four-frequency subset, one phase and preferred direction,
using already inspected recordings from Source Data 5m. It is not a new blind
test, new animal cohort, repeat of the complete 15-coordinate gate or new fitted
peak estimate. Unknown animal overlap, stimulus registration, source provenance
limitations and uncalibrated model-to-voltage mapping remain as documented in
the predecessor report.

For this biological shape comparison only, each fine model curve is normalized
by its **own fine PD1 Hz** endpoint, as the recorded curve is normalized by its
recorded PD1 Hz mean. This differs deliberately from the fixed old anchor used
for all numerical acceptance decisions; no numerical failure is hidden by
renormalization.

| Frequency, Hz | Recorded mean / PD1 Hz | Fine baseline | Fine gain candidate |
|---|---:|---:|---:|
| 0.5 | 1.06820 | 0.53402 | 0.53355 |
| 1 | 1.00000 | 1.00000 | 1.00000 |
| 2.5 | 0.67603 | 1.75716 | 1.75915 |
| 15 | 0.07644 | 1.16585 | 1.18928 |

Both fine model curves still favor 2.5 Hz over 0.5 Hz, opposite to the recorded
comparison. At 15 Hz the gain model predicts 1.189 times its 1 Hz response,
whereas the recorded mean is 0.0764. The tested discrepancy therefore cannot be
removed by the executed sampling refinements or a common positive scalar gain.
This is evidence of a remaining model/stimulus/measurement mismatch under the
declared assumptions, not proof of one missing cell or a specific time constant.

The full old bank's 5 Hz grid maximum and 15/15 failure counts are **not** newly
certified here: 5 Hz, the other phase and null-direction conditions were not
rerun at the finest resolution. Directional suppression remains a separate
unresolved property. The gain candidate's earlier contrast improvement remains
documented evidence from that earlier assay, not revalidated across new sampling
or walking conditions in this round.

## Reproducibility, resources and preserved evidence

Two focused tests pass: refresh indices agree at every sampled time with an
independent rational-integer 60 Hz schedule; valid clock ratios and both error
requirements are checked. Four full old-rate replays reproduce image hashes,
source hashes, rates, final states and checkpoints bitwise at the old solver
step. Independent log1p membrane-proxy arithmetic verifies 28 new endpoint
summaries, maximum difference 6.94e-18. Every numerical pass/fail is separately
recomputed. All pre-motion outputs remain exactly zero; clipping count zero.

All 353 indexed files of the retained predecessor gain-transfer package were
verified, together with the original successful small-turn decoder weights and
cutoff. This is not a claim about historical intentionally retired movie files.
[Prior evidence integrity](../results/hs_temporal_refinement_v1/prior_evidence_integrity.json).

Observation and replay CPU total **1659.42 s**, below the frozen 3600 s cap.
Peak worker RSS **1,454,559,232 bytes**, below 2 GiB. Results before completion
copies were approximately **3.07 MB**, below the 64 MiB whole-run cap and 32 MiB
estimate; more than 20 GiB free reserve remained. No movies, source ZIP copies,
permanent full T4/T5 drives or overwritten historical results. No execution or
scoring failure occurred in this round. Previous scientific/preparation failures
remain intact.

Evidence: [all numerical comparisons](../results/hs_temporal_refinement_v1/numerical_checks.json),
[tabular comparisons](../results/hs_temporal_refinement_v1/numerical_checks.csv),
[fine frequency values](../results/hs_temporal_refinement_v1/fine_frequency_subset.json),
[independent endpoint arithmetic](../results/hs_temporal_refinement_v1/endpoint_review.json),
[execution/resources](../results/hs_temporal_refinement_v1/simulations_complete.json),
[decision](../results/hs_temporal_refinement_v1/decision.json).

The reproducible CLI is `scripts/hs_temporal_refinement_v1.py` with stages
`prepare`, `run`, `analyze`, using the scientific environment recorded in
`environment.json`, `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1`.
Existing output destinations reject writes intentionally. Replay in a separate
tree containing the indexed source/config/protocol files and retained dependency
paths listed in `before_execution.json`; leave the new result directory absent
before `prepare`. Never copy the bulk historical movie archive. `run` verifies
the freeze and receipts before reusing completed cases. `seal` saves exact source,
report and dated progress copies; `audit` independently rehashes files and
dependencies after writer exit. The audit writes one exclusive receipt, so it
also requires a fresh receipt destination if repeated. No second complete
14-case experiment is claimed; four exact legacy replays were executed.

Completion crossed local midnight. Use the companion
`scripts/finish_hs_temporal_refinement_v1.py seal` and `audit` for the completed
archive: its dated progress snapshot uses the actual completion date. This
archive-only correction leaves the frozen simulation implementation and every
scientific criterion unchanged; the original script's hard-coded start-date
archive naming remains preserved in its source snapshot.

## Decision and next alternatives

The bounded numerical milestone is complete: 20/20 new gates pass; zero biological
parameters fitted. Biological validation and walking advancement remain false.
No new small-turn result, biological bIPS causality, autonomous control or
publication acceptance is established.

Recommended next scientific step: evaluate one independently constrained temporal
filtering hypothesis in a separate frontend version, preserving the calibrated
contrast candidate as a comparator. Published temporal measurements must constrain
the mechanism; the now-inspected HS frequency curves are development data.
Freeze the revised model before evaluating a genuinely unused measurement.
Opposite-direction suppression requires its own mechanistic test. Do not choose
a tenfold delay change merely because the sampled peak differs by tenfold.

An alternative is to keep the model fully fixed and prioritize obtaining better
matched upstream temporal recordings and stimulus descriptions before another
revision. That improves biological identifiability but may depend on unavailable
data. Repeating the same decoder optimization or more coarse sampling sweeps is
not supported by this result.

## Undergraduate explanation

We want a neural model that notices small turns **and** responds like real fly
neurons. We already have a limited simulated small-turn success, and a separate
gain adjustment improved contrast responses. Here we checked whether the computer
was taking time steps too large to trust the physiology comparison. Smaller steps
make the tested responses stable within our declared tolerance, but the model
still reacts too strongly to fast visual motion. That tells us refinement alone
does not solve the biological mismatch. We now have a better numerical foundation
for investigating temporal processing without discarding the earlier results.
