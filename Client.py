from socket import *

# no servidor é utilizada a connection para enviar uma mensagem para o cliente
# enquanto no cliente é utilizado o socketServer
serverHost = "localhost"
serverPort = 50001
socketClient = socket(AF_INET, SOCK_STREAM)
print('Cliente solicitando conexão com o servidor ...')
socketClient.connect((serverHost, serverPort))
print('Cliente conectado com o servidor ...')
while True:
    msg = str(input("Digite uma mensagem: "))
    socketClient.send(msg.encode("utf-8"))
    msgServidor = socketClient.recv(1024).decode("utf-8")
    print(msgServidor)
    if msg == ":q" or msgServidor == ":q":
        socketClient.close()
        break
