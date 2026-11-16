"""Online hybrid readout; no onset, scene, yaw truth or future-frame inputs."""
from collections import deque
import numpy as np
from .agreement_yaw_v1 import agreement


class HybridYawMonitor:
    def __init__(self,fit,confirmation=1):
        self.fit=fit;self.confirmation=confirmation;self.neural=deque(maxlen=30)
        self.image=deque(maxlen=10);self.ns=deque(maxlen=confirmation);self.ims=deque(maxlen=confirmation)
        self.last=None

    def push(self,time_s,left_rate,right_rate,image_yaw_deg_s):
        if not np.isfinite(time_s) or time_s<0 or self.last is not None and abs(time_s-self.last-.01)>1e-10:
            raise ValueError('Uniform 100-Hz chronological observations required')
        pair=np.array([left_rate,right_rate],float)
        if not np.isfinite(pair).all():raise ValueError('Finite neural activity required')
        self.last=float(time_s);self.neural.append(pair)
        self.image.append(np.nan if image_yaw_deg_s is None else float(image_yaw_deg_s))
        if len(self.neural)<30 or len(self.image)<10 or not np.isfinite(self.image).all():
            return dict(ready=False,neural_deg_s=None,image_deg_s=None,support=None,decision=None)
        history=np.array(self.neural);feature=history[-10:].mean(0)-history[:10].mean(0)
        b=np.array(self.fit['coefficients']);n=float(b[0]+((feature-self.fit['center'])/self.fit['scale'])@b[1:])
        im=float(np.mean(self.image));self.ns.append(n);self.ims.append(im)
        if len(self.ns)<self.confirmation:return dict(ready=False,neural_deg_s=n,image_deg_s=im,support=None,decision=None)
        support=float(agreement(self.ns,self.ims,self.fit['threshold'],self.confirmation)[-1])
        return dict(ready=True,neural_deg_s=n,image_deg_s=im,support=support,
                    decision=int(np.sign(support)) if abs(support)>1 else 0)
