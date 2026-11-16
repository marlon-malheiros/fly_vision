# History archive guide

This archive is a dated export of the source project's progress log and
directly linked reports and compact technical artifacts. Its timeline has
536 chronological entries; its Git metadata has 265
parent-workspace commits. The commit list contains hashes, parents, dates and
subjects, not the full Git history, authors' email addresses or file diffs.
The source progress log may contain uncommitted work after the recorded Git HEAD.

## Files

- `workspace/docs/PROJECT_PROGRESS_REPORT_2026-11-16.md`: dated public snapshot.
- `timeline.jsonl`: one JSON object per progress section, preserving order, title,
  date and sanitized Markdown body; study status is not inferred automatically.
- `evidence_index.jsonl`: one object per directly referenced path, including
  availability, size and hashes for bundled files, and transformations.
- `git_commits.jsonl`: metadata for the parent workspace's first-parent-inclusive
  `git log HEAD` ancestry, in `git log --reverse HEAD` order; dates can be non-monotonic.
- `workspace/`: selected linked reports, structured outputs and figures, under
  their original relative paths.
- `history_manifest.json`: SHA256 inventory of this history export, independent
  of the frozen pilot's original `../release_manifest.json`.
- `build_history_archive_v1.py`: export method; regeneration requires the source
  workspace and a separate destination. Pass both `--workspace` and `--repository`.

The progress snapshot marks excluded links as `not bundled`. A bundled report
may itself refer to additional files not included here; consult the evidence
index and original workspace before assuming an archive is complete. Directories
are listed as local-only because this export does not copy their complete contents.
The source snapshot and other text files replace machine-specific workspace, home
and temporary prefixes with `<WORKSPACE>`, `<HOME>` and `<TEMP>`; per-file source
and exported hashes plus transformation counts are in the evidence index. These
are sanitized copies, not byte-identical records where transformations are listed.

The 2026-11-01 retirement of 2,823 old generated movies was intentional. The
retirement report, before-retirement list and ledger are included; original
indexes are historical manifests and are not evidence that retired files remain
available. No movies were regenerated for this export.

Historic reports document exploratory work, pre-analysis protocols, failures,
corrections and negative outcomes. Read each with its dates and limitations.
Reproducibility and integrity checks do not establish biological validity, neural
degeneracy, scientific novelty or publication acceptance.

## Source and license

This history contains original project-authored material and outputs derived from
third-party scientific datasets. MIT applies only to original code the author owns.
Data, figures, metadata and other third-party material retain their respective
source terms; source-specific rights are not overridden by the code license.
In particular, the Gruntman stimulus source is CC BY-NC 4.0 as documented in
`../NOTICE.md`. Raw recordings, bulk generated movies and oversized bundles are
not copied. Publication of this archive does not imply original authors' endorsement.

The progress snapshot has source SHA256 `0f013d8db2f73f1632095daa04efd70a351b1a1eff77e9fcd794700e221d711e`. The source workspace's
Git HEAD is `9b0ca8aebbe1303d27ce7dbcbdc9dffe5692f09c`. The exported snapshot
is not a scientific study or a change to a sealed source artifact.
