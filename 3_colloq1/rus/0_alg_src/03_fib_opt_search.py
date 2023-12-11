from math import sqrt

from matplotlib import pyplot as plt

from ODM_func_routines import count_x_y, func


def bine(n):
    return int((((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))))


def fib(a):
    fibs = [1, 1]
    while fibs[len(fibs) - 1] < a:
        fibs.append(fibs[len(fibs) - 1] + fibs[len(fibs) - 2])

    n = len(fibs) - 1
    return n, fibs


def fib_opt_search(l, r, eps):
    crit = (r - l) / eps
    iter_counter, fibs = fib(crit)

    for i in range(iter_counter, 1, -1):
        x1 = l + fibs[i - 2] / fibs[i] * (r - l)
        x2 = l + r - x1
        if func(x1) > func(x2):
            l = x1
        else:
            r = x2


    return (l+r)/2, func((l+r)/2), iter_counter


def main_fib(a, b, eps):
    xopt, fopt, n = fib_opt_search(a, b, eps)

    x, y = count_x_y()

    plt.plot(x, y)
    plt.scatter(xopt, fopt)
    plt.text(xopt, fopt, "fib")
    plt.show()

    print('fib_opt_search')
    print('x_opt:', f'{xopt:.4f}'.format(xopt))
    print('x_opt:', f'{fopt:.4f}'.format(fopt))
    print('iterations:', n)


if __name__ == '__main__':
    eps = 1e-4
    a = 0
    b = 1
    main_fib(a, b, eps)
