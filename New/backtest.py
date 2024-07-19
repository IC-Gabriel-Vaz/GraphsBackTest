from simulation import Simulation
from tcSimulation import TCSimulation

import time


def start_backtest(data,parameters):

    start_time= time.time()

    if parameters.transactionCosts == 0:

        simulation = Simulation(data,parameters)

        simulation.simulate(data,parameters)
    
    else:

        simulation = TCSimulation(data,parameters)

        simulation.simulate(data,parameters)

    end_time = time.time()
    
    simulation_time = end_time - start_time

    print(f"Simulation finished in {simulation_time:.4f} seconds \n")

    print()


