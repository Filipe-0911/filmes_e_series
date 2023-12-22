from classes.Filme import Filme
from classes.Serie import Serie
from classes.PlayList import PlayList

vingadores = Filme('vingadores - guerra infinita')
atlanta = Serie('the walking dead')
tmep = Filme('todo mundo em pânico')
demolidor = Serie('demolidor')
star_wars = Filme('star wars - a vingança dos sith')
friends = Serie('Friends')

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
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