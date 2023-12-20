from classes.Filme import Filme
from classes.Serie import Serie
from classes.PlayList import PlayList

vindagores = Filme('vingadores - guerra infinita', 2018, 160, 'ação, aventura, fantasia, fantasia científica, história de super-heroi')
atlanta = Serie('the walking dead', 2018, 2, 'terror, drama, pós-apocalíptica')
tmep = Filme('todo mundo em pânico', 1999, 100, 'comédia, drama, terror')
demolidor = Serie('demolidor', 2016, 2, 'Ação, História de super-herói, Ficção científica, Aventura')

vindagores.dar_likes()
vindagores.dar_likes()
vindagores.dar_likes()
vindagores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

lista_programas_acao = PlayList('ação')
lista_programas_aventura = PlayList('aventura')
lista_programas_terror = PlayList('terror')
lista_programas_super_heroi = PlayList('super-herói')

listas_recomendacao = [lista_programas_acao, lista_programas_aventura, lista_programas_terror, lista_programas_super_heroi]

for lista in listas_recomendacao:
    lista.receber_dados()
    print(lista)
    print()