from abc import ABC, abstractmethod


class Armazenador(ABC):

    def __init__(self, dado):
        self.dado = dado

    @abstractmethod
    def salvar(self):
        pass
