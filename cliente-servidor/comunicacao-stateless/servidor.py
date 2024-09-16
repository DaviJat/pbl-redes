import socket
import json

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 3000 

# Criação do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

print(f"Servidor rodando em {SERVER_IP}:{SERVER_PORT}")

while True:
    # Aceita uma conexão
    connection, address = server_socket.accept()
    message = connection.recv(1024).decode("utf-8")

    match message:
        case 'menu_principal':
            response = {
                "page_layout": [
                    {"button": {"label": "Mostra lista", "method": "mostra_lista"}},
                    {"button": {"label": "Sair", "method": "sair"}}
                ]
            }
            json_response = json.dumps(response)
            connection.sendall(json_response.encode('utf-8'))
        case 'mostra_lista':
            print('mostra_lista')
        case 'sair':
            print('sair')

    connection.close()
