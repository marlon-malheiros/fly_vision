# Post-outcome bar-sampling diagnostic R3

2026-11-05. The frozen V1/R2 study is complete through its stop decision:
all four primary representations have D=1 outside the development bands;
four of32 refinement checks fail. All four heldout flies remain unscored.
These facts are known before this explicitly **exploratory numerical follow-up**.
It is not a revised primary experiment, biological rescue or fresh validation.

Hypothesis: the symmetric inclusive raster counts both exact bar endpoints on
some refined-grid display frames, adding one full sample to the represented bar
width. Evaluate exact represented width (sum of bar occupancy times dx) for every
display frame at dx1,0.5,0.25deg. The physical continuous bar is exactly5deg wide.

Correct only an exact edge tie: assign half occupancy at each endpoint, retaining
full occupancy inside. This is the symmetric quadrature convention for a step
discontinuity under the existing Gaussian spatial convolution. It is not a
reconstruction of unrecorded biological pixels or an alteration of neural
weights, filters, gains or stimulus speed. This correction should leave the
existing1deg primary trajectories bitwise unchanged because those display
positions do not place a bar edge on a sample. Test this explicitly.

Use only the primary bright-on-dark horizontal T4 input, dt2.5ms and three fixed
spatial grids; both movement directions and all three existing T4 copies. The
existing raw-raster1/0.5deg traces are reused unchanged; simulate only their
corrected counterparts and the raw/corrected0.25deg case. Save compact central
traces and complete peak/D tables. No new physiology is opened, candidate
selected, parameter fitted or old artifact overwritten.

Report raw/corrected exact-width errors and adjacent spatial-refinement changes.
Use the existing5% peak /0.02 D numerical tolerances as diagnostic labels; do not
retroactively replace the original failure verdict. Require corrected width
within1e-10deg when the bar is entirely inside the aperture, and exact primary
trace parity. If refinement still fails, retain it and stop; no further search.
Same one-worker1200CPU-second/32MiB/20GiB-reserve limits. This is new rendering
code only, not an improved biological neural circuit.
