import matplotlib.pyplot as plt

def plot_field(X, Y, u, n, phi):

    plt.clf()

    plt.contourf(X, Y, u, levels=50, cmap="coolwarm")
    plt.contour(X, Y, phi, levels=20, color="black", linewidth=0.3)

    plt.colorbar()

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.title(f"Time Step = {n}")

    plt.pause(0.01)