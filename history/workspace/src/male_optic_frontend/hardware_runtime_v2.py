"""Compiled-frontend runtime and the original episode-based scientific readout.

The episode decoder requires the original response window and known speed. It
does not constitute an instantaneous steering command or a biological decoder.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from .hardware_runtime_v1 import HardwareRuntime
from .deployment_frontend_v2 import DeploymentFrontend,build_frontend
from .streaming_v1 import build_library
from .yaw_sensitivity_v1 import predict_signed


class EpisodeYawReadout:
    def __init__(self,models,roles,sides,known_speed,*,window=(.7,1.4),sample_dt=.01):
        self.models={r['role']:r for r in models if r.get('variant')=='intact' and r['speed']==known_speed}
        if set(self.models)!=set(('hs','h2','bips','dnp15')):
            raise ValueError('A sealed intact readout for the supplied speed is required')
        self.roles=np.asarray(roles);self.sides=np.asarray(sides)
        self.window=tuple(window);self.sample_dt=float(sample_dt)
        # Reproduce the *executed* legacy mask, including its float-clock endpoint.
        # At 10 ms, arange(141)[140]*.01 is 1.4000000000000001 and was excluded.
        clock=np.arange(int(round(window[1]/sample_dt))+1)*sample_dt
        self.window_indices=set(np.flatnonzero((clock>=window[0])&(clock<=window[1])).tolist())
        self.expected=len(self.window_indices)
        self.reset()

    def reset(self):self.samples=[];self.times=[];self.result=None;self.last_time=None

    def step(self,time_s,rates):
        rates=np.asarray(rates,float)
        if rates.shape!=self.roles.shape or not np.isfinite(rates).all():raise ValueError('Invalid neural rates')
        if not np.isfinite(time_s) or (self.last_time is not None and time_s<=self.last_time):raise ValueError('Readout timestamps must increase')
        index=round(time_s/self.sample_dt)
        if not np.isclose(index*self.sample_dt,time_s,atol=1e-12,rtol=0):raise ValueError('Readout must use the declared sample clock')
        if index in self.window_indices:
            if self.times and not np.isclose(time_s-self.times[-1],self.sample_dt,atol=1e-12,rtol=0):
                raise ValueError('Incomplete response window')
            self.samples.append(rates.copy());self.times.append(float(time_s))
        self.last_time=float(time_s)
        if self.result is None and time_s>=self.window[1]-1e-12:
            if len(self.samples)!=self.expected or not np.isclose(self.times[0],min(self.window_indices)*self.sample_dt,atol=1e-12,rtol=0):
                raise ValueError('The complete original response window is required')
            average=np.mean(self.samples,axis=0);self.result={}
            for role,model in self.models.items():
                feature=np.array([[average[(self.roles==role)&(self.sides==side)].mean() for side in ('L','R')]])
                score,decision=predict_signed(feature,model)
                self.result[role]=dict(score_deg_s=float(score[0]),decision=int(decision[0]),cutoff=model['threshold'])
            return self.result
        return None


class HardwareRuntimeV2(HardwareRuntime):
    def __init__(self,model_directory,neural_library,frontend_library,*,solver_dt=.001,known_speed=None):
        super().__init__(model_directory,neural_library,solver_dt=solver_dt)
        graph_parameters=json.loads((Path(model_directory)/'graph/graph.json').read_text())['parameters']
        if self.metadata['parameters']!=graph_parameters:
            raise ValueError('Runtime parameters differ from the preserved graph declaration')
        # Integral clocks are required before accepting any sensor data.
        stride=round(self.input_dt/self.frontend_dt)
        steps=round(self.input_dt/solver_dt)
        if stride<1 or steps<1 or not np.isclose(stride*self.frontend_dt,self.input_dt,rtol=0,atol=1e-12) or not np.isclose(steps*solver_dt,self.input_dt,rtol=0,atol=1e-12):
            raise ValueError('Deployment clocks must be commensurate')
        self.frontend=DeploymentFrontend(self.metadata['frontend'],self.metadata['targets'],frontend_library)
        self.readout=None
        if known_speed is not None:
            models=json.loads((Path(model_directory)/'decoders.json').read_text())
            self.readout=EpisodeYawReadout(models,self.circuit.graph['roles'][self.circuit.wide],
                self.circuit.graph['sides'][self.circuit.wide],known_speed)
        self.last_detection=None

    def reset(self):
        super().reset()
        if self.readout is not None:self.readout.reset()
        self.last_detection=None

    def step(self,timestamp,left,right):
        rate=super().step(timestamp,left,right)
        if rate is not None and self.readout is not None:
            detection=self.readout.step(timestamp,rate)
            if detection is not None:self.last_detection=detection
        return rate


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['build','replay']);parser.add_argument('--model',type=Path,required=True)
    parser.add_argument('--neural-library',type=Path);parser.add_argument('--frontend-library',type=Path)
    parser.add_argument('--frames',type=Path);parser.add_argument('--output',type=Path)
    parser.add_argument('--solver-dt',type=float,default=.001);parser.add_argument('--known-speed',type=float)
    parser.add_argument('--approximate-activation',action='store_true')
    args=parser.parse_args()
    neural=args.neural_library or args.model/'neural_core.so';front=args.frontend_library or args.model/'frontend_core.so'
    if args.action=='build':
        first=build_library(neural,approximate_activation=args.approximate_activation)
        second=build_frontend(front)
        print(json.dumps(dict(neural=first,frontend=second)));return
    if args.frames is None or args.output is None:parser.error('replay requires --frames and --output')
    if args.output.exists():raise FileExistsError(args.output)
    runtime=HardwareRuntimeV2(args.model,neural,front,solver_dt=args.solver_dt,known_speed=args.known_speed)
    rate=[];recorded=[];latency=[]
    with np.load(args.frames,allow_pickle=False) as z:
        for t,l,r in zip(z['time_s'],z['retina_L'],z['retina_R'],strict=True):
            start=time.perf_counter();value=runtime.step(float(t),l,r);latency.append(time.perf_counter()-start)
            if value is not None:rate.append(value);recorded.append(t)
    with args.output.open('xb') as f:
        np.savez_compressed(f,time_s=np.array(recorded),rate=np.array(rate),processing_latency_s=np.array(latency),
            body_ids=runtime.circuit.graph['body_ids'][runtime.circuit.wide],final_state=runtime.circuit.state,
            episode_detection_json=np.array(json.dumps(runtime.last_detection)))
    print(json.dumps(dict(frames=len(latency),neural_samples=len(rate),episode_detection=runtime.last_detection,
                          physical_camera_validated=False,solver_dt=args.solver_dt)))


if __name__=='__main__':main()
