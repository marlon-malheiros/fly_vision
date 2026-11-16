# Shared-eye T4/T5 network and bIPS comparison V1

13 November 2026. Frozen before new graph outcomes. This is a bounded,
retrospective engineering integration and lesion comparison. The seven
source-input movies and source voltages come from an already completed,
previously inspected project study; none is a new holdout or matched
physiological recording. Do not call this a new biological validation.

## Inputs and model

Reuse exactly the seven recorded `source_drive` time series and body IDs from
`results/physiological_population_v1/condition_00` through `condition_06`.
Their original image streams fed all 6,861 cloned published T4 cable and
6,718 published T5 model cells; their recorded run had a 3-second static
adaptation, original axis/imputation and optical sampling choices. The
source drivers are already rectified `max(V+65,0)/65` model units. They
are not physiologically calibrated transmitter release, and the later
per-recording T4 geometry ensemble is not reproduced by these population
drivers. Never call these inputs the newly qualified T4 ensemble. Source
input is passed by exact ID to the unchanged LPi graph. The new causal
held-input solver integrates each input on [sample, next sample) with 1 ms
steps; the historical boundary-interpolation solver is not modified.

## Comparisons

For each of the seven existing source time series, run an intact graph and
a graph with both bIPS cells silenced using the existing active-mask
convention; keep all weights and normalization fixed. Record 10-ms
wide-neuron rates, paired differences, and a predeclared mean over
[0.7,1.4] s for each wide cell and each condition. There is no refit, no
assumed causal claim about real flies, no walking trial and no test scene.

Audit source and model hashes, IDs, bounds, graph identity and unchanged
input across graph variants. On the global-positive condition, compare the
1-ms intact simulation with a 0.5-ms refinement using a `1e-8` maximum
absolute rate guard; independently compare at least one numerical trace with
the separate held-input graph reference. All gates must pass; preserve
failures and do not relax the thresholds after viewing outcomes.

## Biological and walking boundary

The existing population source study reported 0/8 predefined horizontal
subtype-eye groups reaching its 75% direction-selectivity engineering
criterion. That source-level failure is already known and the new graph
solver cannot fix source voltages. It is not itself a direct matched biological
recording test and does not establish that this new graph's downstream
physiology fails. Existing HS/H2 physiological studies concern other source
and graph conditions; do not present them as a matched test of this new
integrated model. Because no matched recorded downstream assay for this
specific source/graph bridge is supplied, report the biological gate as
**unqualified**, not passed or failed.

The user requested walking and bIPS testing. Perform the bIPS comparison on
the seven already-inspected image controls as an exploratory computation, with
no biological necessity claim. Do not spend previously unscored walking
rooms or declare a new decoder valid on a model lacking its prerequisite
matched physiology and source selectivity evidence. The prior user-approved
path stops at failed/unqualified basic checks. Record the remaining walking
implementation and validation as incomplete, rather than silently substituting
the old neural-only walking result.

## Resources and evidence

Single process; no cable solves, no downloads, no regenerated movies. Seven
retained source files are used in place; save only compact wide traces,
analysis, methods and reviews. Planned retained output <32 MiB; maintain
20 GiB free space; stop on I/O or numerical errors. Estimate complete-run
storage before execution and log CPU/wall resources. Read-only hash audit is
limited to these source files and the chosen graph. Progress, precise report,
dated snapshot and independent post-writer integrity check follow.
