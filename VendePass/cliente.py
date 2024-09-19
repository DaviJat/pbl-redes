import tkinter as tk
from tkinter import messagebox
import socket
import json

# Função para limpar a janela do navegador
def clear_navegador(navegador):
    for widget in navegador.winfo_children():
        widget.destroy()

# Função para enviar a requisição para o servidor
def send_request(method):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, int(SERVER_PORT)))
    client_socket.send(method.encode("utf-8"))

    server_response = client_socket.recv(1024).decode('utf-8')
    data = json.loads(server_response)
    
    page_layout = data.get("page_layout", "")
    if page_layout != "":
        for item in page_layout:
            if "button" in item:
                button_data = item["button"]
                button_label = button_data["label"]
                button_method = button_data["method"]
                # Cria botões na interface com base na resposta do servidor
                tk.Button(navegador, text=button_label, command=lambda method=button_method: send_request(method)).pack(pady=10)
    clear_navegador(navegador)

    client_socket.close()

# Função de conexão ao servidor
def on_connect():
    ip = ip_entry.get()
    port = port_entry.get()
    
    # Validações
    if not ip:
        messagebox.showerror("Erro", "Você deve inserir o IP do servidor!")
    elif not port:
        messagebox.showerror("Erro", "Você deve inserir a porta do servidor!")
    else:
        # Limpa a janela
        clear_navegador(navegador)
        global SERVER_IP, SERVER_PORT
        SERVER_IP, SERVER_PORT = ip, port
       
        # Solicita o menu principal para mostrar ao usuário
        send_request('menu_principal')

# Função para iniciar o navegador
def iniciar_navegador():
    global navegador, ip_entry, port_entry, SERVER_IP, SERVER_PORT

    # Criação da janela principal
    navegador = tk.Tk()
    navegador.title("Navegador")

    SERVER_IP, SERVER_PORT = None, None

    # Campo para IP do servidor
    tk.Label(navegador, text="IP do servidor:").grid(row=0, column=0, padx=10, pady=10)
    ip_entry = tk.Entry(navegador)
    ip_entry.grid(row=0, column=1, padx=10, pady=10)

    # Campo para porta do servidor
    tk.Label(navegador, text="Porta do servidor:").grid(row=1, column=0, padx=10, pady=10)
    port_entry = tk.Entry(navegador)
    port_entry.grid(row=1, column=1, padx=10, pady=10)

    # Botão para conectar ao servidor
    connect_button = tk.Button(navegador, text="Conectar", command=on_connect)
    connect_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Inicia o loop principal do Tkinter
    navegador.mainloop()

# Chamada para iniciar o navegador
iniciar_navegador()
