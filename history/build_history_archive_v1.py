"""Build a bounded, provenance-preserving public project-history archive.

Run from the source workspace with --repository pointing to an independent
publication checkout. Never edits a source study or its sealed artifacts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/PROJECT_PROGRESS_REPORT.md"
DATE = "2026-11-16"
TEXT_EXTENSIONS = {".md", ".json", ".jsonl", ".csv", ".py", ".txt", ".xml"}
BINARY_EXTENSIONS = {".png", ".pdf"}
MAX_FILE = 8 * 1024**2
TOTAL_CAP = 96 * 1024**2
DISK_RESERVE = 2 * 1024**3
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SENSITIVE = (
    re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(rb"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    re.compile(rb"\bAKIA[A-Z0-9]{16}\b"),
    re.compile(rb"(?i)(?:x-amz-signature|x-amz-credential|api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|authorization:\s*bearer)"),
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def text(path: Path, content: str) -> None:
    write(path, content.encode("utf-8"))


def json_bytes(value) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()


def jsonl_bytes(rows) -> bytes:
    return "".join(json.dumps(x, ensure_ascii=False, allow_nan=False) + "\n" for x in rows).encode()


def sanitize(data: bytes) -> tuple[bytes, dict]:
    transformations = {}
    for original, replacement, label in (
        (os.fsencode(str(ROOT)), b"<WORKSPACE>", "workspace_paths"),
        (os.fsencode(str(Path.home())), b"<HOME>", "home_paths"),
        (b"/tmp/", b"<TEMP>/", "temporary_paths"),
    ):
        count = data.count(original)
        if count:
            data = data.replace(original, replacement)
            transformations[label] = count
    return data, transformations


def safe(data: bytes, name: str) -> None:
    if any(pattern.search(data) for pattern in SENSITIVE):
        raise RuntimeError(f"Possible sensitive value or field in {name}; inspect before publishing")
    if b"/home/" in data or b"/tmp/" in data:
        raise RuntimeError(f"Unredacted machine path in {name}; inspect before publishing")


def parse_reference(raw: str):
    path_text, _, fragment = raw.partition("#")
    path_text = urllib.parse.unquote(path_text)
    if not path_text or urllib.parse.urlparse(path_text).scheme or path_text.startswith("//"):
        return None
    target = (SOURCE.parent / path_text).resolve()
    try:
        rel = target.relative_to(ROOT).as_posix()
    except ValueError:
        return {"source_path": "[outside source workspace]", "status": "outside_workspace"}
    return {"source_path": rel, "fragment": fragment, "target": target}


def select(item):
    rel, path = item["source_path"], item["target"]
    if path.is_dir():
        return "local_only_directory", "Directory contents not included as a complete archive"
    if not path.is_file():
        return "unavailable", "The linked path did not exist at export time"
    if rel == "AGENTS.md" or rel == "docs/PROJECT_PROGRESS_REPORT.md":
        return "live_file_excluded", "Live instructions and progress are outside immutable inventories"
    if rel.startswith(("data/", "github_release/")):
        return "local_only", "Raw/source data or a separate release is outside this history export"
    if path.suffix.lower() not in TEXT_EXTENSIONS | BINARY_EXTENSIONS:
        return "local_only", "Large binary, bundle, or unsupported file type"
    if path.stat().st_size > MAX_FILE:
        return "local_only", "Individual file exceeds the bounded 8 MiB export limit"
    return "included", ""


def main(repo: Path):
    repo = repo.resolve()
    history = repo / "history"
    if not (repo / ".git").exists() or not (repo / "release_manifest.json").is_file():
        raise RuntimeError("Expected the independent publication Git checkout")
    if history.exists() or (repo / "HISTORY.md").exists():
        raise RuntimeError("Refusing to replace an existing history archive")
    if shutil.disk_usage(repo).free < DISK_RESERVE + 2 * TOTAL_CAP:
        raise RuntimeError("Insufficient reserve for bounded archive and Git objects")
    original = SOURCE.read_bytes()
    source_text = original.decode("utf-8")
    references = {}
    for match in LINK.finditer(source_text):
        item = parse_reference(match.group(2))
        if item is not None:
            references.setdefault(item["source_path"], item)

    # Explicitly include the retirement evidence even if future source wording changes.
    for rel in ("docs/LEGACY_MOVIE_RETIREMENT_REPORT_V2.md",
                "results/legacy_movie_retirement_v2/before_retirement.json",
                "results/legacy_movie_retirement_v2/retirement.jsonl"):
        references.setdefault(rel, dict(source_path=rel, fragment="", target=ROOT / rel))

    ledger = []
    statuses = {}
    total = 0
    for rel, item in sorted(references.items()):
        if "target" not in item:
            ledger.append(dict(source_path=rel, status=item["status"]))
            statuses[rel] = item["status"]
            continue
        status, reason = select(item)
        statuses[rel] = status
        path = item["target"]
        row = dict(source_path=rel, status=status, reason=reason)
        if path.is_file():
            row["source_bytes"] = path.stat().st_size
        if status == "included":
            content = path.read_bytes()
            row["source_sha256"] = sha(content)
            if path.suffix.lower() in TEXT_EXTENSIONS:
                content, transforms = sanitize(content)
            else:
                transforms = {}
            safe(content, rel)
            target_rel = "history/workspace/" + rel
            row.update(archive_path=target_rel, archive_sha256=sha(content),
                       archive_bytes=len(content), transformations=transforms)
            total += len(content)
            if total > TOTAL_CAP:
                raise RuntimeError("History archive exceeds 96 MiB cap")
            write(repo / target_rel, content)
        ledger.append(row)

    def substitute(match):
        label, raw = match.group(1), match.group(2)
        item = parse_reference(raw)
        if item is None:
            return match.group(0)
        rel = item["source_path"]
        if statuses.get(rel) == "included":
            return match.group(0)
        # Preserve the original path as text, with an explicit availability label.
        return f"{label} (not bundled: `{rel}`)"

    updated = LINK.sub(substitute, source_text)
    snapshot, changes = sanitize(updated.encode())
    safe(snapshot, "progress snapshot")
    snapshot_rel = f"history/workspace/docs/PROJECT_PROGRESS_REPORT_{DATE}.md"
    text(repo / snapshot_rel,
         f"<!-- Public history copy: paths sanitized, unavailable links marked; source SHA256 {sha(original)}. -->\n\n"
         + snapshot.decode())

    sections = re.split(r"(?=^## )", snapshot.decode(), flags=re.MULTILINE)
    timeline = []
    for section in sections:
        if not section.startswith("## "):
            continue
        title, _, body = section.partition("\n")
        title = title[3:].strip()
        date_match = re.search(r"\b\d{4}-\d{2}-\d{2}\b", title)
        timeline.append(dict(order=len(timeline)+1, date=date_match.group(0) if date_match else None,
                             heading=title, body_markdown=body.strip()))
    write(history / "timeline.jsonl", jsonl_bytes(timeline))
    write(history / "evidence_index.jsonl", jsonl_bytes(ledger))

    git_format = "%H%x00%P%x00%aI%x00%s"
    log = subprocess.check_output(["git", "-C", str(ROOT), "log", "--reverse", f"--format={git_format}", "HEAD"])
    commits = []
    for line in log.splitlines():
        commit, parents, date, subject = line.decode().split("\0", 3)
        sanitized, _ = sanitize(subject.encode())
        safe(sanitized, "Git commit subject")
        commits.append(dict(commit=commit, parents=parents.split(), author_date=date, subject=sanitized.decode()))
    write(history / "git_commits.jsonl", jsonl_bytes(commits))
    write(history / "build_history_archive_v1.py", Path(__file__).read_bytes())

    overview = f'''# Development and experimental history\n\nThis archive adds the Fly Vision project's main development and experimental\nhistory through {DATE}. The initial README describes the earlier, pilot-only\nrelease; this archive was added afterwards. It does not add the full parent\nworkspace, all raw recordings, or the complete Git object history.\n\n- [Full dated project-progress snapshot]({snapshot_rel})\n- [Machine-readable timeline](history/timeline.jsonl)\n- [Machine-readable evidence index](history/evidence_index.jsonl)\n- [Machine-readable parent Git commit list](history/git_commits.jsonl)\n- [History archive guide](history/README.md)\n\nHistorical reports include failed tests, decisions, numerical corrections and\nexploratory findings. Read each result with its own protocol and limitations.\nNumerical checks are not biological validation, and later corrections do not\nretroactively become prospectively frozen rules.\n'''
    text(repo / "HISTORY.md", overview)
    guide = f'''# History archive guide\n\nThis archive is a dated export of the source project's progress log and\ndirectly linked reports and compact technical artifacts. Its timeline has\n{len(timeline)} chronological entries; its Git metadata has {len(commits)}\nparent-workspace commits. The commit list contains hashes, parents, dates and\nsubjects, not the full Git history, authors' email addresses or file diffs.\nThe source progress log may contain uncommitted work after the recorded Git HEAD.\n\n## Files\n\n- `workspace/docs/PROJECT_PROGRESS_REPORT_{DATE}.md`: dated public snapshot.\n- `timeline.jsonl`: one JSON object per progress section, preserving order, title,\n  date and sanitized Markdown body; study status is not inferred automatically.\n- `evidence_index.jsonl`: one object per directly referenced path, including\n  availability, size and hashes for bundled files, and transformations.\n- `git_commits.jsonl`: metadata for the parent workspace's first-parent-inclusive\n  `git log HEAD` ancestry, in reverse chronological order of the Git output.\n- `workspace/`: selected linked reports, structured outputs and figures, under\n  their original relative paths.\n- `history_manifest.json`: SHA256 inventory of this history export, independent\n  of the frozen pilot's original `../release_manifest.json`.\n- `build_history_archive_v1.py`: export method; regeneration requires the source\n  workspace and a separate destination. Pass both `--workspace` and `--repository`.\n\nThe progress snapshot marks excluded links as `not bundled`. A bundled report\nmay itself refer to additional files not included here; consult the evidence\nindex and original workspace before assuming an archive is complete. Directories\nare listed as local-only because this export does not copy their complete contents.\nThe source snapshot and other text files replace machine-specific workspace, home\nand temporary prefixes with `<WORKSPACE>`, `<HOME>` and `<TEMP>`; per-file source\nand exported hashes plus transformation counts are in the evidence index. These\nare sanitized copies, not byte-identical records where transformations are listed.\n\nThe 2026-11-01 retirement of 2,823 old generated movies was intentional. The\nretirement report, before-retirement list and ledger are included; original\nindexes are historical manifests and are not evidence that retired files remain\navailable. No movies were regenerated for this export.\n\nHistoric reports document exploratory work, pre-analysis protocols, failures,\ncorrections and negative outcomes. Read each with its dates and limitations.\nReproducibility and integrity checks do not establish biological validity, neural\ndegeneracy, scientific novelty or publication acceptance.\n\n## Source and license\n\nThis history contains original project-authored material and outputs derived from\nthird-party scientific datasets. MIT applies only to original code the author owns.\nData, figures, metadata and other third-party material retain their respective\nsource terms; source-specific rights are not overridden by the code license.\nIn particular, the Gruntman stimulus source is CC BY-NC 4.0 as documented in\n`../NOTICE.md`. Raw recordings, bulk generated movies and oversized bundles are\nnot copied. Publication of this archive does not imply original authors' endorsement.\n\nThe progress snapshot has source SHA256 `{sha(original)}`. The source workspace's\nGit HEAD is `{commits[-1]['commit'] if commits else 'none'}`. The exported snapshot\nis not a scientific study or a change to a sealed source artifact.\n'''
    # This records the command's output order without asserting a strict date ordering.
    guide = guide.replace("in reverse chronological order of the Git output", "in `git log --reverse HEAD` order; dates can be non-monotonic")
    text(history / "README.md", guide)
    safe(overview.encode(), "HISTORY.md")
    safe(guide.encode(), "history/README.md")
    manifest_files = [repo / "HISTORY.md"] + sorted(p for p in history.rglob("*") if p.is_file())
    manifest = []
    for p in manifest_files:
        data = p.read_bytes()
        # This program intentionally contains literal detection patterns, so scan
        # the exported content files rather than the scanner's own source text.
        if p.name != "build_history_archive_v1.py":
            safe(data, p.relative_to(repo).as_posix())
        manifest.append(dict(path=p.relative_to(repo).as_posix(), bytes=len(data), sha256=sha(data)))
    write(history / "history_manifest.json", json_bytes(dict(
        date=DATE, scope="History export; excludes live AGENTS and project progress",
        source_progress_sha256=sha(original), source_snapshot_transformations=changes,
        entry_count=len(timeline), parent_git_commits=len(commits),
        included_source_files=sum(r["status"] == "included" for r in ledger),
        reference_count=len(ledger), retained_bytes=sum(r["bytes"] for r in manifest), files=manifest)))
    print(json.dumps(dict(timeline_entries=len(timeline), git_commits=len(commits),
                          source_references=len(ledger), included=sum(r["status"] == "included" for r in ledger),
                          archived_bytes=total, inventory_files=len(manifest)), indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=ROOT,
                        help="Original source workspace; required when running the exported copy")
    parser.add_argument("--repository", type=Path, required=True)
    args = parser.parse_args()
    ROOT = args.workspace.resolve()
    SOURCE = ROOT / "docs/PROJECT_PROGRESS_REPORT.md"
    main(args.repository)
