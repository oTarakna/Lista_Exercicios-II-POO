from models.funcionario import Funcionario

class Empresa:

    def __init__(self, nome):
        self.nome = nome
        self.lista_de_funcionario = []

    def adicionarFuncionario(self, funcionario):
        self.lista_de_funcionario.append(funcionario)

    def listarFuncionario(self):

        print(f"\n--- FUNCIONÁRIOS DA {self.nome} ---")

        if len(self.lista_de_funcionario) == 0:
            print("Nenhum funcionário cadastrado.")
            return

        for funcionario in self.lista_de_funcionario:
            funcionario.mostrarDados()
            print()

    def mostrarFolhaDePagamento(self):

        print(f"\n--- FOLHA DE PAGAMENTO: {self.nome} ---")

        total_folha = 0

        if len(self.lista_de_funcionario) == 0:
            print("Nenhum funcionário cadastrado.")
            return

        for funcionario in self.lista_de_funcionario:

            pagamento = funcionario.calcularPagamento()

            if isinstance(pagamento, str):
                pagamento = float(
                    pagamento.replace("R$", "")
                )

            print(
                f"Funcionário: {funcionario.nome} "
                f"| Salário: R$ {pagamento:.2f}"
            )

            total_folha += pagamento

        print(f"\nTotal Geral: R$ {total_folha:.2f}")
