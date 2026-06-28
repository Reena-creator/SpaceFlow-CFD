from simulations.diffusion_simulation import run_diffusion_simulation
from simulations.poisson_simulation import run_poisson_simulation
from simulations.advection_simulation import run_advection_simulation
from simulations.convection_diffusion_simulation import run_advection_diffusion_simulation
from simulations.grid_independence import run_grid_independence

SIMULATION = "grid"   #CHANGE THIS TO RUN DIFFERENT SIMULATIONS

def main():

    if SIMULATION == "advection":
        run_advection_simulation()
    elif SIMULATION == "diffusion":
        run_diffusion_simulation()
    elif SIMULATION == "convection_diffusion":
        run_advection_diffusion_simulation()
    elif SIMULATION == "poisson":
        run_poisson_simulation()
    elif SIMULATION == "grid":
        run_grid_independence()
    else:
        raise ValueError("Invalid Simulation Selected")

if __name__ == "__main__":
    main()