from models.armazenador import Armazenador

class ArmazenadorArquivo(Armazenador):
    def salvar(self):
        print(f"({self.dado}) Salvo nos Arquivos)")
