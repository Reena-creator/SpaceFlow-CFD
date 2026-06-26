import numpy as np

def gaussian_pulse(X, Y):

    return np.exp(
        -100*((X-0.3)**2 + (Y-0.5)**2)
    )