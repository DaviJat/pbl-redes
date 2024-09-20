
# Cidades disponíveis para origem e destino
CITIES = ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza', 'Belo Horizonte', 'Manaus', 'Curitiba', 'Recife', 'Porto Alegre']

# Trechos disponíveis
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
            {"dropdown": {"name": "origem","label": "Escolha a origem", "options": ["Vermelho", "Azul", "Verde", "Amarelo"]}},
            {"dropdown": {"name": "destino","label": "Escolha o destino", "options": ["1", "2", "3", "4"]}},
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
    print("origem:" + data.get("origem"))
    print("destino:" + data.get("destino"))

    response = {
        "page_layout": [
            {"button": {"label": "Voltar", "method": "menu_principal"}}
        ]
    }

    return response