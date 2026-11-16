# Measured physiological branch validation attempt V1, compatibility R2

2026-11-04. **Whole-circuit biological validation remains incomplete.**
This finite attempt rules out one narrow repair family and implements a different
published T4 mechanism without new parameter fitting. All previous models,
small-turn results, graph parameters and failures remain unchanged.

## What was executed

1. An exhaustive linear-feasibility test of nonnegative, condition-independent
mixtures of the four already-known HS endpoint variants, under all14 retained
frequency/contrast coordinates and their original descriptive bands.
2. A standalone port of the measured-filter T4 model from
[Gonzalez-Suarez et al.2022](https://doi.org/10.1016/j.cub.2022.06.075), using the
[pinned authors' source](https://github.com/ClarkLabCode/TimingModels/tree/100bb2f52cb9628477c3883e4b17774b0b244e67). Thirteen conditions, all61 source velocities
8–512deg/s, both directions and bright/dark bars:3172 scalar outputs. The input
filters, spatial geometry, relative conductances and output observation were
copied from the source, without fitting to our HS curves or walking task.
3. Ten separate time/spatial refinements and seven full-field/four-output
independent author-code oracles, plus all12 temporal kernels.

The [protocol](PHYSIOLOGICAL_BRANCH_VALIDATION_PROTOCOL_V1.md), scientific code and
three passing focused tests were frozen at `dbff5b4` before computing curves.
The source paper and its qualitative outcomes had already been inspected. This
is a **published-mechanism replication**, not a blind test of the MaleCNS model.
The downloaded data are aggregated, deconvolved input kernels; they are not raw
held-out T4, HS, H2, bIPS or DNp15 recordings. Two additional deconvolution files
are retained as retrieved source evidence but were not used or selected between.

## Existing output mixtures cannot repair the HS mismatch

The linear problem is infeasible. Five scored coordinates have bands completely
outside the range of every existing variant and every allowed mixture:

| Flattened assay coordinate | Attainable ratio range | Retained data band |
|---|---:|---:|
| frequency:0 | 0.373051 to 0.637861 | 0.923883 to 1.212523 |
| frequency:2 | 1.199220 to 2.072720 | 0.465000 to 0.887055 |
| frequency:4 | -0.051596 to -0.030670 | -0.543785 to -0.168097 |
| frequency:5 | -0.081713 to -0.080326 | -0.482725 to -0.117246 |
| contrast:9 | -0.081713 to -0.080326 | -0.493989 to -0.166210 |

Frequency coordinate0 means preferred0.5Hz;2 preferred2.5Hz;4 null0.5Hz;
5 null1Hz. Contrast coordinate9 means null100%. The latter and frequency null1Hz
are the same physical stimulus under different source assays, so these are not
five independent physiological observations.

For positive raw weights, normalizing the mixed endpoint by its common PD1Hz
anchor produces a convex combination of the component ratios. Therefore the
mixed ratio cannot exceed the largest component or fall below the smallest.
Preferred0.5Hz reaches at most0.637861, below the band's lower0.923883;
preferred2.5Hz stays at least1.199220, above its upper0.887055. These scalar
certificates independently confirm the linear solver's infeasibility conclusion.

The minimax diagnostic requires 2.048829 additional band
half-widths. Its weights are retained as a diagnostic, not a new fitted candidate
or a relaxed acceptance criterion. This result excludes **only mixtures of the
existing final endpoints**. It does not exclude branch-specific processing before
nonlinear motion computation, different interactions, inhibition or other models.
The old four variants remain useful comparisons; no current model was replaced.

## What the distinct published model achieves

This model has separate Mi1/Tm3 excitation, Mi9 inhibition and parallel Mi4/CT1
inhibition. Each branch uses its own measured temporal kernel. T4 output follows
a quasi-steady conductance equation; the observation is squared rectified voltage.
Conductances are relative author parameters, not measured MaleCNS conductances;
the output is not experimental dF/F. Source spacing5deg and Gaussian blur5.7deg
are retained. No cell count is converted into a physiological conductance.

The model reproduces the six known directions of preferred-velocity tuning
change (positive means a shift toward faster motion):

| Input-kernel substitution | Change in log2-velocity center | Direction agrees with source |
|---|---:|---|
| Mi1_Slo | +0.096384 | True |
| Mi1_SloRNAi | -0.113234 | True |
| Tm3_Slo | -0.170103 | True |
| Tm3_SloRNAi | +0.091970 | True |
| Mi4_CacRNAi | -0.254568 | True |
| CT1_CacRNAi | -0.309493 | True |

These are six qualitative consistency checks, not six independent validation
experiments or a statistical success rate. The small Mi1_SloRNAi effect was not
significant in the paper. The source kernels themselves drive the predictions;
there are no new per-fly downstream confidence intervals or quantitative effect
size acceptance tests here. This is more mechanistically specific than applying
one common filter to every input, but no superiority for yaw is demonstrated.

The two single-inhibitor mutants reverse their aggregate direction preference:
PD/ND=0.326281 and
0.282599. With parallel
inhibition the respective ratios remain
3.156733 and
1.447529. This reproduces the
reported reason for adding a second inhibitory input within the published model;
it does not establish new biological causality from our simulation.

![Measured kernels and published-model responses](../results/physiological_branch_validation_v1/published_branch_comparison_r2.png)

Presentation R2 gives preferred/null curves the same color for each condition;
the original figure with separate automatic colors is retained. No values change.

## Negative findings must remain visible

Aggregate direction preference hides local failures. Null exceeds preferred at
12/61 velocities in WT,
25/61 with the Mi4
kernel substitution and
32/61 with CT1.
Some high-speed reversals have tiny absolute responses, so ratios alone can
exaggerate their importance. But the CT1-mutant64deg/s case is substantive:
PD3.604589 versus ND4.122425 in author observation units; ND is34.20% of that
condition's own peak PD response. Thus preserving aggregate preference does not
mean absence of unwanted null responses at every velocity.

Silencing Mi4 or CT1 shifts this model's log2-velocity center by
+0.092256
or +0.203766.
This does not establish the weak silencing phenotype observed experimentally.
Without raw trials and an equivalence margin, neither exact agreement nor a
statistical contradiction can be claimed. All13 curves, including these adverse
conditions, are retained in [complete CSV](../results/physiological_branch_validation_v1/complete_responses.csv)
and [binary arrays](../results/physiological_branch_validation_v1/curves.npz).

## Numerical verification and preserved implementation failure

All10 predeclared refinements pass, maximum normalized endpoint discrepancy
0.000552002 (0.05520% of that condition's
reference PD maximum). Time and space are refined separately. These checks do
not establish convergence for every one of the61 velocities. Temporal refinement
uses the declared continuum extension that preserves reference-grid convolution
amplitude rather than changing conductance scale with unit-L2 discretization.

The first literal-Octave oracle **failed28/28 endpoints** and remains preserved.
Tiny FFT imaginary residuals trigger magnitude-based complex comparisons in
Octave, unlike MATLAB's real-part `>` semantics. The
[R2 correction](PHYSIOLOGICAL_BRANCH_COMPATIBILITY_CORRECTION_R2.md) was frozen
at `adb1f71` before rerunning the same oracle, with the same model and tolerances.
It asserts residuals <=1e-12 of scale and returns physically real blur arrays.
The original author functions remain byte-identical; nanmean spelling and the
explicit real-FFT shim are documented compatibility changes.

R2 passes all12 kernel and28 endpoint comparisons: maximum kernel error
1.67e-16, endpoint error1.34e-11;
35 FFT checks, largest imaginary residual9.92e-17.
The oracle independently verifies the optimized30deg periodic calculation against
the original full360deg source field. This is MATLAB-equivalent real-image
arithmetic under Octave, not execution in a licensed MATLAB binary.

The original assertion aborted before its terminal resource receipt; complete
V1 CPU accounting is unavailable and no whole-attempt CPU-budget pass is claimed.
R2 oracle wall time18.875s and child CPU
20.101s are recorded separately. Source downloads total
117,704 bytes, no movies or retained retinal source arrays. The final package
is small and its post-exit receipt records exact bytes. Numeric HDF5-to-MAT
conversion is checked bitwise; the source files are retained unchanged.

Independent scalar review reconstructs13 tuning centers from the CSV and14
mixture bounds directly from old raw endpoints, in addition to three unit tests,
the time/spatial checks and the independent author-equation oracle. Source,
retained dependencies and the preceding230-file study are rehashed on sealing.
Historical retired movie archives are outside this integrity claim.

## Decision and finite next milestone

**Biological validation is not complete.** The current HS family still fails its
known physiological comparisons. The new standalone T4 reference reproduces a
more specific published mechanism, with explicit failures. It is not connected
to the MaleCNS network, provides no T5 model, and has not been tested for small
turns. It cannot inherit the old decoder's walking performance. All prior graph,
decoder, threshold and model files remain unchanged.

The supported alternative to further output-filter blending is a separately
versioned input-specific excitation/inhibition frontend. A finite integration
study would need to: (1) retain this fixed T4 reference and the previously audited
published T5 reference as separate source controls; (2) freeze retinal geometry
and a common voltage-to-network coupling assumption before any outcomes;
(3) require both preferred/null response guards, not just six aggregate shifts;
(4) check the known HS curves without refitting the yaw decoder; and only then
(5) evaluate one uninspected, matched recording cohort with predetermined error
criteria. CT1 local mapping, coupling calibration and missing electrical synapses
remain unresolved; aggregate connectivity alone does not solve them. Earlier
full published T4/T5 population attempts and their heterogeneity failures must
be used as controls, not presented as an untried replacement idea.

If steps2–3 cannot be supported, the honest alternative is a scoped functional
small-turn model with limited biological claims, or new matched recording/stimulus
data. Searching old results or changing a tolerance cannot make validation true.
No author contact, new experiments, source parameter fit or closed-loop control
was performed. [Machine-readable decision](../results/physiological_branch_validation_v1/decision.json).

## Reproduction

Use an isolated tree with the indexed dependencies. Retrieve the15 pinned source
files listed by the acquisition manifests. With the scientific interpreter from
environment.json, OPENBLAS_NUM_THREADS=1 and PYTHONDONTWRITEBYTECODE=1, run the
three focused unit tests, then `scripts/physiological_branch_validation_v1.py
prepare` and `simulate`. The literal-Octave failure is expected and preserved;
then use `scripts/physiological_branch_validation_r2.py prepare` and `run` to
execute the frozen compatibility correction and analysis. Run this presentation
script once, then R2 `seal` and V1 `audit`. Stages intentionally refuse to
overwrite existing evidence; use a fresh result revision. Public-source access is
only required for acquisition; all model solves use local code and data.

## Undergraduate explanation

We want a model that detects small turns **and** behaves like real fly neurons.
We found that blending our current outputs cannot fix the remaining biological
mismatch. We then reproduced a different published model in which excitatory
and inhibitory inputs have their own timing. It explains several experimental
trends, but still makes mistakes and is not yet our complete walking circuit.
That gives us a concrete mechanism to investigate, without claiming we have
finished biological validation.
