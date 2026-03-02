import torch
def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    X=torch.tensor(X,dtype=torch.int32)
    W=torch.tensor(W,dtype=torch.int32)
    b=torch.tensor(b,dtype=torch.int32)

    W=torch.concat([W,b.view(1,-1)],dim=0)
    X=torch.concat([X,torch.ones(*(X.shape[0],1),dtype=torch.int32)],dim=1)

    return torch.matmul(X,W).tolist()