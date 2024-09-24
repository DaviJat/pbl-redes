import socket
import json

# Função para enviar a requisição para o servidor
def enviar_requisicao(method, data):
    # Gera a requisição a ser enviada para o servidor
    request = {
        "method": method,
        "data": data
    }

    # Dicionário para armazenar dados da requisição
    data_request = {}

    # Abre o socket de conexão e envia a requisição
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, int(SERVER_PORT)))
    client_socket.send(json.dumps(request).encode("utf-8"))

    # Recebe resposta do cliente
    server_response = client_socket.recv(8192).decode('utf-8')
    response = json.loads(server_response)

    print(response)

    client_socket.close()

# Função de conexão ao servidor
def iniciar_conexao():
    # ip = ip_entry.get() descomentar
    # port = port_entry.get() descomentar

    ip = "servidor"
    port = 61582 # Adiciona a porta diretamente


    global SERVER_IP, SERVER_PORT
    SERVER_IP, SERVER_PORT = ip, port

    # Executa a simulação das requisições do cliente

    method = "menu_principal"
    data = {"origem": "São Paulo", "destino": "Rio de Janeiro"}

    # Solicita o menu principal para mostrar ao usuário
    enviar_requisicao(method, data)

    method = "escolher_destino"
    data = {}

    enviar_requisicao(method, data)

    method = "comprar_rota"
    data = {"rota": "1: São Paulo -> Rio de Janeiro (Distância: 430km) - Disponível"}

    enviar_requisicao(method, data)

# Função para iniciar o navegador
def iniciar_navegador():
    global navegador, ip_entry, port_entry, SERVER_IP, SERVER_PORT

    # Inicia a conexão de forma automática, sem o navegador do cliente
    iniciar_conexao()


# Chamada para iniciar o navegador
iniciar_navegador()
