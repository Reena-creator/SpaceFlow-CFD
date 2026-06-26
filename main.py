from mesh import *
from solver import *
from visualization import *
from boundary import *
from initial_conditions import *
from poisson_solver import poisson_solver
import time

# =====================================
# PARAMETERS
# =====================================

Lx = 1.0
Ly = 1.0

Nx = 100
Ny = 100

dx = Lx/(Nx-1)
dy = Ly/(Ny-1)

cx = 1.0
cy = 0.5

D = 0.001

dt = 0.001
nt = 1000
tolerance = 1e-6

max_50 = 0.537
max_100 = 0.708
max_200 = 0.842

reference = max_200
error_50 = abs(max_50 - reference)
error_100 = abs(max_100 - reference)

grid_sizes = [50, 100, 150]
errors = [error_50, error_100, 0]

# =====================================
# INITIALIZATION
# =====================================

phi = np.zeros((Ny, Nx))

X, Y = generate_mesh(Lx, Ly, Nx, Ny)

b = gaussian_source(X,Y)

# u = gaussian_pulse(X, Y)
residual_history = []

# =====================================
# ANIMATION
# =====================================

# plt.figure(figsize=(6,5))
# start = time.time()
# for n in range(nt):
#     u_old = u.copy()
#     u = solve_diffusion(u, D, dt, dx, dy, Nx, Ny)

#     # Apply BC
#     # u = apply_neumann_bc(u)
#     u = apply_bc(u, "neumann")
#     residual = np.max(np.abs(u-u_old))
#     residual_history.append(residual)
#     if n % 10 == 0:
#         # print(
#         #     # f"Step = {n},"
#         #     # f"Max(u) = {np.max(u):.6f}"
#         #     f"Step = {n},"
#         #     f"Residual = {residual:.8f}"
#         # )
#         plot_field(X, Y, u, n) 
#         if residual<tolerance:
#             print(f"Converged at step {n}")
#             break
        
# # end = time.time()
# # print(end-start)

# plt.ioff()
# plt.show()
# print("Max value = ", np.max(u))

# plt.figure(figsize=(8,5))
# plt.semilogy(residual_history)
# plt.xlabel("Iteration")
# plt.ylabel("Residual")
# plt.title("Residual History")
# plt.grid()
# plt.show()

# plt.figure()
# plt.plot(grid_sizes, errors, marker='o')
# plt.xlabel("Grid Size")
# plt.ylabel("Error")
# plt.title("Grid Convergence Study")
# plt.grid()
# plt.show


phi, residual_history = poisson_solver(phi, b, dx, dy, max_iter=5000, tolerance = 1e-6)

plt.figure(figsize=(8,6))
plt.contourf(X, Y, phi, levels=100, cmap="coolwarm")
plt.colorbar(label="Phi")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Poisson Equation Solution")
plt.show()

plt.figure(figsize=(8,5))
plt.semilogy(residual_history)
plt.xlabel("Iteration")
plt.ylabel("Residual")
plt.title("Residual History")
plt.grid(True)
plt.show()