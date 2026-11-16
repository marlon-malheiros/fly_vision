# Recording-matched benchmark specification and source audit V1

24 October 2026. Parallel workstream of the continuous-yaw study. The metadata
audit and benchmark specification are complete; new image-to-recording scoring
is blocked by the evidence gates below. No neural or observation parameter was
fitted, no new response outcome was scored, and no physiological validation is
claimed. The numerical diagnostic work continues independently.

The primary cohort is **bIPS / sytGCaMP7f / axon / native control**, chosen for a
defined cell family, reporter and compartment. Existing eligibility rules give
11 sessions from eight flies. All eight already appear in the prior 63-fly
physiological analysis; none may be relabeled an uninspected validation animal.
Other reporters, compartments, perturbations and genotypes remain separate.
[Sessions](../results/continuous_yaw_mechanisms_v1/physiology_audit/primary_sessions.csv),
[metadata fields checked](../results/continuous_yaw_mechanisms_v1/physiology_audit/primary_metadata_fields.json).

The [paper's Methods](https://www.nature.com/articles/s41593-025-01948-9#Sec15)
describe a tilted G3 LED display, 32×96 pixels covering 216°×72°, and starfields
generated using modified G3-compatible scripts. The nominal 13-s sequence is
2-s still, 2-s motion, 5-s still, 2-s opposite motion and 2-s still. This timing
and nominal geometry do not identify the exact images or every trial's direction.

Audited the paper-linked [Motion Maker G4 repository](https://github.com/misaacson01/Motion_Maker_G4)
at commit `4ace457c24bc6afce36bcb58b5c38f89db0777e0`; six downloaded source/license
files match their Git blob identities. Its default arena configuration is for
G4; `make_starfield.m` includes randomized initial dots, anti-aliasing and frame
construction parameters. It is useful source evidence, not verified replacement
code for the paper's modified G3 stimulus. The audited primary recording files
have stimulus names and timing but no numeric trial-image field among the
explicit image/parameter fields checked. This bounded audit does not prove
that the original pattern arrays exist nowhere else.
[Source snapshot](../results/continuous_yaw_mechanisms_v1/physiology_audit/source_snapshot),
[complete gate ledger](../results/continuous_yaw_mechanisms_v1/physiology_audit/benchmark_gates.csv).

The proposed benchmark uses binocular yaw, binocular front-to-back motion,
ipsilateral front-to-back and contralateral back-to-front conditions. Replay
verified display frames through the unchanged frontend/circuit, then use an
indicator/compartment-specific forward measurement model calibrated only on
development flies. Match the actual measured baseline/normalization and keep
all source-supported direction conventions. Do not apply a generic 0.5-s
exponential or invent baseline variance. Compare equal-fly waveform error with
the measured zero-response comparator, signed final-500-ms epoch contrasts and
direction/speed tuning. Retain model failures and measurement uncertainty.
[Machine-readable benchmark](../results/continuous_yaw_mechanisms_v1/physiology_audit/benchmark_specification.json).

Required evidence before calling this image-to-recording validation:

1. Original per-trial pattern arrays, or verified modified G3 generator plus
   its parameter structures and random-dot states/seeds.
2. Actual display frame schedule/refresh, gray-level mapping, masks and verified
   world direction conventions for the recorded motion labels.
3. Verified eye/soma/imaged-neurite registration. A soma label alone does not
   establish the complete retinotopic or compartment observation mapping.
4. A specified reporter observation model, fit on development data and frozen
   before validation; neither a good filter fit nor recording z-scores identify
   membrane voltage uniquely.
5. Independent validation animals, or a separately declared held-out-condition
   comparison whose inspected animals and narrower generalization are explicit.

These missing items do not prevent controlled visual or circuit-input studies,
nor require exact reconstruction of the walking-agent simulator. They prevent
a claim that the new diagnostic results quantitatively validate fly physiology.
No message was sent to authors or external collaborators. The ledger provides
the concrete evidence request for a future data handoff.
[Audit outcome](../results/continuous_yaw_mechanisms_v1/physiology_audit/complete.json).
