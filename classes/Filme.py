from classes.Programa import Programa
from classes.Crud import Crud

class Filme(Programa, Crud):

    produto = 'Filme'
    
    def __init__(self, nome):
        super().__init__(nome)
        self.ano = self.dados['ano']
        self.duracao = self.dados['duracao']
        self.nome = self.dados['nome']
        self.sinopse = self.dados['sinopse']
        self.categoria = self.dados['categoria']
        
        del self.dados
        self.inserir(self.detalhar())

    def __str__(self):
        return f"{super().__str__()} - {self.duracao} min"
    
    def inserir(self, item): 
        banco = Crud()
        banco.criar_tabela()
        filtrar_por = self.nome
        produto_duplicado = banco.consultar_dados(self.produto, filtrar_por)

        if produto_duplicado:
            return "Produto já inserido"
        else: 
            banco.inserir_filme(item)
            banco.desconectar_banco()
            print("Produto inserido com sucesso!")