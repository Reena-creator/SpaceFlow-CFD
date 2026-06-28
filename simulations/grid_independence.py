import numpy as np
from visualization.visualization import plot_grid_independence
from simulations.advection_simulation import run_advection_simulation

def run_grid_independence():
    mesh_sizes = [41,81, 161,321]
    peak_values = []
    for N in mesh_sizes:
        print(f"\nRunning Simulation for {N} x {N} Grid")
        X,Y,u,residual = run_advection_simulation(Nx=N, Ny=N, scheme="upwind",show_plots=False)
        peak = np.max(u)
        peak_values.append(peak)
        print(f"Peak Value = {peak:.6f}")

    print("\nGrid Independence Results")
    for N, peak in zip(mesh_sizes, peak_values):
        print(f"{N} x {N} --> {peak:.6f}")

    plot_grid_independence(mesh_sizes, peak_values)