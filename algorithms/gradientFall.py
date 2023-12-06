import numpy as np

# метод градиентного спуска xk+1 = xk - gamma * gradf(xk)
# метод градиентного спуска с моментом xk+1 = xk - vk
                                        # vk = w*vk-1 + gamma * gradf(xk)
# адаптивный градиентный метод gki= dpF\dxi
#             Gk = SUMM(g^2)
#             xk+1 = xk - gamma / sqrt((Gk + eps1) * gk)
#
#               g = gradf(x)
#               G = G + g*g
#               x = x - gamma / sqrt(Gk + eps1) * gk
#
def func(x):
    return 1.5 * x[0] ** 2 + x[1] ** 2 + 2 * x[0] * x[1] + 2 * x[0] ** 3 + 0.5 * x[0] ** 4


def gradf(x):
    x = np.array(x).reshape(np.size(x))
    return np.asarray([
        [3 * x[0] - 2 * x[1] + 6 * x[0] ** 2 + 2 * x[0] ** 3],
        [2 * x[1] - 2 * x[0]]
    ])


def metodNajbrzegPada(gradf, x0, gamma, epsilon, N):
    x = np.array(x0).reshape(np.size(x0))
    for i in range(N):
        g = gradf(x)
        x = x - gamma * g
        if np.linalg.norm(g) < epsilon:
            break

    return x


def main():
    optimum = metodNajbrzegPada(gradf, x0=[2, 2], gamma=0.01, epsilon=1e-6, N=1000)
    vred_kriterijuma = func(optimum)
    print(optimum, '\n', vred_kriterijuma)


if __name__ == '__main__':
    main()
