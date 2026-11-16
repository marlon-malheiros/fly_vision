"""Calibrated stereo-camera input contract for the frozen retinal model.

Ray-to-pixel maps and photometric lookup tables must come from calibration.
This module does not invent camera optics, missing field coverage or exposure
corrections. Synthetic calibration is explicitly tagged for software tests.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib,json
from pathlib import Path
import numpy as np


@dataclass(frozen=True)
class PreparedStereoSample:
    index:int
    reference_ticks:int
    time_s:float
    left:np.ndarray
    right:np.ndarray
    timestamps_ns:tuple[int,int]
    stereo_skew_ns:int
    clock_error_ns:float
    calibration_status:str


class StereoRetinalAdapter:
    def __init__(self,calibration_directory,model_configuration):
        directory=Path(calibration_directory)
        metadata_bytes=(directory/'calibration.json').read_bytes()
        self.metadata_sha256=hashlib.sha256(metadata_bytes).hexdigest()
        self.metadata=json.loads(metadata_bytes)
        if self.metadata.get('schema')!='stereo_retinal_calibration_v1':raise ValueError('Unknown calibration schema')
        if self.metadata.get('status') not in ('MEASURED_CALIBRATION','SYNTHETIC_TEST_ONLY'):
            raise ValueError('Calibration provenance/status must be explicit')
        array_file=directory/'arrays.npz'
        self.fingerprint=hashlib.sha256(array_file.read_bytes()).hexdigest()
        if self.fingerprint!=self.metadata['arrays_sha256']:raise ValueError('Calibration arrays changed')
        timing=[self.metadata[k] for k in ('frame_period_ns','maximum_stereo_skew_ns','maximum_clock_jitter_ns')]
        if any(isinstance(v,bool) or not isinstance(v,int) for v in timing):raise ValueError('Calibration timing bounds must be integer nanoseconds')
        self.period_ns,self.max_skew_ns,self.max_jitter_ns=timing
        if self.period_ns!=5_000_000 or min(self.max_skew_ns,self.max_jitter_ns)<0:
            raise ValueError('Require declared 5-ms frontend cadence and nonnegative timing bounds')
        if max(self.max_skew_ns,self.max_jitter_ns)>=self.period_ns/2:
            raise ValueError('Timing bounds must identify a unique frontend sample')
        if not self.metadata.get('provenance'):raise ValueError('Calibration provenance is required')
        axis=np.arange(-86.,87.)
        if not np.array_equal(self.metadata['retinal_axis_deg'],axis):raise ValueError('Retinal grid differs from frozen model')
        self.maps={}
        with np.load(array_file,allow_pickle=False) as z:
            for side in ('L','R'):
                camera=self.metadata['cameras'][side]
                if not np.allclose(camera['reference_world_deg'],model_configuration['eyes'][side]['reference_world_deg'],atol=1e-12,rtol=0) or not np.allclose(camera['world_to_eye_basis'],model_configuration['eyes'][side]['world_to_eye_basis'],atol=1e-12,rtol=0):
                    raise ValueError('Camera ray map uses a different eye chart')
                height,width=map(int,camera['image_shape'])
                dtype=np.dtype(camera['dtype'])
                if dtype not in (np.dtype('uint8'),np.dtype('uint16')) or min(height,width)<2:
                    raise ValueError('Require a declared monochrome uint8/uint16 camera mode')
                if not camera.get('camera_id') or not np.isfinite([camera['exposure_us'],camera['analog_gain']]).all() or camera['exposure_us']<=0 or camera['analog_gain']<=0:
                    raise ValueError('Camera identity, exposure and gain are required')
                x=np.array(z[side+'_x_px'],dtype=float);y=np.array(z[side+'_y_px'],dtype=float)
                coverage=np.asarray(z[side+'_covered'])
                lut=np.array(z[side+'_photometric_lut'],dtype=float)
                if x.shape!=(173,173) or y.shape!=x.shape or coverage.shape!=x.shape or coverage.dtype!=bool or not coverage.all():
                    raise ValueError('Every frozen retinal sample needs declared calibrated camera coverage')
                if not np.isfinite(x).all() or not np.isfinite(y).all() or np.any((x<0)|(x>width-1)|(y<0)|(y>height-1)):
                    raise ValueError('Ray map requires pixels outside the camera image')
                if lut.shape!=(np.iinfo(dtype).max+1,) or not np.isfinite(lut).all() or np.any((lut<0)|(lut>1)) or np.any(np.diff(lut)<0):
                    raise ValueError('Photometric LUT must be finite, monotone and normalized to [0,1]')
                x0,y0=np.floor(x).astype(int),np.floor(y).astype(int)
                x1,y1=np.minimum(x0+1,width-1),np.minimum(y0+1,height-1)
                self.maps[side]=dict(shape=(height,width),dtype=dtype,x0=x0,x1=x1,y0=y0,y1=y1,
                    wx=x-x0,wy=y-y0,lut=lut)
                for value in self.maps[side].values():
                    if isinstance(value,np.ndarray):value.setflags(write=False)
        self.reset()

    def reset(self):self.index=0;self.reference_ticks=None;self.last_timestamps=None

    def prepare(self,left,right,timestamps_ns,acquisition_modes):
        if len(timestamps_ns)!=2 or any(isinstance(t,(bool,np.bool_)) or not isinstance(t,(int,np.integer)) or t<0 for t in timestamps_ns):
            raise ValueError('Two common-clock nonnegative integer camera timestamps are required')
        stamps=tuple(map(int,timestamps_ns));skew=abs(stamps[0]-stamps[1])
        if skew>self.max_skew_ns:raise ValueError('Stereo exposure timestamps exceed the declared skew bound')
        if self.last_timestamps is not None and any(t<=previous for t,previous in zip(stamps,self.last_timestamps)):
            raise ValueError('Camera frame timestamps repeated or reordered')
        ticks=stamps[0]+stamps[1]
        reference=ticks if self.reference_ticks is None else self.reference_ticks
        error_ticks=ticks-reference-2*self.index*self.period_ns
        if abs(error_ticks)>2*self.max_jitter_ns:raise ValueError('Dropped frame, drift or off-clock camera sample')
        images={}
        for side,frame in (('L',left),('R',right)):
            mapping=self.maps[side];camera=self.metadata['cameras'][side];mode=acquisition_modes[side]
            if any(mode.get(field)!=camera[field] for field in ('camera_id','exposure_us','analog_gain')):
                raise ValueError('Camera acquisition mode differs from photometric calibration')
            image=np.asarray(frame)
            if image.shape!=mapping['shape'] or image.dtype!=mapping['dtype']:
                raise ValueError('Raw camera shape/dtype differs from calibration')
            # Linearize *before* spatial interpolation; gamma and interpolation do not commute.
            lut=mapping['lut'];x0,x1,y0,y1=(mapping[k] for k in ('x0','x1','y0','y1'))
            wx,wy=mapping['wx'],mapping['wy']
            top=lut[image[y0,x0]]*(1-wx)+lut[image[y0,x1]]*wx
            bottom=lut[image[y1,x0]]*(1-wx)+lut[image[y1,x1]]*wx
            images[side]=(top*(1-wy)+bottom*wy).astype(np.float32)
            images[side].setflags(write=False)
        return PreparedStereoSample(self.index,reference,self.index*self.period_ns/1e9,images['L'],images['R'],
            stamps,skew,error_ticks/2.,self.metadata['status'])

    def commit(self,sample):
        if sample.index!=self.index or (self.reference_ticks is not None and sample.reference_ticks!=self.reference_ticks):
            raise ValueError('Prepared sample is stale')
        self.reference_ticks=sample.reference_ticks;self.last_timestamps=sample.timestamps_ns;self.index+=1


class CameraPerceptionPipeline:
    """One binocular pair at a time; no camera driver or motor command is implied."""
    def __init__(self,adapter,runtime):
        self.adapter=adapter;self.runtime=runtime;self.requires_reset=False

    def reset(self):self.adapter.reset();self.runtime.reset();self.requires_reset=False

    def step(self,left,right,timestamps_ns,acquisition_modes):
        if self.requires_reset:raise ValueError('Reset is required after a neural runtime failure')
        prepared=self.adapter.prepare(left,right,timestamps_ns,acquisition_modes)
        try:
            rate=self.runtime.step(prepared.time_s,prepared.left,prepared.right)
        except Exception:
            self.requires_reset=True
            raise
        self.adapter.commit(prepared)
        return dict(time_s=prepared.time_s,rate=rate,stereo_skew_ns=prepared.stereo_skew_ns,
            observed_clock_error_ns=prepared.clock_error_ns,calibration_status=prepared.calibration_status,
            calibration_arrays_sha256=self.adapter.fingerprint,
            calibration_manifest_sha256=self.adapter.metadata_sha256,
            episode_detection=getattr(self.runtime,'last_detection',None))
