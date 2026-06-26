import matplotlib.pyplot as plt

def plot_field(X, Y, field, n):

    plt.clf()

    plt.contourf(X, Y, field, levels=50, cmap="coolwarm")

    plt.colorbar()

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.title(f"Time Step = {n}")

    plt.pause(0.01)

def plot_poisson_solution(X, Y, phi):
    plt.figure(figsize=(8,6))
    plt.contourf(X, Y, phi, levels=100, cmap="coolwarm")
    plt.colorbar(label="Phi")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Poisson Equation Solution")
    plt.show()

def plot_residual_history(residual_history):
    plt.figure(figsize=(8,5))
    plt.semilogy(residual_history)
    plt.xlabel("Iteration")
    plt.ylabel("Residual")
    plt.title("Residual History")
    plt.grid(True)
    plt.show()

def plot_grid_convergence(grid_sizes, errors):
    plt.figure()
    plt.plot(grid_sizes, errors, marker='o')
    plt.xlabel("Grid Size")
    plt.ylabel("Error")
    plt.title("Grid Convergence Study")
    plt.grid()
    plt.show