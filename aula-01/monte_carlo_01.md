# Lançamento de duas moedas.

## Problema

Lançamos duas moedas justas ao mesmo tempo e queremos verificar, através de uma série de simulações, a convergência para o valor exato.

### Solução Analítica

Quando lançamos uma moeda justa, temos a mesma probabilidade de sair cara (H, head), ou coroa (T, tail):
`
P(H) = P(T) = 0.5
`
Ao lançarmos as duas moedas, o resultado da moeda 1 é independente do resultado da moeda 2, desta maneira, podemos calcular a probabilidade de sair cara em ambras, por exemplo, como sendo o produto da probabilidade de cada uma sair cara:
`
P(HH) = P(H)P(H) = (0.5)(0.5 = 0.25
`

### Simulação

Queremos realizar uma simulação para verificar que a medida que jogamos as duas moedas um bom número de vezes e verificar que a medida que jogamos as moedas mais e mais vezes, o  valor se aproxima de 0.25.

#### Passos

1. Criar uma repesentação das moedas.
2. Simular o lançamento das moedas. Isto significa realizar o experimento.
3. Verificar se o resultado do lançamento das moedas corresponde ao evento que queremos estudar: `e = {H, H}`
4. Se o passo 3 retornar verdadeiro, somar 1 a um contador
5. Repita os passos de 2 à 4 até o número de realizações

## Atividade

Copie o código abaixo, complete de forma a realizar a simulação acima. Teste para diferentes valores de `n_runs`: `10, 100, 1000, 10000, 100000`

```python
import numpy as np
import matplotlib.pyplot as plt

def coin_flip_experiment():
    """Simula o lançamento de duas moedas justas e verifica se ambas sairam como H.

    Returns:
        [int]: 0 ou 1 dependendo do resultado do experimento
    """
    coin_1 = # COMPLETE
    coin_2 = # COMPLETE
    
    # Dica: pesquise sobre o método `random.choice()` da biblioteca `NumPy`
    flip_result_1 = # COMPLETE
    flip_result_2 = # COMPLETE

    if # COMPLETE':
        return 1
    else:
        return 0


def gen_graph(exact_value, n_runs, prob, runs):
    """constrói o gráfico das simulações

    Args:
        exact_value (float): Valor exato do experimento
        n_runs (int)): # de execuções
        prob (list): Probabilidades calculadas para cada realização
        runs (list): # de execuções
    """
    plt.hlines(exact_value, 0, n_runs, colors='brown', label='valor exato = 0.25')
    plt.plot(runs, prob, label='Lançamento de duas moedas')
    plt.xlabel('# de lançamentos')
    plt.ylabel('Probabilidade de sair {hh}')
    plt.legend()
    plt.show()


def main():
    n_runs = # COMPLETE
    count = 0
    exact_value = 0.25

    prob = []
    runs = []

    for run in range(n_runs):
        count += # COMPLETE
        prob.append(count/(run+1))
        runs.append(run+1)

    gen_graph(exact_value, n_runs, prob, runs)    

if __name__ == '__main__':
    main()
```
