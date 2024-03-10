import sqlite3
import pandas as pd

def get_assets(app):

    conn = sqlite3.connect("C:/Users/gabri/Simulador/PortSim/portSimMarketData.sqlite")

    query = 'SELECT * FROM ApplicationAsset'

    df = pd.read_sql_query(query, conn)

    df = df.loc[df['app'] == app]

    df_assets = df['asset']
    print(df_assets)
    
    conn.close()

    return df_assets

if __name__ == '__main__':

    app = 'IBOV'

    get_assets(app)

