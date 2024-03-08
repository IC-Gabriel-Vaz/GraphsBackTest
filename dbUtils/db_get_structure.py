import sqlite3

conn = sqlite3.connect("C:/Users/gabri/Simulador/PortSim/portSimMarketData.sqlite")

cursor = conn.cursor()

def fetch_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

def fetch_columns(table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    return [column[1] for column in columns]

def fetch_rows(table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    return rows

tables = fetch_tables()

for table in tables:
    print(f"Table: {table}")
    columns = fetch_columns(table)
    print("Columns:", columns)
    # rows = fetch_rows(table)
    # print("Rows:")
    # for row in rows:
    #     print(row)
    print()

conn.close()
