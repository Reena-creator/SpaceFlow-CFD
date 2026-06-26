import matplotlib.pyplot as plt

def plot_field(X, Y, u, n):

    plt.clf()

    plt.contourf(X, Y, u, levels=50)

    plt.colorbar()

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.title(f"Time Step = {n}")

    plt.pause(0.01)