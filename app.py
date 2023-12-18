from classes.Filme import Filme
from classes.Serie import Serie
from classes.PlayList import PlayList

#ESTUDAR MIXINS

vindagores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('the walking dead', 2018, 2)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vindagores.dar_likes()
vindagores.dar_likes()
vindagores.dar_likes()
vindagores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

tmep.dar_likes()
tmep.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes_e_series = [vindagores, atlanta, demolidor, tmep]
fim_de_semana = PlayList('Fim de semana', filmes_e_series)

# print(f"Tamanho do playlist: {len(fim_de_semana)}")
# for programa in fim_de_semana:
#     print(programa)