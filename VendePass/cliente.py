import json
import tkinter as tk
from tkinter import messagebox
import socket

# Criação do navegador do cliente
root = tk.Tk()
root.title("Navegador")

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
                tk.Button(root, text=button_label, command=lambda method=button_method: send_request(method)).pack(pady=10)

    client_socket.close() 

    
def clear_root(root):
    # Remove todos os widgets da janela sem fechá-la
    for widget in root.winfo_children():
        widget.destroy()

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
        clear_root(root)
        global SERVER_IP, SERVER_PORT
        SERVER_IP, SERVER_PORT = ip, port
       
        send_request('menu_principal')

SERVER_IP, SERVER_PORT = None, None

# Campo para IP do servidor
tk.Label(root, text="IP do servidor:").grid(row=0, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

# Campo para porta do servidor
tk.Label(root, text="Porta do servidor:").grid(row=1, column=0, padx=10, pady=10)
port_entry = tk.Entry(root)
port_entry.grid(row=1, column=1, padx=10, pady=10)

 # Botão para conectar
connect_button = tk.Button(root, text="Conectar", command=on_connect)
connect_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()


