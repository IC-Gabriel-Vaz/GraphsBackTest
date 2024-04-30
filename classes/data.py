import pandas as pd

class Data:

    def __init__(self):

        self.prices  = None
        self.returns = None
        self.official_dates = None
        self.assets = None
        self.date = None
        self.in_Sample_dates = None
        self.out_of_Sample_dates = None

    def get_official_dates(self,app):

        if app == 'IBOV':
            self.official_dates = self.returns.dropna(subset=['BOVA11']).index.to_list()

        return self.official_dates
    
    def get_simulation_dates(self,parameters):

        print(self.official_dates)
        index_date1 = self.official_dates.index(parameters.date1)
        index_date2 = self.official_dates.index(parameters.date2)

        self.in_Sample_dates = self.official_dates[:index_date1+1]
        self.out_of_Sample_dates = self.official_dates[index_date1+1:index_date2+1]

        return self.in_Sample_dates, self.out_of_Sample_dates
    



