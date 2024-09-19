import networkx as nx

# Definir as cidades brasileiras
cidades = ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza',
           'Belo Horizonte', 'Manaus', 'Curitiba', 'Recife', 'Porto Alegre']

# Definir as distâncias reais entre as cidades (em km) e a quantidade de passagens disponíveis por trecho
distancias = {
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

# Criar o grafo
G = nx.Graph()

# Adicionar as arestas com as distâncias reais e a quantidade de passagens disponíveis
for (cidade1, cidade2), (distancia, passagens) in distancias.items():
    G.add_edge(cidade1, cidade2, weight=distancia, tickets=passagens)

# Mostrar as cidades disponíveis para o usuário
print("Cidades disponíveis:")
for i, cidade in enumerate(cidades, start=1):
    if i < 10:
        print(f"0{i} - {cidade}")
    else:
        print(f"{i} - {cidade}")

# Pedir ao usuário para escolher a origem e o destino
origem = int(input("\nEscolha o número da cidade de origem: "))-1
destino = int(input("Escolha o número da cidade de destino: "))-1

cidade_origem = cidades[origem]
cidade_destino = cidades[destino]

# Encontrar todas as rotas possíveis entre origem e destino
caminhos_possiveis = []
for path in nx.all_simple_paths(G, source=cidade_origem, target=cidade_destino):
    count = 0
    passagens_disponiveis = True
    for u, v in zip(path, path[1:]):
        if G[u][v]['tickets'] == 0:
            passagens_disponiveis = False  # Marca como indisponível

    distancia = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
    status = "Disponível" if passagens_disponiveis else "Indisponível"
    caminhos_possiveis.append((path, distancia, status))

caminhos_possiveis.sort(key=lambda x: x[1])

# Exibir as 10 primeiras rotas ordenadas
print(f"\nRotas possíveis de {cidade_origem} para {cidade_destino}, ordenadas por distância (máximo 10 rotas):")
for i, (caminho, distancia, status) in enumerate(caminhos_possiveis[:10], start=1):
    print(f"{i}: {' -> '.join(caminho)} (Distância: {distancia} km) - {status}")

# Solicitar ao usuário que escolha uma rota disponível
if any(status == "Disponível" for _, _, status in caminhos_possiveis):
    while True:
        rota_escolhida = int(input("\nEscolha o número da rota disponível que deseja usar: ")) - 1
        if caminhos_possiveis[rota_escolhida][2] == "Disponível":
            break
        else:
            print("Rota indisponível, escolha outra.")

    # Atualizar as passagens disponíveis nas arestas do caminho escolhido
    for u, v in zip(caminhos_possiveis[rota_escolhida][0], caminhos_possiveis[rota_escolhida][0][1:]):
        G[u][v]['tickets'] -= 1
        print(f"Passagens restantes no trecho {u} -> {v}: {G[u][v]['tickets']}")
else:
    print("\nNão há rotas disponíveis com passagens.")