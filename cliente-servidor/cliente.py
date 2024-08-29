import socket

while True:
        print("----- Iniciar nova conexão -----")
        ip_servidor = input("Endereço do servidor: ")
        porta_servidor = input("Porta do servidor: ")

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_servidor, int(porta_servidor)))

        print("----- Conexão estabelecida -----")

        print("\n----- Chat com o servidor -----")

        while True:
            message_to_send = input("Mensagem para o servidor: ")

            client_socket.send(message_to_send.encode("utf-8"))

            if message_to_send == 'exit':
                client_socket.close()    
                print('\n----- Conexão encerrada -----')
                break

            received_message = client_socket.recv(248).decode("utf-8")
            print("Mensagem do servidor: " + received_message)
        
            
                
