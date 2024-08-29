import socket

counter_received = 0
counter_sent = 0

SERVER_PORT = 12000

NUM_BYTES_PACKAGES_RECEIVED = 248

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", SERVER_PORT))

server.listen(5)

while True:
    msg_to_answer = ""
    msg_received_str = ""

    print("Esperando por cliente:")

    socketConnection, address = server.accept()
    print("Servidor estabeleceu conexão com o cliente: " + str(address))

    msg_bytes = socketConnection.recv()
    clientHost, clientPort = socketConnection.getpeername()
    msg_received_str = msg_bytes.decode("utf-8")
                                        
    if msg_received_str != "":
        print("Mensagem recebida pelo cliente:" + str(msg_received_str))
        print("IP do cliente:" + str(clientHost))
        msg = "mensagem recebida, é nois"
    
    socketConnection.send(msg.encode("utf-8"))

    print("Mensagem enviada para o cliente")
    socketConnection.close()