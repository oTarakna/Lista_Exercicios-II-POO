from notificador import Notificador

class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        print(f"SMS:  {mensagem}")
