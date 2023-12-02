from time import time


def fib(n):
    """Время вычисления след. числа = времени вычисления пред. двух чисел фибоначи. Пример, что не всегда рекурсивный
    алгоритм является оптимальным"""
    if n < 2:
        return 1

    return fib(n-1) + fib(n-2)


for i in range(50):
    t = time()
    n = fib(i)
    t = time() - t
    print(i, n, t)
