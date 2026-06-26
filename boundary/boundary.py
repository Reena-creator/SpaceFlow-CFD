def apply_bc(u, bc_type):

    if bc_type == "dirichlet":

        u[:,0] = 0
        u[:,-1] = 0

        u[0,:] = 0
        u[-1,:] = 0

    elif bc_type == "neumann":

        u[:,0] = u[:,1]
        u[:,-1] = u[:,-2]

        u[0,:] = u[1,:]
        u[-1,:] = u[-2,:]

    elif bc_type == "periodic":

        u[:,0] = u[:,-2]
        u[:,-1] = u[:,1]

        u[0,:] = u[-2,:]
        u[-1,:] = u[1,:]

    else:
        raise ValueError("Invalid BC")

    return u