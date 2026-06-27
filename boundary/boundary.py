def dirichlet_bc(u, value=0):
    u[:, 0] = value
    u[:, -1] = value

    u[0, :] = value
    u[-1, :] = value

    return u

def neumann_bc(u):
    u[:, 0] = u[:, 1]
    u[:, -1] = u[:, -2]

    u[0, :] = u[1, :]
    u[-1, :] = u[-2, :]

    return u

def periodic_bc(u):
    u[:, 0] = u[:, -2]
    u[:, -1] = u[:, 1]

    u[0, :] = u[-2, :]
    u[-1, :] = u[1, :]

    return u

def apply_bc(u, bc_type="dirichlet", value=0):
    if bc_type == "dirichlet":
        return dirichlet_bc(u, value)

    elif bc_type == "neumann":
        return neumann_bc(u)

    elif bc_type == "periodic":
        return periodic_bc(u)

    else:
        raise ValueError("Invalid BC")
