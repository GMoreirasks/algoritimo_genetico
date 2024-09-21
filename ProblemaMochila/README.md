**Problemam da mochila** 

Este projeto vai utilizar um algorítimo genético para resolver o problema da mochila que consite em selecioanr itens de uma lista com pesos e valores, maximizando o valor total enquanto não ultrapassa um peso máximo permitido.


# CONFIGURAÇÕES 
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

Deixei as configurações com a entrada que foi passada no slide, mas é possível alterar por aqui de acordo com a população que vc quer analisar. Basta alterar estes valores ao final do código e rodar novamente.


# INSTALAÇÃO
1. Clone o repositório ou copie o código para sua maquina local.

2. Instale o NumPy(caso não tenha instalado)
bash
pip install numpy

3. Execute o script: 
(Certifique-se de utilizar o caminho correto na sua maquina, ou abra o arquivo e utilize a extensão de python no vsCode que permite executar o código no canto superior direito)
cd algo_gen
cd ProblemaMOchila
cd teste2.py
python teste2.py


Ao executar o código acima, você verá a saída com o valor total, o indivíduo selecionado e a média dos pesos para cada geração.

se você pegar a media dos pesos e somar com o número de cromossomos escolhidos (1) você tera o peso total e vai ver também que não ira passar do peso máximo, mas sempre vai estar próximo do valor. 


