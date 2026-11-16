# Handoff for a new conversation

Prepared 13 November 2026. Latest scientific milestone: 6 November; comprehensive synthesis: 8 November; subsequent operational review: 10 November. This handoff adds no scientific experiment.

## Start here

You are continuing a computational neuroscience project in:

`<WORKSPACE>`

Read `AGENTS.md` and this handoff first. Consult the linked reports as needed; avoid rereading the entire project history before choosing a specific task. Follow the user's next request. The integration work below is a recommendation, not an experiment already executed.

The user is learning the field. Explain decisions simply and briefly. They are concerned about repeated experiments consuming usage without progress. Prefer a bounded question, explicit acceptance/stopping criteria and a clear result. Suggest alternatives when evidence blocks a route. Do not present every failed variant as failure of the entire project.

## Goal

Build a biologically supported neural model explaining how a fly detects small body turns during forward walking, and investigate whether bIPS-associated circuitry helps. Long term: sensorimotor modeling and robotics. Current work is open-loop; no qualified motor controller exists.

The pipeline is:

`3D scene → binocular images → T4/T5 visual signals → MaleCNS circuit → neural activity → yaw readout`

T4/T5 are early motion-sensitive neurons; HS/H2 are wide-field visual neurons; bIPS is a central inhibitory class; DNp15 is a descending class. Yaw means left/right rotation. The project benchmark uses ±2°/s at walking speeds 5.5, 11 and 16.5 mm/s. These are engineering targets, not measured fly detection limits. Vision alone does not identify whether a turn was intended.

## What we have that is solid

**1. Functional platform.** Binocular 3D rendering, numerical controls, a direction-sensitive functional frontend, recurrent MaleCNS simulation, decoder evaluation and controlled ablations all exist. Original/expanded/LPi graphs contain 13,593/13,618/13,624 cells respectively. The frontend's direction-channel routing is an explicit surrogate assumption; functional correctness does not establish biological emergence.

**2. A bounded neural-only small-turn success.** A frozen artificial readout using local T4/T5 and downstream signals passed a fresh 24-room simulation test:

| Walking speed | Correct ±2°/s detections | Straight alarms |
|---|---:|---:|
|5.5 mm/s|48/48|0/24|
|11 mm/s|48/48|0/24|
|16.5 mm/s|42/48|0/24|

It also passed ±5°/s, stationary and 81 numerical checks. Its threshold used 40 separate negative calibration rooms; inference uses neither true speed nor an image-motion estimator. However, an older cohort still has **3/24 fast straight alarms**. General reliability and biological implementation of the learned readout remain open.

**3. A separate T4 physiology success.** The fixed published Gruntman T4 cable plus a predefined ensemble of flash-equivalent retinal registrations passed a prospective comparison on project-reserved moving responses from author cells 6–8. Primary physical-mV predictions have **33.13% lower pooled MSE than a direction-blind reference**, RMSE 4.872612 mV and bootstrap lower statistic 0.102679. Independent numerical review passes.

Limits: one cell is slightly worse than the reference; stationary/early-motion calibration is allowed; the authors' stationary-fit cohort overlaps these recordings; sustained inhibition remains unqualified. These recordings are now inspected data for any future revision.

**These successes belong to different versions/assays. They have not been combined into one validated walking model.** Earlier summaries sometimes obscured the bounded 2°/s success by saying reliability was simply “unfinished”; retain both the success and its counterexample.

## What failed, and what must not be rediscovered

- Original DNp15-only readers often confused straight walking with turns. Some early thresholds failed larger-room or finer-sampling tests.
- bIPS perturbations change gain and bilateral balance; decoder recalibration can recover information. Biological necessity/causality is not established.
- Recorded uLPTCrn/H2rn and horizontal LPi circuitry has already been added and tested. LPi partly corrected null-direction signs but did not satisfy every physiological guard. “Just add LPi” is not a new solution.
- Multiple pretrained/full FlyVis routes, camera geometries, readouts, temporal averaging and physiological parameter families were tested. A 72-model physiology search and an adaptive Mi1 integration failed their complete criteria.
- Dense image-only and hybrid methods passed a separate engineering benchmark; image-only was at least as good. They do not demonstrate a neural contribution or biological validity.
- Some restricted Mi1 and T4c measurement comparisons passed. Their gains cannot be transferred arbitrarily into other neurons or synaptic release.

Failures do not prove the research objective impossible. Combining favorable results from different models does not validate one complete circuit either.

## Recommended next scientific task

**Audit and specify how the newly qualified T4 component could connect to the walking model.** Its somatic voltage is in mV; the existing network accepts bounded/model-unit drive. The voltage-to-drive/release bridge, spatial embedding, contrast behavior and T5/OFF coverage require explicit evidence or declared assumptions.

