from random import randint


def gcs(A: list, B: list) -> list:
    """Наибольшая общая подпоследовательность. Сложность = N x M"""
    C = [[0] * (len(A) + 1) for _ in range(len(B)+1)]  # Длина +1, т.к. есть 0 столбец начальный с которого стартуем

    for i in range(1, len(A)+1):  # Столбец
        for j in range(1, len(B)+1):  # Строка
            if A[i-1] == B[j-1]:
                C[j][i] = C[j-1][i-1] + 1  # Элементы равны берем пред. по диагонали + 1
            else:
                C[j][i] = max(C[j-1][i], C[j][i-1])  # Элементы не равны! Макс. из двух выше и левее

    return C  # В конце в углу лежит результат


def get_cs(A: list, B: list, C: list) -> list:
    """Получение самой наибольшей подпоследовательности в виде [] одной из них (в качестве примера!)"""
    res = [0] * C[-1][-1]
    k = len(res) - 1
    i = len(A)
    j = len(B)
    while C[j][i] != 0:
        if C[j][i] - C[j-1][i-1] == 1 and A[i-1] == B[j-1]:
            res[k] = A[i-1]
            k -= 1
            i -= 1
            j -= 1
        else:
            if C[j-1][i] == C[j][i]:
                j -= 1
            else:
                i -= 1

    return res


if __name__ == '__main__':

    A = [randint(1, 5) for _ in range(15)]
    B = [randint(1, 5) for _ in range(12)]
    C = gcs(A, B)
    print('   ', *A)
    print(' ',  *C[0])

    for j in range(len(B)):
        print(B[j], *C[j+1])

    print(get_cs(A, B, C))
