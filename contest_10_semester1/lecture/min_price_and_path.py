from random import randint


def min_prices(n: int, price: list) -> list:
    """Кузнечик может прыгать на +1 и +2, есть стоимость прыжка на каждую травинку -> [price]. Распространение идет
    вперед, зная решение (стоимость) для текущей травинки"""
    res = [float('+inf')] * n
    res[0] = price[0]
    for i in range(n-1):
        if res[i+1] > res[i] + price[i+1]:
            res[i+1] = res[i] + price[i+1]
        if i+2 < n and res[i+2] > res[i] + price[i+2]:  # Ограничение на i, чтобы не выйти за границу
            res[i+2] = res[i] + price[i+2]
    return res


def min_prices1(n: int, price: list) -> list:
    """Кузнечик может прыгать на +1 и +2, есть стоимость прыжка на каждую травинку -> [price]. Стоимость прыжка равна
    минимальной стоимости из двух пред. травинок + стоимость текущей травинки"""
    res = [float("+inf"), price[0]] + [0] * (n-1)  # Травинка сзади (+inf), текущая травинка (price[0]) и следующие
    for i in range(2, n+1):
        res[i] = price[i-1] + min(res[i-1], res[i-2])

    return res


def path(price: list, min_price: list) -> list:

    res = []
    i = len(price) - 1
    while i != 0:
        res.append(i)
        if min_price[i-1] == min_price[i] - price[i]:
            i -= 1
        else:
            i -= 2

    return [0] + res[::-1]


N = 12
prices = [randint(2, 10) for _ in range(N)]
print('prices', prices)
min_p = min_prices(N, prices)
print('ex1', min_p)
print('ex2', min_prices1(N, prices))
print('path', path(prices, min_p))
