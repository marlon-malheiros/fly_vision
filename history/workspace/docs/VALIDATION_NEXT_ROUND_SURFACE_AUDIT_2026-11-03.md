# Small readiness audit — 2026-11-03

**Verdict: enough evidence for one bounded model-development experiment; a fresh
independent biological-validation benchmark is not established by this audit.**

Scope: existing local reports, selected source/result presence and the latest
compact archive. No simulations, parameter fitting, new downloads, literature
search or historical full-project audit.

| Surface evidence | What was checked | Implication |
|---|---|---|
| Latest numerical evidence | All 200 indexed files match size/SHA256; saved decision has 20/20 refined checks passing | Usable numerical foundation for the tested subset, not full-bank/spatial certification |
| HS biological measurements | Retained source ZIP contains `Source Data 5.xlsx` (11,037,536 uncompressed bytes); extracted targets exist | Contrast/frequency curves available for development; source handling was not re-audited here |
| Calibrated comparator | Gain-model parameter file and refined frequency results exist | Preserve contrast-gain candidate and compare a separately versioned temporal variant |
| Persistent discrepancy | Refined candidate PD ratios 0.53355/1/1.75915/1.18928 at 0.5/1/2.5/15 Hz versus recorded 1.06820/1/0.67603/0.07644 | A specific temporal-response problem remains after refinement |
| Prior physiological implementations | Published T4/T5 wrappers, reproduction scripts and prior prototype/image-clamp reports exist | Useful source-backed starting material; replacing the frontend with these models is already an attempted route |
| Fresh independent acceptance data | Not established; inspected HS curves are development evidence | Do not call another fit/test on these same curves fresh biological validation |

The older source-gate report is a historical checkpoint, not the latest execution
status. Later reports document physiological population implementation and
image-clamp refinement with unresolved transfer problems. Do not restart that
entire route as if it had never been tried. Published dynamics also do not by
themselves supply a calibrated voltage-to-downstream-drive conversion.

The local gain protocol records unavailable public raw data for the Matulis
source. This audit did not recheck current online availability. No fresh raw
temporal-recording dataset or ready-to-use independently calibrated temporal
parameter set was confirmed.

Recommended small next round: first pin **one** temporal mechanism and its
independently supported parameters, then compare it against the existing gain
candidate on a small frequency panel, with contrast/direction guard conditions
and frozen stopping rules. Label this development/mechanism testing. A separate
unused measurement is needed before claiming independent validation. No broad
parameter sweep, decoder retraining or full-eye reconstruction is justified by
this shallow audit alone.

Evidence: [latest numerical report](HS_TEMPORAL_REFINEMENT_REPORT_V1.md),
[contrast-gain report](HS_GAIN_TRANSFER_REPORT_V1.md),
[source-gate history](PHYSIOLOGY_INTEGRATION_SOURCE_GATE_REPORT_V1.md),
[executed physiological prototype](PHYSIOLOGICAL_PROTOTYPE_EXECUTION_REPORT_V1.md),
[image-clamp repair](PHYSIOLOGICAL_IMAGE_CLAMP_REPAIR_REPORT_V1.md),
[latest frozen decision](../results/hs_temporal_refinement_v1/decision.json).
