from random import randint


def gis(A: list):
    """Поиск наибольшей длины возрастающей подпоследовательности. Является подпоследовательность A и B = sorted(A).
    O(n) = N^2 (Быстрая сортировка N log N и подпоследовательность N x N). Мы решаем задачу поиска наибольшей
    возрастающей подпоследовательности, которая заканчивается числом Ai -- меньше по памяти, но сложность одинаковая"""
    C = [0] * len(A)
    for i in range(len(A)):
        m = 0  # Максимум
        for j in range(i):
            if A[j] < A[i] and C[j] > m:
                m = C[j]
        C[i] = 1 + m

    return C, max(C)


if __name__ == '__main__':
    Z = [randint(10, 99) for _ in range(15)]
    print(Z)
    print(gis(Z))
