# Virtual walking through a frozen MaleCNS visual circuit — V1

Completed 2026-10-15 (America/Belem). Open-loop, exploratory model study.

**Outcome:** 36 primary trials across three 3D scenes completed, plus four input-timing refinements and one solver-only refinement. The development-trained DNp15 readout classified yaw sign/presence in 100.0% of 24 held-out trials; the all-cell readout scored 100.0%. DNp15 had higher yaw-versus-forward selectivity than HS in 9/9 scene/speed comparisons. These are deterministic computational predictions, not measured physiology or steering behavior.

## Question and frozen baseline

Can visual responses distinguish straight forward movement from a superimposed yaw rotation, across unfamiliar scenes? The starting point is the [professor technical report](PROFESSOR_FUNCTIONAL_FRONTEND_TECHNICAL_REPORT_V1.md). Existing motion equations, constants, eye-chart transforms, 13,579 target identities/routing, and 13,593-node MaleCNS graph are unchanged. The graph contains 8 HS, 2 H2, 2 PS321/bIPS and 2 DNp15 cells, with 203,861 chemical edges and zero gap edges. We verified the entire 337-entry predecessor seal before and after execution.

## What was simulated

A rigid visual observer moves in textured enclosed 3D rooms, with two eye origins 0.3 mm apart and 2 mm above the floor. Those physical dimensions are declared scenario assumptions, not measured specimen optics. Images are equirectangular panoramas (360×180 pixels, 1° pitch) rendered separately from each eye. Every ray intersects the nearest box face or sphere. Surface luminance is a fixed seeded sum of eight spatial cosines, normalized by a fixed factor; textures do not move or change contrast with condition. Ambient surface color is modeled, without lighting/shadows or a photoreceptor optical blur model. The existing bilinear image sampler then supplies the inherited 173×173 retinal grids to the unchanged fixed-neighbor motion circuit.

Body-forward movement and body yaw are integrated exactly, giving curved trajectories for compound motion. Head and body share orientation; there are no leg dynamics, gait oscillations or independent head stabilization. Motion occurs from 0.5–1.5 s in a 2-s trial. Speeds are 5.5, 11 and 16.5 mm/s; yaw is ±55.5°/s. Per scene: stationary, three forward-only, two yaw-only and six compound conditions. The corridor is the development scene; the wider room and asymmetric sphere scene have new seeds and geometry and are held out from decoder fitting. No scene was dropped after response inspection.

The motion frontend receives only numerical retinal luminance and timestamps. All eight channels are calculated before the inherited channel-to-subtype routing. Network drive is zero at every non-T4/T5 cell. Primary clocks are frontend 5 ms, graph input 10 ms, RK4 1 ms; graph input uses the predecessor’s hold and boundary midpoint convention. The saved graph drives a streamed implementation, checked against the original solver.

![Environments and images](../results/virtual_walking_openloop_v1/figures/scenes_and_binocular_images.png)

![Optic flow](../results/virtual_walking_openloop_v1/figures/analytical_optic_flow.png)

## Analysis fixed before responses

The response is mean signed tanh network rate during 0.7–1.4 s minus the matching scene’s stationary response. Signed negative values denote model inhibition; these rates are not calibrated spikes, millivolts or calcium. HS summaries average the four cells per side; other classes have one per side. Asymmetry is R−L; normalized asymmetry divides by |R|+|L|+1e−12. Texture and connectome asymmetry can produce a nonzero forward-only difference, so a bilateral difference alone is not a categorical rotation detector.

Yaw-versus-forward selectivity compares the bilateral absolute response magnitude for pure yaw (averaged across directions) with forward-only magnitude at each speed: (Y−T)/(Y+T+1e−12). This magnitude metric is prospectively defined here and is not a recreation of a calcium-imaging index. The three-way nearest-centroid decoder uses individual bilateral cell responses, with centering/scaling and class centroids fitted only to the 12 corridor conditions. Labels are no yaw, positive yaw and negative yaw. Held-out scenes use the fixed fit and their stationary baselines. There are eight trials per true class in held-out testing. The tested speeds/yaw magnitude are familiar; scene appearance and geometry are held out. A decoder is an analytical readout, not an extra neural pathway. HS/all-cell readouts have more features than two-cell readouts; their accuracies do not rank intrinsic biological circuit quality.

## Quantitative findings

| Readout | Development accuracy | Held-out accuracy | Held-out errors /24 |
|---|---:|---:|---:|
| HS | 100.0% | 95.8% | 1 |
| H2 | 100.0% | 100.0% | 0 |
| bIPS | 100.0% | 91.7% | 2 |
| DNp15 | 100.0% | 100.0% | 0 |
| All 14 cells | 100.0% | 100.0% | 0 |

