# Study B — chemical reconstruction and physiological benchmarking, V1

Completed 2026-10-19. Separate open-loop study; Study A was completed and sealed first.

**Quantitative outcome.** Expanded DNp15 with the original decoder: 5.5 mm/s: unresolved deg/s, FPR 33%; 11 mm/s: unresolved deg/s, FPR 33%; 16.5 mm/s: 20 deg/s, FPR 0%. With expanded-circuit calibration: 5.5 mm/s: unresolved deg/s, FPR 17%; 11 mm/s: unresolved deg/s, FPR 17%; 16.5 mm/s: unresolved deg/s, FPR 17%. The lesion table and paired response contrasts below identify which changes depend on the new recurrent families and which remain after both are silenced.

The supported reconstruction adds recorded chemical circuitry. A complete physiological reconstruction remains unestablished: electrical conductances, local upstream dynamics and the image-to-fluorescence measurement model are unresolved. We preserved these failures and executed the supported anatomical comparisons without fitting the circuit for yaw classification.

## Anatomical evidence and inherited assumptions

The original 13,593 cells were retained in order. The full 151,856,684-row MaleCNS table yielded 13,618 selected cells and 204,201 chemical connections, including 340 connections involving added neurons. Included families: {'ulptcrn': 17, 'h2rn': 8}. Counts, identities, annotation provenance and transmitter confidence are retained for every added connection/cell. Candidates were selected from ontology-linked identities and GABA consensus with confidence ≥0.5 before inspecting expanded outcomes. Family-level homology remains qualified; no absent counterpart was fabricated. The bounded reconstruction still omits 80,833 recorded incident connections to other cell types (189,280 synapses); their full ledger is retained. This is not a complete reconstruction of every central motion partner. [Identity ledger](../results/anatomical_strengthening_v1/candidate_identities.csv), [edge ledger](../results/anatomical_strengthening_v1/added_neuron_edges.csv), [full audit](../results/anatomical_strengthening_v1/anatomical_audit.json), [omitted partner audit](../results/anatomical_strengthening_v1/omitted_partner_types.csv).

Reconstructing the old-body subset from raw counts recovered 0 additional and omitted 0 old edges; maximum normalized-weight difference 1.11e-16. Adding inputs changes 10,894 old-core entries through the inherited postsynaptic normalization. Therefore additions change both recurrent signals and the normalization of old inputs. Dual-new-family silencing retains those new denominators and helps distinguish transmitted new-cell activity from this normalization effect. There are 0 modeled-sign/consensus disagreements in the explicit identity/NT audit; the frozen old signs were not silently corrected.

Rates are signed tanh model units, permitting negative deviations around zero; they are not calibrated spontaneous firing rates or fluorescence. Idealized zero-rate clamps do not reproduce every effect of TNT, Kir2.1 or receptor perturbations. The expanded circuit uses the existing signed-linear count rule, class gains of one and all original global numerical parameters. The common 20-ms pole applied to new nodes is an inherited numerical assumption, not a newly measured cell-specific time constant. Transmitter prediction is not a receptor/functional-sign measurement. Zero electrical entries mean unavailable conductance constraints, not demonstrated absence of electrical coupling. Published dye-coupling evidence also implicates HS with bIPS/DNp15; no conductance for these links is supplied by this chemical table. Single-node rates cannot represent branch-local shunting interactions. No cross-specimen count, mirrored synthetic neuron or fabricated gap conductance was inserted. [Cross-connectome audit](../results/anatomical_strengthening_v1/cross_connectome_audit.json), [prospective protocol](ANATOMICAL_STRENGTHENING_PROTOCOL_V1.md), [frozen methods](../results/anatomical_strengthening_v1/prospective_manifest.json).

![Anatomy](../results/anatomical_strengthening_v1/figures/chemical_anatomy.png)

The algebraic normalization audit isolates the existing-input dilution: bIPS retains 62.53% (left) and 53.13% (right) of its original normalized input weights, while DNp15 retains 81.48% and 78.28%. The old-cell block identity holds within 1.12e−16. These asymmetric scale changes remain when both added families are silenced, and must be separated from their transmitted activity. [Every cell](../results/anatomical_strengthening_v1/incoming_normalization_by_cell.csv), [identity check](../results/anatomical_strengthening_v1/normalization_audit.json).

