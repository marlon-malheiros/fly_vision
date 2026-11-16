# Physiological branch validation attempt V1

2026-11-04. Two bounded analyses, no modification to existing models or results.

The four existing HS temporal variants and their targets are already inspected
development evidence. First ask whether any **nonnegative, condition-independent
linear mixture of their final HS endpoints** can satisfy all retained frequency
and contrast bands. Normalize by the common physical full-contrast PD1Hz endpoint.
Positive raw mixture weights become convex weights after this normalization.
Solve a linear feasibility problem and a minimax band-relaxation diagnostic;
retain coordinate-wise convex bounds as independently checkable certificates.
No mixture is promoted, fitted into the circuit, or called a biological model.
This result cannot exclude different dynamics interacting before the detector's
nonlinearity, signed mixtures, new connectivity, or an expanded model family.

Second reproduce the measured-filter T4 circuit of Gonzalez-Suarez et al. (2022),
[paper](https://doi.org/10.1016/j.cub.2022.06.075),
[author code](https://github.com/ClarkLabCode/TimingModels), pinned commit
`100bb2f52cb9628477c3883e4b17774b0b244e67`. The public source has now been inspected;
its qualitative findings are known, but no new response curves have been computed.
This is a published-mechanism replication, **not a blind external validation of
our MaleCNS circuit**. Measured input kernels are model inputs, not held-out T4
recordings. No raw per-fly downstream recordings are present in the downloaded
package. Do not manufacture uncertainty intervals from filter SEMs or simulation.

Use the author's already-deconvolved 250ms dataset, five-order discrete Laguerre
projection (alpha0.2), PCHIP interpolation onto [0,1)s, unit L2 kernel norms,
5.7deg Gaussian blur, 5deg input spacing, zero thresholds, leak1,
reversals[-30,+60,-30], gains Mi9=.3, Mi1=Tm3=.05, Mi4=CT1=.15.
Single-inhibitory comparators use .3 for the surviving arm and zero for the other,
exactly as in the author script. These are published modeling assumptions and
relative conductances, not MaleCNS measurements or new fitted parameters.
The calcium observation is max(voltage,0)^2, not mV or experimental dF/F.

Run all61 source velocities8–512deg/s on the source's five-second periodic bright
bar protocol, width5deg/period30deg, dt1/240s and dx0.5deg, both directions.
Thirteen model/condition curves: parallel WT, six kernel substitutions
(Mi1_Slo, Mi1_SloRNAi, Tm3_Slo, Tm3_SloRNAi, Mi4_CacRNAi, CT1_CacRNAi),
two single-arm silences; Mi4-only WT/mutant; CT1-only WT/mutant.
Stream each velocity and retain only61x2 endpoint curves and filter arrays.
Compute log2-velocity centers of mass with the author's equal log spacing.
Record PD/ND ratios at every velocity and integrated PD/ND preferences.

Predeclared source/experimental consistency questions: parallel model keeps its
aggregate PD preference under both inhibitory kernel substitutions; log-velocity
center shifts up/down for Mi1_Slo/Mi1_SloRNAi, down/up for Tm3_Slo/Tm3_SloRNAi,
and down for both inhibitory substitutions. The small Mi1 RNAi change was not
significant in the paper: matching its direction cannot establish a robust effect.
Single-arm reversals are expected replication controls, not desired biology.
Preserve silencing responses: published lack of a strong silencing phenotype
does not imply an exactly zero biological change; without raw trials no formal
equivalence test is possible. Do not count an untested silencing match as a pass.

Numerical checks: independent unmodified author MATLAB functions executed under
Octave10.3 (a nanmean compatibility shim only), full360deg field, at WT16/64/256,
parallel Mi4/CT1 substitutions64 and respective single-arm mutant64
(seven oracle cases). Compare all four polarities/directions with Python.
The optimized Python computes the repeating30deg unit with the full360deg
Gaussian folded onto it; verify against the full original field. Compare all12
smoothed/interpolated input kernels to Octave, and synthetic FIR to direct sums.
Refine dt to1/480 and dx to0.25 separately for WT16/64/256 and parallel
Mi4/CT1 substitutions64. Under dt refinement, multiply unit-L2 kernels by
sqrt(dt/reference_dt) to preserve the author's reference-grid convolution scale;
otherwise changing dt changes the modeled conductance rather than just accuracy.
Record this continuum-extension assumption. Endpoint error must be <=5% of the
same condition's reference PD curve maximum; report all failures without relaxing
tolerance. No claims of complete spatial/time convergence outside tested cases.

Budget: <=600 Python CPU s, <=1200 wall s including Octave, estimated8MiB,
maximum32MiB and20GiB free reserve. No retinal movies, network sweeps, permanent
source-drive arrays, parameter search, decoder fit, or untested T5 substitution.
Failure messages and unsuccessful compatibility probes are recorded. The study
ends with a source/mechanism decision and an explicit integration gate. It cannot
complete whole-circuit biological validation because this T4-only model is not
yet connected, T5 is not supplied by this source, coupling units remain unknown,
and independent downstream recordings are absent here. Any future integration
must be separately frozen and tested rather than silently changing this round.

Hash the complete latest230-file predecessor archive and its frozen dependencies;
check them again at completion. Preserve previous sealed evidence, including its
negative results. Store exact new source/protocol/tests, full numeric curves,
independent checks, figures, report and an actual-date progress snapshot before
sealing. Live progress and AGENTS remain outside the index.
