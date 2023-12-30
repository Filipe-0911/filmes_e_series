# Documentação do Projeto
## Introdução
Este projeto consiste em um sistema de gerenciamento de programas de entretenimento, como filmes e séries, utilizando a API do The Movie Database (TMDb). O sistema permite a inserção, consulta, atualização e exclusão de programas, bem como a criação de playlists e análises de categorias.

Para utilizar, crie um arquivo .env com o a chave obita através do cadastro no [site](https://www.themoviedb.org/?language=pt-BR).

> API_KEY = chave_da_api

## Estrutura do Projeto
O projeto está organizado da seguinte maneira:

classes/: Pasta contendo os arquivos das classes do projeto.

__init__.py: Para o python reconhecer a pasta classes como um Pacote.
Crud.py: Classe para manipulação do banco de dados SQLite.
ConectaAPI.py: Classe para conexão com a API do TMDb.
CategoriaMixin.py: Classe mixin para lidar com categorias.
AnaliseCategoria.py: Classe para análise de categorias.
Programa.py: Classe base para programas de entretenimento.
Filme.py: Classe específica para filmes.
Serie.py: Classe específica para séries.
PlayList.py: Classe para criação de playlists.
app.py: Script principal para execução do programa.
database/: Pasta contendo o banco de dados SQLite.

README.md: Documentação principal do projeto.

## Como Executar o Projeto
### Configuração do Ambiente:

Certifique-se de ter o Python instalado (versão 3.6 ou superior).
Instale as dependências necessárias utilizando o comando: pip install -r requirements.txt.
Execução do Programa:

Execute o script principal main.py para iniciar o programa.

## Funcionalidades Principais

### Classe Programa
A classe base Programa contém funcionalidades comuns a filmes e séries, como inserção, consulta, atualização e exclusão de dados.

```
# Exemplo de Uso
filme = Filme("Nome do Filme")
print(filme)
filme.dar_likes()

serie = Serie("Nome do Serie")
print(serie)
serie.dar_likes()
```

### Classe PlayList
A classe PlayList permite a criação de playlists com base em análises de categorias.
```
# Exemplo de Uso
playlist = PlayList("Ação")
playlist.receber_dados()
print(playlist)
```

### Classe AnaliseCategoria
A classe AnaliseCategoria realiza análises de categorias a partir de dados fornecidos.

```
# Exemplo de Uso
analise = AnaliseCategoria("Ação")
analise.receber_dados()
print(analise.programas)
```

# Autor
> Filipe de Bianchi Andrade

Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.