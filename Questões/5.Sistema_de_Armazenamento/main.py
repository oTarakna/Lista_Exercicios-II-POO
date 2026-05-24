from ui.menu import mostrar_menu

from models.armazenadorArquivo import ArmazenadorArquivo
from models.armazenadorBanco import ArmazenadorBanco
from models.armazenadorNuvem import ArmazenadorNuvem

from services.processador import processar_salvamento


lista_de_armazenamentos = []


while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    match opcao:

        case "1":

            dado = input("Digite o dado: ")

            arquivo = ArmazenadorArquivo(dado)

            lista_de_armazenamentos.append(arquivo)

            print("Armazenador de arquivo criado!")

        case "2":

            dado = input("Digite o dado: ")

            banco = ArmazenadorBanco(dado)

            lista_de_armazenamentos.append(banco)

            print("Armazenador de banco criado!")

        case "3":

            dado = input("Digite o dado: ")

            nuvem = ArmazenadorNuvem(dado)

            lista_de_armazenamentos.append(nuvem)

            print("Armazenador de nuvem criado!")

        case "4":

            print("\n--- PROCESSANDO SALVAMENTOS ---")

            if len(lista_de_armazenamentos) == 0:
                print("Nenhum item cadastrado.")
                continue

            for item in lista_de_armazenamentos:

                processar_salvamento(item)

        case "0":

            print("Sistema encerrado.")
            break

        case _:

            print("Opção inválida!")
