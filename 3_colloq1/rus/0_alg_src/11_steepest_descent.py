import numpy as np

from SD_func_routines import gradf


def steepest_descent(gradf, x0, gamma, epsilon, N):
    x = np.array(x0).reshape(len(x0), 1)
    for k in range(N):
        g = gradf(x)
        x = x - gamma * g
        if np.linalg.norm(g) < epsilon:
            break
    return x


if __name__ == '__main__':
    gamma = 0.1
    epsilon = 1e-4
    max_steps = 100
    x0 = [3, 3]

    print(steepest_descent(gradf, x0, gamma, epsilon, max_steps))
