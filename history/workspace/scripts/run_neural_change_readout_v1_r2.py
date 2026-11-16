"""Correct spawn-worker path initialization; retain the original failed run."""
import argparse
from concurrent.futures import ProcessPoolExecutor,as_completed
import multiprocessing
from pathlib import Path
import time
import traceback
import neural_change_readout_v1 as s

RUN=s.RUN
REV=RUN/'execution_revision_2'


def initialize():
    s.configure_engine();s.engine.initialize()
    assert s.engine.RUN==RUN and s.engine.CFG==s.CFG
    assert s.engine.MODEL['cfg']==s.read(s.CFG)
    assert (s.engine.RUN/'worlds/w00_A.json').is_file()


def probe():
    return dict(run=str(s.engine.RUN),configuration=s.record(s.engine.CFG),
                parameters_unchanged=True,new_world_present=(s.engine.RUN/'worlds/w00_A.json').is_file())


def prepare():
    failure=s.read(RUN/'held_out_complete.json')
    assert failure['status']=='FAIL' and not failure['results'] and len(failure['failures'])==384
    assert all('FileNotFoundError' in r['traceback'] and 'ongoing_walking_yaw_v1/worlds/w' in r['traceback'] for r in failure['failures'])
    assert not any(p.is_file() for p in (RUN/'held_out').rglob('*'))
    s.verify(s.read(RUN/'before_test.json')['files'])
    dest=RUN/'execution_failure_v1';dest.mkdir(exist_ok=False);REV.mkdir(exist_ok=False)
    (RUN/'held_out').rename(dest/'held_out');(RUN/'held_out_complete.json').rename(dest/'held_out_complete.json')
    (RUN/'held_out').mkdir()
    s.write(dest/'preservation.json',dict(original_episode_directory='held_out',renamed_to='execution_failure_v1/held_out',
        original_completion='held_out_complete.json',retained_completion='execution_failure_v1/held_out_complete.json',
        failed_jobs=384,successful_jobs=0,retinal_or_neural_arrays_written=0,
        reason='Spawned engine workers imported old default paths instead of parent process overrides'))
    s.write(REV/'before_execution.json',dict(utc=s.utc(),correction='Initialize paths and frozen configuration in every spawned worker',
        scientific_recipe_change=False,fresh_images_not_generated=True,
        files=[s.record(p) for p in (Path(__file__),RUN/'before_test.json',dest/'held_out_complete.json',dest/'preservation.json')]))
    print('Original 384 path failures preserved; inference and readouts unchanged',flush=True)


def worker_probe():
    s.verify(s.read(REV/'before_execution.json')['files'])
    with ProcessPoolExecutor(max_workers=2,mp_context=multiprocessing.get_context('spawn'),initializer=initialize) as pool:
        results=[f.result() for f in [pool.submit(probe) for _ in range(4)]]
    assert all(r['new_world_present'] for r in results)
    s.write(REV/'worker_probe.json',dict(status='PASS',results=results,no_rendering=True))
    print('Spawn-worker initialization probe PASS',flush=True)


def run():
    s.verify(s.read(REV/'before_execution.json')['files']);s.verify(s.read(RUN/'before_test.json')['files'])
    assert s.read(REV/'worker_probe.json')['status']=='PASS'
    assert not any((RUN/'held_out').iterdir())
    start=time.monotonic();results=[];failures=[]
    tasks=[dict(plan=p,destination=str(RUN/'held_out'/(p['key']+'_primary'))) for p in s.read(RUN/'plans.json')]
    with ProcessPoolExecutor(max_workers=s.read(s.CFG)['workers'],mp_context=multiprocessing.get_context('spawn'),initializer=initialize) as pool:
        pending={pool.submit(s.engine.execute,task):task for task in tasks}
        for future in as_completed(pending):
            try:results.append(future.result())
            except Exception:failures.append(dict(task=pending[future],traceback=traceback.format_exc()))
            if (len(results)+len(failures))%8==0:print('held_out R2',len(results),'/',len(tasks),'failures',len(failures),flush=True)
    s.write(RUN/'held_out_complete.json',dict(utc=s.utc(),status='FAIL' if failures else 'PASS',results=results,
        failures=failures,seconds=time.monotonic()-start,execution_revision=2,preserved_failed_attempt='execution_failure_v1/held_out_complete.json'))
    assert not failures


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('stage',choices=['prepare','worker_probe','run']);a=p.parse_args();globals()[a.stage]()
