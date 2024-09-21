import socket
import threading
import json
import networkx as nx

CITIES = ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza', 'Belo Horizonte', 'Manaus', 'Curitiba', 'Recife', 'Porto Alegre']

DISTANCES = {
    ('São Paulo', 'Rio de Janeiro'): (430, 10),
    ('São Paulo', 'Brasília'): (1015, 5),
    ('São Paulo', 'Salvador'): (1960, 3),
    ('São Paulo', 'Fortaleza'): (3120, 2),
    ('São Paulo', 'Belo Horizonte'): (585, 8),
    ('São Paulo', 'Manaus'): (3930, 4),
    ('São Paulo', 'Curitiba'): (410, 6),
    ('São Paulo', 'Recife'): (2670, 2),
    ('São Paulo', 'Porto Alegre'): (1115, 5),
    ('Rio de Janeiro', 'Brasília'): (1160, 6),
    ('Rio de Janeiro', 'Salvador'): (1660, 4),
    ('Rio de Janeiro', 'Fortaleza'): (2800, 1),
    ('Rio de Janeiro', 'Belo Horizonte'): (440, 7),
    ('Rio de Janeiro', 'Manaus'): (3680, 3),
    ('Rio de Janeiro', 'Curitiba'): (850, 5),
    ('Rio de Janeiro', 'Recife'): (2330, 3),
    ('Rio de Janeiro', 'Porto Alegre'): (1550, 2),
    ('Brasília', 'Salvador'): (1440, 6),
    ('Brasília', 'Fortaleza'): (2200, 2),
    ('Brasília', 'Belo Horizonte'): (740, 7),
    ('Brasília', 'Manaus'): (3490, 1),
    ('Brasília', 'Curitiba'): (1370, 5),
    ('Brasília', 'Recife'): (2200, 3),
    ('Brasília', 'Porto Alegre'): (2020, 4),
    ('Salvador', 'Fortaleza'): (1020, 3),
    ('Salvador', 'Belo Horizonte'): (1370, 6),
    ('Salvador', 'Manaus'): (4430, 2),
    ('Salvador', 'Curitiba'): (2290, 4),
    ('Salvador', 'Recife'): (800, 5),
    ('Salvador', 'Porto Alegre'): (3070, 2),
    ('Fortaleza', 'Belo Horizonte'): (2520, 3),
    ('Fortaleza', 'Manaus'): (5680, 1),
    ('Fortaleza', 'Curitiba'): (3680, 2),
    ('Fortaleza', 'Recife'): (800, 6),
    ('Fortaleza', 'Porto Alegre'): (4570, 1),
    ('Belo Horizonte', 'Manaus'): (3930, 2),
    ('Belo Horizonte', 'Curitiba'): (1000, 4),
    ('Belo Horizonte', 'Recife'): (2090, 3),
    ('Belo Horizonte', 'Porto Alegre'): (1710, 5),
    ('Manaus', 'Curitiba'): (4360, 1),
    ('Manaus', 'Recife'): (5900, 1),
    ('Manaus', 'Porto Alegre'): (4900, 1),
    ('Curitiba', 'Recife'): (3030, 2),
    ('Curitiba', 'Porto Alegre'): (710, 7),
    ('Recife', 'Porto Alegre'): (3700, 2),
}

G = nx.Graph()

for (origin, destination), (distance, ticket) in DISTANCES.items():
        G.add_edge(origin, destination, weight=distance, tickets=ticket)

client_route = {}

def handle_client(client_socket):
    while True:
        try:
            request = client_socket.recv(4096).decode('utf-8')
            if not request:
                break

            response = {"page_layout": []}

            if request == "menu_principal":
                response["page_layout"].append({
                    "dropdown": {
                        "label": "Origem",
                        "options": CITIES,
                        "method": "select_origem"
                    }
                })
                response["page_layout"].append({
                    "dropdown": {
                        "label": "Destino",
                        "options": CITIES,
                        "method": "select_destino"
                    }
                })
                response["page_layout"].append({
                    "button": {
                        "label": "Buscar Rotas",
                        "method": "buscar_rotas"
                    }
                })

                client_socket.send(json.dumps(response).encode('utf-8'))

            elif request.startswith('select_origem:') or request.startswith('select_destino:'):
            # Armazena as seleções para processamento posterior
                client_socket.send(b'Escolha uma origem e um destino e clique em Buscar Rotas.')

            elif request == 'buscar_rotas':
                origin =
                destination =

                possible_paths = []
                for path in nx.all_simple_paths(G, source=origin, target=destination):
                    available_tickets = True
                    for u, v in zip(path, path[1:]):
                        if G[u][v]['tickets'] == 0:
                            available_tickets = False
                            break

                    distancia = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
                    status = "Disponível" if available_tickets else "Indisponível"
                    possible_paths.append((path, distancia, status))

                possible_paths.sort(key=lambda x: x[1])
                

    client_socket.close()

def send_error(client_socket, message):
    response = {"page_layout": [{"label": f"Erro: {message}"}]}
    client_socket.send(json.dumps(response).encode('utf-8'))

def handle_rota_choice(client_socket, origin, destination):
    possible_path = []

    for path in nx.all_simple_paths(G, source=origin, target=destination):
        tickets_available = all(G[u][v]['tickets'] > 0 for u, v in zip(path, path[1:]))
        distance = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
        status = "Disponível" if tickets_available else "Indisponível"
        possible_path.append((path, distance, status))

    possible_path.sort(key=lambda x: x[1])

    response = {"page_layout": [{"label": f"Rotas de {origin} para {destination}:"}]}
    for i, (path, distance, status) in enumerate(possible_path[:10], start=1):
        response["page_layout"].append({
            "label": f"{i}: {' -> '.join(path)} (Distância: {distance} km) - {status}"
        })

    client_socket.send(json.dumps(response).encode('utf-8'))

def start_server():
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    SERVER_PORT = 3000

    # Criação do socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", SERVER_PORT))
    server_socket.listen(5)

    print(f"Servidor rodando em {SERVER_IP} porta :{SERVER_PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

start_server()

