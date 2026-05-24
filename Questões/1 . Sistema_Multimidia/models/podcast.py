from midia import Midia



#CLASSE VIDEO
class Podcast(Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador


    def reproduzir(self):
        print(f"O Podcast está sendo reproduzido, \nTitulo = {self.titulo}, Apresentador = {self.apresentador}")
