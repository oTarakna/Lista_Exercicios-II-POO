from abc import ABC, abstractmethod
from models.salvavel import Salvavel


class Armazenador(ABC):
    def __init__(self,dado):
        self.dado = dado

    def salvar(dado):
        pass



def executarSalvamentoFormal(Armazenador: Armazenador, dado):
    Armazenador.salvar(dado)

def executarSalvamentoFlexivel(objeto: Salvavel, dado):
    objeto.salvar(dado)
