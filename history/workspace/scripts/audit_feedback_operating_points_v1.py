"""Retrospective saved-output audit; no new simulation or acceptance criterion."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
STUDY=ROOT/'results/published_circuit_comparison_v1'


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
    return h.hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True);args=p.parse_args()
    output=(ROOT/args.output).resolve();output.relative_to(ROOT)
    assert not output.exists()
    index=STUDY/'completion_v1/artifact_index.json'
    entries={e['path']:e for e in json.loads(index.read_text())['files']}
    maxima={r:dict(max_abs_rate=-1.) for r in ('hs','h2','bips','dnp15')}
    inspected=[]
    for path in sorted((STUDY/'cases').glob('*/intact.npz')):
        rel=str(path.relative_to(ROOT));entry=entries[rel]
        assert sha(path)==entry['sha256'] and path.stat().st_size==entry['size_bytes']
        with np.load(path,allow_pickle=False) as z:
            rate,roles=z['rate'],z['roles']
            assert rate.shape==(201,14)
            for role in maxima:
                m=float(np.max(abs(rate[:,roles==role])))
                if m>maxima[role]['max_abs_rate']:
                    maxima[role]=dict(max_abs_rate=m,case=path.parent.name,
                                     min_tanh_derivative_at_recorded_rates=1-m*m)
        inspected.append(entry)
    assert len(inspected)==44
    result=dict(status='SAVED_DATA_AUDIT_COMPLETE',date='2026-10-24',retrospective=True,
        prospective_scientific_gate=False,new_simulation=False,source_index_sha256=sha(index),
        scope='44 original intact direct-ray cases; all 201 recorded samples of 14 downstream cells; not all source nodes, intervening solver steps, other rooms or frontend nonlinearities',
        activation='signed tanh: range (-1,1), zero is baseline rather than a clipping boundary',
        derivative_identity='d tanh(x)/dx = 1 - rate**2 for active cells',
        per_role=maxima,source_files=inspected,
        interpretation='Saved downstream operating points are close to the linear origin; this does not support downstream tanh saturation as an explanation in this subset. Other proposed mechanisms remain untested.')
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_files'},indent=2))


if __name__=='__main__':main()
