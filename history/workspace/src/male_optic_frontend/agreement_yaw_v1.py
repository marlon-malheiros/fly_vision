"""Causal engineering agreement of frozen neural and image yaw estimates."""
from __future__ import annotations
import zlib
import numpy as np


def agreement(neural, image, neural_cutoff, confirmation=1):
    """Return dimensionless support, with a decision boundary at abs(support)>1.

    Require both branches to support the same direction and all confirmation
    samples to agree. Unavailable input stays NaN; opposing signs return zero.
    No event, movement label, depth, scene identity or future value is used.
    """
    neural=np.asarray(neural,float);image=np.asarray(image,float)
    if neural.ndim!=1 or neural.shape!=image.shape or neural_cutoff<=0 or not np.isfinite(neural_cutoff):
        raise ValueError('Aligned streams and a finite positive cutoff required')
    if confirmation not in (1,2,3,5):raise ValueError('Unregistered confirmation count')
    base=np.where(neural*image>0,np.sign(neural)*np.minimum(abs(neural)/neural_cutoff,abs(image)),0.)
    base[~(np.isfinite(neural)&np.isfinite(image))]=np.nan
    result=np.full(len(base),np.nan)
    for i in range(confirmation-1,len(base)):
        values=base[i-confirmation+1:i+1]
        if not np.isfinite(values).all():continue
        result[i]=float(min(values)) if np.all(values>0) else float(max(values)) if np.all(values<0) else 0.
    return result


def encode_retina(frames):
    """Lossless XOR/byte-shuffle/deflate encoding of float32 retinal movies."""
    a=np.ascontiguousarray(frames,dtype='<f4')
    if a.ndim!=4 or a.shape[1]!=2:raise ValueError('Time-by-two-eye image array required')
    words=a.view('<u4').copy();words[1:]=np.bitwise_xor(words[1:],words[:-1])
    data=words.view(np.uint8).reshape(-1,4).T.copy().tobytes()
    return zlib.compress(data,6)


def decode_retina(data,shape):
    raw=zlib.decompress(data);shape=tuple(int(v) for v in shape)
    if len(shape)!=4 or shape[1]!=2 or len(raw)!=int(np.prod(shape))*4:raise ValueError('Invalid retina shape or payload')
    words=np.frombuffer(raw,dtype=np.uint8).reshape(4,-1).T.copy().view('<u4').reshape(shape)
    np.bitwise_xor.accumulate(words,axis=0,out=words)
    return words.view('<f4')
