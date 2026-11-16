"""Run the selected hybrid on fresh worlds without changing frozen physics."""
from __future__ import annotations
import argparse
from concurrent.futures import ProcessPoolExecutor,as_completed
import multiprocessing
from pathlib import Path
import shutil
import time
import traceback
import numpy as np
import agreement_yaw_v1 as g
from male_optic_frontend.agreement_yaw_v1 import agreement,encode_retina,decode_retina
from male_optic_frontend.hybrid_yaw_monitor_v1 import HybridYawMonitor

RUN,ROOT,CFG=g.RUN,g.ROOT,g.CFG
engine=g.neural.engine


def source_files():
    return g.sources()+[Path(__file__),ROOT/'scripts/review_agreement_yaw_v1.py',
        ROOT/'src/male_optic_frontend/hybrid_yaw_monitor_v1.py',ROOT/'tests/test_hybrid_yaw_monitor_v1.py',
        ROOT/'configs/agreement_yaw_model_v1.json',ROOT/'scripts/monitor_hybrid_yaw_v1.py']


def save_arrays(path,**arrays):
    path=Path(path)
    if path.name!='retina.npz':return g.save(path,**arrays)
    frames=arrays.pop('frames')
    g.save(path.with_name('retina_metadata.npz'),shape=np.array(frames.shape),**arrays)
    with path.with_name('retina_xor.zlib').open('xb') as f:f.write(encode_retina(frames))


def retina(folder):
    values=g.load(folder/'retina_metadata.npz');shape=values.pop('shape')
    values['frames']=decode_retina((folder/'retina_xor.zlib').read_bytes(),shape)
    return values


def initialize():
    engine.RUN=RUN;engine.CFG=RUN/'simulation_config.json';engine.MODEL.clear();engine.initialize();engine.save=save_arrays
    assert engine.RUN==RUN and engine.MODEL['cfg']['image_dt_s']==.005


def execute(task):
    engine.MODEL['cfg']['end_s']=task['plan']['end_s']
    return engine.execute(task)


def prepare():
    cfg=g.read(CFG);selected=g.read(RUN/'selection.json')['selected_confirmation'];assert selected is not None
    assert shutil.disk_usage(ROOT).free>=cfg['minimum_free_disk_bytes']
    parent={e['path']:e for e in g.read(g.W/'completion_v1/artifact_index.json')['files']}
    inputs=[]
    def archived(p):
        e=g.record(p);assert e==parent[e['path']];inputs.append(e)
    for name in ('renderer.so','neural.so','neural_strict.so'):
        p=g.W/'methods'/name;archived(p);shutil.copyfile(p,RUN/'methods'/name)
    sim=g.read(ROOT/'configs/ongoing_walking_yaw_v1.json');g.write(RUN/'simulation_config.json',sim)
    scenes=[];plans=[];seeds=set();inventories=[]
    for p in sorted((ROOT/'results').glob('*/scenes.json')):
        values=g.read(p)
        if isinstance(values,list):
            seeds.update(s['seed'] for s in values if isinstance(s,dict) and 'seed' in s);inventories.append(g.record(p))
    for i in range(cfg['test_rooms']):
        seed=cfg['test_seed_start']+i;assert seed not in seeds
        rng=np.random.default_rng(seed);ext=rng.uniform([65,26,30],[85,40,55])
        spheres=[[float(rng.uniform(25,55)),float((-1 if j%2 else 1)*rng.uniform(10,21)),float(rng.uniform(2,5)),float(rng.uniform(1.5,3.5))]
                 for j in range(3 if i%2 else 0)]
        scene=dict(id=f'{cfg["test_prefix"]}{i:02}',seed=seed,split='held_out',spheres=spheres,
                   bounds_mm=[[-float(ext[0]),float(ext[0])],[-float(ext[1]),float(ext[1])],[0,float(ext[2])]])
        scenes.append(scene);world=engine.world(scene,'A');g.write(RUN/'worlds'/f'{world["id"]}.json',world)
        for speed,yaw in [(0.,0.)]+[(v,y) for v in cfg['speeds_mm_s'] for y in cfg['yaw_deg_s']]:
            plans.append(dict(scene=scene['id'],world=world['id'],split='held_out',speed=speed,yaw=yaw,
                key=f'{scene["id"]}_v{speed:g}_y{yaw:+g}',end_s=cfg['turn_end_s'] if yaw else cfg['straight_end_s']))
    g.write(RUN/'scenes.json',scenes);g.write(RUN/'plans.json',plans)
    g.write(RUN/'seed_audit.json',dict(prior_distinct_seeds=len(seeds),inventories=inventories,fresh_seeds_disjoint=True))
    for key in ('w00_A','w01_A'):
        p=g.W/'worlds'/f'{key}.json';archived(p);shutil.copyfile(p,RUN/'worlds'/p.name)
    g.write(RUN/'simulation_inputs.json',dict(files=inputs,frozen_parent_files=g.read(g.P/'before_development.json')['files']))
    g.write(RUN/'before_parity.json',dict(utc=g.utc(),files=[g.record(p) for p in source_files()+[RUN/'simulation_config.json',RUN/'simulation_inputs.json']]))
    print('Prepared 384 fresh plans; no new-room images generated',flush=True)


