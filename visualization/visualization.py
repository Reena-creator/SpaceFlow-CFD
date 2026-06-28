import matplotlib.pyplot as plt

def plot_field(X, Y, field, n):

    plt.clf()

    plt.contourf(X, Y, field, levels=50, cmap="coolwarm", vmin=0, vmax=1)

    plt.colorbar(label="Scalar Field")

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.title(f"Time Step = {n}")
    plt.tight_layout()
    plt.pause(0.01)

def plot_poisson_solution(X, Y, phi, filename):
    plt.figure(figsize=(8,6))
    plt.contourf(X, Y, phi, levels=100, cmap="coolwarm", vmin=0, vmax=1)
    plt.colorbar(label="Phi")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Poisson Equation Solution")
    plt.tight_layout()
    save_figure(filename)
    plt.show()

def plot_residual_history(residual_history,filename):
    plt.figure(figsize=(8,5))
    plt.semilogy(residual_history, linewidth=2)
    plt.xlabel("Iteration")
    plt.ylabel("Residual")
    plt.title("Residual Convergence History")
    plt.grid(True)
    plt.tight_layout()
    save_figure(filename)
    plt.show()

def plot_grid_convergence(grid_sizes, errors, filename):
    plt.figure()
    plt.plot(grid_sizes, errors, marker='o')
    plt.xlabel("Grid Size")
    plt.ylabel("Error")
    plt.title("Grid Convergence Study")
    plt.grid()
    save_figure(filename)
    plt.show()

def plot_grid_independence(mesh_sizes, peak_values, filename):
    plt.figure(figsize=(6,4))
    plt.plot(mesh_sizes, peak_values, marker="o", linewidth=2, markersize=8)
    plt.xlabel("Grid Size")
    plt.ylabel("Peak Value")
    plt.title("Grid Independence Study")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    save_figure(filename)
    plt.show()

def save_figure(filename):
    plt.tight_layout()
    plt.savefig(
        f"results/{filename}",
        dpi=300,
        bbox_inches="tight"
    )

def save_final_field(X, Y, field, title, filename):

    plt.figure(figsize=(8,6))

    plt.contourf(X, Y, field, levels=50, cmap="coolwarm")

    plt.colorbar(label="Scalar Field")

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.title(title)

    plt.tight_layout()

    plt.savefig(
        f"results/{filename}",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()