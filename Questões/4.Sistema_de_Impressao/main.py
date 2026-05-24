from ui.menu import mostrar_menu

from models.boleto import Boleto
from models.etiqueta import Etiqueta
from models.relatorioSimples import RelatorioSimples

from models.processador import processarImpressao


lista_de_impressoes = []


while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    match opcao:

        # BOLETO
        case "1":

            codigo = input("Código do boleto: ")
            valor = float(input("Valor: "))
            requisito = input("Requisito: ")

            boleto = Boleto(
                codigo,
                valor,
                requisito
            )

            lista_de_impressoes.append(boleto)

            print("Boleto criado com sucesso!")

        # ETIQUETA
        case "2":

            destinatario = input("Destinatário: ")
            endereco = input("Endereço: ")
            requisito = input("Requisito: ")

            etiqueta = Etiqueta(
                destinatario,
                endereco,
                requisito
            )

            lista_de_impressoes.append(etiqueta)

            print("Etiqueta criada com sucesso!")

        # RELATÓRIO
        case "3":

            titulo = input("Título: ")
            requisito = input("Requisito: ")

            relatorio = RelatorioSimples(
                titulo,
                requisito
            )

            lista_de_impressoes.append(relatorio)

            print("Relatório criado com sucesso!")

        # IMPRIMIR
        case "4":

            print("\n--- IMPRIMINDO DOCUMENTOS ---")

            if len(lista_de_impressoes) == 0:
                print("Nenhum item cadastrado.")
                continue

            for item in lista_de_impressoes:
                processarImpressao(item)
                print()

        # SAIR
        case "0":

            print("Sistema encerrado.")
            break

        case _:

            print("Opção inválida!")
