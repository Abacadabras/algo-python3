import time


cache = [-1] * 102
cache[0] = 0
cache[1] = 1


def fib(n):
    """Рекурсия с кешированием (один из подходов динамического программирования)"""
    if cache[n] != -1:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


for i in range(100):
    t = time.time()
    x = fib(i)
    t = time.time() - t
    print(i, fib(i), t)
