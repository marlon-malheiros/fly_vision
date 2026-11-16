"""Acquire immutable MaleCNS v1.0 flat tables and extract the OMR subgraph.

Run with the isolated CPython reader under .data_runtime/python/python.exe.
The model itself uses the normal scientific Python environment.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import time
import urllib.request
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.feather as feather
import pyarrow.ipc as ipc

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://storage.googleapis.com/flyem-male-cns/v1.0/connectome-data/flat-connectome/"
SOURCES = {
    "annotations": ("body-annotations-male-cns-v1.0-minconf-0.5.feather", 14483314,
                    "2177e246113e4cfbf1e7772ec37c6da1955ff22e8063d0b1f833101f99a9a3b2"),
    "transmitters": ("body-neurotransmitters-male-cns-v1.0.feather", 43282834,
                     "95c9289220663abeb3409f3ad9e5a7f8a53f8093f5139d15502cd08da8879621"),
    "weights": ("connectome-weights-male-cns-v1.0-minconf-0.5.feather", 1051241946,
                "e35da783d1c686b2b58b3b87cd6a403ae43bfcfba8bff28e08ef752c1a56afc1"),
}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def acquire(key):
    name, expected_bytes, expected_hash = SOURCES[key]
    path = ROOT / "data/raw" / name
    if not path.exists():
        temporary = path.with_suffix(".partial")
        print(f"Downloading {key}: {expected_bytes / 1e6:.1f} MB", flush=True)
        started = time.monotonic()
        with urllib.request.urlopen(BASE + name, timeout=60) as response, temporary.open("wb") as target:
            while block := response.read(4 * 1024 * 1024):
                target.write(block)
        temporary.rename(path)
        print(f"Download finished in {time.monotonic() - started:.1f} s", flush=True)
    digest = hashlib.file_digest(path.open("rb"), "sha256").hexdigest()
    if path.stat().st_size != expected_bytes or digest != expected_hash:
        raise RuntimeError(f"Source integrity failure: {name}; observed SHA256 {digest}")
    return path


def admit():
    path = acquire("annotations")
    table = feather.read_table(path)
    print("Annotation schema:", table.schema, flush=True)
    rows = table.to_pylist()
    counts = {}
    matches = []
    for row in rows:
        kind = str(row.get("type") or "")
        if re.match(r"^(?:HS|H2|PS321|bIPS|DNp15|uLPTCrn|LPi12|LPi21|T4|T5)", kind):
            counts[kind] = counts.get(kind, 0) + 1
            if not kind.startswith(("T4", "T5")):
                matches.append(row)
    write_json(ROOT / "data/derived/annotation_admission.json", {
        "source": str(path.name), "counts": counts, "central_candidates": matches,
        "columns": table.column_names, "n_annotation_rows": len(rows),
    })
    print("Candidate type counts:", json.dumps(counts, indent=2), flush=True)
    print("First central metadata rows:", json.dumps(matches[:5], indent=2), flush=True)
    return rows


CORE_TYPES = {"HSN", "HSE", "HSS", "HST", "H2", "PS321", "DNp15", "LPi12", "LPi21"}
INPUT_TYPES = {"T4a", "T4b", "T5a", "T5b"}


def extract():
    annotation_path = acquire("annotations")
    rows = feather.read_table(annotation_path).to_pylist()
    selected = [r for r in rows if r["status"] == "Traced" and r.get("type") in CORE_TYPES | INPUT_TYPES]
    central = sorted([r for r in selected if r["type"] in CORE_TYPES], key=lambda r: r["bodyId"])
    inputs = sorted([r for r in selected if r["type"] in INPUT_TYPES], key=lambda r: r["bodyId"])
    for kind in CORE_TYPES | INPUT_TYPES:
        if not any(r["type"] == kind for r in selected):
            raise RuntimeError(f"Missing required cell type: {kind}")
    nt_path = acquire("transmitters")
    nt_table = feather.read_table(nt_path)
    print("Neurotransmitter schema:", nt_table.schema, flush=True)
    selected_nt = nt_table.filter(pc.is_in(nt_table["body"], value_set=pa.array([r["bodyId"] for r in selected], type=pa.int64())))
    nt_rows = selected_nt.to_pylist()
    nt_map = {r["body"]: r for r in nt_rows}
    for row in selected:
        row["transmitter_prediction"] = nt_map.get(row["bodyId"], {})
    write_json(ROOT / "data/derived/selected_neurons.json", {"central": central, "inputs": inputs})
    print("Selected", len(central), "central neurons and", len(inputs), "horizontal motion inputs", flush=True)
    weights_path = acquire("weights")
    core_ids = np.array([r["bodyId"] for r in central], dtype=np.int64)
    input_ids = np.array([r["bodyId"] for r in inputs], dtype=np.int64)
    total_incoming = np.zeros(len(central), dtype=np.int64)
    total_outgoing = np.zeros(len(central), dtype=np.int64)
    rows_scanned = 0
    edges, feedback, recurrent_inputs = [], [], 0
    reader = ipc.open_file(str(weights_path))
    print("Weight schema:", reader.schema, "record batches", reader.num_record_batches, flush=True)
    names = reader.schema.names
    pre_name = next(n for n in ("body_pre", "bodyId_pre", "pre") if n in names)
    post_name = next(n for n in ("body_post", "bodyId_post", "post") if n in names)
    weight_name = next(n for n in ("weight", "syn_count", "syn_count_total") if n in names)
    for bi in range(reader.num_record_batches):
        batch = reader.get_batch(bi)
        pre = batch.column(names.index(pre_name)).to_numpy()
        post = batch.column(names.index(post_name)).to_numpy()
        weight = batch.column(names.index(weight_name)).to_numpy()
        rows_scanned += len(pre)
        mask = np.isin(post, core_ids)
        p, q, w = pre[mask], post[mask], weight[mask]
        np.add.at(total_incoming, np.searchsorted(core_ids, q), w)
        keep = np.isin(p, np.concatenate((core_ids, input_ids)))
        edges.extend(zip(p[keep].tolist(), q[keep].tolist(), w[keep].tolist()))
        outgoing = np.isin(pre, core_ids)
        np.add.at(total_outgoing, np.searchsorted(core_ids, pre[outgoing]), weight[outgoing])
        fb = outgoing & np.isin(post, input_ids)
        feedback.extend(zip(pre[fb].tolist(), post[fb].tolist(), weight[fb].tolist()))
        if bi % 100 == 0:
            print(f"Scanned {rows_scanned:,} source rows", flush=True)
    destination = ROOT / "data/derived"
    for name, values in (("chemical_edges.csv", edges), ("cut_feedback_edges.csv", feedback)):
        with (destination / name).open("w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(["body_pre", "body_post", "synapse_count"])
            writer.writerows(sorted(values))
    write_json(destination / "connectome_provenance.json", {
        "dataset": "MaleCNS v1.0", "source_page": "https://male-cns.janelia.org/download/",
        "license": "CC-BY-4.0", "source_files": {k: {"filename": v[0], "bytes": v[1], "sha256": v[2]} for k, v in SOURCES.items()},
        "central_types": sorted(CORE_TYPES), "input_types": sorted(INPUT_TYPES),
        "central_neurons": len(central), "input_neurons": len(inputs), "source_rows_scanned": rows_scanned,
        "retained_edges": len(edges), "retained_synapses": sum(e[2] for e in edges),
        "clamped_source_feedback_edges": len(feedback), "clamped_source_feedback_synapses": sum(e[2] for e in feedback),
        "central_boundary": [{"bodyId": int(b), "total_incoming_synapses": int(i), "total_outgoing_synapses": int(o),
                              "retained_incoming_synapses": sum(e[2] for e in edges if e[1] == b)}
                             for b, i, o in zip(core_ids, total_incoming, total_outgoing)],
        "scope": "Neuron-resolved central recurrent circuit. T4/T5 inputs are clamped functional camera-motion sources; their own recurrence and feedback dynamics are not simulated.",
        "not_biologically_validated": True,
    })
    print("Derived connectome extraction complete:", len(edges), "retained directed edges", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--admit", action="store_true")
    parser.add_argument("--extract", action="store_true")
    args = parser.parse_args()
    extract() if args.extract else admit()
