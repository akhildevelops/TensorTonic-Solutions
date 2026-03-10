import torch
def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a=torch.tensor(set_a)
    set_b=torch.tensor(set_b)
    print(set_a.shape[0]==0,set_b.shape[0]==0)
    if set_a.shape[0]==0 and set_b.shape[0]==0:
        return 0
    
    a_b, counts = torch.cat([set_a,set_b]).unique(return_counts=True)
    return a_b[torch.where(counts>1)].shape[0]/a_b.shape[0]
