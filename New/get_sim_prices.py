import pandas as pd


def get_simulation_prices(parameters, adm):

    conn = adm.connection
    query = f'''
    SELECT ap.date, aa.asset, ap.close
    FROM AssetPrice ap
    JOIN ApplicationAsset aa ON ap.asset = aa.asset
    WHERE aa.app = '{parameters.app}'
    '''
    df = pd.read_sql_query(query, conn)

    conn.close()

    df_pivot = df.pivot(index='date', columns='asset', values='close')

    #print(df_pivot)

    df_pivot.index = pd.to_datetime(df_pivot.index)

    return df_pivot