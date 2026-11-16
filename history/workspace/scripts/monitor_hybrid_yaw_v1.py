"""Replay the portable online detector from neural/reference arrays, without labels."""
import argparse
import json
from pathlib import Path
import numpy as np
from male_optic_frontend.hybrid_yaw_monitor_v1 import HybridYawMonitor

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--network',type=Path,required=True)
    parser.add_argument('--reference',type=Path,required=True)
    parser.add_argument('--speed',type=float,choices=[5.5,11.,16.5],required=True)
    parser.add_argument('--model',type=Path,default=ROOT/'configs/agreement_yaw_model_v1.json')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();model=json.loads(args.model.read_text())
    fit=next(row['fitted'] for row in model['readouts'] if row['speed']==args.speed)
    monitor=HybridYawMonitor(fit,model['confirmation'])
    with np.load(args.network,allow_pickle=False) as z:net={k:z[k] for k in z.files}
    with np.load(args.reference,allow_pickle=False) as z:ref={k:z[k] for k in z.files}
    cells=[np.flatnonzero((net['roles']=='dnp15')&(net['sides']==side)) for side in ('L','R')]
    assert all(len(c)==1 for c in cells)
    rows=[];j=0
    for i,t in enumerate(net['time_s']):
        while j<len(ref['time_s']) and ref['time_s'][j]<t-1e-12:j+=1
        image=float(ref['yaw_deg_s'][j]) if j<len(ref['time_s']) and abs(ref['time_s'][j]-t)<1e-10 else None
        rows.append(monitor.push(float(t),float(net['rate'][i,cells[0][0]]),float(net['rate'][i,cells[1][0]]),image))
    arrays={field:np.array([np.nan if row[field] is None else row[field] for row in rows])
            for field in ('neural_deg_s','image_deg_s','support')}
    arrays.update(time_s=net['time_s'],ready=np.array([row['ready'] for row in rows]),
                  decision=np.array([row['decision'] if row['ready'] else 0 for row in rows],np.int8))
    with args.output.open('xb') as f:np.savez_compressed(f,**arrays)
    print(json.dumps(dict(samples=len(rows),ready=int(arrays['ready'].sum()),
        positive_callbacks=int(np.sum(arrays['decision']==1)),negative_callbacks=int(np.sum(arrays['decision']==-1)),
        output=str(args.output),movement_labels_used=False)))


if __name__=='__main__':main()
