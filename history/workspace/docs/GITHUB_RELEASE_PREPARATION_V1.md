# GitHub preparation — alignment pilot V1

16 November 2026.

Prepared a focused, separate repository at
[github_release/alignment-assessment-pilot](../github_release/alignment-assessment-pilot/README.md),
with a [ZIP for review](../github_release/alignment-assessment-pilot-2026-11-16.zip).
Nothing was committed, pushed, submitted or published; no remote is configured.
The full research workspace remains intact, including unrelated unfinished work.

## Scope and decisions

The workspace has 1,510 tracked files and a long research history. The export
contains the completed alignment pilot rather than treating the entire workspace
or its Git history as publication-ready. Earlier walking, optic-flow, connectome,
voltage and neural-comparison studies are outside this focused export.

The user explicitly selected **MIT for code they own**. The export includes the
MIT license, attribution scopes, a concise scientific README, provenance, eight
meaningful tests, pinned direct dependencies, a portable replay/review command,
a GitHub Actions workflow and the initial manuscript. Original code and release
documentation use MIT; the draft manuscript has no additional reuse grant.

The archived primary Figshare metadata declares **CC BY-NC 4.0** for the recording
source, separate from the paper's license. Six small derived stimulus-image banks
are included with source attribution, declared transformations and retained data
terms. Raw neural recordings, source MATLAB implementation, bulk movies, personal
application settings and the parent Git history are excluded. See
[NOTICE](../github_release/alignment-assessment-pilot/NOTICE.md) and
[data provenance](../github_release/alignment-assessment-pilot/data/README.md).
A new metadata API request failed because DNS was unavailable; the exact cached
metadata receipt and its hash are included. No source data were redownloaded.

Expanded the workspace `.gitignore` to cover generated output, local credential
and tool directories, build products and the separately published export. Added
a current-state pointer to the historical workspace README. The live AGENTS and
progress report remain tracked and outside immutable evidence indexes.

## Validation

Testing used a relocated copy, with the workspace import path removed and the
installed scientific libraries: Python 3.14.10, NumPy 2.4.6, SciPy 1.18.1,
pytest 9.1.1. Eight tests pass. The complete portable replay exactly reproduces
all 27 corrected synthetic summary rows, all 225 centre rows and 18 optical
cell/blur comparisons. Recomputed bank values have maximum contrast error zero.
The separate squared-distance reviewer reproduces 135,000 candidate-family
assessments; 810 scalar integrations have maximum discrepancy 1.11e-16.

Existing output directories and output into the shipped reference evidence are
refused. A deliberately modified temporary source file is detected by inventory
verification; the temporary original was restored. No source archive was changed.

All 21 local Markdown links checked at the initial document audit resolve. The
LaTeX export changes only absolute figure paths. It builds twice successfully,
has no overfull boxes and produces text identical to the reviewed reference PDF.
The shipped PDF and Markdown remain byte-identical to their sealed sources.

The first complete numerical replay took 0.88 wall seconds and retained 203,348
bytes before its run receipt. The complete release is estimated below 8 MiB;
preparation requires a 1 GiB free-space reserve. No movie regeneration occurred.

The release scan checks a bounded set of credential patterns, absolute machine
paths, unexpected large files and unwanted local directories. This is a scoped
preparation check, not a proof that every conceivable sensitive string is absent.
The final manifest and ZIP receipt record the actual inventory and scan result.

The workflow uses the [official checkout/setup-python v7 examples](https://github.com/actions/setup-python)
with read-only repository permissions. Fresh dependency downloads and a hosted
Actions run were not verified because this environment cannot resolve external
hosts. The relocated run uses existing installed dependencies; it is not a clean
online installation test. Other Python/library versions remain untested.

## Evidence preservation and scientific limits

Rehashed all 55 indexed files of the completed alignment pilot, totaling
3,181,898 bytes, before copying selected evidence. Original index SHA256:
`6e0a016a1b4121cecabf22e1179dd80bf71bb1d9896758e73b5292f3c85df8b4`.
This is scoped to the retained alignment pilot; the historical movie retirements
are outside scope and were neither regenerated nor relabeled as corruption.

The export has its own inventory; it does not reuse the original historical index
to imply full archive availability. Its live AGENTS/progress files remain outside
the manifest, with a dated release progress snapshot inside. Source hashes and
every copied-file adaptation are in
[export provenance](../github_release/alignment-assessment-pilot/export_provenance.json).
The original sealed reports, manuscript and methods remain unchanged.

The exported results retain the limiting optical result, original numerical
failure, post-outcome R2 correction, unresolved cases and wrong-family retention.
Replay begins with derived image banks; raw extraction, historical fit provenance
and the full author's archive are not re-established. Numerical reproducibility
does not establish biological validation, neural degeneracy, novelty, publication
readiness or acceptance. Manuscript authorship and declarations remain for
investigator review before submission.

Detailed release evidence:
[validation snapshot](../github_release/alignment-assessment-pilot/docs/RELEASE_VALIDATION_2026-11-16.json),
[inventory](../github_release/alignment-assessment-pilot/release_manifest.json),
[ZIP receipt](../github_release/alignment-assessment-pilot-2026-11-16.receipt.json).

## Final package verification

The export inventory covers 53 files totaling 2,020,945 bytes, excluding the
manifest itself and the two live reporting files. The ZIP is 1,397,755 bytes;
its SHA256 is `0b197d5b09e7d90269cd7ffe770d9dd30ac67fcbef264e6c6796e956f3c5ea90`.
The bounded scan found no machine paths or matching credential patterns.
After the sealer exited, a separate process extracted the ZIP, passed its CRC
checks, verified its receipt hash and all 53 inventory entries, and confirmed
that the exported program and tests are byte-identical to the relocated tested
copy. [Post-exit verification](../github_release/alignment-assessment-pilot-2026-11-16.post_exit_verification.json).
All local Markdown links across the final export and this report resolve;
`git diff --check` passes for tracked workspace changes. No remote operation
or public posting occurred.
