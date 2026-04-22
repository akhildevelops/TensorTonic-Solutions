import torch
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    v = torch.asarray(values)
    return torch.log(v+1).tolist()