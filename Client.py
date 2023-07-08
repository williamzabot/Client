from socket import *

# no servidor é utilizada a connection para enviar uma mensagem para o cliente
# enquanto no cliente é utilizado o socketServer
serverHost = "localhost"
serverPort = 1024
socketClient = socket(AF_INET, SOCK_STREAM)
print('Cliente solicitando conexão com o servidor ...')
socketClient.connect((serverHost, serverPort))
print('Cliente conectado com o servidor ...')

def receive():
    return socketClient.recv(1024).decode("utf-8")

def send(message):
    socketClient.send(message.encode("utf-8"))

while True:
    msgServidor = socketClient.recv(1024).decode("utf-8")
    print(msgServidor)
    msg = str(input("Escolha: "))
    socketClient.send(msg.encode("utf-8"))
    if msgServidor == ":q":
        socketClient.close()
        break


