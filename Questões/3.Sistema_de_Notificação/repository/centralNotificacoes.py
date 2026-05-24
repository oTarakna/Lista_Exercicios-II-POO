from notificador import Notificador


class CentralNotificacoes:
    def __init__(self):
        self.lista_de_notificadores = []

    def adicionar_notificador(self,notificador):
        self.lista_de_notificadores.append(notificador)

    
    def enviar_para_todos(self, mensagem):
        for notificador in self.lista_de_notificadores:
            notificador.notificar(mensagem)
