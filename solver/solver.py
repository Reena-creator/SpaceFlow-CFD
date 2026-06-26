# solve_advection()
# solve_diffusion()
# solve_advection_diffusion()

def solve_advection(u, cx, cy, dt, dx, dy, Nx, Ny):

    u_new = u.copy()

    for i in range(1, Ny-1):
        for j in range(1, Nx-1):

            advection_x = (
                -cx*(u[i,j] - u[i,j-1])/dx
                # -cx*(u[i,j+1] - u[i,j-1])/dx
            )

            advection_y = (
                -cy*(u[i,j] - u[i-1,j])/dy
                # -cy*(u[i+1,j] - u[i-1,j])/dy
            )

            u_new[i,j] = (
                u[i,j]
                + dt*(advection_x + advection_y)
            )

    return u_new

def solve_diffusion(u, D, dt, dx, dy, Nx, Ny):

    u_new = u.copy()

    # for i in range(1, Ny-1):
    #     for j in range(1, Nx-1):

    #         diffusion_x = (
    #             u[i,j+1]
    #             - 2*u[i,j]
    #             + u[i,j-1]
    #         ) / dx**2

    #         diffusion_y = (
    #             u[i+1,j]
    #             - 2*u[i,j]
    #             + u[i-1,j]
    #         ) / dy**2

    #         u_new[i,j] = (
    #             u[i,j]
    #             + D*dt*(diffusion_x + diffusion_y)
    #         )
    diffusion_x = (
        u[1:-1,2:]
        - 2*u[1:-1,1:-1]
        + u[1:-1,:-2]
    ) / dx**2

    diffusion_y = (
        u[2:,1:-1]
        - 2*u[1:-1,1:-1]
        + u[:-2,1:-1]
    ) / dy**2

    u_new[1:-1,1:-1] = (
        u[1:-1,1:-1] 
        +D*dt*(diffusion_x + diffusion_y)
    )

    return u_new

def solve_advection_diffusion(
        u,
        cx,
        cy,
        D,
        dt,
        dx,
        dy,
        Nx,
        Ny):

    u_new = u.copy()

    for i in range(1, Ny-1):
        for j in range(1, Nx-1):

            advection_x = (
                -cx*(u[i,j] - u[i,j-1])/dx
            )

            advection_y = (
                -cy*(u[i,j] - u[i-1,j])/dy
            )

            diffusion_x = (
                u[i,j+1]
                - 2*u[i,j]
                + u[i,j-1]
            ) / dx**2

            diffusion_y = (
                u[i+1,j]
                - 2*u[i,j]
                + u[i-1,j]
            ) / dy**2

            u_new[i,j] = (
                u[i,j]
                + dt*(
                    advection_x
                    + advection_y
                    + D*(diffusion_x + diffusion_y)
                )
            )

    return u_new