import pandas as pd
from datetime import datetime , timedelta

class Parameters:


    def __init__(self,txt):

        self.app =  txt['app']
        self.db_path = txt['databasePath']
        self.date1 = datetime.strptime(txt['date1'], "%Y-%m-%d")
        self.date2 = datetime.strptime(txt['date2'], "%Y-%m-%d")
        self.rebalance_frequency = int(txt['rebalance'])
        self.investment = int(txt['investment'])
        

    
