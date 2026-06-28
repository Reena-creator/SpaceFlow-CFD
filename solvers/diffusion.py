import numpy as np
import matplotlib.pyplot as plt
import config as cfg
from mesh.mesh import generate_mesh
from initial_conditions.initial_conditions import gaussian_pulse
from boundary.boundary import apply_bc
from visualization.visualization import plot_field, plot_residual_history

def solve_diffusion(u, D, dt, dx, dy, Nx, Ny):

    u_new = u.copy()

    # for i in range(1, Ny-1):
    #     for j in range(1, Nx-1):

    #         diffusion_x = (
    #             u[i,j+1]
    #             - 2*u[i,j]
    #             + u[i,j-1]
    #         ) / dx**2

    #         diffusion_y = (
    #             u[i+1,j]
    #             - 2*u[i,j]
    #             + u[i-1,j]
    #         ) / dy**2

    #         u_new[i,j] = (
    #             u[i,j]
    #             + D*dt*(diffusion_x + diffusion_y)
    #         )
    diffusion_x = (
        u[1:-1,2:]
        - 2*u[1:-1,1:-1]
        + u[1:-1,:-2]
    ) / dx**2

    diffusion_y = (
        u[2:,1:-1]
        - 2*u[1:-1,1:-1]
        + u[:-2,1:-1]
    ) / dy**2

    u_new[1:-1,1:-1] = (
        u[1:-1,1:-1] 
        +D*dt*(diffusion_x + diffusion_y)
    )

    return u_new