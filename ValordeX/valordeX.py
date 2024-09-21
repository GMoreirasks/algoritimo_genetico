import numpy as np

# Configurações
POPULACAO_TAMANHO = 100
TAXA_MUTACAO = 0.09
NUM_GERACOES = 100
CROSSOVER_PONTOS = 2
ELITISMO = True
PERCENTUAL_ELITISTA = 0.2
MIN_X = -10
MAX_X = 10
BITS = 20

def funcao(x):
    return x**3 - 6*x + 14

def bin_to_dec(b):
    decimal = int(''.join(map(str, b)), 2)
    return MIN_X + (decimal / (2**BITS - 1)) * (MAX_X - MIN_X)

class Individuo:
    def __init__(self, genoma=None):
        if genoma is None:
            self.genoma = np.random.randint(2, size=BITS)
        else:
            self.genoma = genoma
        self.aptidao = self.avaliar()

    def avaliar(self):
        x = bin_to_dec(self.genoma)
        return funcao(x)

def selecionar(populacao):
    torneio = np.random.choice(populacao, size=2)
    return min(torneio, key=lambda ind: ind.aptidao)

def crossover(pai1, pai2):
    ponto_corte1 = np.random.randint(1, BITS - 1)
    if CROSSOVER_PONTOS == 2:
        ponto_corte2 = np.random.randint(ponto_corte1 + 1, BITS)
        filho_genoma = np.concatenate((pai1.genoma[:ponto_corte1], pai2.genoma[ponto_corte1:ponto_corte2], pai1.genoma[ponto_corte2:]))
    else:
        filho_genoma = np.concatenate((pai1.genoma[:ponto_corte1], pai2.genoma[ponto_corte1:]))
    return Individuo(genoma=filho_genoma)

def mutacao(individuo):
    for i in range(BITS):
        if np.random.rand() < TAXA_MUTACAO:
            individuo.genoma[i] = 1 - individuo.genoma[i]

def algoritmo_genetico(populacao_tamanho=POPULACAO_TAMANHO, taxa_mutacao=TAXA_MUTACAO, num_geracoes=NUM_GERACOES):
    populacao = [Individuo() for _ in range(populacao_tamanho)]
    melhores = []

    for geracao in range(num_geracoes):
        nova_populacao = []

        if ELITISMO:
            num_elitistas = int(populacao_tamanho * PERCENTUAL_ELITISTA)
            elitistas = sorted(populacao, key=lambda ind: ind.aptidao)[:num_elitistas]
            nova_populacao.extend(elitistas)

        while len(nova_populacao) < populacao_tamanho:
            pai1 = selecionar(populacao)
            pai2 = selecionar(populacao)
            filho = crossover(pai1, pai2)
            mutacao(filho)
            nova_populacao.append(filho)

        populacao = nova_populacao
        melhores.append(min(populacao, key=lambda ind: ind.aptidao))

    melhor_individuo = min(melhores, key=lambda ind: ind.aptidao)
    x_min = bin_to_dec(melhor_individuo.genoma)
    aptidao_min = melhor_individuo.aptidao

    return x_min, aptidao_min

if __name__ == "__main__":
    x_min, aptidao_min = algoritmo_genetico(
        populacao_tamanho=10,
        taxa_mutacao=0.01,
        num_geracoes=100
    )
    print(f'O valor de x que minimiza a funcao e aproximadamente {x_min:.4f} com aptidao {aptidao_min:.4f}')
