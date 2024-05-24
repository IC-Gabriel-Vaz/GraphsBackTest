import pandas as pd
import sys
import time

import get_sim_prices as gp


class Data:

    def __init__(self,parameters,adm):

        start_time = time.time()

        self.prices  = gp.get_simulation_prices(parameters , adm)
        self.all_assets = self.prices.columns
        self.official_dates = self.get_official_dates(parameters)
        self.in_Sample_dates, self.out_of_Sample_dates = self.get_in_out_Sample_dates(parameters)

        self.in_Sample_prices = self.get_in_Sample_prices()
        self.out_of_Sample_prices = self.get_out_of_Sample_prices()
        self.in_Sample_assets = self.in_Sample_prices.columns
        self.out_of_Sample_assets = self.out_of_Sample_prices.columns

        self.rebalance_dates = self.get_rebalance_dates(parameters)

        end_time = time.time()
        initialization_time = end_time - start_time
        print(f"Data loaded in {initialization_time:.4f} seconds \n")


    def get_official_dates(self,parameters):

        if parameters.app == 'IBOV':
            official_dates = self.prices.dropna(subset=['BOVA11']).loc[:parameters.date2].index.to_list()

        return official_dates
    
    def get_in_out_Sample_dates(self, parameters):

        try:
            index_date1 = self.official_dates.index(parameters.date1)
        except ValueError:
            index_date1 = max([i for i, date in enumerate(self.official_dates) if date < parameters.date1], default=-1)
            
        try:
            index_date2 = self.official_dates.index(parameters.date2)
        except ValueError:
            index_date2 = min([i for i, date in enumerate(self.official_dates) if date > parameters.date2], default=len(self.official_dates))

        self.in_Sample_dates = self.official_dates[:index_date1+1]
        self.out_of_Sample_dates = self.official_dates[index_date1+1:index_date2+1]

        return self.in_Sample_dates, self.out_of_Sample_dates
    
    def get_in_Sample_prices(self):

        self.in_Sample_prices = self.prices.loc[self.in_Sample_dates]

        self.in_Sample_prices = self.check_nan_prices(self.in_Sample_prices)

        return self.in_Sample_prices
    
    def get_out_of_Sample_prices(self):

        self.out_of_Sample_prices = self.prices.loc[self.out_of_Sample_dates]

        self.out_of_Sample_prices = self.check_nan_prices(self.out_of_Sample_prices)

        return self.out_of_Sample_prices

    def check_nan_prices(self,prices):

        columns_to_remove = prices.columns[prices.isna().sum() >= 0.5*len(prices)]
        columns_to_remove.to_list()

        for ativo in columns_to_remove:
            del prices[ativo]

        prices = prices.ffill()
        prices =  prices.bfill()

        return prices

    def get_rebalance_dates(self,parameters):

        return self.out_of_Sample_dates[::parameters.rebalance_frequency]
    






