from classes.Filme import Filme
from classes.Serie import Serie
from classes.PlayList import PlayList
from classes.Crud import Crud

# Filmes
vingadores = Filme('vingadores - guerra infinita')
vingadores_ultron = Filme('vingadores - a era de ultron')
tmep = Filme('todo mundo em pânico')
star_wars = Filme('star wars - a vingança dos sith')
o_chamado = Filme('the ring')
toy_story = Filme('Toy Story')
a_batalha_de_natal = Filme('a batalha de natal')
brilho_eterno = Filme('brilho eterno de uma mente sem lembranças')
show_de_truman = Filme('show de truman')
eu_sei_o_que_vcs_fizeram_no_verao_passado = Filme('eu sei o que vocês fizeram no verão passado')
esposa_de_mentirinha = Filme('esposa de mentirinha')
as_branquelas = Filme('as branquelas')

# Series
twd= Serie('the walking dead')
demolidor = Serie('demolidor')
friends = Serie('friends')
mr_robot = Serie('mr robot')
tbbt = Serie('the big bang theory')
a_casa_do_dragao = Serie('House of the dragon')
young_sheldon = Serie('young sheldon')

# Playlists
lista_programas_acao = PlayList('ação')
lista_programas_aventura = PlayList('aventura')
lista_programas_terror = PlayList('terror')
lista_programas_comedia = PlayList('comédia')
lista_programas_drama = PlayList('drama')

# Dar likes
twd.dar_likes()
twd.dar_likes()
twd.dar_likes()
twd.dar_likes()
twd.dar_likes()
twd.dar_likes()

listas_criadas = [lista_programas_acao, lista_programas_aventura, lista_programas_terror, lista_programas_comedia, lista_programas_drama]

def imprime_listas_criadas(listas):  
    for lista in listas:
        lista.receber_dados()
        print(lista)
        print()

def verificar_programas_com_mais_likes():
    banco = Crud
    lista_tuplas = banco.recomenda_conforme_likes()
    
    for programa in lista_tuplas:
        print(f"Nome: {programa[1]}, Likes: {programa[4]}")


imprime_listas_criadas(listas_criadas)
verificar_programas_com_mais_likes()