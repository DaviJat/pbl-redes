import socket
import os

# Configurações básicas
SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 3000 

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((SERVER_IP, SERVER_PORT))
my_socket.listen(1)

print(SERVER_IP, SERVER_PORT)

while True:
    connection, address = my_socket.accept()
    request = connection.recv(1024).decode('utf-8')
    try:
        # Tentando abrir e ler o arquivo HTML
        file_path = os.path.join(os.path.dirname(__file__), 'index.html')
        print(file_path)

        with open(file_path, 'r') as file:
            response = file.read()

        # Cabeçalho de sucesso
        header = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
        # Transforma o conteúdo do HTML em bytes
        response = response.encode('utf-8')

    except Exception as e:
        print(e)
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<h1>404 Not Found</h1>'.encode('utf-8')

    # Envia a resposta
    final_response = header.encode('utf-8') + response
    connection.send(final_response)
    connection.close()
