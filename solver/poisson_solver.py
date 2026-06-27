import numpy as np

residual_history = []

def poisson_solver(phi, b, dx, dy, max_iter, tolerance):
    phi_new = phi.copy()
    for n in range(max_iter):

        phi_old = phi_new.copy()

        phi_new[1:-1, 1:-1] = (
            (phi_old[1:-1, 2:] + phi_old[1:-1, :-2])*dy**2
            +
            (phi_old[2:, 1:-1] + phi_old[:-2, 1:-1])*dx**2
            -
            b[1:-1, 1:-1]*dx**2*dy**2
        )/(2*(dx**2 + dy**2))

        phi_new[0,:] = 0
        phi_new[-1,:] = 0
        phi_new[:,0] = 0
        phi_new[:,-1] = 0

        residual = np.max(np.abs(phi_new - phi_old))
        if residual < tolerance:
            print(f"Converged in {n+1} iterations")
            break
        residual_history.append(residual)


    return phi_new, residual_history