The central structural audit records 105 reciprocal pairs involving added neurons. Its two-edge walks include 25 bIPS→uLPTCrn→bIPS, 14 bIPS→uLPTCrn→DNp15 and eight H2→H2rn→H2 paths. These establish recorded signed motifs; static weight products are not effective dynamical gains. Every simulation still includes the complete selected T4/T5 recurrence and feedback. [All paths and reciprocal pairs](../results/anatomical_strengthening_v1/structural_motif_audit.json).

## Paired yaw results

All 424 Study A source arrays, including sixteen timing refinements, were replayed unchanged through fifteen graph copies. The original twelve interventions are joined by uLPTCrn-family, H2rn-family and dual-family silencing. Primary comparisons use the original Study A decoder/cutoff. Secondary comparisons use the expanded intact decoder or separately retrain each lesion, always on the original training/calibration scenes. Six held-out scenes never enter any fit. A separately timestamped development-only fit saved all 180 decoder models before test scoring; the final analysis reproduces them exactly. [Separation check](../results/anatomical_strengthening_v1/readout_separation_review.json). The same sustained ≥80% detection/sign accuracy and ≤10% false-positive rule applies. All thresholds remain grid-qualified finite-scene model results.

| Readout | Speed | Original threshold / FPR | Expanded, original decoder | Expanded, recalibrated |
|---|---:|---|---|---|
| HS | 5.5 | unresolved / 33% | unresolved / 33% | unresolved / 33% |
| HS | 11 | unresolved / 33% | unresolved / 17% | unresolved / 33% |
| HS | 16.5 | unresolved / 17% | 10 / 0% | unresolved / 17% |
| H2 | 5.5 | 20 / 0% | 20 / 0% | 20 / 0% |
| H2 | 11 | 40 / 0% | 40 / 0% | 40 / 0% |
| H2 | 16.5 | 40 / 0% | 40 / 0% | 40 / 0% |
| bIPS | 5.5 | unresolved / 17% | unresolved / 67% | unresolved / 17% |
| bIPS | 11 | unresolved / 17% | unresolved / 50% | unresolved / 17% |
| bIPS | 16.5 | 20 / 0% | 40 / 0% | unresolved / 17% |
| DNp15 | 5.5 | unresolved / 17% | unresolved / 33% | unresolved / 17% |
| DNp15 | 11 | unresolved / 33% | unresolved / 33% | unresolved / 17% |
| DNp15 | 16.5 | 20 / 0% | 20 / 0% | unresolved / 17% |

![Detection comparison](../results/anatomical_strengthening_v1/figures/original_expanded_detection.png)

![Lesions](../results/anatomical_strengthening_v1/figures/expanded_lesion_thresholds.png)

![Asymmetry](../results/anatomical_strengthening_v1/figures/new_family_yaw_asymmetry.png)

The full sign-accuracy, detection, false-positive and correctly directed detection curves are preserved even when a threshold is unresolved. Fixed-decoder failure and lesion-retrained recovery have different meanings. Changes under an idealized lesion demonstrate causal effects inside these equations; they do not establish biological causality. [All curves](../results/anatomical_strengthening_v1/detection_curves.csv), [thresholds](../results/anatomical_strengthening_v1/detection_thresholds.csv), [predictions](../results/anatomical_strengthening_v1/decoder_predictions.csv), [DNp15 paired contrasts](../results/anatomical_strengthening_v1/dn_yaw_separation_summary.csv).

![Chemical mechanisms](../results/anatomical_strengthening_v1/figures/expanded_current_mechanisms.png)

## Physiological benchmark and unsuccessful reconstruction gates

The prior native-model evidence was reverified, preserving its original seals. Eight T4 figure-level peaks give recording RMSE 0.831981 mV and author-simulation RMSE 0.043807 mV. These are same-study figure-derived comparisons. The T4 source is the [published electrophysiology/model study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5967973/). The T5 author-equation audit and image-transfer controls are retained with their original failures; they validate scoped ports/transfers, not this entire motion frontend. Native T5 moving-bar peaks have mean absolute recording error 1.89575 mV. Native grating scored-window waveform RMSE is 4.020545 mV; the weak mean-response finding is retained alongside positive bar-direction controls. [Physiological source gate](../results/anatomical_strengthening_v1/physiological_source_gate.json), [dataset/measurement map](ANATOMICAL_STRENGTHENING_DATASET_MAP_V1.md).

