class RelatorioSimples:
    def __init__(self, titulo, requesito):
        self.titulo = titulo
        self.requesito = requesito


    def imprimir(self) -> None:
        print(f"Informações do Relatório\nTitulo = {self.titulo}\nrequesito = {self.requesito}")
