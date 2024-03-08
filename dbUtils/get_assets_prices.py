import sqlite3
import pandas as pd

import get_assets 

def get_prices(app):

    conn = sqlite3.connect("C:/Users/gabri/Simulador/PortSim/portSimMarketData.sqlite")

    query = 'SELECT * FROM AssetPrice'

    df = pd.read_sql_query(query, conn)

    assets = get_assets.get_assets(app)

    for asset in assets:
        
        df_asset_prices = df.loc[df['asset'] == asset]

        print(df_asset_prices)


if __name__ == '__main__':
    get_prices('IBOV')