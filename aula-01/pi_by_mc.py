"""Cálculo de Pi a partir da área de um círculo

    A = Pi r^2, se r = 1 => A = Pi
    x^2 + y^2 = r^2 = 1

    e: x^2 + y^2 < 1

    x <- uniform(0, 1)
    y <- uniform(0, 1)
"""
import numpy as np
import matplotlib.pyplot as plt


def experiment():
    x = np.random.rand()
    y = np.random.rand()

    if x**2 + y**2 < 1:
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
    plt.hlines(exact_value, 0, n_runs, colors='brown', label='valor exato = 3.14}')
    plt.plot(runs, prob, label='Cálculo de Pi usando o MC')
    plt.xlabel('# de lançamentos')
    plt.ylabel('Valor de Pi')
    plt.legend()
    plt.show()


def main():
    n_runs = 1000
    count = 0
    exact_value = np.pi

    prob = []
    runs = []

    # caem dentro da circunferência
    x_inner = []
    y_inner = []

    # caem fora da circunferência
    x_outer = []
    y_outer = []

    for run in range(n_runs):
        x = np.random.rand()
        y = np.random.rand()

        if x**2 + y**2 < 1:
            count += 1
            x_inner.append(x)
            y_inner.append(y)
            prob.append(4*count/(run+1))
            runs.append(run+1)
        else:
            x_outer.append(x)
            y_outer.append(y)

    gen_graph(exact_value, n_runs, prob, runs)

    plt.scatter(x_inner, y_inner, color='purple', alpha=0.8)
    plt.scatter(x_outer, y_outer, color='pink', alpha=0.4)
    plt.show()

if __name__ == '__main__':
    main()