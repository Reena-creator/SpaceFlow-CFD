import numpy as np
import config as cfg
from mesh.mesh import generate_mesh
from initial_conditions.initial_conditions import gaussian_pulse
from boundary.boundary import apply_bc
from solvers.advection import advection_solver
from visualization.visualization import plot_field, plot_residual_history
from utils.cfl import compute_cfl

def run_advection_simulation(Nx=cfg.Nx, Ny=cfg.Ny, scheme="upwind", show_plots=True):
    dx = cfg.Lx/(Nx-1)
    dy = cfg.Ly/(Ny-1)
    dt = cfg.CFL * min(dx/abs(cfg.cx), dy/abs(cfg.cy))
    nt = int(cfg.t_final/dt)

    X,Y = generate_mesh(cfg.Lx, cfg.Ly, Nx, Ny)
    u = gaussian_pulse(X, Y)
    residual_history = []
    
    cfl = compute_cfl(cfg.cx, cfg.cy, dt, dx, dy)
    print(f"CFL Number = {cfl:.3f}")

    if cfl>1:
        print("⚠️ WARNING: CFL > 1. Solution may become unstable.")

    for n in range(nt):
        u_old = u.copy()
        # u = solve_advection(u, cfg.cx, cfg.cy, cfg.dt, cfg.dx, cfg.dy, cfg.Nx, cfg.Ny)
        # u = solve_advection_central(u, cfg.cx, cfg.cy, cfg.dt, cfg.dx, cfg.dy, cfg.Nx, cfg.Ny)
        u = advection_solver(u, cfg.cx, cfg.cy, dt, dx, dy, Nx, Ny, scheme)
        u = apply_bc(u, "neumann")
        residual = np.max(np.abs(u - u_old))
        residual_history.append(residual)
        # if residual<cfg.tolerance:
        #     print(f"Converged at step {n}")
        #     break
        if show_plots and n % 10 == 0:
            plot_field(X, Y, u, n) 
    if show_plots:
        plot_residual_history(residual_history)
    return X, Y, u, residual_history