The larger optic export provides upstream Mi/Tm connectivity and the full MaleCNS count table confirms CT1 contacts. Aggregate counts do not supply a wide-field CT1 neuron’s local branch inputs, all subtype-specific spatiotemporal filters, or a voltage-to-normalized-drive calibration. Consequently an evidence-constrained physiological replacement of the imposed T4/T5 routing was unsuccessful at the integration gate. The original functional surrogate is preserved; anatomical availability alone was not mislabeled physiological validation.

Erginkaya et al. (2025) provide published calcium recordings, methods, source endpoints and analysis code. We retain the prior whole-fly split and signed epoch-difference ratio, with no new fit. The nine validation endpoints come from five flies; a split audit confirms zero overlap with the original gain-fitting flies. Baseline and expanded circuits receive the same historical signed analytic flow clamp. This diagnostic bypasses the image frontend. Its rate endpoint is compared with a calcium-derived endpoint, conditional on that explicit cross-modal observation convention. Missing original movies, source-specific reporter dynamics and baseline/noise mapping prevent a primary image-matched fluorescence validation; deterministic zero-baseline variance is not repaired by invented noise.

| Circuit | Existing split | Endpoints | Conditional RMSE | Conditional MAE |
|---|---|---:|---:|---:|
| baseline | calibration | 38 | 1.42399 | 1.25698 |
| baseline | validation | 9 | 1.41410 | 1.18464 |
| expanded | calibration | 38 | 1.56032 | 1.48721 |
| expanded | validation | 9 | 1.42312 | 1.20647 |

Held-out diagnostic errors by class (the same nine endpoints from five flies):

| Class | Endpoints / flies | Original conditional RMSE | Expanded conditional RMSE |
|---|---:|---:|---:|
| HS | 4 / 2 | 1.07462 | 1.07462 |
| H2 | 2 / 1 | 2.00000 | 2.00000 |
| bIPS | 1 / 1 | 2.00000 | 1.95460 |
| DNp15 | 2 / 1 | 0.83003 | 0.94542 |

The expanded circuit does not improve this frozen conditional endpoint comparison overall (held-out RMSE 1.41410 → 1.42312), and DNp15 error increases. These are bounded signed-index errors, not errors in fluorescence or voltage units.

A separately labeled post hoc readout audit retains L/R and pooled epoch components without replacing any benchmark endpoint. The legacy readout pools both anatomical sides, whereas experimental ROIs are hemisphere-aligned individual neurites. Soma/root labels do not establish the imaged axon/dendrite correspondence. Pooling can cancel or reverse response components and produce saturated ±1 ratios. No favorable side was selected. This unresolved observation alignment further prevents interpreting the conditional RMSE as validated physiological goodness of fit. Yaw decoding retains separate left/right features; the pooling issue concerns this legacy physiological diagnostic. [Component audit](../results/anatomical_strengthening_v1/physiology_readout_components.csv), [side/provenance audit](../results/anatomical_strengthening_v1/physiology_readout_audit.json).

![Physiology diagnostic](../results/anatomical_strengthening_v1/figures/conditional_physiology_diagnostic.png)

These conditional errors are not calcium validation, and improvements in a diagnostic do not erase the missing measurement constraints. No physiological model or classifier was tuned to force agreement. [Every endpoint](../results/anatomical_strengthening_v1/physiology_endpoint_diagnostics.csv), [benchmark provenance](../results/anatomical_strengthening_v1/physiology_benchmark.json).

