import sqlite3
import os.path

class Crud:

    def __init__(self, nome_banco="data.db"):
        pasta_raiz = os.path.dirname(os.path.dirname(__file__))
        pasta_db = os.path.join(pasta_raiz, 'database')
        caminho_banco = os.path.join(pasta_db, nome_banco)

        self.nome_banco = caminho_banco
        self.conectar_banco()

    def conectar_banco(self):
        try:
            if not os.path.exists(os.path.dirname(self.nome_banco)):
                os.makedirs(os.path.dirname(self.nome_banco))

            self.conn = sqlite3.connect(self.nome_banco)
            self.cursor = self.conn.cursor()
        
        except Exception as error:
            print(f"Erro ao conectar ao banco de dados: {error}")

    def desconectar_banco(self):
        self.conn.close()
    
    def criar_tabela(self):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS Serie (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            ano TEXT,
                            temporadas TEXT,
                            likes INTEGER
            )""")
        
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS Filme (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            ano TEXT,
                            duracao INTEGER,
                            likes INTEGER
            )
            """)
        self.conn.commit()

    def inserir_filme(self, filme):
        self.cursor.execute("""
            INSERT INTO Filme(nome, ano, duracao, likes)
                            VALUES(?,?,?,?)
                            """, (filme['_nome'], filme['ano'], filme['duracao'], filme['_likes']))
        self.conn.commit()

    def inserir_serie(self, serie):
        self.cursor.execute("""
            INSERT INTO Serie(nome, ano, temporadas, likes)
                            VALUES(?,?,?,?)
                            """, (serie['_nome'], serie['ano'], serie['temporadas'], serie['_likes']))
        self.conn.commit()
    
    def consultar_dados(self, produto, id=None):
        if id:
            self.cursor.execute(f'SELECT * FROM {produto} WHERE nome=?', (id,))
        else:
            self.cursos.execute(f'SELECT * FROM {produto}')

        return self.cursor.fetchall()
    
    def atualizar_registro(self, id, modificacoes, banco, parametro_busca):
        if not modificacoes:
            return "Não foi informada nenhuma modificação"
        
        campos_atualizar = ', '.join(f"{campo} =?" for campo in modificacoes.keys())
        valores_atualizar = tuple(modificacoes.values())

        self.cursor.execute(f"""
            UPDATE {banco}
            SET {campos_atualizar}
            WHERE {parametro_busca}=?
        """, valores_atualizar + (id, ))
        self.conn.commit()
    
    def excluir_registro(self, id, banco):
        self.cursor.execute(f"DELETE FROM {banco} WHERE id=?", (id,))
        self.conn.commit()
        return f"{banco} excluído com sucesso"