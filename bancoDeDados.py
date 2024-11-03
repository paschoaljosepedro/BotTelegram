import pyodbc
class Database:
    def __init__(self):
        self.dadosConexao = (
            "Driver={SQL Server};"
            "Server=DESKTOP-HJLJC64\SQLEXPRESS;"
            "Database=Python_SQL;"
        )
        self.conexao = pyodbc.connect(self.dadosConexao)
        print("Conexão bem-sucedida!")
       
        self.cursor = self.conexao.cursor()

    def insert(self, table, id, nome, capitulo):
        comando = f"INSERT INTO {table} (id, nome, capitulo) VALUES (?, ?, ?)"
        self.cursor.execute(comando, (id, nome, capitulo))
        self.conexao.commit()

    def delete(self, table, nome):
        comando = f"DELETE FROM {table} WHERE nome = ?"
        self.cursor.execute(comando, (nome,))
        self.conexao.commit()

    def update(self,table,nome,capitulo):
        comando = f"UPDATE {table} SET capitulo = ? where nome = ?"
        self.cursor.execute(comando,(nome,capitulo))
        self.conexao.commit()

    def mostrarNomes(self, table):
        comando = f"SELECT nome FROM {table}"
        self.cursor.execute(comando)
        return self.cursor.fetchall()
    
    def mostarTudo(self,table):
        comando = f"SELECT nome, capitulo FROM {table}"
        self.cursor.execute(comando)
        return self.cursor.fetchall()
    
    def verificaSeExiste(self, table, nome, capitulo):
    # Consulta o banco de dados para ver se o título já existe
        comando = f"SELECT nome, capitulo FROM {table} WHERE nome = ?"
        self.cursor.execute(comando, (nome,capitulo))
        record = self.cursor.fetchone()
        return record[0]  if record else None

    


            