Retained held-out errors: HS labeled wide_room/forward_16.5 as negative yaw; bIPS labeled wide_room/forward_16.5 as positive yaw; bIPS labeled clutter/forward_16.5 as negative yaw.

Each class has equal sample counts, so balanced accuracy equals accuracy. Development scores reuse fit data and are descriptive. Held-out observations are scene/condition cases, not independent flies; no biological significance test or population confidence interval is justified.

| Scene | Speed (mm/s) | HS rotation selectivity | DNp15 rotation selectivity | bIPS rotation selectivity |
|---|---:|---:|---:|---:|
| corridor | 5.5 | 0.45780 | 0.59227 | 0.51654 |
| corridor | 11 | 0.17842 | 0.35163 | 0.25369 |
| corridor | 16.5 | 0.01635 | 0.20315 | 0.09660 |
| wide_room | 5.5 | 0.41137 | 0.59818 | 0.49454 |
| wide_room | 11 | 0.12945 | 0.36180 | 0.23092 |
| wide_room | 16.5 | -0.01473 | 0.22359 | 0.08892 |
| clutter | 5.5 | 0.39882 | 0.58609 | 0.47979 |
| clutter | 11 | 0.11554 | 0.34169 | 0.21058 |
| clutter | 16.5 | -0.03910 | 0.19457 | 0.05761 |

The frozen compound-response measure is the change in R−L asymmetry between positive and negative yaw at the same forward speed. Its magnitude measures directional separation without assigning a favorable anatomical sign. The following fast/slow ratios are descriptive summaries of those saved contrasts, not additional acceptance rules.

| Scene | HS fast/slow magnitude | H2 | bIPS | DNp15 |
|---|---:|---:|---:|---:|
| corridor | 1.1315 | 0.5085 | 0.9746 | 0.9443 |
| wide_room | 1.0090 | 0.7602 | 0.9193 | 0.9208 |
| clutter | 1.0818 | 0.5881 | 0.9254 | 0.9104 |

Across all three scenes, DNp15’s yaw/forward index exceeds HS at each tested speed. Increasing forward speed reduces that index in every class, so rotational preference is not speed-invariant. Compound yaw asymmetry contrast changes less for DNp15 and bIPS than for H2 in this particular design. This descriptive ordering does not identify a causal circuit mechanism.

All 504 individual-cell rows, 144 class summaries, 36 selectivity rows and 180 decoder predictions are retained, including every decoding error. [Cell results](../results/virtual_walking_openloop_v1/cell_responses.csv), [class results](../results/virtual_walking_openloop_v1/class_responses.csv), [selectivity](../results/virtual_walking_openloop_v1/rotation_selectivity.csv), [decoder errors and successes](../results/virtual_walking_openloop_v1/decoder_predictions.csv).

![Trajectories](../results/virtual_walking_openloop_v1/figures/class_response_trajectories.png)

![Asymmetry](../results/virtual_walking_openloop_v1/figures/bilateral_asymmetry.png)

![Selectivity](../results/virtual_walking_openloop_v1/figures/rotation_selectivity_by_speed.png)

![Compound yaw contrast](../results/virtual_walking_openloop_v1/figures/compound_yaw_contrast_by_speed.png)

![Decoding](../results/virtual_walking_openloop_v1/figures/held_out_decoding.png)

## Numerical evidence and retained limitations

- Tests: 17 preflight checks plus 20 existing sampler/adapter regression checks passed (37 total). Scalar intersections: 1,728 rays, maximum depth error 5.33e-15 mm. Analytical angular flow versus fixed-landmark reprojection: maximum error 1.12e-08 rad/s. Translational inverse-depth dependence, central-camera rotation depth independence and instantaneous flow superposition passed.
- Independent source check: 30,416,960 channel samples across seven frames per eye in every trial, using lfilter and direct convolution rather than the production delay recurrence and uniform filter. Maximum channel error 3.72e-09; final-delay error 6.66e-16. It is a numerical subset check, not a second complete source implementation at every frame.
- Reflected geometry, world texture, yaw and eye origins reproduce all 401 frames of one compound movie, maximum luminance error 0; three physical frames replay bitwise. This checks physical binocular symmetry, not symmetry of an asymmetric connectome.
- Original legacy solver: one complete 2-s compound trial, maximum 14-cell state error 0, full-graph float32 recording error 9.31e-10. Array-only graph replay is bitwise equal. The whole 40-trial network set is not independently reintegrated by the original solver.
- Stationary source maximum 0; stationary downstream maximum 0. Independent compensated-sum review checked 504 means and all decoder fits/predictions.
- Timing refinement: 0/8 summaries exceed the predefined 10% flag, worst relative mean change 4.38% with denominator floor 0.001. Solver-only half-step maximum wide-cell state change 9.58e-06. These are four development conditions only, not universal convergence or a spatial-resolution test. [Complete refinement](../results/virtual_walking_openloop_v1/timing_refinement.json).

