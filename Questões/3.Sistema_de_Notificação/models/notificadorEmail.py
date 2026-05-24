from notificador import Notificador

class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        print(f"Email:  {mensagem}")
