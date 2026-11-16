# Functional motion frontend — simple summary

Decision: **FUNCTIONAL_END_TO_END_PASS**.

We built a new fixed-neighbor motion circuit. It receives pixels and computes
all motion channels everywhere through delays and neighboring interactions.
Every target is covered; output routing uses declared surrogate channel slots.
Twenty-eight focused tests and independent numerical checks pass.

| Texture | Horizontal groups passing | Minimum expected fraction |
|---|---:|---:|
| 42 | 8/8 | 99.88% |
| 78201 | 8/8 | 100.00% |
| 78202 | 8/8 | 100.00% |
| 78203 | 8/8 | 99.88% |

Supplemental speed groups: 16/16. Grating
comparisons: 16/16. STATIC maximum motion
signal: 0. Frozen downstream expected global directions: 40/40; unilateral signs: 40/40.

This is a tested functional prototype, with conventions and failures reported.
It is not evidence of accurate individual T4/T5 physiology or neural degeneracy.
The full report and saved controls make it reviewable by a supervisor.

[Technical report](FIXED_NEIGHBOR_MOTION_REPORT_V1.md) · [Progress](PROJECT_PROGRESS_REPORT.md).

Vertical-like slots also respond selectively to horizontal random textures; their tuning remains a stated limitation. Memory interruptions and a reference-checker boundary bug were corrected and preserved; no scientific parameters or thresholds changed.
