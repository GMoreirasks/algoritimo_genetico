Esse projeto executa um código de um algorítimo genético para encontrar o valor de x que vai minimizar a função de f(X) = x³ - 6x + 14, considerando que x é um número Real no intervalo de [-10,10]



# COMO FUNCIONA

O algoritmo genético simula um processo evolutivo para encontrar soluções cada vez melhores para o problema de minimização. Ou seja, ele trabalha uma população de indíviduos, onde cada um um representa uma solução em potencial



# CONFIGURAÇÕES

Configurações estão alocadas no começo do código para que vc possa lembrar de configurar primeiro antes de rodar:

POPULACAO_TAMANHO: Número de indivíduos na população.
TAXA_MUTACAO: Probabilidade de mutação em cada bit do genoma.
NUM_GERACOES: Número máximo de gerações a serem executadas.
CROSSOVER_PONTOS: Número de pontos de corte no crossover (1 ou 2).
ELITISMO: Define se o elitismo será utilizado ou não.
PERCENTUAL_ELITISTA: Percentual de melhores indivíduos que serão preservados para a próxima geração (se o elitismo estiver ativado).
MIN_X e MAX_X: Intervalo de valores reais para x.
BITS: Número de bits usados para codificar x.


# USO

1. Clone o repositório ou copie o código para sua maquina local.

2. Instale o NumPy(caso não tenha instalado)


pip install numpy

3. Execute o script: 
(Certifique-se de utilizar o caminho correto na sua maquina, ou abra o arquivo e utilize a extensão de python no vsCode que permite executar o código no canto superior direito)
cd algo_gen
cd ValordeX
cd valordeX.py
python valordeX.py


O script irá retornar o valor aproximado de x que minimiza a função, juntamente com a aptidão mínima (valor da função nesse ponto).  De acordo com as configurações que vc utilizou.


# DEPENDÊNCIAS

python 
NumPy