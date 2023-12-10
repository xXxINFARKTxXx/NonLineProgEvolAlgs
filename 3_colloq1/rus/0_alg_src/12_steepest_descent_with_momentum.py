import numpy as np

from SD_func_routines import gradf


def steepest_descent_with_momentum(gradf, x0, gamma, epsilon, omega, max_iterations):
    x0 = np.array(x0)
    v = 0

    for i in range(max_iterations):
        g = gradf(x0)
        v = omega * v + gamma * g
        x0 = x0 - v
        if np.linalg.norm(g) < epsilon:
            break
    return x0, i + 1


if __name__ == "__main__":
    x0 = [-3, -0.1]
    gamma = 0.7 * 0.8  ## разбиваем множитель для gamma и omega (который в сумме дает 1) на доли для gamma и omega
    epsilon = 1e-8
    omega = 0.1 * 0.2
    max_iterations = 1000

    steepest_descent_with_momentum(gradf, x0, gamma, epsilon, omega, max_iterations)
