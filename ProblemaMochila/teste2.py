import numpy as np


def calcular_valor_peso(individuo, pesos_e_valores):
    peso_total = sum(pesos_e_valores[i][0] for i in range(len(individuo)) if individuo[i] == 1)
    valor_total = sum(pesos_e_valores[i][1] for i in range(len(individuo)) if individuo[i] == 1)
    return valor_total, peso_total

def calcular_media_pesos(individuo, pesos_e_valores):
    pesos_marcados = [pesos_e_valores[i][0] for i in range(len(individuo)) if individuo[i] == 1]
    if pesos_marcados:
        return np.mean(pesos_marcados)
    else:
        return 0


def avaliar(individuo, pesos_e_valores, peso_maximo):
    valor_total, peso_total = calcular_valor_peso(individuo, pesos_e_valores)
    if peso_total <= peso_maximo:
        return valor_total
    else:
        return 0  


def gerar_populacao(n, tamanho_individuo):
    return [np.random.randint(2, size=tamanho_individuo).tolist() for _ in range(n)]


def selecionar(populacao, fitnesses):
    indices = np.argsort(fitnesses)[::-1]
    selecionados = [populacao[i] for i in indices[:len(populacao)//2]]
    return selecionados


def cruzar(pai1, pai2):
    ponto_corte = np.random.randint(1, len(pai1)-1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def mutar(individuo, taxa_mutacao):
    return [1 - gene if np.random.rand() < taxa_mutacao else gene for gene in individuo]


def algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes, taxa_mutacao=0.01):
    tamanho_individuo = len(pesos_e_valores)
    populacao = gerar_populacao(numero_de_cromossomos, tamanho_individuo)
    melhor_individuo_por_geracao = []

    for geracao in range(geracoes):
        fitnesses = [avaliar(individuo, pesos_e_valores, peso_maximo) for individuo in populacao]
        melhor_individuo = populacao[np.argmax(fitnesses)]
        media_pesos = calcular_media_pesos(melhor_individuo, pesos_e_valores)
        melhor_individuo_por_geracao.append((np.max(fitnesses), melhor_individuo, media_pesos))
        
        populacao_selecionada = selecionar(populacao, fitnesses)
        nova_populacao = []
        while len(nova_populacao) < numero_de_cromossomos:
            pai1, pai2 = np.random.choice(len(populacao_selecionada), 2, replace=False)
            filho1, filho2 = cruzar(populacao_selecionada[pai1], populacao_selecionada[pai2])
            nova_populacao.append(mutar(filho1, taxa_mutacao))
            nova_populacao.append(mutar(filho2, taxa_mutacao))
        
        populacao = nova_populacao[:numero_de_cromossomos]

    return melhor_individuo_por_geracao


pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

resultado = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)
for valor, individuo, media_pesos in resultado:
    print(f"Valor: {valor}, Indiveduo: {individuo}, Media dos Pesos: {media_pesos:.2f}")
