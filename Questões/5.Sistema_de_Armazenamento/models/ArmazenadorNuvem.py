class ArmazenadorNuvem:
    def __init__(self,dado):
        self.dado = dado

    
    def salvar(self) -> None:
        print(f"({self.dado}) Salvo na Nuvem)")
