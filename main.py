import config as cfg
from solver.diffusion import run_diffusion_simulation
# from solver.poisson_simulation import run_poisson_simulation

def main():
    u, residual_history = run_diffusion_simulation()    
    # run_poisson_simulation()

if __name__ == "__main__":
    main()