Suggested sequence:

1. Inspect the existing interfaces and source evidence; write one versioned integration contract and finite execution plan.
2. Run a small static/PD/ND/contrast/frequency control batch if that contract is supportable.
3. Freeze the candidate and decoder policy before new walking outcomes. A changed encoder does not inherit the old decoder's qualification.
4. Compare baseline/candidate on identical held-out walking images, with straight controls and ±2/±5°/s at all three speeds.

Stop on unsupported coupling, failed numerical controls or failed predefined criteria. Do not launch another broad tuning search on the same physiology recordings. Broader fixed-detector reliability or a matched T5 component are distinct alternatives.

## Read only the relevant files

| Purpose | File |
|---|---|
| Complete situation, references and history | [Technical report](PROJECT_TECHNICAL_REPORT_2026-11-08_V1.md), especially sections 7–9 and 14–15 |
| Neural-only 2°/s result | [Readout report](docs/RAW_LOCAL_CALIBRATION_REPAIR_REPORT_V1.md), [outcomes](results/raw_local_calibration_repair_v1/test_results.json) |
| Latest T4 physiological result | [Reserved T4 report](docs/T4_RESERVED_TRANSFER_REPORT_V1.md), [protocol](docs/T4_RESERVED_TRANSFER_PROTOCOL_V1.md), [decision](results/t4_reserved_transfer_v1/decision.json) |
| Why retinal registration matters | [Geometry report](docs/T4_GEOMETRY_IDENTIFIABILITY_REPORT_V1.md) |
| Actual T4 implementation | [Cable model](src/male_optic_frontend/physiological_t4.py), [image/voltage interface](src/male_optic_frontend/t4_cable_matched_v1.py), [study driver](scripts/t4_reserved_transfer_v1.py), [worker](scripts/t4_cable_matched_worker_v1.py) |
| Current decisions | Recent entries of [progress report](docs/PROJECT_PROGRESS_REPORT.md) |

Main literature: Erginkaya 2025 (central disinhibition), Gruntman 2018/2019 (T4/T5 physiology), Lappalainen 2024 (FlyVis), Ammer 2023 (opponency), Pokusaeva 2024 (electrical interactions). Exact titles, DOI links, data and provenance are in section 17 of the technical report.

## Practical constraints and preservation

- Append dated decisions, results, failures and limitations to `docs/PROJECT_PROGRESS_REPORT.md`. Preserve sealed studies; use new versions and development/test separation. Do not invent missing connections or electrical conductances.
- Original functional frontend and new T4 reference remain separate. Full T5/downstream physiology, robust generalization and biological bIPS mechanism remain unresolved. Four reserved C2/C3 animals remain unscored in the reviewed record.
- Large obsolete movies were intentionally retired in November. Check `docs/LEGACY_MOVIE_RETIREMENT_REPORT_V2.md` before interpreting missing old files. Do not regenerate the bulk archive. Stream images, store compact evidence and estimate resources before new runs.
- **Last inspected hardware, 8 November:** i5-12450H, about 15 GiB RAM, RTX 2050 detected but NVIDIA driver inaccessible; about 147 GiB filesystem space free. Recheck only what a new task needs. CPU execution is the preferred initial target.
- Scientific Python is usually `../mech_male_fly_cns/.venv/bin/python` with `PYTHONPATH=src:scripts`, `PYTHONDONTWRITEBYTECODE=1` and `OPENBLAS_NUM_THREADS=1`. Archived environments govern reproduction.
- The temporary T4 worker environment was absent on 8 November. A new cable rerun requires restoring its recorded Python 3.11 / NEURON 8.2.7 / NumPy 1.26.4 environment. Saved sources/data/results remain available.
- V9 camera work is unrelated unfinished work. Preserve its untracked configs/scripts/tests. Its prior timing experiment stopped at an affinity assertion; do not label it deployed.
- At handoff creation the progress file already contained uncommitted 10 November operational entries. Preserve those edits. No new scientific results since the reserved T4 study were established by the subsequent reviews.
- The 8 November audit rehashed six selected intact archives (8,670 entries), all passing. That is historical scoped evidence, not today's universal archive check. No need to repeat a full audit merely to start a conversation.

## Suggested first message in the new conversation

> Read `AGENTS.md` and `CONVERSATION_HANDOFF_2026-11-13.md` in our project directory. Continue from the documented state. Give me a brief assessment and a bounded plan for the T4-to-MaleCNS interface audit, with a clear success/stopping rule before substantial new simulations. Keep explanations accessible and update the progress report as work completes.
