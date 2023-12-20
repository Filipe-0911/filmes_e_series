from classes.Crud import Crud

class AnaliseCategoria(Crud):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def receber_dados(self):
        filmes = Crud().consultar_dados('Filme')
        series = Crud().consultar_dados('Serie')
        
        lista_com_todos_os_produtos = []

        # Adicione filmes à lista
        lista_com_todos_os_produtos.extend(filmes)
        # Adicione séries à lista
        lista_com_todos_os_produtos.extend(series)
        
        dados = self._agrupa_dados(lista_com_todos_os_produtos)
        
        for dado in dados:
            self._programas.append(dado)
    
    def _agrupa_dados(self, lista_produtos):
        dados_agrupados = []

        for row in lista_produtos:
            # Certifique-se de que row tem pelo menos 6 elementos
            if len(row) >= 6:
                categorias = row[5]

                # Verifique se categorias é uma string antes de dividi-la
                if isinstance(categorias, str):
                    # Utilize compreensão de lista para filtrar as categorias que correspondem a self.nome
                    categorias_filtradas = [cat for cat in categorias.split(', ') if cat.lower() == self.nome.lower()]

                    # Adiciona à lista de dados_agrupados se houver categorias filtradas
                    if categorias_filtradas:
                        dados_agrupados.append({'id':f"{row[0]}",'nome':f"{row[1]}", 'categorias':f"{categorias_filtradas[0]}"})
                else:
                    print(f"A sexta coluna de {row} não é uma string.")

            else:
                print(f"A linha {row} não tem pelo menos 6 elementos.")

        return dados_agrupados
