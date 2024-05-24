from simulation import Simulation


def start_backtest(data,parameters):

    simulation = Simulation(data,parameters)

    simulation.simulate(data)


