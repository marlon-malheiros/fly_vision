# Exhaustive physiological factorial search V1

2026-11-04. **The declared72-combination search is complete. Whole-model biological validation remains incomplete.**
This is exhaustive within a specified finite source-supported grid, not over every possible neural model. All target recordings were previously inspected development data. No new physiological experiment, animal holdout, yaw-decoder fit, graph change or closed-loop simulation was used.

The [prospective protocol](PHYSIOLOGICAL_FACTORIAL_SEARCH_PROTOCOL_V1.md) and scientific sources were committed at `4ac7878` before source-family or visual candidate outcomes. [Exact pre-execution hashes](../results/physiological_factorial_search_v1/before_execution.json). A serialization-only continuation was separately frozen at `204146d` after all screens, without changing equations, thresholds or rankings.

## Scope and what was actually executed

Crossed fixed contrast normalization off/on, all three author calcium-deconvolution assumptions (200/250/300ms), three published inhibitory architectures and four already-tested T5 partners. This gives24 primary parallel-inhibition candidates and48 single-arm historical diagnostics. The surviving single arm uses the author comparator conductance, so it is not a cell lesion. All candidates preserve the full recurrent MaleCNS graph, its parameters, vertical T4 routing and original eye chart.

Each of ten primary images was evaluated in80 graph copies:72 candidates, four complete legacy references and four matched horizontal-T4 external-input-omission controls. Omitting the external drive leaves neurons and recurrent connections intact; it is not biological silencing. All80 copies received strict0.25ms repeats at preferred1Hz and15Hz. Three nominees from distinct gain/kernel families were fixed before stricter confirmation across all ten images, stationary controls, four image/source refinements, a half-solver step and horizontal-sampling refinement.

Source consistency covers18 families ×7 WT/substitution conditions ×61 author velocities ×4 outputs = **30,744 scalar outputs**. All are saved, including wrong direction preferences. The six source perturbation signs are qualitative consistency checks, not six independent validations; the small Mi1 RNAi trend was not significant in the source paper. The source data are input kernels and cannot independently validate the downstream predictions.

## Quantitative outcomes

Source gates passed 6/18 families, including 6/6 parallel families. All-copy strict numerical checks passed 160/160; the separate finalist refinements passed 18/18.

| Strict finalist | Frequency RMSE | Frequency band violations | PD half-contrast ratio | Fast PD ratio | Failed development guards |
|---|---:|---:|---:|---:|---|
| g1_k250_parallel_T5_slowing_only | 0.296081 | 4/7 | 0.962157 | -0.075529 | preferred_signs |
| g1_k300_parallel_T5_slowing_only | 0.292411 | 4/7 | 0.962786 | -0.021504 | preferred_signs, null_error |
| g0_k300_parallel_T5_slowing_only | 0.295335 | 4/7 | 0.733365 | -0.017247 | preferred_signs, null_error, half_contrast |

The best primary screen frequency RMSE is **0.292411**, for `g1_k300_parallel_T5_slowing_only`. Its failed guards are: preferred_signs, null_error. A better single metric does not qualify a model. The frozen rule requires source consistency, numerical checks, nonnegative preferred responses, frequency error/count, full-null suppression and both half-contrast coordinates simultaneously.

Across the24 primary models, failed-guard counts are: numerical: 0/24; source_consistency: 0/24; parallel_architecture: 0/24; preferred_signs: 12/24; frequency_rmse: 21/24; frequency_bands: 13/24; null_error: 9/24; half_contrast: 17/24. These counts describe deterministic candidate copies, not independent biological replicates. The [matched-factor contrasts](../results/physiological_factorial_search_v1/complete_matched_factor_contrasts.csv) hold the other three factors fixed for each gain/kernel/architecture/T5 comparison. They quantify within-model effects without selecting only favorable examples.

A concrete partial repair is the contrast-normalized250ms parallel/slowing candidate: contrast normalization changes the earlier half-contrast preferred ratio from about0.740 to about0.962, inside the retained0.827–1.000 band. The improvement does not require a newly fitted sigma or circuit parameter. Its fastest preferred response must still have the correct sign to qualify; an acceptable contrast curve cannot cancel that failure.

Conditional expansion results, when triggered, are retained in the [full-bank and phase review](../results/physiological_factorial_search_v1/conditional_full_bank_review.json). These use the original full-assay bands/missingness and exclude the old preferred10/25% contrast calibration coordinates. Phase dependence is descriptive, with no new post hoc cutoff. Agreement on these inspected recordings would still be conditional compatibility, not fresh-animal biological validation.

**Finalists passing every declared guard: 0/3.** Therefore the additional14 old full-bank conditions and four phase controls were skipped under the predeclared stop rule. This is not an unreported incomplete search.

