import config as cfg
# from solver.diffusion import run_diffusion_simulation
# from solver.poisson_simulation import run_poisson_simulation
# from solver.advection import run_advection_simulation
from simulation.convection_diffusion_simulation import run_advection_diffusion_simulation

def main():
    # u, residual_history = run_diffusion_simulation()    
    # run_poisson_simulation()
    # run_advection_simulation()
    run_advection_diffusion_simulation()

if __name__ == "__main__":
    main()