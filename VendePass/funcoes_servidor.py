# Função que retorna o menu principal
def retorna_menu_principal():
    response = {
        "page_layout": [
            {"button": {"label": "Mostra lista", "method": "mostra_lista"}},
            {"button": {"label": "Sair", "method": "sair"}}
        ]
    }

    return response    

# Função que retorna o menu principal
def retorna_lista_trechos():
    response = {
        "page_layout": [
            {"button": {"label": "Voltar", "method": "menu_principal"}}
        ]
    }

    return response  