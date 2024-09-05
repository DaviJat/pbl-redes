import socket
import random

SERVER_PORT = random.randint(15000, 65535)
SERVER_IP = socket.gethostbyname(socket.gethostname())

counter_received = 0
counter_sent = 0

NUM_BYTES_PACKAGES_RECEIVED = 248

while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    print("IP do servidor: " + SERVER_IP)
    print("Porta do servidor: " + str(SERVER_PORT))

    server.listen(5)

    print("Esperando por cliente: \n")

    socketConnection, address = server.accept()
    print("Servidor estabeleceu conexão com o cliente: " + str(address) + "\n")
    print(("-"*5) + " Chat com o cliente " + ("-"*5))

    while True:
        msg_bytes = socketConnection.recv(1024)
        clientHost, clientPort = socketConnection.getpeername()
        msg_received_str = msg_bytes.decode("utf-8")

        if msg_received_str != "exit":
            print("Mensagem do cliente: " + str(msg_received_str))
            msg = input("Mensagem para o cliente: ")
            socketConnection.send(msg.encode("utf-8"))
        else:
            print("Cliente saiu do chat")
            print(("-"*5) + " Conexão Encerrada " + ("-"*5) + "\n\n")
            break;
    