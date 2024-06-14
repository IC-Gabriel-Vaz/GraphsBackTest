from simulation import Simulation
import time


def start_backtest(data,parameters):

    start_time= time.time()

    simulation = Simulation(data,parameters)

    simulation.simulate(data)

    end_time = time.time()
    
    simulation_time = end_time - start_time

    print(f"Simulation finished in {simulation_time:.4f} seconds \n")

    print()


