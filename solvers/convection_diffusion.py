import config as cfg
import numpy as np
from mesh.mesh import generate_mesh
from initial_conditions.initial_conditions import gaussian_pulse
from boundary.boundary import apply_bc
from visualization.visualization import plot_field, plot_residual_history

def solve_advection_diffusion(
        u,
        cx,
        cy,
        D,
        dt,
        dx,
        dy,
        Nx,
        Ny):

    u_new = u.copy()

    for i in range(1, Ny-1):
        for j in range(1, Nx-1):

            advection_x = (
                -cx*(u[i,j] - u[i,j-1])/dx
            )

            advection_y = (
                -cy*(u[i,j] - u[i-1,j])/dy
            )

            diffusion_x = (
                u[i,j+1]
                - 2*u[i,j]
                + u[i,j-1]
            ) / dx**2

            diffusion_y = (
                u[i+1,j]
                - 2*u[i,j]
                + u[i-1,j]
            ) / dy**2

            u_new[i,j] = (
                u[i,j]
                + dt*(
                    advection_x
                    + advection_y
                    + D*(diffusion_x + diffusion_y)
                )
            )

    return u_new