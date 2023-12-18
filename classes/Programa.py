from classes.Crud import Crud

class Programa(Crud):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1
        modificacoes = {'likes': self._likes}
        id = self._get_id()
        return Crud().atualizar_registro(id, modificacoes, self.produto, 'id')

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def detalhar(self):
        return self.__dict__
    
    def __str__(self):
       return f"Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}"
    
    def _get_id(self):
        return Crud().consultar_dados(self.produto, self.nome)[0][0]