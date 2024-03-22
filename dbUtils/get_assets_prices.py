import sqlite3
import pandas as pd

import get_official_dates
import get_assets 

def get_prices(app, adm):

    conn = adm.connection

    query = 'SELECT * FROM AssetPrice'

    df = pd.read_sql_query(query, conn)
    #print(df)
    assets = get_assets.get_assets(app,adm)
    #print(assets)
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
    
    ##print(df_asset_prices)

    merged_df = pd.concat(df_asset_prices, axis=1, join='outer')
    merged_df.sort_index()

    if app == 'IBOV':
        official_dates = merged_df.dropna(subset=['BOVA11']).index.to_list()

    merged_df = merged_df.loc[official_dates]

    colunas_para_remover = merged_df.columns[merged_df.isna().sum() >= 1802]
    colunas_para_remover.to_list()

    for ativo in colunas_para_remover:
        del merged_df[ativo]

    merged_df = merged_df.ffill()
    merged_df =  merged_df.bfill()

    #print(merged_df)


    return merged_df
