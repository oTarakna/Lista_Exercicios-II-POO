from midia import Midia

#CLASSE TEXTO NARRADO
class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self.idioma = idioma


    def reproduzir(self):
        print(f"Texto narrado está sendo reprozido, \nTitulo = {self.titulo}, Idioma = {self.idioma}")
