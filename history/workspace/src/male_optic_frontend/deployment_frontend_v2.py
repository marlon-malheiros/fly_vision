"""Separate deployment acceleration; original scientific frontend stays frozen."""
from __future__ import annotations
import ctypes,subprocess
from pathlib import Path
import numpy as np
from .streaming_v1 import StreamingFrontend


def build_frontend(destination):
    destination=Path(destination)
    if destination.exists():raise FileExistsError(destination)
    destination.parent.mkdir(parents=True,exist_ok=True)
    command=['g++','-std=c++17','-O3','-fno-fast-math','-ffp-contract=off','-shared','-fPIC',
             str(Path(__file__).with_suffix('.cpp')),'-o',str(destination)]
    subprocess.run(command,check=True,capture_output=True,text=True)
    return command


class DeploymentFrontend(StreamingFrontend):
    def __init__(self,config,targets,library,grid=None):
        super().__init__(config,targets,grid)
        size=int(np.prod(self.grid.shape))
        self.delays=np.zeros((2,2,size));self.previous_contrasts=np.zeros_like(self.delays)
        self.side_index=np.zeros(len(targets),np.int32)
        self.routes=np.empty(len(targets),np.int32)
        self.vertices=np.empty((len(targets),4),np.int32)
        self.weights=np.empty((len(targets),4),float)
        for index,side in enumerate(('L','R')):
            item=self.sides[side];where=item['indices'];self.side_index[where]=index
            self.routes[where]=item['route'];self.vertices[where]=item['readout'].vertices
            self.weights[where]=item['readout'].weights
        self.lib=ctypes.CDLL(str(Path(library).resolve()));self.function=self.lib.optic_frontend
        array=np.ctypeslib.ndpointer;real=array(np.float64,flags='C_CONTIGUOUS');integer=array(np.int32,flags='C_CONTIGUOUS')
        self.function.restype=ctypes.c_int
        self.function.argtypes=[ctypes.c_int]*5+[ctypes.c_double,real,real,real,ctypes.c_int,
                                               integer,integer,integer,real,array(np.float32,flags='C_CONTIGUOUS')]

    def reset(self):
        super().reset()
        if hasattr(self,'delays'):self.delays.fill(0);self.previous_contrasts.fill(0)

    def step(self,time_s,left,right):
        if not np.isfinite(time_s) or time_s<0 or (self.last_time is not None and time_s<=self.last_time):
            raise ValueError('Frame timestamps must increase')
        images=np.ascontiguousarray(np.array([left,right]),dtype=float)
        if images.shape!=(2,*self.grid.shape) or not np.isfinite(images).all() or np.any((images<0)|(images>1)):
            raise ValueError('Invalid calibrated retinal frames')
        first=self.last_time is None
        alpha=0. if first else float(-np.expm1(-(time_s-self.last_time)/self.config.delay_tau_s))
        output=np.empty(len(self.targets),np.float32)
        code=self.function(self.grid.shape[1],self.grid.shape[0],self.config.neighbor_steps,
            self.config.pooling_radius_steps,int(first),alpha,images,self.delays,self.previous_contrasts,
            len(output),self.side_index,self.routes,self.vertices,self.weights,output)
        if code:raise FloatingPointError(f'Frontend kernel failure: {code}')
        self.last_time=float(time_s)
        return output
