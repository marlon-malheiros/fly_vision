# Evidence audit and scope correction — 12 October 2026

**TLDR:** The latest numerical result survives an independent saved-data audit.
We found and addressed a configuration-reuse defect in the validation tooling;
it does not change any completed scientific result. The original horizontal
diagnostic and the later compensation research answer different questions.
We can finish a defensible computational report now. A positive biological
degeneracy result remains an open research objective.

[Machine-readable audit](../results/t5_evidence_audit_v1/audit.json),
[execution log](../results/t5_evidence_audit_v1/audit.log),
[tests](../results/t5_evidence_audit_v1/tests.xml),
[audit protocol](T5_EVIDENCE_AUDIT_PROTOCOL_V1.md),
[completion plans](PROJECT_COMPLETION_ALTERNATIVES_V1.md),
[supervisor brief](SUPERVISOR_EVIDENCE_BRIEF_V1.md).

**What was checked.** This is a new post-analysis audit, not a new experiment or
an independent research team's replication. The checker is separately written
and does not call the production scorer when recomputing scientific verdicts.
It imports that scorer only for the explicitly counterfactual defect fixture.
It reads every saved trajectory with `allow_pickle=False`, checks complete
identities, clocks and windows, forms the 39 direction pairs from stimulus
metadata, and recomputes features and all 43 candidate/reference/control scores.
All 84 parameter sets' readouts and both finite-difference matrices are checked.
No model parameters, observations, scores or sealed sources were edited.

| Check executed in this audit | Result |
|---|---|
| Ten study indexes, including every indexed file's size and SHA-256 | 12,480 entries intact; entries overlap across indexes |
| Original assignment bundle | 35 files intact, including all 14 requested artifacts and seven batches |
| Saved parameter sets / conditions / trajectories represented | 84 / 78 / 6,552 |
| Independent primary/mean feature arithmetic | Maximum discrepancy 7.11e-15 mV |
| Voltage recomputed algebraically from saved conductances | Maximum discrepancy 2.75e-14 mV |
| Jacobian reconstructed from independent readouts | Maximum discrepancy 2.17e-13 scaled units |
| Every stored output, material-distance and conductance verdict | Reproduced |
| New defensive tests plus existing active-sensitivity regression tests | 16 passed: 8 new + 8 existing |
| Fresh neural integrations, new recordings, parameter fitting | None |

The previous matrix-exponential review of all 6,552 trajectories remains intact:
maximum voltage disagreement 6.18e-12 mV and four-state disagreement 7.05e-13.
We verified the integrity of that evidence; **we did not rerun those integrations
in this audit**. Algebraic voltage agreement by itself would not verify the
differential equations. Neither check establishes physiological prediction.

**Finding 1 — real validation defect, no impact on frozen results.** The sealed
`run_t5_active_sensitivity_v1.py` uses literals for several response, waveform,
DSI, response-floor and conductance gates even though the config names those
values. Its independent review also repeats several literals. Thus agreement
between them would not detect a changed configuration being ignored.

A synthetic fixture scales the saved baseline features and voltage by 1.06 and
requests a 0.10 response margin. The old scorer still rejects the primary
response, because it applies 0.05. The new configuration-driven checker accepts
the primary response as requested. This fixture is deliberately **not a
physically simulated candidate** and supplies no new scientific evidence.

The executed configuration actually specifies the same values as the old
literals. Recomputing every real score with its recorded configuration reproduces
all verdicts. This is a latent reuse defect, not an explanation for the negative
search result. The repair is the new
[audit module](../src/male_optic_frontend/t5_evidence_audit.py) and
[entrypoint](../scripts/audit_t5_evidence_v1.py). They read the configuration,
reject corrupt/incomplete inputs, and use explicit exceptions that remain active
under Python optimization. The sealed V1 runner stays intact; it must not be
reused as a configurable new-study runner. Future runs should use a versioned
runner that calls the new gates and freezes the exact dependency hashes.

**Finding 2 — the local search conclusion is supported.** All 40 new candidates
were valid and tested. Twelve meet the material-change definition; none of those
preserves every output. Ten smaller candidates preserve all outputs. Eleven
change both final conductances by at least 10%; none preserves every output.
The known timing-compensation reference still passes all gates on all 78 inputs.
It is excluded from the count of *new* successful candidates, as specified in
the protocol. There is no contradiction between that earlier success and this
negative new bank.

The closest material alternative exceeds the 5% scalar gates: primary response
11.4062%, mean 8.0922%, and waveform 11.7490%. The negative result is not explained
solely by a binary DSI cutoff. It also does not prove that a nonlinear search,
another region, another model or another output contract has no solutions.

**Finding 3 — timing dominance is locally reproducible; exact identifiability
is unproven.** A new descriptive comparison of the two saved step sizes finds
angles of 0.6471° and 0.5738° between their two weakest full-matrix directions.
The corresponding weakest two-dimensional subspaces differ by at most 0.3386°.
The smallest singular values are 0.0477723 and 0.0477571. About 99.681% of the
weakest vector's squared norm lies in timing coordinates under the declared
normalization. This supports the qualitative local timing interpretation.

The matrix difference has spectral norm 0.29586, larger than the smallest
singular value. This two-step difference is **not** a rigorous error bound;
neither those numbers nor a machine-epsilon rank cutoff certify the exact
rank of the true response map. Quantile-based features can change which samples
determine their derivatives. The saved numerical rank 10/10 describes the finite
matrix; it must not be promoted to proof of unique parameters or absence of
degeneracy. The candidate waveform verdicts do not depend on such a proof.

