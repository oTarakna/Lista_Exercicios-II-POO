from ui.menu import mostrarMenu

from repository.empresa import Empresa

from models.funcionarioAssalariado import FuncionarioAssalariado
from models.funcionarioHorista import FuncionarioHorista
from models.funcionarioComissionado import FuncionarioComissionado


empresa = Empresa("Tech Solutions")


while True:

    mostrarMenu()

    opcao = input("Escolha uma opção: ")

    match opcao:

        # ASSALARIADO
        case "1":

            nome = input("Nome: ")
            cpf = input("CPF: ")
            salario = float(input("Salário Mensal: "))

            funcionario = FuncionarioAssalariado(
                nome,
                cpf,
                salario
            )

            empresa.adicionarFuncionario(funcionario)

            print("Funcionário assalariado cadastrado!")

        # HORISTA
        case "2":

            nome = input("Nome: ")
            cpf = input("CPF: ")
            horas = float(input("Horas Trabalhadas: "))
            valor_hora = float(input("Valor por Hora: "))

            funcionario = FuncionarioHorista(
                nome,
                cpf,
                horas,
                valor_hora
            )

            empresa.adicionarFuncionario(funcionario)

            print("Funcionário horista cadastrado!")

        # COMISSIONADO
        case "3":

            nome = input("Nome: ")
            cpf = input("CPF: ")
            vendas = float(input("Total de Vendas: "))
            percentual = float(
                input("Percentual de Comissão: ")
            )

            funcionario = FuncionarioComissionado(
                nome,
                cpf,
                vendas,
                percentual
            )

            empresa.adicionarFuncionario(funcionario)

            print("Funcionário comissionado cadastrado!")

        # MOSTRAR FUNCIONÁRIOS
        case "4":

            empresa.listarFuncionario()

            empresa.mostrarFolhaDePagamento()

        # SAIR
        case "0":

            print("Sistema encerrado.")
            break

        case _:

            print("Opção inválida!")
