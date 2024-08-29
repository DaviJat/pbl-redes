import socket

SERVER_PORT = 12000
SERVER_IP = "localhost"

while True:
    try: 
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))

        message = input("Mensagem para o servidor: ")

        client_socket.send(message.encode("utf-8"))

        client_socket.close()

        print('Mensagem enviada. A conexão foi encerrada.')
        
    except Exception as error:
        print(f"Ocorreu um erro: {error}")
