import pandas as pd
import sys
from datetime import datetime , timedelta

sys.path.append("../classes")
sys.path.append('../dbUtils')

import read_txt
from admin import Admin
import get_assets_prices as gp
from simulation import Simulation

if __name__ == '__main__':

    parameters = read_txt.read_txt('C:/Users/gabri/ICDev/GraphsBackTest/parameters.txt')
    app = parameters['app']
    db_path = parameters['databasePath']
    initial_date = parameters['start_date']
    end_date = parameters['end_date']
    rebalance = int(parameters['rebalance'])

    initial_date = datetime.strptime(initial_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    date = initial_date

    adm = Admin(db_path)
    adm.connect()

    print('Carregando Dados ... \n')
    
    prices = gp.get_prices(app , adm)
    #print(prices)

    returns = prices.pct_change().dropna()
    print(returns.loc[date + timedelta(days=1)])

    print('Dados carregados com sucesso \n')

    simulation = Simulation()

    # while date != end_date:
    #     dates = []
    #     for i in range(rebalance):
    #         current_date = date + timedelta(days=1)
    #         dates.append(current_date)
        
    #     simulation_returns = returns.loc[returns.index.isin(dates)]
    #     print(simulation_returns)
    #     date += timedelta(days=100)