![All72 scores](../results/physiological_factorial_search_v1/all_72_frequency_scores.png)

![Strict finalist curves](../results/physiological_factorial_search_v1/strict_finalist_frequency_curves.png)

![Frequency/contrast trade-offs](../results/physiological_factorial_search_v1/frequency_contrast_tradeoffs.png)

[All scores CSV](../results/physiological_factorial_search_v1/complete_scores.csv), [complete scores/guards](../results/physiological_factorial_search_v1/screen_scores.json), [strict confirmation](../results/physiological_factorial_search_v1/confirmation_scores.json), [source gates](../results/physiological_factorial_search_v1/source_controls/gates.json), [source responses CSV](../results/physiological_factorial_search_v1/source_controls/complete_responses.csv), [Pareto trade-offs/selection](../results/physiological_factorial_search_v1/selection.json).

## Mechanistic interpretation and limits

The finite factorial comparisons isolate changes in pre-T4 contrast normalization, input-kernel measurement assumptions, inhibitory architecture and the functional T5 partner. These are interventions within model copies. They do not establish biological causality or identify a unique missing biological mechanism. The source voltage/60 bridge remains unmeasured; conductances are source-model assumptions, and T5 remains a functional surrogate. The comparison therefore tests whether these explicit combinations repair known HS constraints, not whether a whole visual circuit is physiologically reconstructed.

The retained target intervals are descriptive simultaneous bands under the original conditional stimulus-order interpretation. The12 source worksheet rows have not been verified as12 independent animals. No new confidence level or statistical success rate is inferred from the9 correlated coordinates,72 candidates or six source perturbation trends. Frequency and contrast assays give different observed ratios for the same physical full-contrast1Hz null stimulus; both remain visible under their original definitions.

The full [group response table](../results/physiological_factorial_search_v1/complete_group_responses.csv) retains left/right HS, H2, bIPS and DNp15 outputs for every screen/control case. The [bilateral differences](../results/physiological_factorial_search_v1/complete_bilateral_asymmetry.csv) and [all-group omission contrasts](../results/physiological_factorial_search_v1/all_group_input_omission_contrasts.csv) retain both absolute sides and signed differences. The [matched input-omission contrasts](../results/physiological_factorial_search_v1/matched_input_omission_contrasts.csv) quantify the horizontal-T4 external-drive contribution to HS while holding the T5 partner fixed. These are exploratory mechanistic diagnostics; no new physiological targets for those other groups were silently introduced. No finalist inherits the older small-turn qualification.

A positive common output gain cannot change a normalized ratio: (gR)/(gRref)=R/Rref. That rules out another scalar observation-gain search as a repair for these ratios. Earlier nonnegative mixtures of the four old final HS outputs were also proven infeasible; this round instead changes the computation before nonlinear motion detection. Failure here excludes the tested combinations under this bridge and numerical resolution, not all branch models, conductances, input geometries or neural solutions. Only three finalists received the complete strict refinements; unselected coarse candidates are not proven incapable of benefiting from further numerical work.

## Evidence map: stones already turned and what remains

