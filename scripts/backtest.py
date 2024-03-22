import pandas as pd
import sys
sys.path.append("../classes")
sys.path.append('../dbUtils')

import read_txt
from admin import Admin
import get_assets_prices as gp

if __name__ == '__main__':

    parameters = read_txt.read_txt('C:/Users/gabri/ICDev/GraphsBackTest/parameters.txt')
    app = parameters['app']
    db_path = parameters['databasePath']

    adm = Admin(db_path)
    adm.connect()
    print(adm.connection)

    prices = gp.get_prices(app , adm)