from abc import ABC, abstractmethod


#CLASSE MÃE
class Midia(ABC):
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
    
    
    def mostrarInfo(self):
        print(f"TItulo = {self.titulo}\nDuração = {self.duracao}")


    @abstractmethod
    def reproduzir(self):
        pass
