import sqlite3
import os.path
import numpy as np

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
                            likes INTEGER,
                            categoria TEXT,
                            sinopse TEXT
            )""")
        
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS Filme (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            ano TEXT,
                            duracao INTEGER,
                            likes INTEGER,
                            categoria TEXT,
                            sinopse TEXT
            )
            """)
        self.conn.commit()

    def inserir_filme(self, filme):
        self.cursor.execute("""
            INSERT INTO Filme(nome, ano, duracao, likes, categoria, sinopse)
                            VALUES(?,?,?,?,?,?)
                            """, (filme['_nome'], filme['ano'], filme['duracao'], filme['_likes'], filme['categoria'], filme['sinopse']))
        self.conn.commit()

    def inserir_serie(self, serie):
        self.cursor.execute("""
            INSERT INTO Serie(nome, ano, temporadas, likes, categoria, sinopse)
                            VALUES(?,?,?,?,?,?)
                            """, (serie['_nome'], serie['ano'], serie['temporadas'], serie['_likes'], serie['categoria'], serie['sinopse']))
        self.conn.commit()
            
    def _consultar_dados(self, produto, nome=None):
        if nome:
            self.cursor.execute(f'SELECT * FROM {produto} WHERE nome=?', (nome,)) 
        else:
            self.cursor.execute(f'SELECT * FROM {produto}')
        result = self.cursor.fetchall()
        
        if not result and nome:
            self.cursor.execute(f"SELECT * FROM {produto} WHERE nome LIKE ?", (f"%{nome}%",))
            result = self.cursor.fetchall()
            if not result:
                result = False

        return result
    
    def _atualizar_registro(self, id, modificacoes, banco, parametro_busca='id', nome=None):
        if not modificacoes:
            return "Não foi informada nenhuma modificação"
               
        campos_atualizar = ', '.join(f"{campo} =?" for campo in modificacoes.keys())
        valores_atualizar = tuple(modificacoes.values())
        
        mensagem = "Cadastro alterado com sucesso"
        
        self.cursor.execute(f"""
            UPDATE {banco}
            SET {campos_atualizar}
            WHERE {parametro_busca}=?
        """, valores_atualizar + (id, ))
        self.conn.commit()
        
        if nome:
            nome = self._consultar_dados(banco, nome)
            mensagem = f"Você deu like em {nome}"
            
        return mensagem 
 
    def _excluir_registro(self, id, banco):
        self.cursor.execute(f"DELETE FROM {banco} WHERE id=?", (id,))
        self.conn.commit()
        return f"{banco} excluído com sucesso"
    
    def modificar_tabela(self, tabela, nova_coluna, tipo_da_coluna):
        self.cursor.execute(f"ALTER TABLE {tabela} ADD COLUMN {nova_coluna} {tipo_da_coluna}")
        self.conn.commit()
        self.conn.close()
    
    @staticmethod
    def recomenda_conforme_likes():
        series = Crud()._consultar_dados('Serie')
        filmes = Crud()._consultar_dados('Filme')
        
        programas = [serie for serie in series]
        programas += [filme for filme in filmes]
        
        programas_array = np.array(programas, dtype=[
                                                        ('a', int),
                                                        ('b', 'U999'),
                                                        ('c', int),
                                                        ('d', int),
                                                        ('e', int),
                                                        ('f', 'U999'),
                                                        ('g', 'U999')
                                                    ]
                                   )
        
        programas_array.sort(order='e')
        programas_array = programas_array[::-1]
        
        return programas_array