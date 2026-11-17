# Student handoff: connectome-constrained optomotor model

Prepared 16 November 2026. This guide concerns the new optomotor_closed_loop folder. It does not replace the older alignment manuscript or the parent project's historical evidence.

## 1. Objective and present status

The research objective is to explain fly optomotor processing using connectome-constrained circuitry, test neural and perturbation predictions against biological evidence, and implement an embodied system for realistic evaluation.

The current R2 is an executable **reduced model and virtual-robot feasibility result**. Its processing chain is:

`random-square cylindrical display -> camera images -> ON/OFF motion channels -> measured central chemical network -> DNp15 left/right difference -> motor command -> changed pose -> next image`

It contains 20 individual central neurons. Functional drive from 6,753 horizontal T4a/b and T5a/b cells is pooled into eight type/side channels. It retains 24,910 measured chemical pairs and 404,007 corresponding synapses. It does not simulate the full fly or the omitted original engine from the collaborator's workspace.

The R2 experiment has six held-out synthetic patterns, three translation speeds (0, 0.04, 0.08 m/s), +/-20 degrees/s disturbances, straight/static controls and five controller/lesion conditions: **270 episodes**.

| Check/result | Reference R2 |
|---|---:|
| Implementation tests | 14 pass |
| Engineering gates | 3 pass |
| Intact disturbed cases improved | 36/36 |
| Median intact yaw-RMS reduction | 66.38% |
| Median straight-travel yaw RMS | 0.1973 degrees/s |
| Maximum selected half-step RMS change | 0.0423% |
| Conventional-controller yaw-RMS reduction | 67.24% |
| Evaluation plus numerical reruns | 140.65 seconds on the original machine |

There is no demonstrated advantage over conventional visual control. Biological recording validation and physical robot tests have not been performed. Only about 10-13% of PS321/bIPS-associated and 14-17% of DNp15 incoming synapses are retained. The bIPS-associated lesion's small effect cannot be interpreted as biological lack of importance.

## 2. Obtain the right code

After this pull request is merged, clone your own repository normally:

```text
git clone https://github.com/marlon-malheiros/fly_vision.git
cd fly_vision
git switch -c codex/student-anatomy-audit
```

If it is not yet merged, obtain the published handoff branch while keeping your own repository as origin:

```text
git clone https://github.com/marlon-malheiros/fly_vision.git
cd fly_vision
git remote add handoff https://github.com/squareshorts/fly_vision.git
git fetch handoff codex/optomotor-r2-student-handoff
git switch -c codex/student-anatomy-audit FETCH_HEAD
```

Use a new destination directory if fly_vision already exists. Do not overwrite an existing working copy. Record `git rev-parse HEAD` as your baseline revision before editing scientific code. To verify a historical baseline after future changes, check out that revision in a separate clean checkout.

## 3. Install and reproduce before changing anything

Use Python **3.14** for the documented reference setup. The original run used Python 3.14.6 with NumPy 2.4.6, SciPy 1.18.0 and Matplotlib 3.11.1. Scientific package versions are pinned in requirements-reproduce.txt.

### Windows PowerShell

```powershell
cd optomotor_closed_loop
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-reproduce.txt
.\.venv\Scripts\python.exe tools/check_baseline.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe tools/replay_baseline.py --output generated/student_baseline_01
```

### Linux/macOS

```bash
cd optomotor_closed_loop
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements-reproduce.txt
.venv/bin/python tools/check_baseline.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tools/replay_baseline.py --output generated/student_baseline_01
```

Direct interpreter paths avoid shell-activation and PowerShell execution-policy problems. If the requested Python is absent, install Python 3.14 first. In Colab or another environment, document the actual Python/package versions and use the replay comparison as the compatibility check; do not assume compatibility from a successful import alone.

Ordinary replay uses the shipped compact anatomy. It needs no neuPrint token, no PyArrow, no 1.1-GB connectome download, and no neural recording download.

Expected outcomes:

