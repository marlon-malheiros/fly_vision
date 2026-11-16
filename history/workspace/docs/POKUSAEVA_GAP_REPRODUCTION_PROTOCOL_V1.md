# Published HS–H2 coupling: bounded reproduction and walking transfer, V1

Date: 2026-10-26. Preserve all earlier models, results and acceptance criteria.

## Question and stopping rule

Can the authors' published steady-state HS–H2 coupling calculation be reproduced,
and does that fixed circuit improve the existing small-yaw benchmark under an
explicit interface to our unchanged functional frontend? Complete the published
comparison first. Stop this candidate if its equations cannot be reproduced or
its primary qualitative comparison fails; preserve evidence of failure. Only
after success, freeze a separate walking-transfer manifest before computing new
walking responses. No conductance fitting, new MaleCNS edges, motor feedback,
or general missing-data search belongs to this experiment.

## Evidence and reproduction

Primary source: [Pokusaeva et al. 2024](https://www.nature.com/articles/s41467-024-53173-w),
Methods “HS-H2 network simulation” and Supplementary Fig. 15. Execute the
[author notebook](https://github.com/joesch-lab/Bilateral-course-control/blob/114dd16720501570ba0e6bfe27b04d6a39cba46b/flyagentmodel.ipynb)
at the archived commit; preserve its exact bytes, license, provenance and selected
cell text. Execute definition cells 7, 11, 16, 21 and paper calculation cells
49, 50. Skip only imports, plotting and irrelevant exploratory sweeps. Supply
the same NumPy, pandas and SciPy symbols, and fixed random seeds 0 and 1.
Instrument fsolve to retain unrounded solutions, residuals and termination codes;
do not change its equations, default tolerances, or random initial guesses.

Compare all eight abstract stimuli and six author variants against an independent
11-state matrix solution. Unrounded state/residual discrepancies must be at most
1e-9; rounded author states must differ by at most 0.000500001. Flag solver
termination failures even when the residual passes. Compare author DI calculation
against an independently computed range-based index. More negative DI denotes
greater rotational selectivity. Primary qualitative gate: gap_0.5 has a more
negative DNp15 DI than gap_0.0 by at least 0.002, and no cell class has DI worsened
by more than 0.002. Publish the full numbers, including any exceptions.

The clean electrical comparison is gap_0.5 versus gap_0.0, which keeps
WHScontra=0 and WH2contra=0.1. The notebook's `original` variant has different
contralateral weights and is a separate comparison. Its H2_0.0 condition also
changes WHSU from 0.5 to 0.7: reproduce it literally and flag this confound.
These are dimensionless phenomenological equations, not measured electrical
conductances. The notebook has no saved outputs. Equation parity and the published
direction of effect are checkable; exact agreement with independent published
numerical figure values is not established by agreement with our own matrix.
The source ZIP's S15 workbook supplies chemical connectivity, not a DI oracle.

## Conditional walking transfer

Use the 704 already examined V2 episodes, 44 rooms, including stationary controls,
speeds 5.5/11/16.5 mm/s and yaw 0/±2/±5 degrees/s. This is a **retrospective
transfer experiment**. Existing test-room outcomes are known; keep the original
4 training / 16 calibration / 24 test room split for new decoders, but do not
claim independent prospective validation. No variant/interface selection on test
results. Report both interfaces and all four fixed variants.

Reuse baseline source-group means from sealed source-path attribution outputs;
verify their indexed hashes. Steady-state linearity permits time averaging before
solving. Check four selected raw source arrays independently, including straight,
positive/negative yaw and stationary; verify body-ID ordering. Equal-weight mean
T4a/T5a is F, T4b/T5b is B on each side. Primary signed opponent interface uses
(F−B, B−F) per eye, matching the author's signed stimulus vectors. Secondary
rectified interface uses (F,B). Both are explicit modeling assumptions with no
physiological calibration. They do not reconstruct the authors' retinal detector.
Apply each interface identically to all published variants. No additional
rectification, rate baseline, dynamic time constant or calcium transform.

Read out bilateral means for HS, H2, bIPS, uLPTCrn and DNp15. Train the existing
standardized ridge signed-yaw decoder on training rooms only, separately by speed,
variant and role. Set cutoff to maximum absolute score on calibration straight
walking; freeze fitted decoders before loading test features. Use existing criteria:
at least 80% detection, 80% raw-sign accuracy, at most 10% false alarms, with
performance sustained at ±5 degrees/s to report a ±2 threshold. Count undetected
turns in sign accuracy. Preserve every feature, prediction, fit and count. Report
paired 24-room bootstrap effects with 10,000 draws and fixed seed 2026102601.
Compare original MaleCNS results on these same inputs as context; no refitting
or rewriting previous results. Report scene-offset SD / median absolute ±2 odd
response, and exact rank of the DNp15 bilateral mapping of signed-opponent inputs.

Call a promising engineering result only if DNp15 meets all original criteria at
all speeds and gap_0.5 improves detection by at least 20 percentage points over
gap_0.0 at any speed without increasing false alarms beyond 10%. Such a result
would require a separately frozen fresh-room experiment. An abstract DI gain
alone is insufficient to declare the small-turn problem fixed. If transfer fails,
close this bounded candidate rather than tune its coupling or interface.

## Preservation and validation

Separate reproduction and transfer freezes, exclusive new-file writes, retained
solver warnings/failures, independent numerical checks and fresh-process replay.
Numerical code reproduction and qualitative consistency with a paper do not
establish physiological validation or biological causality. Preserve the frozen
MaleCNS graph and frontend hashes. Record code/config/protocol provenance, figures,
report, a dated progress snapshot and an artifact index; exclude the live progress
report and AGENTS.md. Review the index after all writers exit.

## Wrapper correction before successful reproduction

The first execution in `results/pokusaeva_gap_reproduction_v1` failed when the
independent DI wrapper divided by zero for a class silenced in an author lesion
condition. The author's NumPy calculation emits NaN for this undefined index.
Preserve it as JSON null rather than zero; compare definedness explicitly.
Keep the failed attempt and its frozen source copies. Use the fresh namespace
`results/pokusaeva_gap_reproduction_v1_r2` for the corrected execution. This
portability/output correction changes no weights, stimuli or acceptance criteria.
