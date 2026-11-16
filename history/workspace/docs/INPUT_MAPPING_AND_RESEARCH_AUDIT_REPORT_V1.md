# Input mapping and research-direction audit V1

24 October 2026. **Completed: no production mapping mismatch was found in the
tested path. No justified neural-model repair was identified.** The audit also
found a real risk of repeating completed diagnostics. We close that branch
within its tested scope and specify a distinct, unfinished data task.
[Frozen protocol](INPUT_MAPPING_AND_RESEARCH_AUDIT_PROTOCOL_V1.md),
[question/evidence/decision ledger](../results/input_mapping_research_audit_v1/research_decision_ledger.csv).

## What the implementation audit establishes

All 13,579 active T4/T5 IDs match their curated type, hemisphere, eyemap
coordinates, declared channel and graph identity. All eight symmetric-world
straight/static cases were retained: s07/s12 × 0/5.5/11/16.5 mm/s, yaw zero.
These are known diagnostic inputs, not new test environments.

Replayed 3,208 binocular retinal frames through the unchanged frontend. An
independent regular-grid interpolation method reconstructed 21,835,032 saved
source-drive values with maximum absolute error 5.56×10⁻¹⁷; the production replay
matches exactly. Left/right images and computed fields remain equal. Independent
normalized sampling measures reconstruct side/channel means within
4.57×10⁻¹³ model units. Five deliberately corrupted metadata fixtures are
rejected. These are checker controls, not observed production failures.
[Execution and all errors](../results/input_mapping_research_audit_v1/complete.json),
[target crosswalk](../results/input_mapping_research_audit_v1/target_crosswalk.csv),
[independent arithmetic review](../results/input_mapping_research_audit_v1/independent_review.json).

A supplementary check exercises the actual production loader, rather than
only the algebra of permutations: all 3,216 original/shuffled input-assembly
calls reproduce the same body-ID-assigned drive exactly. All states stay zero
and no ODE step executes; these are software fixtures, not neural simulations.
[Coverage addendum](INPUT_MAPPING_LOADER_CHECK_ADDENDUM_V1.md),
[loader results](../results/input_mapping_research_audit_v1/production_loader_complete.json).

## Why equal images still give unequal population means

The two sides contain different sampling locations, multiplicities and channel
proportions. The same motion field evaluated through different sampling measures
can yield different averages. The following exact identity separates the
all-source mean input difference into within-channel spatial and between-channel
mixture terms. It does not decompose recurrent neural outputs or false alarms.

| Known symmetric case | Observed L−R | Within-channel spatial term | Channel-mixture count term |
|---|---:|---:|---:|
| s07, 5.5 mm/s | −5.11224 | −3.09063 | −2.02161 |
| s07, 11 mm/s | −6.22387 | −2.50443 | −3.71945 |
| s07, 16.5 mm/s | −4.38138 | +0.59221 | −4.97360 |
| s12, 5.5 mm/s | −3.14884 | −2.03951 | −1.10933 |
| s12, 11 mm/s | −1.81136 | +0.39381 | −2.20517 |
| s12, 16.5 mm/s | −2.38847 | +0.81855 | −3.20702 |

All entries are external source-drive model units ×10⁻⁶. Both stationary cases
are exactly zero. Accounting residuals are below 4.88×10⁻²⁰. The two components
sometimes oppose each other, so percentage attribution can be misleading.
Means within one channel depend on its spatial distribution, rather than its
population size alone. These are imposed drives, not emitted T4/T5 rates,
spikes, membrane voltage or calcium measurements.
[Complete accounting](../results/input_mapping_research_audit_v1/population_difference_accounting.csv),
[all channels and reconstruction errors](../results/input_mapping_research_audit_v1/channel_reconstruction.csv).

Applying the same virtual sampling measure to both equal fields makes their
mean drives exactly equal. This is a mathematical control, with no invented
homolog pairing. It does not establish that biological populations should have
equal means, that altered drives preserve relevant spatial information, or that
DNp15 detection would improve. No source balancing was installed in the model.
[Virtual control](../results/input_mapping_research_audit_v1/virtual_common_sampling.csv).

![Sampling measures and input accounting](../results/input_mapping_research_audit_v1/presentation_v2/input_sampling_accounting.png)

## Are we running in circles?

**There was a risk of doing so.** My latest recommendation to recheck basic eye
signs and labels substantially overlapped the October 6 coordinate audit and
October 13 functional-frontend checks. It should not have been presented as
though those tests had never been done. This audit explicitly reused that
evidence, added the spatial/count accounting and checked the active loader.
Passing the declared mapping does not establish an accurate optical model.

The larger historical sequence did add distinct evidence: unfamiliar-room
testing challenged early six-room thresholds; sampling refinement exposed input
smoothing dependence; the conditional published-circuit comparison examined a
different mechanism; continuous-response and preserved-weight controls separated
gain, offsets and normalization. These were not identical repetitions. The
problem is reopening their questions without stating what new evidence would
change the answer.

