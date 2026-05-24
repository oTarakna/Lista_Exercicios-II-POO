from ui.menu import mostrarMenu

from models.video import Video
from models.podcast import Podcast
from models.textonarrado import TextoNarrado


class Plataforma:

    def __init__(self, nome):
        self.nome = nome
        self.listaDeMidia = []

    def adicionarMidia(self, midia):
        self.listaDeMidia.append(midia)

    def listaMidia(self):

        print(f"\n--- MÍDIAS DA {self.nome} ---")

        if len(self.listaDeMidia) == 0:
            print("Nenhuma mídia cadastrada.")
            return

        for midia in self.listaDeMidia:
            midia.mostrarInfo()

    def reproduzirTodas(self):

        print("\n--- REPRODUZINDO TODAS ---")

        if len(self.listaDeMidia) == 0:
            print("Nenhuma mídia cadastrada.")
            return

        for midia in self.listaDeMidia:
            midia.reproduzir()



plataforma = Plataforma("Educação Online")

while True:

    mostrarMenu()

    opcao = input("Escolha uma opção: ")

    match opcao:

        case "1":

            titulo = input("Título do vídeo: ")
            duracao = input("Duração: ")
            resolucao = input("Resolução: ")

            video = Video(titulo, duracao, resolucao)

            plataforma.adicionarMidia(video)

            print("Vídeo adicionado com sucesso!")

        case "2":

            titulo = input("Título do podcast: ")
            duracao = input("Duração: ")
            apresentador = input("Apresentador: ")

            podcast = Podcast(
                titulo,
                duracao,
                apresentador
            )

            plataforma.adicionarMidia(podcast)

            print("Podcast adicionado com sucesso!")

        case "3":

            titulo = input("Título do texto narrado: ")
            duracao = input("Duração: ")
            idioma = input("Idioma: ")

            texto = TextoNarrado(
                titulo,
                duracao,
                idioma
            )

            plataforma.adicionarMidia(texto)

            print("Texto narrado adicionado com sucesso!")

        case "4":
            plataforma.listaMidia()

        case "5":
            plataforma.reproduzirTodas()

        case "0":
            print("Sistema encerrado.")
            break

        case _:
            print("Opção inválida!")
