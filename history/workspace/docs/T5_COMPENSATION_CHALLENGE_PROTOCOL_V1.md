# Prospective T5 compensation challenge — protocol V1

Client date: 2026-10-12 (America/Belem). Evidence timestamps use UTC.

Test whether the fixed `i_poles_spread` alternative from the completed parameter
pilot preserves the published cell-7/iteration-52 baseline beyond the original
26-condition benchmark. This candidate was selected using earlier scores; the
new challenge is prospective relative to its responses, not blind candidate
selection. No fitting, parameter search or physiological observations are added.

## Finite synthetic challenge, frozen before responses

52 conditions, 26 pairs:

- 32 moving bars: widths 1/2/**3**/4 native columns, steps **20/60/120/240 ms**,
  both author directions. Width 3 and all speeds are new. The nine-column
  aperture clips entering/exiting bars; widths above 4 are excluded because the
  unchanged published schedule only explicitly supports the relevant edge cases.
- 20 moving gratings: dwell **10/20/60/120/240 ms** (periods 80/160/480/960/1920 ms;
  frequencies 12.5/6.25/2.08333/1.04167/0.520833 Hz), starting phases **2/6**,
  both native phase directions. All dwell values and starting phases are new.
  Retain the source's 25 holds (three eight-phase cycles plus its final hold).

Use the released eight phase-position patterns and unchanged 27-column model
coordinates. Zero initial states, synthetic clock from −100 ms through effective
input end plus 650 ms; source effective onset 25 ms. No physical LED onset or new
image-to-retina validation is inferred. Inputs are native OFF occupancy patterns.

Four fixed sets: published baseline, exactly copied pilot alternative, an exact
E/I pole-label-swap control, and a deliberate E-gain ×0.75 mismatch control.
Primary clock 1 ms for all four (208 trajectories). Baseline and candidate also
run at 0.5 ms (104 trajectories): **312 total**, fixed before any new responses.
The fine clock is a sensitivity check, not a rescue after failing a criterion.

## Readouts and fixed engineering gates

Bars: primary 0.995 quantile of relative voltage in [0,duration), and mean in the
same window. Gratings: primary half(q95−q05) and baseline-subtracted mean in
[25+period,25+3*period), discarding cycle 1. Use NumPy linear quantiles. The model
baseline is neutral/zero, with the synthetic [-100,0) baseline retained for checks.
Actual recordings are not available for these conditions.

Primary equivalence: all 52 primary errors ≤5% (denominator
max(abs(baseline feature),0.065 mV)), all 26 DSI changes ≤0.02, and unchanged
resolved status, raw expected-sign flag and passed classification. Direction
labels remain author/native labels, even if a new condition is weak or reversed.
Pair DSI is (PD−ND)/(abs(PD)+abs(ND)); resolution floors remain response 0.065 mV,
difference 0.065 mV, abs(DSI) 0.1, denominator epsilon 6.5e-11 mV. Never discard a
weak or reversed baseline case.

Full-waveform equivalence: every trace's max(abs(candidate−baseline)) divided by
max(max(abs(baseline voltage)),0.065 mV) ≤5%. Mean equivalence: all signed means
within 5% using the same response floor, with all mean-pair DSI and classification
gates preserved. This is an explicitly broader challenge definition; earlier
pilot criteria and findings remain unchanged. Preserving a weak mean is not
fixing agreement with recorded physiology.

Sampling sensitivity: each model's 1-ms versus 0.5-ms primary features and means
must differ ≤1%, all primary/mean pair DSI changes ≤0.005, and pair classes stay
unchanged. Common-clock voltages must match within 1e-8 mV. If sensitive, keep
both results and mark the primary decision provisional rather than replacing it.

Three prospective scientific decisions:

1. `CHALLENGE_EQUIVALENCE_COMPLETE`: primary, waveform and mean gates all pass.
2. `PRIMARY_FEATURE_EQUIVALENCE_ONLY`: primary passes; waveform or mean fails.
3. `EQUIVALENCE_BREAKS_ON_CHALLENGE`: primary fails.

Report each gate and all failures even if the combined decision fails. No new
candidate is substituted and no stimulus, window or tolerance changes after
scoring. These margins are engineering definitions, not confidence intervals.
Control requirements: swapped poles preserve all voltages within 1e-8 mV;
E-gain control differs by >1e-4 mV and fails primary equivalence on at least one
condition. Controls never count as mechanistic or degeneracy candidates.

## Validation and reporting

Before freezing, integration tests must load real source phase metadata and
both copied parameter vectors. Check all 52 plans, width-3 clipping against the
unchanged source schedule, phases/direction, complete scoring clocks and gate
behavior. Freeze config, plans, parameter sets, tests, scripts, methods and input
hashes. Verify all eight predecessor indexes and their entries before/after.

Review all 312 waveforms and all four internal filter states with independently
assembled Gaussian drives and augmented matrix-exponential integration.
Reconstruct the stimulus geometry/phase schedule separately from the published
schedule branch. Independently recompute quantiles, signed means, pair classes,
gate decisions, waveform/conductance comparisons and sampling sensitivity.
Save every output and failed case. Add report, short summary, figures, progress
entries, local Git checkpoint, progress snapshot and immutable artifact index.

This can strengthen or limit **model parameter compensation**. Even a complete
pass supplies no new cells/repeats, no connectome/population degeneracy evidence,
and no resolution of earlier T4, HS/H2, texture or physiological mean failures.
