
class Boleto:
    def __init__(self, codigo, valor, requesito):
        self.codigo = codigo
        self.valor = valor
        self.requesito = requesito

    
    def imprimir(self) -> None:
        print(f"Informações de Boleto\nCod = {self.codigo}\nValor = R${self.valor}")
