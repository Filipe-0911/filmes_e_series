from classes.Filme import Filme
from classes.Serie import Serie
from classes.PlayList import PlayList
from classes.Crud import Crud

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
tmep.dar_likes()
tmep.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes_e_series = [vindagores, atlanta, demolidor, tmep]
fim_de_semana = PlayList('Fim de semana', filmes_e_series)

for programa in fim_de_semana:
    print(programa)