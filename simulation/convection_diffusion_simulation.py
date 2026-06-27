import numpy as np
import config as cfg
from mesh.mesh import generate_mesh
from initial_conditions.initial_conditions import gaussian_pulse
from boundary.boundary import apply_bc
from solver.convection_diffusion import solve_advection_diffusion
from visualization.visualization import plot_field, plot_residual_history
from utils.cfl import compute_cfl
from utils.error_norms import l1_norm, l2_norm, linf_norm
from utils.timer import start_timer, stop_timer

def run_advection_diffusion_simulation():
    timer = start_timer()
    X,Y = generate_mesh(cfg.Lx, cfg.Ly, cfg.Nx, cfg.Ny)
    u = gaussian_pulse(X, Y)
    residual_history = []

    cfl = compute_cfl(cfg.cx, cfg.cy, cfg.dt, cfg.dx, cfg.dy)
    print(f"CFL Number = {cfl:.3f}")

    if cfl>1:
        print("⚠️ WARNING: CFL > 1. Solution may become unstable.")

    for n in range(cfg.nt):
        u_old = u.copy()
        u = solve_advection_diffusion(u, cfg.cx, cfg.cy, cfg.D, cfg.dt, cfg.dx, cfg.dy, cfg.Nx, cfg.Ny)

        u = apply_bc(u, "dirichlet")
        residual = np.max(np.abs(u-u_old))
        residual_history.append(residual)
        if residual<cfg.tolerance:
            print(f"Converged at step {n}")
            break
        if n % 10 == 0:
            plot_field(X, Y, u, n) 

    plot_residual_history(residual_history)
    error = u - u_old
    print("\nError Norms")
    print(f"L1 = {l1_norm(error):.6e}")
    print(f"L2 = {l2_norm(error):.6e}")
    print(f"Linf = {linf_norm(error):.6e}")

    elapsed = stop_timer(timer)
    iterations = n+1
    print(f"\nSimulation Time : {elapsed:.4f} seconds")
    print(f"Average Time/Iteration : {elapsed/iterations:.6f} seconds")
    return u, residual_history