import numpy as np
import matplotlib.pyplot as plt
import config as cfg
from mesh.mesh import generate_mesh
from initial_conditions.initial_conditions import gaussian_pulse
from boundary.boundary import apply_bc
from visualization.visualization import plot_residual_history, plot_field

def solve_advection(u, cx, cy, dt, dx, dy, Nx, Ny):
    u_new = u.copy()

    for i in range(1, Ny-1):
        for j in range(1, Nx-1):

            advection_x = (
                -cx*(u[i,j] - u[i,j-1])/dx
                # -cx*(u[i,j+1] - u[i,j-1])/dx
            )

            advection_y = (
                -cy*(u[i,j] - u[i-1,j])/dy
                # -cy*(u[i+1,j] - u[i-1,j])/dy
            )

            u_new[i,j] = (
                u[i,j]
                + dt*(advection_x + advection_y)
            )

    return u_new

def solve_advection_central(u, cx, cy, dt, dx, dy, Nx, Ny):
    u_new = u.copy()

    for i in range(1, Ny-1):
        for j in range(1, Nx-1):

            advection_x = (
                -cx*(u[i,j+1] - u[i,j-1])/(2*dx)
            )

            advection_y = (
                -cy*(u[i+1,j] - u[i-1,j])/(2*dy)
            )

            u_new[i,j] = (
                u[i,j]
                + dt*(advection_x + advection_y)
            )

    return u_new