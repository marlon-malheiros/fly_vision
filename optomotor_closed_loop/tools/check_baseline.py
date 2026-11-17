"""Read-only verification of the shipped baseline and exact source capsule."""
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def checked_path(relative):
    path = (ROOT / relative).resolve()
    if ROOT != path and ROOT not in path.parents:
        raise RuntimeError(f"Inventory escapes project root: {relative}")
    if not path.is_file():
        raise RuntimeError(f"Missing file: {relative}")
    return path


def verify():
    checks = 0
    manifest_path = ROOT / "release_manifest_r2.json"
    if not manifest_path.is_file():
        raise RuntimeError("The publication manifest is missing")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    paths = [entry["path"] for entry in manifest["files"]]
    if len(paths) != len(set(paths)):
        raise RuntimeError("Duplicate publication inventory entries")
    for entry in manifest["files"]:
        path = checked_path(entry["path"])
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != entry["sha256"] or path.stat().st_size != entry["bytes"]:
            raise RuntimeError(f"Publication inventory mismatch: {entry['path']}")
        checks += 1
    lock = json.loads((ROOT / "results/r2/before_test.json").read_text(encoding="utf-8"))
    for relative, expected in lock["sources"].items():
        if hashlib.sha256(checked_path(relative).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"Frozen R2 source differs: {relative}")
    receipt = json.loads((ROOT / "results/r2/arithmetic_review.json").read_text(encoding="utf-8"))
    for name, expected in receipt["artifact_hashes"].items():
        if hashlib.sha256(checked_path("results/r2/" + name).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"R2 evidence differs: {name}")
    capsule = json.loads((ROOT / "results/v1/source_bytes.json").read_text(encoding="utf-8"))
    for name, record in capsule["files"].items():
        data = base64.b64decode(record["base64"], validate=True)
        if hashlib.sha256(data).hexdigest() != record["sha256"]:
            raise RuntimeError(f"V1 source capsule differs: {name}")
    print(f"PASS: {checks} publication files, {len(lock['sources'])} frozen R2 inputs, "
          f"{len(receipt['artifact_hashes'])} R2 artifacts and {len(capsule['files'])} original V1 sources")
    return {"publication_files": checks, "frozen_r2_inputs": len(lock["sources"]), "v1_capsule_files": len(capsule["files"])}


if __name__ == "__main__":
    verify()
