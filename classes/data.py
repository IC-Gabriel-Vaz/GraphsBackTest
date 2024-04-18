import pandas as pd

class Data:

    def __init__(self):

        self.prices  = None
        self.returns = None
        self.official_dates = None
        self.assets = None
        self.date = None

    def get_official_dates(self,app):

        if app == 'IBOV':
            self.official_dates = self.returns.dropna(subset=['BOVA11']).index.to_list()

        return self.official_dates
    
