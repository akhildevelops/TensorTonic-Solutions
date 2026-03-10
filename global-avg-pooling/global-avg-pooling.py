import numpy as np
import torch
def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    if x.ndim<3:
        
        raise ValueError() 

    x=torch.tensor(x)
    _x=torch.sum(x,dim=[x.ndim-2,x.ndim-1])
    return (_x/(x.shape[x.ndim-2]*x.shape[x.ndim-1])).numpy()
    pass