def parity():
    initialize();(RUN/'parity').mkdir(exist_ok=False);checks=[]
    for key in ('w00_v16.5_y+0','w01_v16.5_y-2'):
        p=next(p for p in g.read(g.W/'plans.json') if p['key']==key);p=dict(p,end_s=1.8 if not p['yaw'] else 1.25)
        folder=RUN/'parity'/key;execute(dict(plan=p,destination=str(folder)))
        old=g.W/'held_out'/(key+'_primary');a=retina(folder);b=g.load(old/'retina.npz');n=len(a['time_s'])
        for i in range(n):assert np.array_equal(a['frames'][a['frame_index'][i]],b['frames'][b['frame_index'][i]])
        for name in ('source.npz','network.npz','reference.npz'):
            x,y=g.load(folder/name),g.load(old/name)
            for field in x:
                if field=='final_state' and p['yaw']:continue
                expected=y[field][:len(x[field])] if field in ('time_s','drive','rate','yaw_deg_s','source','local_yaw_deg_s','weights') else y[field]
                exact=np.array_equal(x[field],expected,equal_nan=True) if x[field].dtype.kind not in 'US' else np.array_equal(x[field],expected)
                assert exact,(key,name,field)
        checks.append(dict(key=key,retinal_frames=n,all_shared_arrays_exact=True))
    g.write(RUN/'parity_review.json',dict(status='PASS',checks=checks,codec_lossless=True,simulation_prefix_unchanged=True))
    print('Historical raw arrays and lossless retina parity PASS',flush=True)


def control_streams(folder):
    # Keep the detector's prescribed 100-Hz callbacks when refining visual input.
    net=g.load(folder/'network.npz');ref=g.load(folder/'reference.npz')
    keep=np.flatnonzero(abs(net['time_s']/.01-np.round(net['time_s']/.01))<1e-8)
    net={k:v[keep] if k in ('time_s','rate') else v for k,v in net.items()}
    keep=np.flatnonzero(abs(ref['time_s']/.01-np.round(ref['time_s']/.01))<1e-8)
    t=ref['time_s'][keep];image=np.full(len(t),np.nan);raw=ref['yaw_deg_s'][keep]
    for i in range(9,len(t)):image[i]=np.mean(raw[i-9:i+1])
    _,features=g.neural.role_features(net,'dnp15')
    fit=next(f['fitted'] for f in g.read(g.W/'calibration/readouts.json') if (f['mode'],f['role'],f['speed'])==('change','dnp15',16.5))
    b=np.array(fit['coefficients']);ns=b[0]+((features-fit['center'])/fit['scale'])@b[1:]
    j=np.searchsorted(net['time_s'],t-1e-12);return t,ns[j],image,fit['threshold']


def numerics():
    cfg=g.read(CFG);count=g.read(RUN/'selection.json')['selected_confirmation'];checks=[]
    for yaw in (0.,-2.,2.):
        key=f'f00_v16.5_y{yaw:+g}';t,n,im,c=control_streams(g.P/'development'/(key+'_primary'))
        j=int(np.flatnonzero(t<1.2-1e-12)[-1]);base=agreement(n,im,c,count)[j]
        for profile in ('spatial','temporal'):
            ft,fn,fi,fc=control_streams(g.P/'controls'/(key+'_'+profile));k=int(np.flatnonzero(ft<1.2-1e-12)[-1])
            fine=agreement(fn,fi,fc,count)[k];error=abs(base-fine)
            decisions=(int(np.sign(base)) if abs(base)>1 else 0,int(np.sign(fine)) if abs(fine)>1 else 0)
            checks.append(dict(key=key,profile=profile,primary_margin=float(base),finer_margin=float(fine),margin_error=float(error),
                neural_error_deg_s=float(abs(n[j]-fn[k])),image_error_deg_s=float(abs(im[j]-fi[k])),decisions=decisions,
                passed=bool(error<=cfg['sampling_margin_tolerance'] and max(abs(n[j]-fn[k]),abs(im[j]-fi[k]))<=.2 and decisions[0]==decisions[1])))
    g.write(RUN/'numerical_review.json',dict(status='PASS' if all(r['passed'] for r in checks) else 'FAIL',checks=checks,
        clock='100 Hz for all readouts; refined visual/source trajectories sampled at common arrival times',
        inherited_solver=g.record(g.P/'numerical_review.json'),physiological_validation=False))
    print('Finite-case numerical checks:',all(r['passed'] for r in checks),flush=True)


