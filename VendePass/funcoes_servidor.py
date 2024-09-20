from rotas import criar_grafo, obter_rotas_disponiveis, cidades

# Função que retorna o menu principal
def retorna_menu_principal():
    response = {
        "page_layout": [
            {"button": {"label": "Escolher destino", "method": "escolher_destino"}},
        ]
    }

    return response    

# Função que retorna o menu principal com dois dropdowns e um botão
def retorna_escolha_destino():
    response = {
        "page_layout": [
            {"dropdown": {"name": "origem", "label": "Escolha a origem", "options": cidades}},
            {"dropdown": {"name": "destino", "label": "Escolha o destino", "options": cidades}},
            {"button": {"label": "Enviar Seleções", "method": "trechos_disponiveis"}}
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

def retorna_trechos_disponiveis(data):
    grafo = criar_grafo()
    origem = data.get("origem")
    destino = data.get("destino")

    rotas_disponiveis = obter_rotas_disponiveis(grafo, origem, destino)

    response = {"page_layout": []}

    if rotas_disponiveis:
        rotas = []
        for i, (caminho, distancia, status) in enumerate(rotas_disponiveis, start=1):
            rota_str = f"{i}: {' -> '.join(caminho)} (Distância: {distancia} km) - {status}"
            rotas.append(rota_str)
        response["page_layout"].append({"dropdown": {"name": "rota", "label": "Escolha a rota", "options": rotas}})
    else:
        response["page_layout"].append({"message": "Nenhuma rota disponível."})

    # MOSTRA AS ROTAS, FALTA COLOCAR O BOTAO DE COMPRAR ROTA, QUE VAI CHAMAR UM MÉTODO PARA VERIFICAR SE AINDA ESTÁ DISPONÍVEL,
    # E SEGUIR O RESTO DA LOGICA, SE COMPRAR, TIRAR DO GRAFO, SE NÃO COMPRAR AVISAR QUE ESTÁ INDISPONÍVEL
    return response

