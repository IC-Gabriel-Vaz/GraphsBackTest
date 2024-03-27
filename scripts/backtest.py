import pandas as pd
import sys
from datetime import datetime , timedelta

sys.path.append("../classes")
sys.path.append('../dbUtils')

import read_txt
from admin import Admin
import get_assets_prices as gp
from simulation import Simulation
import get_assets as ga

if __name__ == '__main__':

    parameters = read_txt.read_txt('C:/Users/gabri/ICDev/GraphsBackTest/parameters.txt')
    app = parameters['app']
    db_path = parameters['databasePath']
    initial_date = parameters['start_date']
    end_date = parameters['end_date']
    rebalance_frequency = int(parameters['rebalance'])
    investiment = int(parameters['investiment'])

    initial_date = datetime.strptime(initial_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    date = initial_date

    adm = Admin(db_path)
    adm.connect()

    print('Carregando Dados ... \n')
    
    prices = gp.get_prices(app , adm)

    returns = prices.pct_change().dropna()

    simulation = Simulation(investiment)


    if app == 'IBOV':
        official_dates = returns.dropna(subset=['BOVA11']).index.to_list()
    
    i = 0
    results = []
    weights = {}

    assets = prices.columns

    for asset in assets:

        weights[asset] = 1/len(assets)

    while i < len(official_dates):

        print('****** Rebalacing ****** \n')

        sequency = official_dates[i: i + rebalance_frequency]
        rebalance_prices = prices.loc[pd.to_datetime(sequency)]
        print(rebalance_prices)

        result = simulation.backtest_portfolio(weights, rebalance_prices)
        results.append(result)

        i += rebalance_frequency

    for df in results:
        print(df)