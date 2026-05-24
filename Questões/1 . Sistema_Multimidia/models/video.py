from models.midia import Midia
from abc import ABC, abstractmethod

#CLASSE VIDEO
class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"O Video está sendo reproduzido, \nTitulo = {self.titulo}, Resolucao = {self.resolucao}")
