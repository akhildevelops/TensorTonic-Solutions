import torch

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y=torch.tensor(y)
    _,counts=torch.unique(y,return_counts=True)
    counts=counts/y.shape[0]
    return float(-1*torch.dot(counts,torch.log2(counts)))
    pass