**Finding 4 — the biological evidence remains narrow.** The 78 stimuli and
6,552 simulated trajectories are not independent biological replicates. The
matched recordings use one selected published T5 example. Eighteen original bars
and eight gratings have corresponding recordings; the 52 challenge conditions
are synthetic. The image/native transfer studies demonstrate correct delivery
of the modeled input. They cannot validate population physiology or HS/H2.

The original T5 comparison retains 4/4 expected grating-amplitude directions,
0/4 model mean passes, 3/4 recorded mean passes, and a fourth recorded mean with
opposite sign. The scored grating waveform RMSE is 4.020545 mV. Moving-bar primary
and mean directions pass 9/9 for model and observations, with nonzero amplitude
and waveform discrepancies. Slow model grating mean DSIs near 0.0915 also show
why continuous values must accompany the 0.1 classification threshold.
See the [matched observation report](T5_MATCHED_GRATING_OBSERVATION_REPORT_V1.md)
and [bar report](T5_MOVING_BAR_TRANSFER_REPORT_V1.md).

Preserving an imperfect model's outputs cannot repair its physiological
discrepancies. The 5% equivalence and 10% conductance thresholds are engineering
definitions, not measured biological uncertainty. The timing example establishes
approximate parameter compensation within a fixed cascade model, rather than
distinct biological circuits performing the same validated computation.

**Finding 5 — assignment completion must be stated conditionally.** The original
professor prompt explicitly allows a weak or negative answer and prohibits
tuning to obtain the desired direction. It does not require a positive degeneracy
finding. The later parameter searches were separately authorized investigations;
they cannot substitute for the original no-search diagnostic. The original
seven-condition run, its first startup failure and the later initialization
study remain distinguishable records.

The original geometry verdict was `VISUAL_GEOMETRY_VALIDATED` **under declared
source-chart conventions**. The coordinate crosswalk uses T4a/T4c functional
anchors; angular pitch and eye centers are assigned conventions, and the left
model mirrors the right model's weights. Those facts were disclosed earlier.
This audit does not upgrade them to independent specimen registration. If the
professor requires measured anatomy-to-optics registration, that stricter part
is outstanding. No invented geometry failure or retroactive label change is
needed: report the completed diagnostic and its explicit registration limit.

| Original part | Evidence / current disposition |
|---|---|
| 1. Left/right geometry | Explicit mirrored transform and complete target coverage; conditional on documented chart conventions, not independently measured optics |
| 2. Remove direction-coded frontend | Route B path documented; runtime metadata/label invariance recorded |
| 3. Nondirectional encoding | Pixel-derived local luminance; STATIC retinal input constant |
| 4. Locate motion computation | Upstream audit and explicit frozen FlyVis motion module; downstream circuit preserved |
| 5. No fitting to answer | Original diagnostic froze model/parameters; later compensation searches are a separate research scope |
| 6. Anti-leakage checks | Static scan, label replay and metadata-removal full-path controls recorded |
| 7. One seven-condition experiment | All seven saved batches; opposite field stationary in unilateral trials |
| 8. Every T4/T5 and subtype/side analysis | Complete source/drive/downstream tables; only 1/8 horizontal groups reaches original 75% criterion |
| 9. Every HS/H2 | All ten targets recorded; H2 reference eyes from body-specific afferents; directional comparison qualitative |
| 10. Negative controls | Executed; original neural STATIC stability failed despite stationary pixels. Later adaptation fixes settling; that follow-up has global trials, not a replacement adapted seven-condition run |
| 11. Prohibited operations | Recorded clean path and frozen diagnostic; no direction-based input repair is introduced here |
| 12. Preserve smoke | Preserved as software propagation evidence; biological interpretation superseded |
| 13. Required outputs | All 14 files freshly hash-verified in original run bundle |
| 14. Separate decisions | Geometry qualified as above; motion `DIRECTION_SELECTIVITY_WEAK_OR_INCOMPLETE`; biological validation not established |

Primary original evidence: [completion audit](POSTFIX_COMPLETION_AUDIT_V1.md),
[coordinate evidence](POSTFIX_COORDINATE_EVIDENCE_V2.md),
[original bundle](../results/postfix_horizontal_execution_v2/), and
[initialization follow-up](POSTFIX_INITIALIZATION_COMPLETION_AUDIT_V1.md).
This table is a documentary requirement audit with fresh integrity checks. We
did not repeat the original networks or every historical control today.

**Recommended disposition.** Close the bounded compensation search and use the
prepared supervisor brief to report the completed diagnostic and narrow T5
result. Resolve the required claim before adding computation. The alternative
plans distinguish a deliverable we can finish using current evidence from
new biological validation and degeneracy research with explicit data gates.

**Reproduction.** From the repository root, in the recorded NumPy/SciPy runtime:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 <TEMP>/maleoptic-texture-analysis-venv/bin/python -m pytest tests/test_t5_evidence_audit.py tests/test_t5_active_sensitivity.py -q
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:scripts OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 <TEMP>/maleoptic-texture-analysis-venv/bin/python scripts/audit_t5_evidence_v1.py --output <TEMP>/t5-evidence-audit-recheck.json
```

Use a fresh output path; the CLI refuses an existing file. Runtime and exact
original commands are recorded in the audit package. No thresholds were changed,
and no failed numerical checks were hidden. Preserve the final audit index and
its referenced old indexes together; hashes provide integrity, not an off-device
backup or a public archive.