| Direction | Existing evidence and present implication |
|---|---|
| Source IDs, eye routing and sampling | [Mapping audit](INPUT_MAPPING_AND_RESEARCH_AUDIT_REPORT_V1.md) found no production assignment mismatch under the declared chart. Reopen only with a concrete changed source/counterexample; the chart remains an anatomical assumption. |
| Missing inhibitory families and LPi | [Family dissection](BIOLOGICAL_FAMILY_DISSECTION_REPORT_V1.md) and [opponency study](HORIZONTAL_OPPONENCY_REPORT_V1.md) already tested supported additions. More cell counts do not supply unknown electrical conductances. |
| Published full neural circuits and new readouts | [Published circuit comparison](PUBLISHED_CIRCUIT_COMPARISON_REPORT_V1.md), [population yaw](PUBLISHED_POPULATION_YAW_REPORT_V1.md) and [model options](NEURAL_MODEL_OPTIONS_REPORT_V1.md) already contain attempts and failures. Repeating them unchanged is not new evidence. |
| Temporal components and output mixtures | [Component dissection](HS_TEMPORAL_COMPONENTS_REPORT_V1.md) and [source replication](PHYSIOLOGICAL_BRANCH_VALIDATION_REPORT_V1.md) close the existing endpoint-mixture rescue. This round evaluates every declared nonlinear source combination. |
| Reliable small turns | [Existing milestone](NEURAL_SMALL_TURN_MILESTONE_2026-11-02.md) supports a qualified functional neural readout at2deg/s in a finite room sample; it does not establish physiological validity or bIPS mediation. |
| Exact external validation | Original modified Erginkaya stimulus arrays/generator and calibrated voltage-to-release constraints remain unavailable in audited sources; inspected traces cannot become blind holdouts again. |
| Newly located upstream evidence | [Pang et al.2025](https://doi.org/10.1016/j.cub.2024.11.064) provide L1/L2 feedback source and data; [Henning et al.2026](https://doi.org/10.7554/eLife.108529) provide C2/C3 perturbation analyses/data. Small source files and pinned repository manifests were saved without consuming trial values. These are possible new upstream constraints, not a completed repair. |
| Distinct next path | Obtain an independent stimulus-matched physiological target with verified units/measurement model, or define a new separately calibrated reconstruction using explicit physiological bounds and a reserved holdout. More arbitrary parameter sweeps on the same curves cannot supply missing validation evidence. |

The primary source is [Gonzalez-Suarez et al.2022](https://doi.org/10.1016/j.cub.2022.06.075) and its [pinned authors’ code](https://github.com/ClarkLabCode/TimingModels/tree/100bb2f52cb9628477c3883e4b17774b0b244e67). The200/250/300ms settings describe calcium deconvolution, not three independently measured neuron time constants. Contrast normalization follows the existing frozen implementation; [Drews et al.2020](https://doi.org/10.1016/j.cub.2019.10.035) supports the general computation, not our sigma value or a completed anatomical reconstruction.

The supplemental [public-source audit](../results/physiological_factorial_search_v1/feedback_source_audit/retrieval_review.json) pins L1/L2 code at7fa5829 and C2/C3 code at745c611. The L1/L2 source exposes a two-state recurrent model and small processed flash files; its simulation notebook also contains placeholder paths and an external natural-image requirement. C2/C3 manifests list processed control/perturbation T4/T5 data and MaleCNS/FAFB connectivity files. The README says some raw behavior and STRF inputs are not uploaded. File presence is not a completed provenance/stimulus/units audit. The49.6GB L1/L2 raw archive was not downloaded. Adding this feedback on top of measured Mi1/Tm3 kernels could double-count dynamics already present in those kernels; a new reconstruction must resolve that before integration. These discoveries did not change this round’s grid, rank or guards.

## Reproducibility, failures and resources

The independent log-odds endpoint checker reproduced 1,005 endpoints with maximum discrepancy 1.15e-17; frequency scores and all case receipts were recomputed/verified. All previously sealed228 pilot, 230 temporal and59 source artifacts were rehashed unchanged. The packed nonlinear solver reproduced the original binary bitwise on synthetic controls, including its large-state branch; visual references and the nominal stopped pilot were checked again at the strict step.

Scientific CPU use: 7960.06s. Peak worker RSS: 1.836GiB. Storage is summarized in the completion manifest; only compact neural arrays/tables/receipts are retained, with no movie or large source-drive archive. The initial unittest invocation lacked PYTHONPATH and failed to import the package; the same three scientific tests passed after setting PYTHONPATH=src, without source changes. After all ten screens completed, V1 failed while serializing numpy.bool_ in the null-error guard. The original traceback and partial JSON were preserved. R2 converts NumPy scalars to native JSON values, verifies the completed numerical-check table by exact equality and resumes selection/confirmation without repeating a completed simulation. The scientific producer remains byte-identical to its pre-execution freeze. Exact failures and corrections, if any, are retained alongside the execution receipts. [Independent review](../results/physiological_factorial_search_v1/independent_review.json), [decision](../results/physiological_factorial_search_v1/decision.json).

To reproduce, use the scientific Python environment recorded in environment.json, OPENBLAS_NUM_THREADS=1 and PYTHONDONTWRITEBYTECODE=1. Check the frozen dependencies, then use a fresh workspace containing the pinned read-only input studies and no outputs from this new study. Run `scripts/check_physiology_factorial_backend_v1.py` first (creates the output directory and builds the binary), then `scripts/check_physiology_factorial_stress_v1.py`, and run the three unit tests with PYTHONPATH=src. Run `scripts/physiological_factorial_search_v1.py prepare` (performs lossless conversion) and `run`. That exact V1 reproduces the archived NumPy serialization failure after the complete screen; continue with `scripts/continue_physiological_factorial_search_r2.py prepare` and `run`. Finally run this reporting script. Producers refuse to overwrite existing stages. For a new version in this workspace, change the copied scripts’ study paths consistently; the sealed V1 paths must remain unchanged.

## Undergraduate explanation

We want a neural model that detects tiny turns and also responds like real fly neurons. Here we tested every combination in a fixed72-model list, changing only choices supported by published source models or earlier frozen components. A model has to get several kinds of response right at once; doing better on one curve is not enough. Numerical checks tell us whether the computer solved our equations consistently. Biological validation needs the equations to predict independent measurements, with the stimulus and measurement units properly matched. Those are different achievements.