Coarse and fine source clocks are propagated to the network, so the combined timing comparison includes input sampling and solver changes. The separate solver-only test isolates integration at fixed held input. Frozen numerical tolerance flags are retained even if the scientific pattern remains similar. A 1° image/retinal lattice and point sampling do not guarantee absence of aliasing; no optical calibration, spatial refinement, sensor noise, natural image statistics or physiological recording fit is supplied. Three fixed scenes do not establish general performance in all environments.

The predecessor’s vertical channels retain some responses to horizontal textures. Real 3D translation also produces vertical flow, so c/d activity here would not by itself distinguish true vertical motion from that surrogate cross-axis limitation. The selected graph omits uLPTCrns and H2rns, in addition to lacking gap edges; it does not instantiate every experimentally discussed middle-layer mechanism.

## Comparison with experiments

Erginkaya et al. reported that DNp15 favors yaw over symmetric forward-like visual motion more strongly than HS, and that bIPS modulation changes with forward speed. Our DNp15-versus-HS magnitude-index ordering agrees in 9/9 scene/speed cases. This is a qualitative test, with a different readout. Their display projection lacks the physical depth/parallax present here; the paper also reduced compound-stimulus speeds after attenuation. Our physical speeds and yaw are scenario choices informed by that context, not a matched reproduction. No neural fit or circuit lesion was performed, so no causal attribution to disinhibition follows. [Erginkaya et al. (2025)](https://www.nature.com/articles/s41593-025-01948-9).

Pokusaeva et al. found that bilateral electrical interactions participate in HS–H2 course control. This saved graph has no gap edges, so that mechanism is absent. [Pokusaeva et al. (2024)](https://doi.org/10.1038/s41467-024-53173-w). Fujiwara et al. showed that HS also carries walking-related nonvisual signals. None are modeled here; this study isolates image-driven responses. [Fujiwara et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/27798632/). Walking-state changes in HS sensitivity further limit a fixed-gain model’s physiological interpretation. [Chiappe et al. (2010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4435946/).

## Supported predictions and next scientific step

The supported result is finite-scene visual discrimination by an unchanged model, quantified above, with DNp15 held-out accuracy 100.0%. Individual forward-only asymmetries, speed effects and classification errors remain part of the result. Numerical consistency supports implementation correctness under the specified conditions. Biological validity, neural degeneracy, active correction of unintended rotation, and publication acceptance have not been established.

A useful next study would prospectively specify recording-matched images, measurement conversion and uncertainty, then test those predictions without refitting this baseline. Generalization should also cover more scene seeds, spatial sampling and realistic state-dependent inputs. Open-loop analysis is complete for this finite design; any closed-loop motor controller requires a separate protocol and is not implemented here.

## Reproduction and evidence

See [reproduction instructions](VIRTUAL_WALKING_OPENLOOP_REPRODUCTION_V1.md), [frozen protocol](VIRTUAL_WALKING_OPENLOOP_PROTOCOL_V1.md), [prospective hashes](../results/virtual_walking_openloop_v1/prospective_manifest.json), and [artifact index](../results/virtual_walking_openloop_v1/artifact_index.json). New scripts and code are V1; predecessor reports/indexes were never rewritten. Failure/correction records: no execution failure recorded at report build time. Any later packaging correction is recorded separately. Raw image sequences, both retinal sequences, all routed drives/channels, sampled full-graph states and full-precision 14-cell traces are retained in the study directory. Source-equation assumptions remain those of the functional surrogate.

## Undergraduate explanation: what we did, what we want, and why

Imagine walking down a hallway. Even though the walls are still, their images slide across your eyes. This apparent movement is optic flow. Moving forward tends to produce outward motion on both sides. Turning adds a different pattern, which can be hard to notice when forward motion is already strong.

We built a virtual fly with two cameras and moved it through three rooms. We showed the camera images to the existing visual model and measured HS, H2, bIPS and DNp15, without changing their connections or settings. We also gave a simple mathematical readout examples from one room and tested it in two unfamiliar rooms. That checks whether useful information survives a change of scenery.

For this experiment, the DNp15 readout identified whether and which way the fly was turning in 100.0% of the unfamiliar-room cases. That number describes this computer model under these conditions. It does not mean that a real fly has the same accuracy or that the model can already steer.

We want to learn how a visual circuit separates ordinary forward movement from an added turn. This matters because an animal must detect small deviations to keep its course. The next scientific goal is to compare carefully matched predictions with real neural recordings. Keeping the model frozen makes both successes and failures informative: the results cannot be explained by adjusting it until it gives the answer we hoped for.
