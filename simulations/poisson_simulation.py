import numpy as np

from mesh.mesh import generate_mesh
from initial_conditions.initial_conditions import gaussian_source
from solvers.poisson_solver import poisson_solver
from visualization.visualization import (
    plot_poisson_solution,
    plot_residual_history,
)

import config as cfg


def run_poisson_simulation():

    phi = np.zeros((cfg.Ny, cfg.Nx))

    X, Y = generate_mesh(
        cfg.Lx,
        cfg.Ly,
        cfg.Nx,
        cfg.Ny
    )

    b = gaussian_source(X, Y)

    phi, residual_history = poisson_solver(
        phi,
        b,
        cfg.dx,
        cfg.dy,
        max_iter=5000,
        tolerance=cfg.tolerance
    )

    plot_poisson_solution(X, Y, phi)

    plot_residual_history(residual_history)