import socket # Importa o módulo socket para permitir a comunicação em rede

# Define a porta do servidor como 3000
SERVER_PORT = 3000 
# Obtém o endereço IP do servidor, pegando o IP da máquina local.
SERVER_IP = socket.gethostbyname(socket.gethostname())

while True:
    # Cria um socket servidor usando o protocolo IPv4 (AF_INET) e TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associa o IP local e a porta fornecida ao socket do servidor
    server_socket.bind((SERVER_IP, SERVER_PORT))

    # Exibe o IP e a porta do servidor
    print("IP do servidor: " + SERVER_IP)
    print("Porta do servidor: " + str(SERVER_PORT))

    # Coloca o servidor em modo de escuta, esperando por conexões (máximo de 1 conexão)
    server_socket.listen(1)
    print("Esperando por cliente: \n")

    # Aceita a conexão com o cliente e captura o socket da conexão e o endereço do cliente
    socketConnection, address = server_socket.accept()
    print("Servidor estabeleceu conexão com o cliente: " + str(address) + "\n")
    print("----- Chat com o cliente -----")

    # Loop com a troca de mensagens entre cliente e servidor
    while True:
        # Recebe a mensagem enviada do cliente (limitando a 248 bytes)
        msg_received_bytes = socketConnection.recv(248)

        # Decodifica os bytes recebidos para string
        msg_received_str = msg_received_bytes.decode("utf-8")

        # Encerra conexão se o cliente enviar a mensagem "exit"
        if msg_received_str != "exit":
            print("Cliente saiu do chat")
            print("----- Conexão Encerrada -----" + "\n\n")
            break
        else:
            # Mostra a mensagem recebida do cliente
            print("Mensagem do cliente: " + str(msg_received_str))
            
            # Envia resposta digitada para o cliente codificada em formato UTF-8
            msg = input("Mensagem para o cliente: ")
            socketConnection.send(msg.encode("utf-8"))
            
    