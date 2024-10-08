import socket
import json
import threading
from funcoes_servidor import *

# Função que lida com a comunicação com o cliente
def tratar_cliente(client_socket):
    try:
         # Recebe a requisição do cliente
        request = client_socket.recv(8192).decode('utf-8')
        print(f"Requisição recebida: {request}")

        # Converte a string JSON para um dicionário
        request_data = json.loads(request)
        
        # Acessa os dados da requisição
        method = request_data.get("method")
        data = request_data.get("data")

        # Processamento da requisição e preparo da resposta
        if method == 'menu_principal':
            response = retorna_menu_principal()
        elif method == 'escolher_destino':
            response = retorna_escolha_destino()
        elif method == 'trechos_disponiveis':
            response = retorna_trechos_disponiveis(data)
        elif method == 'comprar_rota':
            response = retorna_confirmacao_rota(data)
        else:
            response = {"page_layout": []}  # Resposta vazia para requisições desconhecidas

        # Envia resposta ao cliente em formato JSON
        client_socket.send(json.dumps(response).encode('utf-8'))
    
    except Exception as e:
        print(f"Erro ao lidar com cliente: {e}")
    
    finally:
        # Fecha a conexão com o cliente após enviar a resposta
        client_socket.close()

# Função para iniciar o servidor
def iniciar_servidor():
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    SERVER_PORT = 61582

    # Criação do socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)

    print(f"servidor rodando em {SERVER_IP} na porta {SERVER_PORT}")

    # Loop para aceitar conexões de clientes
    while True:
        try:
            # Aceita uma nova conexão
            client_socket, addr = server_socket.accept()
            print(f"Conexão aceita de {addr}")

            # Inicia uma nova thread para lidar com o cliente
            client_handler = threading.Thread(target=tratar_cliente, args=(client_socket,))
            client_handler.start()

        except KeyboardInterrupt:
            print("\nservidor encerrado.")
            server_socket.close()
            break

# Inicializa o servidor
iniciar_servidor()
