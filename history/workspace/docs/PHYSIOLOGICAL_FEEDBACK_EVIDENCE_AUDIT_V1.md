# Additional upstream feedback evidence audit V1

2026-11-04. This is a supplemental source/availability audit conducted while the
separately frozen72-model study runs. It changes neither its grid nor its rules.
No physiological trial values were downloaded or evaluated in this audit.

[Pang et al.2025](https://doi.org/10.1016/j.cub.2024.11.064) provide an L1/L2
recurrent feedback model and voltage-imaging data. The authors' repository is
pinned at `7fa5829e37d566e02beaaa87efd6a0f1de4e48c0`.
The saved simulation notebook contains a two-state feedback implementation with
published/default parameters, but also placeholder paths and an external
natural-image requirement. Small processed flash datasets are listed in the
repository. The associated [Dryad archive](https://doi.org/10.5061/dryad.ngf1vhj4c)
is49.6GB; it was not downloaded. Source availability makes a bounded upstream
benchmark feasible to investigate, not already complete or necessarily
transferable to a MaleCNS T4/T5 frontend.

[Henning et al.2026](https://doi.org/10.7554/eLife.108529) report C2/C3-mediated
inhibition of nonpreferred responses and temporal sharpening, with Mi1 implicated
in the ON pathway. Their [repository](https://github.com/silieslab/C2C3_feedback_Henning)
is pinned at `745c6114b72a61dabc9389a1f024dbe22f679edf`.
Its manifest lists T4/T5 control and silencing datasets, Mi1 data, analysis code
and connectivity files, including MaleCNS partner exports. The README explicitly
states that some raw behavioral and STRF-analysis inputs are not uploaded.
The eight processed direction-selectivity MAT files total about24MB. Listing
these files is not verification of their metadata, stimulus logs, independent
animal units, observation model or suitability for a held-out comparison.

What this changes: there is a concrete additional upstream feedback direction
with published data/code to audit, rather than an unsupported instruction to add
generic inhibition. What it does not provide: measured coupling from that
mechanism to our network, complete electrical conductances, or a ready-to-run
end-to-end model validated on HS/H2/bIPS/DNp15 or small walking turns.

The current measured Mi1/Tm3/Mi4/CT1/Mi9 kernels already contain dynamics of the
intact upstream circuit. Simply adding a feedback filter in front could count
those dynamics twice. A reconstruction must resolve the input level and
calibration/validation split before such a cascade is scientifically meaningful.
Do not select feedback strengths to fit our inspected HS or yaw results.

The [retrieval receipt](../results/physiological_factorial_search_v1/feedback_source_audit/retrieval_review.json)
records three exact source files totaling19,879bytes plus repository metadata.
The acquisition script has a per-request size cap; no whole-repository clone,
trial archive or stimulus movie was retained. These sources are evidence for a
possible next study, not additional members of the frozen factorial grid.
