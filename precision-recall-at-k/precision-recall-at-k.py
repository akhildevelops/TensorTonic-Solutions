import torch
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended=torch.tensor(recommended)
    relevant=torch.tensor(relevant)
    rel_recommended, counts=torch.cat([recommended[:k],relevant]).unique(return_counts=True)
    tps=rel_recommended[counts.gt(1)]

    return [tps.shape[0]/k, tps.shape[0]/relevant.shape[0]]

    