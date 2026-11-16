# Supervisor evidence brief — 12 October 2026

**Question assigned:** Can physical moving images produce T4/T5 and downstream
HS/H2 direction selectivity after removing direction labels from the image
input and explicitly registering left/right visual coordinates?

**What we completed:** A clean model pathway, seven prescribed horizontal
conditions, individual/subtype/side analyses, all ten HS/H2 targets, anti-leakage
controls, and all 14 requested output files. The model's left/right transform
uses documented chart conventions and functional anchors. It is not an
independent measurement of this specimen's optics.

**What happened:** Geometry is internally consistent under those conventions.
T4/T5 horizontal selectivity remains weak/incomplete: only 1/8 required horizontal
subtype/eye groups meets the original criterion. The original stationary neural
response had startup drift. A separately frozen initialization study stabilizes
every recorded cell but does not rescue the weak direction result. The original
positive HS/H2 contrasts therefore cannot be used alone as proof of success.

**Later narrowed result:** A published T5 model reproduces direction of grating
oscillation amplitude in 4/4 comparisons and moving-bar responses in the expected
direction in 9/9 pairs. It still has quantitative waveform and grating-mean
discrepancies. Verified image/native transfer shows that the sampler implements
the tested inputs accurately. One substantial change to two inhibitory filter
times preserves modeled responses on 78 stimuli; this is parameter compensation
within one model. A subsequent 40-candidate local search finds no new material
alternative preserving all outputs, including no qualifying substantial E/I
conductance compensation.

**Confidence and limits:** The new evidence audit verifies 12,480 indexed entries,
the original 14-file/seven-batch bundle, and every latest candidate decision from
saved traces. Sixteen tests pass. A hard-coded-threshold reuse defect is addressed
in a separate configuration-driven checker; completed results are unchanged.
Numerical verification is strong. Independent population physiology, measured
bilateral optics and biological degeneracy are not established.

**Recommendation:** Finish the computational diagnostic report with these
limitations and retain the T5 study as a clearly separate extension. The original
instructions allow a negative result; repeated searching for a positive answer
is not an assignment requirement.

The specific scope decision for supervisor review is: **Is the completed
diagnostic under documented coordinate conventions sufficient, or is independently
measured anatomical registration / broader physiological validation required?**
If stronger validation is required, start with the published T5 data and model
provenance, using the bounded alternative plan; do not rebuild the frontend
without evidence of a new implementation defect.

[Audit and all-14-part mapping](T5_EVIDENCE_AUDIT_REPORT_V1.md) ·
[End-to-end alternatives](PROJECT_COMPLETION_ALTERNATIVES_V1.md) ·
[Original completion audit](POSTFIX_COMPLETION_AUDIT_V1.md) ·
[Latest T5 result](T5_ACTIVE_SENSITIVITY_REPORT_V1.md).

Prepared locally for review. No message, submission or public upload has been sent.