The qualitative recurrent-inhibition hypothesis follows [Erginkaya et al.](https://www.nature.com/articles/s41593-025-01948-9); the chemical-only reconstruction cannot test the electrical HS–H2 mechanism of [Pokusaeva et al.](https://doi.org/10.1038/s41467-024-53173-w), or walking-related nonvisual modulation reported by [Fujiwara et al.](https://doi.org/10.1038/nn.4435). Cross-dataset homology links are from [uLPTCrn ontology](https://flybase.org/cgi-bin/cvreport.pl?childdepth=2&cvterm=FBbt%3A00053518&rel=is_a) and [H2rn ontology](https://flybase.org/cgi-bin/cvreport.pl?childdepth=2&cvterm=FBbt%3A00053519&rel=is_a). The official anatomical release is [MaleCNS v1.0](https://male-cns.janelia.org/download/).

## Numerical evidence, limitations and experimental predictions

An independent equation audit bounds the continuous tanh dynamics of all 27 original/expanded copies as contractive, with minimum margin 6.321 s−1. Frozen-Jacobian RK4 amplification bounds are below one at both timesteps. This is a mathematical stability property of the inherited rate equations, not a measured neural time constant or proof of full nonlinear/spatial convergence. [Derivation and per-copy bounds](../results/anatomical_strengthening_v1/analytical_stability_review.json).

Every expanded intervention was compared with the independent Python equations on artificial inputs before freezing. All final grouped currents and 248,040 compensated cell means were independently reconstructed; maximum errors 5.69e-19 and 4.34e-18. Six complete actual-input graph-copy trajectories also matched the Python reference within 1.73e-18; two ±2°/s solver-only refinements retain the same delivered inputs. Held-out counts and every threshold were checked independently. Timing refinements produced 0 mean flags, 15 contrast flags and 80 decision changes. Every flagged case is preserved. These are subset convergence checks, not a declaration that all small-yaw thresholds are numerically invariant. Initial fast-math compilation produced a 5.42e−20 sham discrepancy in an artificial-input preflight. Before freezing or running yaw inputs, strict floating-point flags restored bitwise sham identity and all Python-reference checks passed. The failed binary, arrays and traceback are preserved; no neural parameter or scientific criterion was changed. [Numerical review](../results/anatomical_strengthening_v1/numerical_statistics_review.json), [timing decisions](../results/anatomical_strengthening_v1/timing_decisions.csv).

Testable predictions are the full speed-dependent DNp15 left/right response curves and their paired changes after bIPS, uLPTCrn-family or H2rn-family perturbation. Experiments should compare changes during straight walking as well as rotations: false alarms can change without a loss of yaw response. Measure matched stimuli and the same identified subtypes, fit measurement mappings only on calibration flies, and test them on independent flies. Candidate-family ambiguity, missing electrical coupling and the inherited dynamics can be challenged directly rather than hidden in classification accuracy.

This output completes the supported chemical reconstruction and comparative experiments. Full physiological reconstruction/validation remains incomplete at the documented evidence gates. The observer has coupled head/body orientation and receives no motor-intention signal: these tests concern visual evidence of yaw, not discrimination of intended versus unintended turns. No closed-loop locomotion or robot controller was implemented. [Study A](YAW_SENSITIVITY_ABLATION_REPORT_V1.md), [reproduction](ANATOMICAL_STRENGTHENING_REPRODUCTION_V1.md), [undergraduate explanation](YAW_STUDIES_UNDERGRAD_SUMMARY_V1.md).

## Interpretation of the completed paired results

The following is descriptive interpretation of the frozen rules and complete tables. It adds no acceptance criterion, neural fit or selected subset of environments.

| Speed (mm/s) | Original DNp15 | Expanded, original readout | Expanded, recalibrated readout |
|---:|---|---|---|
| 5.5 | unresolved / FPR 17% | unresolved / FPR 33% | unresolved / FPR 17% |
| 11 | unresolved / FPR 33% | unresolved / FPR 33% | unresolved / FPR 17% |
| 16.5 | 20 / FPR 0% | 20 / FPR 0% | unresolved / FPR 17% |

Smallest-yaw evidence is kept separate from higher-yaw threshold crossings:

| Speed | Original ±2°/s detection | Expanded, recalibrated ±2°/s detection | Original / expanded sign accuracy | Original / expanded straight false alarms |
|---:|---|---|---|---|
| 5.5 | 8/12 | 8/12 | 92% / 92% | 1/6 / 1/6 |
| 11 | 4/12 | 4/12 | 67% / 67% | 2/6 / 1/6 |
| 16.5 | 3/12 | 2/12 | 67% / 67% | 0/6 / 1/6 |

At fast walking, the targeted effects depend on which readout is held fixed:

| Expanded graph copy | Expanded intact readout | Lesion-specific recalibration |
|---|---|---|
| intact | unresolved / FPR 17% | unresolved / FPR 17% |
| bips_silence | unresolved / FPR 50% | unresolved / FPR 17% |
| bips_to_dnp15 | unresolved / FPR 50% | unresolved / FPR 17% |
| ulptcrn_silence | unresolved / FPR 17% | unresolved / FPR 17% |
| h2rn_silence | unresolved / FPR 33% | 20 / FPR 0% |
| new_families_silence | unresolved / FPR 33% | 20 / FPR 0% |
| hs_silence | unresolved / FPR 100% | 40 / FPR 0% |
| h2_silence | 10 / FPR 0% | unresolved / FPR 17% |

The dual-new-family clamp removes their transmitted activity while retaining the new input denominators. Since the raw old-core counts match exactly and the old-block scaling identity holds to roundoff, differences between this clamp and the original model isolate normalization effects within these equations. Differences between expanded intact and this clamp include transmitted new-family activity. The following absolute ±2°/s bilateral separations are descriptive response contrasts, not detection thresholds:

| Speed | Expanded / original separation | Dual-family clamp / original separation |
|---:|---:|---:|
| 5.5 | 0.7173 | 0.7406 |
| 11 | 0.7180 | 0.7405 |
| 16.5 | 0.7169 | 0.7398 |

Timing controls changed 80 of 2880 recorded decisions, including 1 expanded-intact DNp15 comparisons across the three decoder modes. These are decision comparisons, with repeated inputs/modes, not independent biological trials. Full finer-clock threshold recalibration and spatial decoder convergence remain unestablished.

Anatomical additions are not automatically a performance improvement. Interpret resolved thresholds together with false alarms, sign accuracy, response balance and the normalization control; recalibration can recover a code without restoring an original operating point. The causal statements here concern interventions in this numerical graph. Biological mechanisms require matched neurite recordings, a justified measurement model, and perturbations whose targets match the modeled lesion.

The frozen physiological diagnostic also did not improve overall, and its pooled readout/stimulus/fluorescence limitations remain explicit. Neither good yaw classification nor a static anatomical motif establishes physiological validity. No electrical conductance, upstream dynamics, motor-intention signal or closed-loop controller was added.

## Localization of numerical timing limitations

All 15 cell-level contrast flags are in H2rn-family candidates; none are in HS, H2, bIPS or DNp15. The largest relative change is 43.64%, with the declared 1e−7 contrast floor. Largest absolute error among flagged cells is 1.45451e-06 signed model units. The source summaries are reproduced exactly. This localizes the limitation rather than dismissing it: precise H2rn contrast predictions require additional numerical checks. The expanded-intact DNp15 fixed-baseline readout also changes one +2°/s decision from detection to no detection in the refinement subset. [All cell comparisons](../results/anatomical_strengthening_v1/timing_contrast_by_cell.csv), [localized flags](../results/anatomical_strengthening_v1/timing_contrast_cell_details.json).

## Central scientific answer

Reliable detection of 2–5°/s yaw across the tested walking speeds was not established by these readouts. The original circuit supports a primary-grid DNp15 threshold of 20°/s at 16.5 mm/s under the frozen rule; lower-speed thresholds are limited by false alarms. bIPS supports the original response balance, especially through its direct DNp15 outputs, but recalibration can recover the fast threshold after its suppression. Thus these results do not establish that yaw information disappears without bIPS.

Adding the candidate recurrent families does not establish improved small-yaw detection or physiological agreement. With the original decoder, the expanded circuit retains the fast 20°/s result; with its own recalibration it has one straight false alarm in six test rooms and no resolved DNp15 threshold. At ±2°/s, bilateral DNp15 separation falls to about 72% of the original; it is about 74% when both new families are silenced. Most of that amplitude reduction therefore remains without transmitted new-family activity and reflects the inherited input normalization. H2rn and H2 lesion outcomes depend on the readout, which argues against a simple universal benefit or necessity claim.

These are supported or negative findings in a specified computational circuit, not proof about biological causality or fly sensory thresholds. The most direct experimental tests are speed-dependent bilateral response curves and changes in forward-only baseline balance after targeted perturbations, using verified neurite identities and matched measurements. Full physiological reconstruction, electrical coupling, source-specific measurement calibration and spatial/threshold convergence remain unresolved. No neural parameter was tuned for expected yaw responses and no closed-loop controller was implemented.
