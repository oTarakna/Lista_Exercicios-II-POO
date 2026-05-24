class Etiqueta:
    def __init__(self, destinatario, endereco, requesito):
        self.destinatario =  destinatario
        self.endereco = endereco
        self.requesito = requesito


    def imprimir(self) -> None:
        print(f"Informações de Etiqueta\nEndereço =  {self.endereco}\n requesito = {self.requesito}")
