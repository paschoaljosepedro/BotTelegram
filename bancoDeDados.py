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

    def mostrarNomes(self, table):
        comando = f"SELECT nome FROM {table}"
        self.cursor.execute(comando)
        return self.cursor.fetchall()
    
    def mostarTudo(self,table):
        comando = f"SELECT nome, capitulo FROM {table}"
        self.cursor.execute(comando)
        return self.cursor.fetchall()
    
    def update(self, table, nome, capitulo):
    # Consulta o banco de dados para ver se o título já existe
        comando = f"SELECT nome, capitulo FROM {table} WHERE nome = ?"
        self.cursor.execute(comando, (nome,))
        record = self.cursor.fetchone()

    # Se o título já existir no banco, verificamos o capítulo
        if record:
            if record[1] != capitulo:  # Se o capítulo no banco for diferente do novo
            # Atualiza o capítulo no banco de dados
                com = f"UPDATE {table} SET capitulo = ? WHERE nome = ?"
                self.cursor.execute(com, (capitulo, nome))
                self.conn.commit()  # Confirma a atualização no banco
                return True  # Houve atualização
            else:
                return False  # Nenhuma atualização foi necessária
        else:
        # Se o título não existir, insere um novo registro
            com = f"INSERT INTO {table} (nome, capitulo) VALUES (?, ?)"
            self.cursor.execute(com, (nome, capitulo))
            self.conn.commit()  # Salva as mudanças
            return True  # Considerado uma atualização porque é um novo registro


            