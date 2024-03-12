import pandas as pd
import get_assets_prices
import sqlite3

def official_dates(app):

    conn = sqlite3.connect("C:/Users/gabri/Simulador/PortSim/portSimMarketData.sqlite")

    query = "SELECT * FROM AssetPrice"

    df = pd.read_sql(query, conn)

    

    print(official_dates)

    return official_dates


if __name__ == '__main__':

    official_dates('IBOV')