1. check_baseline.py reports PASS for the publication inventory, the 17 frozen R2 source/data inputs, saved artifact hashes and nine original V1 source files.
2. unittest reports **Ran 14 tests ... OK**.
3. replay_baseline.py finishes with **PASS: baseline replay and all 270 saved trajectories match within declared tolerance**. Tolerances are absolute 1e-10 and relative 1e-8 for stored trajectories.
4. A new generated/student_baseline_01/baseline_replay_receipt.json has passed=true and cases_compared=270. Generated outputs are ignored by Git.

The baseline evaluation took about 2 minutes 21 seconds on the original CPU. Allow a few minutes for a replay and longer for first-time dependency installation or a slower computer. This timing does not estimate biological research or hardware development.

If a command fails, save its complete error and package versions, diagnose the cause, and keep the reference files unchanged. To repeat, choose generated/student_baseline_02. Existing directories are refused deliberately. Do not weaken tolerances or change the baseline to match your environment.

## 4. Read these files in this order

| File | Purpose |
|---|---|
| docs/RESULTS_APPRAISAL_R2.md | What the current result supports and what it does not |
| docs/PROTOCOL_V1.md | Original question, assumptions and engineering criteria |
| docs/NUMERICAL_CORRECTION_R2.md | Post-outcome filter correction, new square stimulus and fresh R2 seeds |
| configs/experiment_r2.json | Fixed simulation conditions and seed namespaces |
| optomotor/vision.py | Random-square display and causal motion frontend |
| optomotor/circuit.py | Measured chemical coupling, normalization, signs and descending readout |
| optomotor/simulation.py | Image-only controller and motor/pose feedback |
| scripts/run_experiment.py | Motor calibration, test grid, metrics and numerical checks |
| data/derived/connectome_provenance.json | Exact source hashes, selection and boundary coverage |
| results/r2/report.md and overview.png | Reference findings |

The repository also contains important prior work. Before suggesting a circuit addition, consult these reports to avoid repeating a previously tested repair:

- ../history/workspace/docs/ANATOMICAL_STRENGTHENING_REPORT_V1.md
- ../history/workspace/docs/HORIZONTAL_OPPONENCY_REPORT_V1.md
- ../history/workspace/docs/H2_T4_RECORDING_COMPARISON_REPORT_V1.md
- Sections 4, 8-11 and 14 of ../history/workspace/PROJECT_TECHNICAL_REPORT_2026-11-08_V1.md, as needed.

Those historical models are different versions and assays. Their favorable results do not automatically validate R2. The original history documents a failed H2 integration comparison and earlier attempts to add recurrent partners/LPi; treating those as untried solutions would be misleading.

## 5. The first assignment and the next biological task

**The first assignment is [FIRST_STUDENT_TASK.md](FIRST_STUDENT_TASK.md): a bounded gain-and-delay characterization with fixed neural weights.** The supervisor requested this first step to improve and interpret the engineering numbers. The configured loop gain of 2 has an idealized steady-state reduction of 66.7%, close to the measured 66.4%; the baseline number is not a demonstrated circuit ceiling. Test stronger feedback fairly against conventional control, preserve drift/transient limits, select settings on development patterns, and test once on untouched patterns. The detailed assignment contains the candidate grid, proposed seed namespaces, provisional 80% target, execution estimate, deliverables and an AI prompt.

After that single bounded study, proceed to the anatomical boundary audit below. Improved control performance does not supply missing biological evidence.

**Next biological task: an anatomical boundary audit, without a neural tuning search.**

Create a new study directory such as studies/anatomy_boundary_v1. Begin with the shipped metadata and coverage ledger. Produce one table per central neuron containing body ID, type, side, neurotransmitter prediction, full incoming counts, retained incoming counts, retained fraction and explicit identity uncertainties.

Then identify what additional source information is required to rank omitted partners of PS321/DNp15 and recover the qualified recurrent families. The shipped selected-edge table cannot identify every omitted partner. If full reconstruction is needed, first specify the versioned source files, available disk/RAM, streaming extraction method and destination. Acquire in a separate reconstruction workspace; do not overwrite data/derived. The acquisition script is a reference implementation, not permission to rerun its overwrite-prone reconstruction inside the frozen baseline.

