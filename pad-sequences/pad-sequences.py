import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len is not None:
        L = max_len
    else:
        L = max(len(seq) for seq in seqs)
    for seq in seqs:
        while len(seq) < L:
            seq.append(pad_value)
    
    seqs = [seq[:L] for seq in seqs]
    return seqs
    pass