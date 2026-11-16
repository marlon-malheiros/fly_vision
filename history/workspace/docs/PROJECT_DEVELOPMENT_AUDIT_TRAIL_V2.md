# Project development and evidence trail, V2

Updated 11 October 2026 after the bounded repair. V1 is preserved. This is a retrospective navigation index of existing
records, followed by the current repair's prospective records. It does not
reconstruct missing Git commits or turn past exploratory decisions into preregistration.

## Can the development be reported reliably?

Yes, for findings linked to saved inputs, outputs, protocols, code/configuration
hashes and numerical audits. Report the actual assay, cell set and result with
its limits. Include failures and subsequent corrections. A deterministic replay
or software test is evidence of reproducibility, not independent biological validation.
Post-analysis diagnostics must remain identified as such.

At the start of this tracking audit, `git log` showed **no commits** and source,
configuration and documentation were untracked. The scientific artifact records
therefore provide a stronger existing history than Git. A current source snapshot
can start version control, but cannot recover every earlier edit or its ordering.
Artifacts are stored locally; hashes detect changes but do not provide an off-device
backup. No remote upload or communication is authorized by this task.

## Major milestones and where their evidence lives

| Stage | Record | Reportable conclusion and limits |
| --- | --- | --- |
| Original assignment and frontend diagnostic | [Horizontal random-square technical report](HORIZONTAL_RANDOM_SQUARES_TECHNICAL_REPORT_V1.md) | Earlier assignment/diagnostic evidence; use the version's actual implementation and validation limits. |
| Postfix implementation | [Implementation handoff](POSTFIX_IMPLEMENTATION_HANDOFF_V1.md) | Development plan; a plan alone does not prove execution or successful validation. |
| Physiological recovery, 9 October | [Execution report](PHYSIOLOGICAL_PROTOTYPE_EXECUTION_REPORT_V1.md) | Full fixed T4/T5 dynamics, 80/80 local controls, complete source/circuit repeat and separately declared warm initialization; individual source criterion remains 0/8. Local controls do not validate every numerical or biological property. |
| Source-only texture replication, 11 October | [Protocol](PHYSIOLOGICAL_TEXTURE_REPLICATION_PROTOCOL_V1.md), [report](PHYSIOLOGICAL_TEXTURE_REPLICATION_REPORT_V1.md) | 624 cases, 12 new textures plus reproduction anchor, 0/8 horizontal cells robust and 5/8 pooled; prospective stop/pivot retained. |
| Saved-grating readout comparison, 11 October | [Protocol](PHYSIOLOGICAL_GRATING_READOUT_COMPARISON_PROTOCOL_V1.md), [report](PHYSIOLOGICAL_GRATING_READOUT_COMPARISON_REPORT_V1.md) | All 256 traces retained; 64/64 amplitude curves pass, 9/32 horizontal mean curves pass. Formal comparison invalid because a baseline prerequisite failed. |
| Subsequent baseline diagnosis | [Diagnostic](PHYSIOLOGICAL_GRATING_READOUT_BASELINE_DIAGNOSTIC_V1.md) | Explicitly post-analysis: future-dependent T4 clamp setup and cycle drift; all raw grating mean directions correct, weak DSI from shared mean response. Neither a repaired model nor the cause of random-texture sign reversals is established. |
| Fixed image-clamp repair, completed 11 October | [Prospective protocol](PHYSIOLOGICAL_IMAGE_CLAMP_REPAIR_PROTOCOL_V1.md), [report](PHYSIOLOGICAL_IMAGE_CLAMP_REPAIR_REPORT_V1.md) | 662 cases; prefix discrepancy 0.150695 mV → 0; all 256 old gratings and 104 compatibility outputs bitwise reproduced; all 256 long trajectories converged. Horizontal mean 16/32 pass, raw signs all expected. Numerical repair succeeds; complete mean transfer and biological validity remain unestablished. |

The newer baseline diagnosis limits the older broad statement that implementation
failure was excluded. The earlier arithmetic/replay results remain reproducible;
their tests did not check invariance of an output prefix to future input.
Corrections update interpretation through new records, without overwriting old evidence.

## Sealed evidence checkpoints

| Artifact index | SHA-256 at this audit | Entries |
| --- | --- | ---: |
| [Recovery](../results/physiological_execution_artifact_index_v1.json) | `c70985904cb48dcbd2260475a8f73897ba721592950dfc5e103c0a2c115e6235` | 8,418 |
| [Texture replication](../results/physiological_texture_replication_v1/artifact_index.json) | `fe7b1841edea2af6782eadddbcba5ece0b91bc4acf826e02778143ab8db53597` | 427 |
| [Grating comparison](../results/physiological_grating_readout_comparison_v1/artifact_index.json) | `b95a441b83c36489ec5c99ad4cacc18e2d0147e03082a683727033393807a0a9` | 46 |

These indexes contain root-relative filenames, byte counts and hashes. Verification
checks each indexed file, not just the index's own hash. Entries overlap between
milestones, so their sum is a number of entry verifications, not unique observations.
Later study indexes should retain these hashes as predecessors.

## Reporting rules for this project

1. Identify the version, exact input/stimulus, units, cell/sample set, window and criterion.
2. State whether rules were frozen before the new scores or introduced after inspection.
3. Link raw records, complete numerical tables and the independent arithmetic audit.
4. Distinguish a successful audit from a successful scientific test; retain rejected hypotheses.
5. Use the latest interpretation, while citing the historical result with its original context.
6. Claim biological validation, degeneracy or publication novelty only when independently supported.

This trail and the experiment ledgers support a technical development/methods report
now. They do not support a claim that the final biological research objective has
already been achieved. Maintain Git snapshots from this point onward alongside the
scientific artifact indexes, and arrange an off-device backup separately.

## Development tracking introduced in this repair

The initial current-source Git commit is `e430690a7f263e3243e9ba71ea33ad1c7f98e448`,
covering 424 source/configuration/documentation files. A second snapshot records
this repair; exact IDs are in [the snapshot record](../results/physiological_image_clamp_repair_v1/git_snapshots.json).
Git records start here; older edit history is not reconstructed. The new
[artifact index](../results/physiological_image_clamp_repair_v1/artifact_index.json)
adds complete numeric inputs/outputs, causal interventions, 21 tests, independent
replays, parameter audits and timestamped execution logs. Three previous indexes
and 8,891 entries (overlapping, not unique observations) were preserved.

The [observation inventory](../results/physiological_image_clamp_repair_v1/physiological_observation_inventory.json)
identifies existing measured T5 grating data and the single-bar fitting workflow.
Stimulus-held-out status of the archived selection still needs a provenance audit.
The present record distinguishes that candidate comparison from validation already
performed. No new biological scoring or external publication took place.
