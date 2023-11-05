
from random import randint


def rsort2(X):
    """Поразрядная сортировка 10 числа в 2 системе счисления"""
    x = 1
    singles = []
    zeros = []
    while x < 10000:
        singles.clear()
        zeros.clear()

        for el in X:
            if el & x:
                singles.append(el)
            else:
                zeros.append(el)
        X.clear()
        X.extend(zeros)
        X.extend(singles)
        x <<= 1


a = list([randint(0, 10000) for _ in range(15)])
print(a)
rsort2(a)
print(a)
