"""Run with python -m alignment_assessment from the repository root."""
import argparse
import hashlib
import json
import platform
from pathlib import Path
import shutil
import sys
import time

from .reproduce import ROOT, optical, synthetic, write_json
from .review import review


def verify():
    manifest = json.loads((ROOT / "release_manifest.json").read_text())
    for row in manifest["files"]:
        path = ROOT / row["path"]
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"Missing or symlinked release file: {row['path']}")
        if path.stat().st_size != row["bytes"] or hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise RuntimeError(f"Release file changed: {row['path']}")
    return dict(passed=True, files_checked=len(manifest["files"]),
                scope="Shipped release files; live AGENTS.md and project progress excluded")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("verify", help="Check the release inventory and SHA256 values")
    replay = sub.add_parser("reproduce", help="Replay both checks and an independent review")
    replay.add_argument("--output", type=Path, default=Path("generated/replay"),
                        help="New directory; existing destinations are refused")
    args = parser.parse_args()
    integrity = verify()
    if args.command == "verify":
        print(json.dumps(integrity, indent=2))
        return
    output = args.output.resolve()
    if output == ROOT or ROOT in output.parents and output.relative_to(ROOT).parts[0] != "generated":
        parser.error("Outputs inside the repository must be under generated/")
    if output.exists():
        parser.error("Output already exists; choose a new directory to preserve previous runs")
    # Complete run estimate: < 1 minute, < 512 MiB RSS, < 8 MiB retained.
    if shutil.disk_usage(output.parent if output.parent.exists() else Path.cwd()).free < 1024**3:
        parser.error("Replay requires a 1 GiB free-space reserve")
    output.mkdir(parents=True)
    start = time.monotonic()
    try:
        import numpy
        import scipy
        result = dict(passed=False, integrity=integrity, python=platform.python_version(),
                      numpy=numpy.__version__, scipy=scipy.__version__,
                      optical=optical(output), synthetic=synthetic(output),
                      independent_review=review(output), biological_validation=False)
        size = sum(p.stat().st_size for p in output.iterdir() if p.is_file())
        if size > 8*1024**2:
            raise RuntimeError("Retained-output estimate exceeded")
        result.update(passed=True, wall_seconds=time.monotonic()-start, retained_bytes=size)
        write_json(output / "run_report.json", result)
        print(json.dumps(result, indent=2))
    except Exception as error:
        write_json(output / "failure.json", dict(passed=False, error_type=type(error).__name__,
                                               message=str(error)))
        raise


if __name__ == "__main__":
    main()
