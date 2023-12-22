from dotenv import load_dotenv
from mtranslate import translate
import requests
import os
load_dotenv()

class ConectaApi:
    api_key = str(os.getenv('API_KEY'))
    params = {'api_key': api_key, 'language':'pt-BR'}
    
    def __init__(self, obj):
        self.nome = obj.nome
        self.ano = None
        self.duracao = None
        self.categoria = None
        self.temporadas = None
        self.sinopse = None
        self.produto = obj.produto
           
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
                
                self.dados = dados_id_filme
                
                return self.formatar_dados()
        else:

            print(f"Erro na solicitação: {response.status_code}")
            return None
        
    def formatar_dados(self):
        dados = self.dados
        if self.produto == 'Filme':
            generos = dados['genres']
            generos_string = [genero['name'] for genero in generos]
            
            return {
                        'nome': f"{dados['title']}",
                        'ano' : f"{dados['release_date'].split('-')[0]}",
                        'duracao' : f"{dados['runtime']}",
                        'categoria' : f"{', '.join(generos_string)}",
                        'sinopse': f"{dados['overview']}"        
                    }
            
        else:
            generos = dados['genres']
            generos_ = [genero['name'] for genero in generos]
            generos__ = [generos.split(' & ') for generos in generos_]
            generos___ = [elemento for sublista in generos__ for elemento in sublista]
            generos_final = [traduzir_texto(genero_traduzido) for genero_traduzido in generos___]
            
            return {
                        'nome': f"{dados['original_name']}",
                        'ano' : f"{dados['first_air_date'].split('-')[0]}",
                        'temporadas' : f"{dados['number_of_seasons']}",
                        'categoria' : f"{', '.join(generos_final)}",
                        'sinopse': f"{dados['overview']}"        
                    }
           
def traduzir_texto(texto):
    return translate(texto, 'pt')