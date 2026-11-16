# Shared-eye T4/T5 and bIPS comparison V1

13 November 2026. This is a **retrospective computational comparison** of
previously inspected visual conditions, not a new biological or walking test.
The [frozen protocol](SHARED_EYE_T4T5_BIPS_PROTOCOL_V1.md) and source/method
hashes preceded the new graph outcomes.

## What was implemented and tested

Seven previously completed shared-image time series supply drives for all
13,579 T4/T5 source IDs: 6,861 T4 and 6,718 T5. Their original full-population
study used published full-cable T4 and published T5 dynamics on shared
binocular images. The identical saved source time series now feed the LPi
graph with the explicitly held-input timing rule. This is the **older
population frontend**, not the later cell-specific T4 registration ensemble;
the latter's biological result does not automatically transfer.

Each input was simulated with the intact graph and with both bIPS cells
silenced, without changing weights, source inputs or normalization. Both
variants completed all seven conditions. The predeclared 1 ms versus 0.5 ms
network refinement passes: maximum wide-rate difference `4.36542e-10`, below
`1e-8`. The intact C++ output and an independently implemented Python
held-input graph agree within `2.78e-17`. An additional independent review
reproduces the silenced output within `2.78e-17`, verifies both bIPS identities,
checks all seven source/trace hashes and independently recomputes every role
summary. [Results](../results/shared_eye_t4t5_bips_v1/comparison.json),
[review](../results/shared_eye_t4t5_bips_v1/independent_review.json).

The model's average DNp15 rate over 0.7–1.4 s increased when bIPS was silenced
in all seven conditions. For the static image the two-cell average changed
from `0.01964934` to `0.02190314` model units; for global positive motion it
changed from `0.01728972` to `0.01925898`. These are **absolute modeled
rates**, including static activity, not a new estimate of rotation sensitivity.
They show a modeled contribution under these conditions; they do not prove
biological necessity or that bIPS improves small-turn detection. All source
conditions and responses were already inspected before this study.

A separately tested [shared-image input generator](../src/male_optic_frontend/shared_eye_population_v1.py)
now accepts left/right movies and streams T4/T5 input chunks with exact source
IDs and the inherited 3-second first-image adaptation. It reuses the
existing spatial/ON/OFF sampler. Two synthetic tests check separate eyes,
contrast polarity, prehistory, clocks and identity. This generator was
written **after** the retrospective replay; it was not used to generate those
seven saved source time series and is not yet an end-to-end walking runner.
Twenty-two focused checks across the new generator, graph and bridge pass.

## Biological and walking status

The pre-existing population source study found that **0/8** horizontal T4/T5
subtype/eye groups reached its predeclared 75% direction-selectivity
engineering criterion. That is a known source-level failure, not a newly
matched biological assay. This study does not contain downstream responses to
the exact stimuli used in an independent HS/H2/bIPS/DNp15 recording, and its
voltage-to-drive conversion remains an uncalibrated engineering assumption.
Therefore biological agreement for this new combined version is
**unqualified**.

The user requested new walking tests. They were **not executed**: under the
predeclared staged stopping rule, the known source failure and absence of a
matched downstream physiological gate prevent treating a new walking score
as the requested biologically constrained test. No previously unscored room
or animal was opened, and the separate existing neural-only small-turn
benchmark was not attributed to this model. Implementing a practical
full-population walking executor, specifying and passing a matched physiology
gate, freezing a decoder policy and testing fresh walking scenes all remain.

## Resources and scope

Seven input artifacts were rehashed against the original completed manifest
before use. Graph execution including the 0.5-ms refinement and Python
reference replay took 42.31 wall seconds and 41.58 process CPU seconds, with
167,510,016 bytes peak process RSS. Seven compact output traces and methods
occupy under 32 MiB; no cable rerun, new recording, download or movie was
required. The earlier full-population direction result, former numerical
failures and sealed archives remain unchanged. Numerical reproducibility does
not establish biological validity.