def freeze_test():
    for name in ('development_review.json','parity_review.json','numerical_review.json'):assert g.read(RUN/name)['status']=='PASS'
    assert not any((RUN/'held_out').iterdir());g.verify(g.read(RUN/'before_development.json')['files']);g.verify(g.read(RUN/'before_parity.json')['files'])
    g.verify(g.read(RUN/'simulation_inputs.json')['frozen_parent_files'])
    files=source_files()+[RUN/n for n in ('simulation_config.json','simulation_inputs.json','selection.json','development_review.json',
        'numerical_review.json','parity_review.json','scenes.json','plans.json','seed_audit.json')]+list((RUN/'methods').iterdir())+list((RUN/'worlds').iterdir())
    g.write(RUN/'before_test.json',dict(utc=g.utc(),new_room_images_not_generated=True,files=[g.record(p) for p in files]))
    print('Selected detector and numerical checks frozen before fresh images',flush=True)


def run():
    g.verify(g.read(RUN/'before_test.json')['files']);results=[];failures=[];start=time.monotonic()
    tasks=[dict(plan=p,destination=str(RUN/'held_out'/(p['key']+'_primary'))) for p in g.read(RUN/'plans.json')]
    with ProcessPoolExecutor(max_workers=g.read(CFG)['workers'],mp_context=multiprocessing.get_context('spawn'),initializer=initialize) as pool:
        jobs={pool.submit(execute,t):t for t in tasks}
        for future in as_completed(jobs):
            try:results.append(future.result())
            except Exception:failures.append(dict(task=jobs[future],traceback=traceback.format_exc()))
            if (len(results)+len(failures))%8==0:print('fresh',len(results),'/',len(tasks),'failures',len(failures),flush=True)
    g.write(RUN/'held_out_complete.json',dict(status='FAIL' if failures else 'PASS',results=results,failures=failures,seconds=time.monotonic()-start))
    assert not failures


def monitor(folder):
    net=g.load(folder/'network.npz');ref=g.load(folder/'reference.npz');p=g.read(folder/'summary.json')['plan']
    if not p['speed']:return None
    fit=next(f['fitted'] for f in g.read(g.W/'calibration/readouts.json') if (f['mode'],f['role'],f['speed'])==('change','dnp15',p['speed']))
    obj=HybridYawMonitor(fit,g.read(RUN/'selection.json')['selected_confirmation']);out=[]
    ri=0
    for i,t in enumerate(net['time_s']):
        while ri<len(ref['time_s']) and ref['time_s'][ri]<t-1e-12:ri+=1
        image=float(ref['yaw_deg_s'][ri]) if ri<len(ref['time_s']) and abs(ref['time_s'][ri]-t)<1e-10 else None
        left=float(net['rate'][i,(net['roles']=='dnp15')&(net['sides']=='L')][0]);right=float(net['rate'][i,(net['roles']=='dnp15')&(net['sides']=='R')][0])
        out.append(obj.push(float(t),left,right,image))
    return net['time_s'],out