The first deliverable is an evidence-backed proposal for a small R3 circuit, with body IDs, recorded connections, identity confidence, boundary coverage, omitted feedback and normalization choices. Specify a coverage target and explain it before scoring the new circuit. Stop if the required identities or measurements cannot be supported. Do not invent electrical conductances, neuron counterparts or retinal maps.

Once that proposal is supported, write an R3 protocol before new outcomes. Keep R2 reference evidence intact, retain the conventional controller, and separate motor calibration from new test scenes. R2 test patterns are now inspected data and are not future blind validation. A new model can be developed under studies/r3 or another explicit versioned namespace; a baseline Git revision must remain recoverable.

Subsequent workstreams:

1. **Physiology:** matched stimulus and measurement comparisons for central neurons and perturbations, with source provenance and development/validation separation. Existing inspected recordings remain development evidence.
2. **Robustness:** independently declared contrast, square-size/density, sensor-noise, delay and disturbance-frequency tests. Do not pick the best-looking condition as the new acceptance rule.
3. **Embodiment:** introduce a calibrated camera and motor interface, latency measurements, saturation and safety limits for a specified robot. Continue image-only inference. A physical hardware result requires real device measurements.

## 6. Evidence and Git rules

- Treat results/r2, results/calibration_r2, results/v1 and results/calibration_v1 as immutable reference evidence.
- Use tools/check_baseline.py for read-only verification. scripts/review_results.py writes a receipt; use it only on a new generated run, not the sealed reference directory.
- The V1 numerical FAIL is retained. Its readable source copies normalize line endings; results/v1/source_bytes.json preserves byte-exact original source contents.
- Preserve .gitattributes: byte changes and automatic line-ending conversion can invalidate source receipts.
- Keep raw connectome files, environments, credentials and generated replays out of commits.
- Before new outcomes, record the question, assumptions, version, split, endpoints, controls, numerical requirements and stopping criteria. Afterward, report failures and all comparators.
- Append completed work to ../docs/PROJECT_PROGRESS_REPORT.md. Keep the live report outside immutable inventories; include a dated snapshot when sealing a new study.
- Unit-test success means implementation correctness. Engineering compensation, biological explanation and field deployment each require their own evidence.
- Work on a codex/ branch and review the diff before committing. If your own origin is writable, push that branch and open a pull request for review. Never force-push over the supplied baseline.

## 7. Copyable AI prompts

Use one prompt at a time. The prompts intentionally define a bounded task and a clear deliverable. GPT-6.1 Sol Max is sufficient for the first steps. Consider Ultra only when independent workstreams can be delegated with a shared frozen protocol.

### Prompt A — resume and reproduce

```text
We are working in the fly_vision repository, in optomotor_closed_loop. The main goal is a connectome-constrained fly optomotor circuit, biological validation, and eventual embodied testing. Read the repository-root AGENTS.md, optomotor_closed_loop/AGENTS.md, STUDENT_HANDOFF.md, docs/RESULTS_APPRAISAL_R2.md and docs/NUMERICAL_CORRECTION_R2.md.

Record the current Git revision. Check the installed Python/package versions, run tools/check_baseline.py, run the 14 unittest checks, and run tools/replay_baseline.py into a new generated directory. Compare all 270 trajectories with the reference. Do not edit model code, thresholds or sealed evidence. Report the exact commands, results, receipt path, execution time and any failure. Explain the model's current limitations in plain language. Append completed checks to the root progress report.
```

### Prompt B — the first student experiment

Use the complete prompt in FIRST_STUDENT_TASK.md. It fixes the gain/delay study and prevents uncontrolled retuning on final test patterns.

### Prompt C — anatomical boundary audit

