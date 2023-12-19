from classes.Filme import Filme
from classes.Serie import Serie
from classes.PlayList import PlayList

#ESTUDAR MIXINS

vindagores = Filme('vingadores - guerra infinita', 2018, 160, 'ação, aventura, fantasia, fantasia científica')
atlanta = Serie('the walking dead', 2018, 2, 'horror, drama, pós-apocalíptica')
tmep = Filme('todo mundo em pânico', 1999, 100, 'comédia, drama, horror')
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

filmes_e_series = [vindagores, atlanta, demolidor, tmep]
fim_de_semana = PlayList('Fim de semana', filmes_e_series)

for programa in fim_de_semana:
    print(programa)