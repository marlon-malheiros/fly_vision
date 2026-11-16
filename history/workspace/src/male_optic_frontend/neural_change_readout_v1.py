"""Causal activity/change features; no locomotor labels enter these features."""
from __future__ import annotations
import numpy as np


def paired_activity(times, rates, roles, sides, role, *, window_s=.1, lag_s=.2):
    """Return current bilateral means and means minus the lagged own history.

    Each row uses only that row and earlier observations. At 100 Hz, row 1.19 s
    averages 1.10--1.19 s and subtracts 0.90--0.99 s. No onset argument,
    matched straight trial, image-derived confidence, or velocity is used.
    Unavailable full windows are NaN; they cannot be silently classified.
    """
    times=np.asarray(times,float);rates=np.asarray(rates,float)
    roles=np.asarray(roles);sides=np.asarray(sides)
    if times.ndim!=1 or len(times)<2 or rates.shape!=(len(times),len(roles)) or sides.shape!=roles.shape:
        raise ValueError('Aligned time-by-cell observations required')
    dt=float(times[1]-times[0])
    if dt<=0 or not np.isfinite(rates).all() or not np.allclose(np.diff(times),dt,rtol=0,atol=1e-10):
        raise ValueError('Finite rates and uniform increasing timestamps required')
    n=round(window_s/dt);lag=round(lag_s/dt)
    if n<1 or lag<n or abs(n*dt-window_s)>1e-10 or abs(lag*dt-lag_s)>1e-10:
        raise ValueError('Nonoverlapping windows must align with the clock')
    bilateral=[]
    for side in ('L','R'):
        keep=(roles==role)&(sides==side)
        if not keep.any():raise ValueError('Both sides of the role are required')
        bilateral.append(rates[:,keep].mean(axis=1))
    bilateral=np.column_stack(bilateral)
    current=np.full((len(times),2),np.nan);change=current.copy()
    for i in range(n-1,len(times)):
        current[i]=bilateral[i-n+1:i+1].mean(axis=0)
        if i>=n+lag-1:change[i]=current[i]-current[i-lag]
    return current,change
