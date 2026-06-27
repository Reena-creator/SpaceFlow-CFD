import numpy as np

def l1_norm(error):
    return np.mean(np.abs(error))

def l2_norm(error):
    return np.sqrt(np.mean(error**2))

def linf_norm(error):
    return np.max(np.abs(error))