| Question already investigated | Current evidence | Decision now |
|---|---|---|
| Basic sign, ID and routing consistency | Passes under the specified chart | Close routine bug hunt; reopen for a concrete counterexample or changed source |
| Downstream tanh saturation | Unsupported at recorded operating points | Drop as a current explanation |
| More neurons improve yaw processing | Effects strongly depend on weight normalization | Require new biological constraints before another expansion |
| More static/temporal readout features fix generalization | No consistent improvement in fresh rooms | Avoid another search on inspected test rooms |
| Symmetric input proves the model is biologically correct | Not established | Preserve separation of implementation and physiology |
| Exact Erginkaya files must be found before any comparison | Public examples support qualified approximations | Stop repeating the same bounded source search |

The full ledger links the original evidence and conditions for reopening each
question. A negative result is a research result; it does not guarantee a
software bug exists. The existing optical chart assigns eye centers, angular
spacing and cardinal directions using construction choices. Those assumptions
still need external evidence. The [eye-structure study](https://www.nature.com/articles/s41586-025-09276-5)
and its [public code](https://github.com/reiserlab/eyemap_T4) provide relevant
geometry/physiology context, not exact MaleCNS specimen registration.

## One concrete unfinished task, using data already here

The source audit found that Zhao H2 electrophysiology was already downloaded
and admitted on September 30. The local public MATLAB file is 3,106,787,136
bytes and again matches its deposited SHA-256. Its author documentation identifies
seven cells, two protocols and stimulus-indexed responses. The processed
78-row file contains tuning summaries; it cannot replace the full trial table.
The earlier source-audit report already names the missing MATLAB MCOS table
decoder. No active scored H2 raw-tuning result was located in the inspected
project scripts/results. This is an unfinished task, not a newly discovered
dataset. An older source record in the separate legacy workspace still says
the deposit was not downloaded; the local verified availability record below
supersedes that availability statement, without supplying a validation result.
[Earlier data-admission report](VALIDATION_SOURCE_FETCH_AUDIT_V1.md),
[current presence/hash/schema check](../results/input_mapping_research_audit_v1/existing_h2_resource.json),
[public recording deposit](https://doi.org/10.25378/janelia.28462100.v2).

The next distinct deliverable is **a checked H2 stimulus/trial table and one
external directional-tuning benchmark specification**. It has these stop gates:

1. Decode `cellNum`, `protNum`, `newIndex`, orientation, location, polarity and
   duration. Cross-check every metadata-to-response join with the authors' script.
   Ambiguous/duplicate mappings stop model scoring; do not infer them from a
   preferred model response.
2. Establish display-to-eye conventions and the exact statistic/normalization
   used for PD and DSI. Distinguish bright/dark, location, cell and repeat.
3. Freeze stimulus reconstruction uncertainty and the observation/readout
   definition before neural prediction. Start with normalized direction tuning;
   do not compare raw model rate directly with voltage or spike frequency.
4. State which measurements were already inspected and what is truly held out.
   Previously seen aggregate tuning cannot become a fresh-animal validation set.
5. Run one specified benchmark and retain disagreement. A failure must identify
   a particular violated prediction or unresolved mapping before another model
   revision is attempted.

This audit admits that next task; it does not claim the decoder or H2 benchmark
has been executed. H2 local tuning would test a downstream response property,
not directly establish ±2°/s walking detection or explain every DNp15 error.
It offers an external constraint before choosing a new biological model change.

## Reproduction, failures and scope

[Reproduction recipe](INPUT_MAPPING_AND_RESEARCH_AUDIT_REPRODUCTION_V1.md).
The original pre-analysis hash freeze and supplemental loader freeze verify
unchanged. Independent arithmetic and production-loader checks pass. No new
neural trajectory, unused environment, detector threshold, circuit parameter,
optical parameter or closed-loop controller was introduced. The ±2°/s
reliability objective remains unmet. The audit's pass closes the tested
implementation-mismatch branch; it does not rule out all bugs or model errors.

The first optional H2 schema check failed because the simulation interpreter
lacked `h5py`. The existing project test interpreter includes it; the unchanged
script then passed without installing or changing baseline software. Both logs
are retained. The initial figure legend obscured one point; its layout is
preserved, and V2 moves the legend without changing numerical data. No failed
scientific gate was relaxed. No second complete eight-case replay is claimed.

## Undergraduate explanation: what we did, what we want, and why

We checked whether the model receives the wrong visual information because of
a coding mistake. In these tests, it receives exactly what its current design
specifies. Its two sides sample the same pictures differently, so their average
inputs can differ even during straight walking. Forcing those averages to match
would change the model without showing that the change is biologically correct.
We still want reliable turn detection, but the next useful step is to constrain
the model with real recordings. We already have suitable H2 data to investigate;
the immediate job is to decode their stimulus labels correctly. This lets us
test a new question instead of repeatedly checking the same calculations.
