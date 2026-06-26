import numpy as np
import matplotlib.pyplot as plt
import config as cfg
from mesh.mesh import generate_mesh
from initial_conditions.initial_conditions import gaussian_pulse

from solver.solver import solve_diffusion
from boundary.boundary import apply_bc
from visualization.visualization import plot_field, plot_residual_history

def run_diffusion_simulation():
    X,Y = generate_mesh(cfg.Lx, cfg.Ly, cfg.Nx, cfg.Ny)
    u = gaussian_pulse(X, Y)
    residual_history = []

    for n in range(cfg.nt):
        u_old = u.copy()
        u = solve_diffusion(u, cfg.D, cfg.dt, cfg.dx, cfg.dy, cfg.Nx, cfg.Ny)

        u = apply_bc(u, "neumann")
        residual = np.max(np.abs(u-u_old))
        residual_history.append(residual)
        if n % 10 == 0:
            plot_field(X, Y, u, n) 
            if residual<cfg.tolerance:
                print(f"Converged at step {n}")
                break

    plot_residual_history(residual_history)
    
    return u, residual_history
