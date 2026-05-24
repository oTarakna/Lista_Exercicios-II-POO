from models.armazenador import Armazenador


class ArmazenadorBanco(Armazenador):
    def salvar(self):
        print(f"({self.dado}) Salvo no Banco)")
