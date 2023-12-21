from dotenv import load_dotenv
from mtranslate import translate
import requests
import os
load_dotenv()

class ConectaApi:  
    def __init__(self, obj):
        self.nome = obj.nome
        self.produto = obj._produto()
        self._api_key = api_key = str(os.getenv('API_KEY'))
        self._params = {'api_key': api_key, 'language':'pt-BR'}
    
    # def traduzir_texto(texto):
    #     return translate(texto, 'pt')
        
    def verifica_produto(self):
        if self.produto == 'Filme':
            url = f'https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={self.nome}'
        else:
            url = f'https://api.themoviedb.org/3/search/tv?api_key={self.api_key}&query={self.nome}'
            
        response = requests.get(url, params=self.params)
        
        return response
    
    def conecta_api(self):
        response = self.verifica_produto()
        
        if response.status_code == 200:
            dados_filme = response.json()
            id = dados_filme['results'][0]['id']
            
            url_id = f'https://api.themoviedb.org/3/movie/{id}'if self.produto == 'Filme' else f'https://api.themoviedb.org/3/tv/{id}'
            
            response = requests.get(url_id, params=self.params)
            
            if response.status_code == 200:
                dados_id_filme = response.json()
                
                return dados_id_filme
        else:

            print(f"Erro na solicitação: {response.status_code}")
            return None
    
    @property
    def api_key(self):
        return self._api_key
    
    @property
    def params(self):
        return self._params
    
    @classmethod
    def _produto(cls):
        produto = cls.produto
        print(produto)
        return produto