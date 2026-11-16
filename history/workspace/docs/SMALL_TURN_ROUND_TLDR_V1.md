# Small-turn round: plain-language result

1 November 2026.

**Goal:** detect a 2-degree/s body turn while walking, with few false alarms,
using neural activity. Agreement with real neurons remains a separate requirement.

**What we tried:** four new readers of existing neural activity, a published
smaller circuit with and without feedback, two training objectives, three response
times, two alarm policies and a final timing follow-up. That totals 16 fitted
readers and 44 tested reader/policy combinations. We ran 640 reduced-circuit walking
episodes and 108 numerical-control runs, each in two circuit copies.

**Result:** none passes across all walking speeds. One reader detects 32/32 slow
turns, but 17/32 medium and 9/32 fast turns. The best worst-speed reader detects
20/32, 15/32 and 14/32. These are known-room development results, not fresh tests.

**Why:** the three new MaleCNS readers identify left versus right correctly on
every actual small turn, yet some straight walks also produce strong turn-like
responses. Avoiding those false alarms makes the readers miss real small turns.
More waiting and the tested feedback circuit do not solve this. Three reduced
readers pass every numerical refinement but still fail detection, so the failure
persists in numerically stable candidates. We have not identified one proven
biological cause or shown that small-turn detection is impossible.

**What remains usable:** the earlier bounded 5-degree/s neural detector is preserved.
The complete 2-degree/s and biological-validation objectives remain unfinished.

**A different next option:** train a new, separately versioned neural visual encoder
on diverse walking image motion, then test its task performance and physiology
separately. This option is not yet tested. The reduced published motif was now
actually tried; repeating it unchanged is not a new direction.

[Complete report and evidence](SMALL_TURN_ROUND_REPORT_V1.md).

**TL;DR:** We tested another full round. No reliable 2-degree/s neural detector
emerged. The clearest problem is separating genuine small turns from strong
straight-walking responses, rather than merely assigning the correct turn direction.
