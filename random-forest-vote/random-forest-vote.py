import numpy as np
import torch
def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    predictions=torch.tensor(predictions)
    labels_max=[]
    for col in range(predictions.shape[1]):
        labels,count=torch.unique(predictions[:,col],return_counts=True)
        labels_max.append(labels[torch.argmax(count)].item())
    return labels_max

