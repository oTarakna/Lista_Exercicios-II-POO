from models.midia import Midia



#CLASSE PLATAFORMA
class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.listaDeMidia = []


    def adicionarMidia(self,midia):
        self.listaDeMidia.append(midia)

    
    def listaMidia(self):
        print(f"\n---Mostrando dados {self.nome}---")
        for midia in self.listaDeMidia:
            midia.mostrarInfo()


    def reproduzirTodas(self):
        print("\n---Vou ser Reproduzido---")
        for midia in self.listaDeMidia:
            midia.reproduzir()
