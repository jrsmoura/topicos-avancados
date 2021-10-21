"""
    Aula 01 -  
Lançamento de uma moeda justa: S = {h, t} => P(h) = P(t) = 1/2

e = {sair h}

Lançamento de duas moedas não viciadas.
e = {ambas sairem h}

Lançamento de um dado e de uma moeda, ambos justos.
e = {sair t na moeda e 3 no dado}
"""
import numpy as np
import matplotlib.pyplot as plt

def coin_flip_experiment():
    """[summary]

    Returns:
        [type]: [description]
    """
    coin_1 = ['h', 't']
    coin_2 = ['h', 't']
    
    flip_result_1 = np.random.choice(coin_1)
    flip_result_2 = np.random.choice(coin_2)

    if flip_result_1 == 'h' and flip_result_2 == 'h':
        return 1
    else:
        return 0

def coin_dice_experiment():
    """[summary]

    Returns:
        [type]: [description]
    """
    dice = ['1', '2', '3', '4', '5', '6']
    coin = ['h', 't']

    coin_result = np.random.choice(coin)
    dice_result = np.random.choice(dice)

    if dice_result == '3' and coin_result == 't':
        return 1
    else:
        return 0


def gen_graph(exact_value, n_runs, prob, runs):
    """constrói o gráfico das simulações

    Args:
        exact_value (float): [description]
        n_runs (int)): [description]
        prob (list): [description]
        runs (list): [description]
    """
    plt.hlines(exact_value, 0, n_runs, colors='brown', label='valor exato = 1/12')
    plt.plot(runs, prob, label='Lançamento de uma moeda e de um dado de 6 lados')
    plt.xlabel('# de lançamentos')
    plt.ylabel('Probabilidade de sair {hh} E {3}')
    plt.legend()
    plt.show()


def main():
    n_runs = 100000
    count = 0
    exact_value = 1/12

    prob = []
    runs = []

    for run in range(n_runs):
        count += coin_dice_experiment()
        prob.append(count/(run+1))
        runs.append(run+1)

    gen_graph(exact_value, n_runs, prob, runs)    

if __name__ == '__main__':
    main()