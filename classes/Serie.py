from classes.Programa import Programa
from classes.Crud import Crud

class Serie(Programa, Crud):

    produto = 'Serie'

    def __init__(self, nome):
        super().__init__(nome)
        self.ano = self.dados['ano']
        self.temporadas = self.dados['temporadas']
        self.nome = self.dados['nome']
        self.sinopse = self.dados['sinopse']
        self.categoria = self.dados['categoria']
        
        del self.dados
        self.inserir(self.detalhar())

    def __str__(self):
        return f"{super().__str__()} - {self.temporadas} Temporadas"
    
    def inserir(self, item):
        banco = Crud()
        banco.criar_tabela()
        filtrar_por = self.nome
        produto_duplicado = banco.consultar_dados(self.produto, filtrar_por)

        if produto_duplicado:
            print("Produto já inserido")
            return "Produto já inserido"
        else: 
            banco.inserir_serie(item)
            banco.desconectar_banco()
            print("Produto inserido com sucesso!")