import sqlite3
import pandas as pd

def get_assets(app,adm):

    conn = adm.connection

    query = 'SELECT * FROM ApplicationAsset'

    df = pd.read_sql_query(query, conn)

    
    df = df.loc[df['app'] == app]

    df_assets = df['asset']
    
    # for asset in df_assets:
    #     print(asset)
    

    return df_assets
