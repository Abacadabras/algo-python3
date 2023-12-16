from random import randint


def grass_st(n):
    """Стандартный кузнечик: количество способов попасть на травинку N, если может прыгать только на +1 и +2"""
    A = [0] * n
    A[1] = 1
    for i in range(2, n+1):
        A[i] = A[i-1] + A[i-2]

    return A[n]


def grass_st1(n):
    """Стандартный кузнечик: количество способов попасть на травинку N, если может прыгать только на +1 и +2.
    Но распространение идет вперед, зная решения для текущей травинки"""
    A = [0] * (n+1)  # Чтобы не было ошибки выхода за индекс т.к. прыгает на +2
    A[0] = 1
    for i in range(n-1):
        A[i+1] += A[i]
        A[i+2] += A[i]

    return A[n-1]


def grass_st2(n):
    """Стандартный кузнечик: количество способов попасть на травинку N, если может прыгать только на +1 и +2 и +3"""
    A = [0] * n
    A[1] = 1
    A[2] = 1
    for i in range(3, n+1):
        A[i] = A[i-1] + A[i-2] + A[i-3]

    return A[n]


def grass_st3(n):
    """Стандартный кузнечик: количество способов попасть на травинку N, если может прыгать только на +1 и +2 и +3.
    Но распространение идет вперед, зная решение для текущей травинки"""
    A = [0] * (n+2)  # Чтобы не было ошибки выхода за индекс т.к. прыгает на +2
    A[0] = 1
    for i in range(n-1):
        A[i+1] += A[i]
        A[i+2] += A[i]
        A[i+3] += A[i]

    return A[n-1]


def grass(n: int, free: list) -> list:
    """Стандартный кузнечик: количество способов попасть на травинку N, если может прыгать только на +1 и +2 Внимание:
    Некоторые травинки могут быть заняты (прыгать на них нельзя)"""
    A = [0] * n
    A[0] = 1
    for i in range(n-1):
        if i+1 < n and free[i+1]:  # Чтобы не выйти за индекс свободных травинок -> i+1 < n
            A[i+1] += A[i]
        if i+2 < n and free[i+2]:
            A[i+2] += A[i]

    return A


def grass1(n: int, free: list) -> list:
    """Стандартный кузнечик: количество способов попасть на травинку N, если может прыгать только на +1 и +2 Внимание:
    Некоторые травинки могут быть заняты (прыгать на них нельзя). Но распространение идет вперед, зная решение для
    текущей травинки """
    res = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        if free[i-1]:
            res[i] = res[i-1] + res[i-2]
    return res


N = 10  
allowed = [True] * N

allowed[randint(1, N-2)] = False  # Заблокированная травинка
print(allowed)
print(grass(N, allowed))
print(grass1(N, allowed))
