import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X)
    u = X.mean(axis=axis)
    if axis==1:
        u=u.reshape(-1,1)
    std = X.std(axis=axis)+eps
    if axis==1:
        std = std.reshape(-1,1)
    return ((X-u)/std).tolist()
    pass