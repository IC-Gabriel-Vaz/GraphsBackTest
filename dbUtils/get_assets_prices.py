import sqlite3
import pandas as pd

conn = sqlite3.connect("C:/Users/gabri/Simulador/PortSim/portSimMarketData.sqlite")

query = "SELECT * FROM AssetPrice;"

df = pd.read_sql_query(query, conn)

conn.close()

print(df.columns)
