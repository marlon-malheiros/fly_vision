# Numerical tie handling amendment R2

16 November 2026. The independent reviewer failed to reproduce one single-fit
count using the algebraic squared-distance identity: 3,866 versus 3,877
rejections for a wrong-family comparison. Original code and results are
preserved. Symmetric/near-identical calibration fits make exact floating-point
argmin sensitive to roundoff. This is a numerical analysis correction after
outcomes were seen, not a new blind method or outcome-selected model revision.

Repeat the identical synthetic experiment and random stream in a new directory.
Keep all inputs, observations, models, geometry, absolute compatibility and
test thresholds unchanged. For the single-fit baseline, choose the first
lexicographic candidate whose calibration chi-square statistic is within 1e-9
of the minimum. This dimensionless tolerance is negligible relative to the
chi-square decision thresholds; it resolves numerical ties, not statistical
equivalence. The compatibility-set procedure is unchanged. Independently
recompute the amended choices via the quadratic-distance identity; preserve
any remaining disagreement rather than increasing this tolerance.

Report original and amended results together and whether the substantive
conclusions change. Do not promote a candidate because its corrected count is
more favorable. Freeze the amendment and wrapper before regenerated outcomes.