def analyze():
    g.verify(g.read(RUN/'before_test.json')['files']);rows=[];selected=g.read(RUN/'selection.json')['selected_confirmation']
    (RUN/'streams').mkdir(exist_ok=False)
    online_error=0.;online_samples=0
    for folder in sorted((RUN/'held_out').iterdir()):
        p,t,n,i,c=g.streams(folder)
        values={'hybrid':agreement(n,i,c,selected),'neural':n/c,'image':i} if p['speed'] else {'hybrid':np.full(len(t),np.nan),'neural':np.full(len(t),np.nan),'image':i}
        idx=int(np.flatnonzero(t<1.2-1e-12)[-1]);mask=(t>=1.-1e-12)&(t<1.8-1e-12)
        for method,stream in values.items():
            value=float(stream[idx]) if np.isfinite(stream[idx]) else None
            rows.append(dict(**p,method=method,support=value,decision=None if value is None else int(np.sign(value)) if abs(value)>1 else 0,
                pre_support=float(stream[int(np.flatnonzero(t<1.-1e-12)[-1])]) if p['speed'] else None,
                rolling_alarm=bool(np.any(abs(stream[mask])>1)) if not p['yaw'] and p['speed'] else None,
                rolling_undefined=bool(np.any(~np.isfinite(stream[mask]))) if not p['yaw'] and p['speed'] else None))
        g.save(RUN/'streams'/f'{p["key"]}.npz',time_s=t,neural=n,image=i,hybrid=values['hybrid'])
        result=monitor(folder)
        if result:
            times,online=result;where=np.searchsorted(times,t-1e-12)
            expected=values['hybrid'];actual=np.array([np.nan if online[j]['support'] is None else online[j]['support'] for j in where])
            assert np.array_equal(np.isfinite(expected),np.isfinite(actual))
            err=float(np.max(abs(expected[np.isfinite(expected)]-actual[np.isfinite(actual)])));assert err<1e-10
            online_error=max(err,online_error);online_samples+=len(t)
    g.write(RUN/'analysis/predictions.json',rows);curves=[]
    for method in ('hybrid','neural','image'):
        for speed in g.read(CFG)['speeds_mm_s']:
            rr=[r for r in rows if (r['method'],r['speed'])==(method,speed)];zero=[r for r in rr if r['yaw']==0]
            false=sum(r['decision'] is None or r['decision']!=0 for r in zero);rolling=sum(r['rolling_alarm'] or r['rolling_undefined'] for r in zero)
            for mag in (2.,5.):
                turns=[r for r in rr if abs(r['yaw'])==mag];det=sum(r['decision'] is not None and r['decision']!=0 for r in turns)
                sign=sum(r['support'] is not None and r['support']*r['yaw']>0 for r in turns);joint=sum(r['decision'] is not None and r['decision']*r['yaw']>0 for r in turns)
                missing=sum(r['support'] is None for r in zero+turns);passed=bool(det>=39 and sign>=39 and false<=2 and rolling<=2 and not missing)
                curves.append(dict(method=method,speed=speed,magnitude=mag,detected=det,turns=48,raw_sign_correct=sign,joint_correct_detected=joint,
                    false_positives=false,straight=24,rolling_alarm_rooms=rolling,undefined=missing,qualifies=passed))
    g.table(RUN/'analysis/curves.csv',curves)
    g.write(RUN/'online_review.json',dict(status='PASS',samples=online_samples,maximum_error=online_error,no_event_or_true_velocity_inputs=True))
    conclusion={m:all(c['qualifies'] for c in curves if c['method']==m) for m in ('hybrid','neural','image')}
    g.write(RUN/'analysis/conclusion.json',dict(capability_by_method=conclusion,physiological_validation=False))
    figures(curves);print(conclusion,flush=True)


def figures(curves):
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,4,figsize=(15,4),layout='constrained')
    for method,label,color in (('neural','Neural change only','#7030a0'),('image','Image estimate only','#007a87'),('hybrid','Agreement detector','#222222')):
        cc=[c for c in curves if c['method']==method and c['magnitude']==2]
        for ax,key,den in zip(axes,('detected','raw_sign_correct','false_positives','rolling_alarm_rooms'),(48,48,24,24)):
            ax.plot([c['speed'] for c in cc],[100*c[key]/den for c in cc],'-o',color=color,label=label)
    for ax,title,gate in zip(axes,('±2°/s detected by 200 ms','Raw direction correct','Endpoint straight alarms','Any rolling straight alarm'),(80,80,10,10)):
        ax.axhline(gate,ls='--',color='gray');ax.set(title=title,xlabel='Walking speed (mm/s)',ylabel='Observed trials/rooms (%)',ylim=(-2,105));ax.grid(alpha=.2)
    axes[0].legend(fontsize=8)
    for ext in ('png','pdf'):fig.savefig(RUN/f'figures/fresh_agreement.{ext}',dpi=170)
    plt.close(fig)


def replay():
    initialize();checks=[]
    for key in ('c00_v16.5_y+0','c01_v16.5_y-2','c02_v5.5_y+2','c03_v11_y+5'):
        p=next(p for p in g.read(RUN/'plans.json') if p['key']==key);dest=RUN/'replay'/key
        execute(dict(plan=p,destination=str(dest)));old=RUN/'held_out'/(key+'_primary');count=0
        for name in ('source.npz','network.npz','reference.npz'):
            a,b=g.load(dest/name),g.load(old/name)
            for field in a:
                exact=np.array_equal(a[field],b[field],equal_nan=True) if a[field].dtype.kind not in 'US' else np.array_equal(a[field],b[field])
                assert exact,(key,name,field);count+=1
        a,b=retina(dest),retina(old)
        for field in a:assert np.array_equal(a[field],b[field]);count+=1
        assert (dest/'retina_xor.zlib').read_bytes()==(old/'retina_xor.zlib').read_bytes()
        checks.append(dict(key=key,arrays=count,codec_payload_exact=True))
    g.write(RUN/'reproduction_review.json',dict(status='PASS',checks=checks))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('stage',choices=['prepare','parity','numerics','freeze_test','run','analyze','replay']);args=parser.parse_args();globals()[args.stage]()
