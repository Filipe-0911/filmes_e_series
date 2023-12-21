from classes.Programa import Programa
from classes.Crud import Crud

class Filme(Programa, Crud):

    produto = 'Filme'
    
    def __init__(self, nome, ano, duracao, categoria=None, sinopse=None):
        super().__init__(nome, ano, categoria, sinopse)
        self.duracao = duracao

        self.inserir(self.detalhar())

    def __str__(self):
        return f"{super().__str__()} - {self.duracao} min"
    
    def inserir(self, item): 
        banco = Crud()
        banco.criar_tabela()
        filtrar_por = self.nome
        produto_duplicado = banco.consultar_dados(self.produto, filtrar_por)

        if produto_duplicado:
            # print("Produto já inserido")
            return "Produto já inserido"
        else: 
            banco.inserir_filme(item)
            banco.desconectar_banco()
            print("Produto inserido com sucesso!")