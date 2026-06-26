import numpy as np

# def gaussian_pulse(X, Y):

#     return np.exp(
#         -100*((X-0.3)**2 + (Y-0.5)**2)
#     )

def gaussian_source(X,Y):
    b = (
        500*np.exp(-500*((X-0.25)**2 + (Y-0.25)**2))
        -
        500*np.exp(-500*((X-0.75)**2 + (Y-0.75)**2))
    )
    return b