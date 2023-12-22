from classes.AnaliseCategoria import AnaliseCategoria

class PlayList(AnaliseCategoria):
    def __init__(self, nome, programas=[]):
        super().__init__(nome, programas)

    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
    
    def __str__(self):
        return f"{self._retorna_nome_programa(self.programas)}"
    
    def _retorna_nome_programa(self, lista_strings):
        lista_filtrada = filter(lambda x: 'nome' in x, lista_strings)
        lista_de_nomes = [item['nome'] for item in lista_filtrada]
        string = f"{self.nome.upper()}: "
        
        for item in lista_de_nomes:
            string += str(item) + ', '
            
        return string
    
    @property
    def programas(self):        
        return self._programas       