from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf =  cpf

    def mostrarDados(self):
        print(f"Nome = {self.nome}\nCPF = {self.cpf}")


    @abstractmethod
    def calcularPagamento(self):
        pass
