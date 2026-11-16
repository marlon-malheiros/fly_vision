# Biological gain-control round — 2026-11-02

Goal: reproduce measured neuron responses while preserving the successful baseline small-turn detector.

One separate gain-control frontend was calibrated using only PD10/25 and PD100 reference. At 50% contrast: recordings 91.4% of full response, baseline 21.8%, revised 94.8%. The complete contrast/direction test has 1/7 mismatches, and the frequency test 15/15. Recorded peak 0.5 Hz, candidate peak 5 Hz. Numerical checks 22/26 pass. No graph, neural time constant or original detector changed; the revised frontend does not inherit the old detector's walking result.

Four preferred-direction time-resolution checks at 2.5/15 Hz fail, so the exact frequency curve is not certified converged. All failures remain recorded; no criterion was weakened.

Initial missing-source handling failed before neural simulation. The corrected version retains four blanks/all recordings and the identical fitted parameter. Both failures and all evidence remain preserved. Unknown animal identity/overlap, display calibration and the functional observation model still limit biological claims.

This candidate does not pass the complete physiological advancement rule. No full biological validation is claimed. [Detailed report](HS_GAIN_TRANSFER_REPORT_V1.md), [protocol](HS_GAIN_TRANSFER_PROTOCOL_V1.md), [missingness amendment](HS_GAIN_TRANSFER_MISSINGNESS_AMENDMENT_R2.md).

TL;DR: we tested a specific sensitivity repair and measured what it fixes and what remains wrong; calibration success alone is not validation.
