import pandas as pd
import sys
from datetime import datetime , timedelta
import argParse

from admin import Admin
from parameters import Parameters

import backtest as bt

from data import Data

if __name__ == '__main__':

    txt = argParse.argParse()

    parameters = Parameters(txt)

    adm = Admin(parameters.db_path)
    adm.connect()

    print('Loading Data ... \n')

    data =  Data(parameters, adm)

    print('******Starting Simulation****** \n')

    bt.start_backtest(data,parameters)



