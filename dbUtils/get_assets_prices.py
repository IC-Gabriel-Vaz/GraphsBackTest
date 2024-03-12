import sqlite3
import pandas as pd

import get_assets 

def get_prices(app):

    conn = sqlite3.connect("C:/Users/gabri/Simulador/PortSim/portSimMarketData.sqlite")

    query = 'SELECT * FROM AssetPrice'

    df = pd.read_sql_query(query, conn)

    assets = get_assets.get_assets(app)
    df_asset_prices = []

    for asset in assets:
        
        df_asset = df.loc[df['asset'] == asset]
        novo_df = df_asset[['date', 'close']].copy()
        novo_df.set_index('date', inplace=True)
        novo_df.columns = [asset]

        #print(novo_df)

        df_asset_prices.append(novo_df)

    for df in df_asset_prices:
        df.index = pd.to_datetime(df.index)

    for df in df_asset_prices:
        df.sort_index(inplace=True)
    

    #print(df_asset_prices)

    merged_df = pd.concat(df_asset_prices, axis=1, join='outer')
    merged_df.sort_index()


    print(merged_df)

    return merged_df

if __name__ == '__main__':
    get_prices('IBOV')