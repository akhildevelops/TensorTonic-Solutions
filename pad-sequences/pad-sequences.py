import numpy as np
from functools import reduce
def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len is None:
        max_len=reduce(lambda x,y:max(x,len(y)),seqs,len(seqs[0]))
    array=np.full((len(seqs),max_len),pad_value)
    for index,seq in enumerate(seqs):
        array[index,:len(seq[:max_len])]=seq[:max_len]

    
    return array


        


    


    
    pass