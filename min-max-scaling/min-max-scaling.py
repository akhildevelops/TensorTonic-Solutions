import torch
def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    data = torch.asarray(data)
    _min = torch.amin(data,dim=(0,))
    _max = torch.amax(data,dim=(0,))
    data = (data-_min)/(_max-_min+1e-12)
    return data.tolist()