from classes.Filme import Filme
from classes.Serie import Serie
from classes.PlayList import PlayList

# vingadores = Filme('vingadores - guerra infinita')
# atlanta = Serie('the walking dead')
# tmep = Filme('todo mundo em pânico')
# demolidor = Serie('demolidor')
# star_wars = Filme('star wars - a vingança dos sith')
# friends = Serie('friends')
# mr_robot = Serie('mr robot')
# o_chamado = Filme('the ring')
# a_batalha_de_natal = Filme('a batalha de natal')
# as_branquelas = Filme('as branquelas')
# eu_sei_o_que_vcs_fizeram_no_verao_passado = Filme('eu sei o que vocês fizeram no verão passado')

# vingadores.dar_likes()
# vingadores.dar_likes()
# vingadores.dar_likes()
# vingadores.dar_likes()
# vingadores.dar_likes()
# vingadores.dar_likes()

# atlanta.dar_likes()
# atlanta.dar_likes()
# atlanta.dar_likes()
# atlanta.dar_likes()
# atlanta.dar_likes()
# atlanta.dar_likes()

# tmep.dar_likes()
# tmep.dar_likes()
# tmep.dar_likes()
# tmep.dar_likes()

# demolidor.dar_likes()
# demolidor.dar_likes()
# demolidor.dar_likes()

# star_wars.dar_likes()

lista_programas_acao = PlayList('ação')
lista_programas_aventura = PlayList('aventura')
lista_programas_terror = PlayList('terror')
lista_programas_comedia = PlayList('comédia')
lista_programas_drama = PlayList('drama')

listas_recomendacao = [lista_programas_acao, lista_programas_aventura, lista_programas_terror, lista_programas_comedia, lista_programas_drama]

for lista in listas_recomendacao:
    lista.receber_dados()
    print(lista)
    print()