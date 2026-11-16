# Public stimulus retrieval and practical benchmark path

24 October 2026. The user reports no access to private stimulus files and asks
whether we can obtain them elsewhere. This follow-up adds public-source
retrieval; it does not alter the completed numerical study or fit physiology.

## What we obtained

Downloaded the paper's three supplementary MP4 stimulus examples and two PDF
supplements directly from its [publisher page](https://www.nature.com/articles/s41593-025-01948-9#Sec37).
The movies cover basic rotational/translational patterns, speed tuning and
compound optic flow. They are H.264, 1120×480 at 30 frames/s, with durations
48.00, 24.07 and 51.73 s. These are presentation movies with borders/color and
resampling, rather than verified original 32×96 per-trial LED arrays.
The 4-s frame of movie 1 was visually inspected. Publisher captions identify
the stimulus families, not which recording trial used each random-dot state.

Local downloads:

- [Basic motion movie](../results/continuous_yaw_mechanisms_v1/stimulus_search_followup_v1/supplements/41593_2025_1948_MOESM3_ESM.mp4)
- [Speed-tuning movie](../results/continuous_yaw_mechanisms_v1/stimulus_search_followup_v1/supplements/41593_2025_1948_MOESM4_ESM.mp4)
- [Compound-motion movie](../results/continuous_yaw_mechanisms_v1/stimulus_search_followup_v1/supplements/41593_2025_1948_MOESM5_ESM.mp4)
- [Supplementary information](../results/continuous_yaw_mechanisms_v1/stimulus_search_followup_v1/supplements/41593_2025_1948_MOESM1_ESM.pdf)
- [Retrieval URLs, hashes and HTTP receipts](../results/continuous_yaw_mechanisms_v1/stimulus_search_followup_v1/retrieval.json)

## Additional search scope and negative results

Inspected the complete seven-commit tree history, branch/tag/fork listings of
the [paper repository](https://github.com/ChiappeLab/Erginkaya_et_al_2025).
It has one branch, no tags and no listed forks at retrieval. Retrieved the full
39-commit history of [Motion Maker G4](https://github.com/misaacson01/Motion_Maker_G4),
including its development branch and available pull refs, and the listed
39-commit [fork](https://github.com/toddappleby/Motion_Maker_G4). Full bundles
and per-commit path inventories are preserved. No path explicitly labeled G3
was found in those histories; this filename search does not prove that all
code is incapable of G3 adaptation. No experiment-specific modified generator
or trial-pattern correspondence was established.

The [cited Zenodo archive](https://zenodo.org/records/14967806) API currently
lists one version, containing `data.zip` and `README.md`. The previously audited
ZIP inventory and MAT metadata already provide recordings and stimulus labels;
they do not identify original per-trial image sequences. The browser could not
open the archive page, but direct public API retrieval succeeded. The first
sandboxed network attempt could not resolve DNS; approved network retrieval
then completed with no download errors. This is a bounded public search, not
proof that no unpublished or separately deposited copy exists.
[Full history and video metadata](../results/continuous_yaw_mechanisms_v1/stimulus_search_followup_v1/history_extension/complete.json),
[earlier archive inventory](../results/published_circuit_comparison_v1/audit/zenodo_archive_inventory.json).

## A feasible solution without private files

Proceed in a new study with a **stimulus-family comparison**. Use the paper's
documented display dimensions, dot density/size and timing to reconstruct
random-dot ensembles; use the example movies to check qualitative motion,
masking and direction. Preserve independently generated dot realizations and
test sensitivity to uncertain rendering/clock/side assumptions. Do not choose
those assumptions for better neural agreement. The movies can also support a
separate demonstration replay after an explicit crop/display mapping audit.
Neither route supplies the missing recording-trial identity.

Start with direction preference and baseline-subtracted sustained epoch
contrasts using the recorded reporter and compartment. If fitting an observation
model, use declared development recordings, freeze it before testing and label
previously inspected animals honestly. Do not score raw rate activity against
calcium fluorescence or adopt an arbitrary calcium decay. Uncertain display
and measurement mapping should produce uncertainty bounds, not fitted facts.

This can test qualitative compatibility and robustness to plausible stimuli.
It cannot establish exact waveform prediction for the published trials or
fresh physiological validation. Exact replay would require a direct author
data request for modified G3 scripts/patterns, random-dot states and display
clocks; the request can be made by the project lead, without requiring the
professor to possess those files. No external message was sent. The current
numerical study is complete independently of that future benchmark.
