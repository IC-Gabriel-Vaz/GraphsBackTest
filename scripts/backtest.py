import pandas as pd
import sys
from datetime import datetime , timedelta
import argParse

sys.path.append("../classes")
sys.path.append('../dbUtils')


############ Classes ##############
from admin import Admin
from simulation import Simulation
from data import Data
from parameters import Parameters
###################################

########### Functions #############
import read_txt
import get_assets_prices as gp
import get_assets as ga
import argParse

###################################


if __name__ == '__main__':

    txt = argParse.argParse()
    #print(parameters)

    parameters = Parameters(txt)

    adm = Admin(parameters.db_path)
    adm.connect()

    print('Loading Data ... \n')

    data = Data(parameters,adm)

    simulation = Simulation(parameters, data)
    print(simulation.shares)
    i = 0
    results = []
    weights = {}

    data.assets = data.prices.columns

    for asset in data.assets:

        weights[asset] = 1/len(data.assets)

    while i < len(data.in_Sample_dates):

        print('************* Rebalacing ************ \n')
        sequency = data.official_dates[i: i + parameters.rebalance_frequency]
        rebalance_prices = data.prices.loc[pd.to_datetime(sequency)]
        #print(rebalance_prices)

        result = simulation.backtest_portfolio(weights, rebalance_prices)
        results.append(result)

        i += parameters.rebalance_frequency

    print('Simulação Finalizada \n')
    #print(f'Valor final do Portfólio: {simulation.portfolio_values[-1]} \n')
    print(simulation.portfolio_values)

    