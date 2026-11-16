"""Optional child-process OpenMP placement; no neural parameters are modified."""
from __future__ import annotations
import argparse
import os
from pathlib import Path


def topology(allowed=None, *, sys_root=Path('/sys/devices/system/cpu')):
    allowed=sorted(os.sched_getaffinity(0) if allowed is None else allowed)
    rows=[]
    for cpu in allowed:
        base=Path(sys_root)/f'cpu{cpu}'
        row=dict(cpu=int(cpu))
        for field in ('physical_package_id','core_id'):
            row[field]=int((base/'topology'/field).read_text())
        path=base/'cpufreq/cpuinfo_max_freq'
        row['declared_max_frequency_khz']=int(path.read_text()) if path.exists() else None
        rows.append(row)
    return rows


def validate_cpus(cpus, rows):
    if len(cpus)!=4 or any(isinstance(c,bool) or not isinstance(c,int) or c<0 for c in cpus) or len(set(cpus))!=4:
        raise ValueError('Require four different nonnegative logical CPU numbers')
    lookup={r['cpu']:r for r in rows}
    if not set(cpus)<=set(lookup):raise ValueError('Requested CPUs are outside the allowed topology')
    physical={(lookup[c]['physical_package_id'],lookup[c]['core_id']) for c in cpus}
    if len(physical)!=4:raise ValueError('Place workers on four distinct physical cores')
    return tuple(cpus)


def select_cpus(rows):
    representatives={}
    for row in sorted(rows,key=lambda r:r['cpu']):
        key=row['physical_package_id'],row['core_id']
        representatives.setdefault(key,row)
    if len(representatives)<4:raise ValueError('Four distinct allowed physical cores are required')
    candidates=list(representatives.values())
    if any(r['declared_max_frequency_khz'] is None or r['declared_max_frequency_khz']<=0 for r in candidates):
        raise ValueError('Missing declared frequency evidence; select explicit CPUs instead')
    candidates.sort(key=lambda r:(-r['declared_max_frequency_khz'],r['cpu']))
    return validate_cpus([r['cpu'] for r in candidates[:4]],rows)


def environment(mode,cpus,rows,base=None):
    if mode not in ('unbound','bound'):raise ValueError('Unknown placement profile')
    env=dict(os.environ if base is None else base)
    for key in ('OMP_PLACES','GOMP_CPU_AFFINITY'):env.pop(key,None)
    env.update(OMP_NUM_THREADS='4',OMP_WAIT_POLICY='ACTIVE',OMP_DYNAMIC='FALSE',OPENBLAS_NUM_THREADS='1')
    if mode=='bound':
        cpus=validate_cpus(list(cpus),rows)
        env.update(OMP_PROC_BIND='TRUE',OMP_PLACES=','.join('{'+str(c)+'}' for c in cpus))
    else:env['OMP_PROC_BIND']='FALSE'
    return env


def thread_masks():
    result=[]
    for path in sorted(Path('/proc/self/task').iterdir(),key=lambda p:int(p.name)):
        try:
            tid=int(path.name);result.append(dict(tid=tid,name=(path/'comm').read_text().strip(),cpus=sorted(os.sched_getaffinity(tid))))
        except (FileNotFoundError,ProcessLookupError):continue
    return result


def check_masks(records,mode,cpus,allowed):
    masks=sorted(r['cpus'] for r in records)
    expected=sorted([[c] for c in cpus]) if mode=='bound' else [sorted(allowed)]*4
    if masks!=expected:raise RuntimeError(f'Observed worker masks {masks}; expected {expected}')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--mode',choices=['unbound','bound'],default='unbound')
    p.add_argument('--cpus',help='Four comma-separated CPUs; required for explicit bound launch')
    p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
    command=a.command[1:] if a.command and a.command[0]=='--' else a.command
    if not command:p.error('Supply a command after --')
    if a.mode=='bound' and a.cpus is None:p.error('Bound launch requires an explicit --cpus list')
    try:cpus=[] if a.cpus is None else [int(c) for c in a.cpus.split(',')]
    except ValueError:p.error('CPU numbers must be integers')
    rows=topology();env=environment(a.mode,cpus,rows)
    os.execvpe(command[0],command,env)


if __name__=='__main__':main()
