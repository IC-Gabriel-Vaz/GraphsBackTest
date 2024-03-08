import pandas as pd
import sqlite3

def get_applications():

    conn = sqlite3.connect("C:/Users/gabri/Simulador/PortSim/portSimMarketData.sqlite")

    query = "SELECT * FROM ApplicationAsset;"

    df = pd.read_sql_query(query, conn)

    conn.close()

    applications = df['app'].unique()

    return applications

if __name__ == '__main__':
    get_applications()