def compute_cfl(cx, cy, dt, dx, dy):
    cfl_x = abs(cx)*dt/dx
    cfl_y = abs(cy)*dt/dy

    return max(cfl_x, cfl_y)