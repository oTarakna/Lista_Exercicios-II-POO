from notificador import Notificador

class NotificarApp(Notificador):
    def notificar(self, mensagem):
        print(f"APP: {mensagem}")
