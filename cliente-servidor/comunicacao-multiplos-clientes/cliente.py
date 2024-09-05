import socket # Importa o módulo socket para permitir a comunicação em rede

while True:
        # Solicita ao usuário o endereço IP do servidor e a porta para a conexão
        print("----- Iniciar nova conexão -----")
        ip_servidor = input("IP do servidor: ")
        porta_servidor = input("Porta do servidor: ")

        # Cria um socket cliente usando o protocolo IPv4 (AF_INET) e TCP (SOCK_STREAM)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Inicia conexão com servidor do endereço fornecido
        client_socket.connect((ip_servidor, int(porta_servidor)))
        print("----- Conexão estabelecida -----\n")

        # Loop com a troca de mensagens entre cliente e servidor
        while True:
            # Recebe a resposta do servidor, até 248 bytes, e decodifica de UTF-8 para string.    
            received_message = client_socket.recv(248).decode("utf-8")
            print(received_message)

            # Envia resposta digitada para o servidor codificada em formato UTF-8
            message_to_send = input("Informe o índice da cidade para remover: ")
            client_socket.send(message_to_send.encode("utf-8"))

            # Recebe resposta da lista atualizada
            received_message = client_socket.recv(248).decode("utf-8")
            print(received_message)
        
            
                
