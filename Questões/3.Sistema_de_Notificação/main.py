from ui.menu import mostrar_menu

from services.centralNotificacoes import CentralNotificacoes

from models.notificadorEmail import NotificadorEmail
from models.notificadorSMS import NotificadorSMS
from models.notificadorApp import NotificadorApp


central = CentralNotificacoes()


while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    match opcao:

        case "1":

            email = NotificadorEmail()

            central.adicionar_notificador(email)

            print("Notificador EMAIL adicionado!")

        case "2":

            sms = NotificadorSMS()

            central.adicionar_notificador(sms)

            print("Notificador SMS adicionado!")

        case "3":

            app = NotificadorApp()

            central.adicionar_notificador(app)

            print("Notificador APP adicionado!")

        case "4":

            mensagem = input("Digite a mensagem: ")

            central.enviar_para_todos(mensagem)

        case "0":

            print("Sistema encerrado.")
            break

        case _:
