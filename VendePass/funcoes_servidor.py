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

# Mostra 10 melhores trechos disponíveis para o cliente
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

    response["page_layout"].append({"button": {"label": "Comprar rota", "method": "comprar_rota"}})
    response["page_layout"].append({"button": {"label": "Voltar", "method": "escolher_destino"}})

    return response

# Retorna confirmação de compra da rota selecionada
def retorna_confirmacao_rota(data):
    print(data)
    # Exemplo de print
    # {'rota': '3: Brasília -> Belo Horizonte -> Recife (Distância: 2830 km) - Disponível'}

    # Essa rota foi a que o cliente escolheu para comprar
    # Nessa função deve ser feita a confirmação de compra, verificando se essa rota ainda está disponível

    # Se estiver disponível, muda para uma tela simples com um botão (Compra confirmada. voltar ao menu principal)
    # e e remove os trechos dos trechos disponíveis

    # Se NÃO estiver disponível, muda para uma tela com o botão (Rota não está mais disponível indisponível, 
    # voltar para a escolha de destino )
