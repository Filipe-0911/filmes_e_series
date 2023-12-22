from classes.Crud import Crud

class AnaliseCategoria(Crud):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def receber_dados(self):
        filmes = Crud().consultar_dados('Filme')
        series = Crud().consultar_dados('Serie')
        
        lista_com_todos_os_produtos = []

        lista_com_todos_os_produtos.extend(filmes)
        
        lista_com_todos_os_produtos.extend(series)
        
        dados = self._agrupa_dados(lista_com_todos_os_produtos)
        
        for dado in dados:
            self._programas.append(dado)
    
    def _agrupa_dados(self, lista_produtos):
        dados_agrupados = []

        for row in lista_produtos:
            if len(row) >= 6:
                categorias = row[5]

                if isinstance(categorias, str):   
                    categorias_filtradas = [cat for cat in categorias.split(', ') if cat.lower() == self.nome.lower()]
    
                    if categorias_filtradas:
                        dados_agrupados.append({'id':f"{row[0]}",'nome':f"{row[1]}", 'categorias':f"{categorias_filtradas[0]}"})
                else:
                    print(f"A sexta coluna de {row} não é uma string.")

            else:
                print(f"A linha {row} não tem pelo menos 6 elementos.")

        return dados_agrupados
