from midia import Midia
from repository.plataforma import Plataforma
from podcast import Podcast
from textonarrado import TextoNarrado
from video import Video

minhaplat = Plataforma("Sosos")

video = Video("Em busca da casa Automatica EP 43","30min","1080")

podcast = Podcast("PodZé", "47", "José Menezes")

textonarrado =  TextoNarrado("A vingança dos que nao foram", "67", "japones")


minhaplat.adicionarMidia(video)

minhaplat.adicionarMidia(podcast)

minhaplat.adicionarMidia(textonarrado)

minhaplat.listaMidia()
minhaplat.reproduzirTodas()
