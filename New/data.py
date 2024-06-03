import pandas as pd
import sys
import time

import get_sim_prices as gp


class Data:

    def __init__(self,parameters,adm):

        start_time = time.time()

        self.prices  = gp.get_simulation_prices(parameters , adm)
        self.official_dates = self.get_official_dates(parameters)
        self.in_Sample_dates, self.out_of_Sample_dates = self.get_in_out_Sample_dates(parameters)

        self.out_of_Sample_prices = self.get_out_of_Sample_prices()
        self.all_assets = self.out_of_Sample_prices.columns
        self.in_Sample_prices = self.get_in_Sample_prices()

        self.all_prices = self.combine_in_out_prices() # All prices used in simulation

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

        start_date = parameters.date1 - pd.Timedelta(days=100)

        index_start_date = self.official_dates.index(start_date)

        self.in_Sample_dates = self.official_dates[index_start_date:index_date1+1]
        self.out_of_Sample_dates = self.official_dates[index_date1+1:index_date2+1]

        return self.in_Sample_dates, self.out_of_Sample_dates
    
    def get_in_Sample_prices(self):

        self.in_Sample_prices = self.prices.loc[self.in_Sample_dates, self.all_assets]

        return self.in_Sample_prices
    
    def get_out_of_Sample_prices(self):

        self.out_of_Sample_prices = self.prices.loc[self.out_of_Sample_dates]

        self.out_of_Sample_prices = self.out_of_Sample_prices.dropna(axis=1, how='all')


        return self.out_of_Sample_prices
    
    def combine_in_out_prices(self):

        df_concat = pd.concat([self.in_Sample_prices, self.out_of_Sample_prices], axis=0)

        return df_concat


    def get_rebalance_dates(self,parameters):

        return self.out_of_Sample_dates[::parameters.rebalance_frequency]
    






