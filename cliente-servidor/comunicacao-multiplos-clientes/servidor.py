import socket
import threading
import random

# Função para enviar a lista atualizada para todos os clientes conectados
def broadcast_list(cities):
    global clients
    for client in clients:
        try:
            # Enviar a lista atualizada para o cliente
            client.sendall(f"Lista atualizada: {cities}\n".encode("utf-8"))
        except socket.error:
            clients.remove(client)  # Remove o cliente se houver erro na conexão

# Função para lidar com cada cliente
def handle_client(client_socket, client_address, cities):
    print(f"Servidor estabeleceu conexão com o cliente: {client_address}\n")
    clients.append(client_socket)

    while True:
        # Enviar a lista atualizada para o cliente
        try:
            socketConnection.sendall(f"Escolha um índice da lista para remover: {cities}\n".encode("utf-8"))
            msg_bytes = socketConnection.recv(1024)
            if not msg_bytes:
                break
            index_str = msg_bytes.decode("utf-8")

            # Verificar se o índice é válido
            if index_str.isdigit():
                index = int(index_str)
                if 0 <= index < len(cities):
                    removed_item = cities.pop(index)
                    print(f"Cliente {address} removeu o item: {removed_item}")
                    # Atualizar todos os clientes
                    broadcast_list(cities)
                else:
                    socketConnection.send("Índice inválido. Tente novamente.\n".encode("utf-8"))
            else:
                socketConnection.send("Entrada inválida. Por favor, insira um número.\n".encode("utf-8"))

        except Exception as e:
            print(f"Erro: {e}")
            break

    # Remover o cliente da lista
    socketConnection.close()
    clients.remove(socketConnection)
    print(f"Cliente {address} desconectado.\n")


# Definir a porta e o IP do servidor
SERVER_PORT = 45209
SERVER_IP = socket.gethostbyname(socket.gethostname())

# Lista compartilhada de itens
brazilian_cities = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Brasília', 'Fortaleza',
                    'Belo Horizonte', 'Manaus', 'Curitiba', 'Recife', 'Porto Alegre']
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(5)

print(f"IP do servidor: {SERVER_IP}")
print(f"Porta do servidor: {SERVER_PORT}")
print("Esperando por clientes...\n")

while True:
    # Aceitar a conexão de novos clientes
    socketConnection, address = server.accept()
    # Criar uma nova thread para lidar com o cliente
    client_thread = threading.Thread(target=handle_client, args=(socketConnection, address, brazilian_cities))
    client_thread.start()