import sqlite3

class Admin():

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection= sqlite3.connect(self.db_name)
            print("Conexão com a Base de Dados estabelecida!")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
    
    def disconnect(self):
        if self.connection == True:
            self.connection.close()
            print("Conexão encerrada")

    def execute_query(self, query, parameters=None):
        if not self.connection:
            self.connect()
        try:
            cursor = self.connection.cursor()
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao executar a query: {e}")
            return None
        finally:
            cursor.close()

    