```text
The R2 baseline has been reproduced. Perform the next anatomical boundary audit in a new studies/anatomy_boundary_v1 directory. Read the handoff and the prior anatomical-strengthening, horizontal-opponency and H2-integration reports before proposing changes.

Using the shipped anatomy first, tabulate each central neuron's identity/side, predicted transmitter, full versus retained incoming synapses and boundary coverage. Distinguish PS321-to-bIPS correspondence from confirmed cell identity. Identify which omitted-partner information is unavailable in the compact export. Write a bounded source-acquisition/extraction plan if needed, including versions, hashes, resource estimate and a separate destination. Do not download bulk data before resource admission, alter R2, invent connections, run a new gain search or claim biological validation. Deliver an anatomy audit and a small, evidence-backed R3 candidate specification with explicit stopping criteria.
```

### Prompt D — implement the specified R3 candidate

```text
Read the accepted R3 anatomical specification and write a versioned protocol before computing new neural outcomes. Implement only the specified candidate in a separate study namespace, keeping the R2 baseline and conventional visual controller available. Preserve measured asymmetry and document every sign, time constant, omitted input and normalization rule.

Use camera images only during inference. Fit motor conversion on separate calibration patterns, freeze it, and then evaluate new test-seed namespaces. Keep normalization fixed for silencing controls. Include continuous yaw metrics, straight-travel errors, both yaw directions and numerical refinements. Preserve every failed condition. Run one predeclared comparison, report all outcomes and resources, and stop rather than repeatedly adjusting the model on the new test set.
```

### Prompt E — prepare a biological validation study

```text
Design a matched physiological/perturbation validation for the optomotor circuit. First inspect the actual public data, stimulus metadata, cell/hemisphere/neurite identities, recording units, prior model fitting and which recordings this project already inspected. Consult the existing dataset map and failed H2 report.

Separate neural dynamics from the observation model and camera/display reconstruction. Do not equate model-unit rates with spikes, voltage or fluorescence without a justified mapping. Fit any necessary observation parameters only on development data. Identify an independent validation set or state that one is missing. Deliver a data-suitability table, a fixed protocol and stopping rules before downloading large recordings or computing validation scores. If exact stimuli or independent data are unavailable, report that specific limitation without inventing missing measurements.
```

### Prompt F — realistic sensory and motor robustness

```text
Starting from the frozen baseline or an explicitly specified accepted candidate, define one bounded robustness study covering predeclared square contrast/size/density, sensor noise, camera/motor delay and continuous yaw disturbance frequencies. Keep the original random-square conditions as a reference and retain conventional control.

Choose calibration/test partitions and acceptance criteria before new outcomes. Quantify compensation, phase/latency where identifiable, straight-travel drift, saturation and numerical sensitivity. Keep simulator truth out of inference. Produce a complete result table, all failures, a compact figure and an execution/resource report. Do not interpret synthetic robustness as a biological or physical field test.
```

### Prompt G — robot implementation plan

```text
Prepare a robotic implementation of the accepted optomotor model. First identify the intended robot or simulator, camera geometry/frame rate, motor command units and limits, compute budget and measured latency. Ask only for essential missing hardware information.

Keep the controller's image-only inference interface. Define camera calibration, image preprocessing, motor mapping, logging, paired conventional-control tests and disturbance trials. Implement and test adapters in simulation/replay first, with versioned outputs and no changes to sealed scientific evidence. Prepare a reviewable physical test procedure before operating actuators. Distinguish simulation, replay, hardware-in-the-loop and actual field evidence in the final report.
```

### Prompt H — publication appraisal after the new evidence

```text
Audit the optomotor-circuit evidence against its original scientific goal. Separate anatomy, numerical verification, engineering performance, biological prediction and physical embodiment. Compare the final contribution with relevant published circuit/agent models, including Erginkaya et al. 2025, and report negative comparisons and missing evidence.

Assess what can actually support a paper. If recommending journals or calls, verify current official journal scope, current deadlines, title-specific CAPES APC coverage, UFPA participation and corresponding-author requirements. Do not redirect the main contribution to the supporting alignment pilot or treat a reproducible prototype as a validated biological mechanism. Deliver a concise submission-readiness verdict and the smallest remaining evidence gap.
```
