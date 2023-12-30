from classes.Programa import Programa

class Filme(Programa):

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