import numpy as np

def generate_mesh(Lx, Ly, Nx, Ny):

    x = np.linspace(0, Lx, Nx)
    y = np.linspace(0, Ly, Ny)

    X, Y = np.meshgrid(x, y)

    return X, Y