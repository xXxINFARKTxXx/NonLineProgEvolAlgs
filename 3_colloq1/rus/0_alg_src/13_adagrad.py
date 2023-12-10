import numpy as np

from SD_func_routines import gradf


def adagrad(gradf, x0, gamma, eta, epsilon, max_iterations):
    x0 = np.array(x0)
    v = np.zeros(len(x0))
    G = np.zeros(len(x0))

    for i in range(max_iterations):
        g = gradf(x0)
        G += np.multiply(g, g)
        v = gamma * np.ones_like(G) / np.sqrt(G + eta) * g
        x0 = x0 - v
        if (np.linalg.norm(g) < epsilon):
            break

    return x0, i


if __name__ == '__main__':
    x0 = [3, -0.1]
    gamma = 1
    epsilon = 1e-8
    eta = 1e-8  ## Порядка epsilon
    max_iterations = 1000

    adagrad(gradf, x0, gamma, eta, epsilon, max_iterations)
