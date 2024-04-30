import pandas as pd
import sys

sys.path.append("../classes")
sys.path.append('../dbUtils')

import get_assets_prices as gp
import get_assets as ga

class Data:

    def __init__(self,parameters,adm):

        self.prices  = gp.get_prices(parameters.app , adm)
        self.returns = self.prices.pct_change().dropna()
        self.official_dates = self.get_official_dates(parameters.app)
        self.assets = self.prices.columns
        self.date = None
        self.in_Sample_dates, self.out_of_Sample_dates = self.get_simulation_dates(parameters)
        self.in_Sample_prices = self.get_in_Sample_prices()

    def get_official_dates(self,app):

        if app == 'IBOV':
            self.official_dates = self.returns.dropna(subset=['BOVA11']).index.to_list()

        return self.official_dates
    
    def get_simulation_dates(self,parameters):

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

        self.in_Sample_prices = self.prices.loc[pd.to_datetime(self.in_Sample_dates)]

        return self.in_Sample_prices

