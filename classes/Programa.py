from classes.Crud import Crud
from classes.CategoriaMixin import CategoriaMixin
from classes.ConectaAPI import ConectaApi

class Programa(CategoriaMixin, Crud, ConectaApi):
    def __init__(self, nome, ano, categoria, sinopse):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        self.sinopse = sinopse
        super().__init__(categoria)
    
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1
        modificacoes = {'likes': self._likes}
        id = self._get_id()
        return Crud().atualizar_registro(id, modificacoes, self.produto, 'id', self.nome)

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
    
    def excluir_dados(self):
        id = self._get_id()
        return Crud().excluir_registro(id, self.produto)
    
    def atualizar_dados(self, dados_novos):
        id = self._get_id()
        
        if 'nome' in dados_novos:
            dados_novos['nome'] = dados_novos['nome'].title()
            self.nome = dados_novos['nome']
            
        for chave, valor in dados_novos.items():
            if hasattr(self, chave):
                setattr(self, chave, valor)
            
        return Crud().atualizar_registro(id, dados_novos, self.produto)        
    
    @classmethod
    def consultar_informacoes(cls, item=None):
        if item: item = item.title()
        return Crud().consultar_dados(cls.produto, item)