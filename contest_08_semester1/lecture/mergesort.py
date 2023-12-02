from random import randint


def mergesort(A: list):
    """Скорость всегда = N * log2 n, нужна дополнительная память такая же как и размер списка (для слияния)
    Даже если будет отсортирована все равно сложность такая же!"""
    if len(A) == 1:
        return

    n = len(A) // 2
    B = A[:n]
    C = A[n:]
    mergesort(B)
    mergesort(C)
    i = j = k = 0
    while i < len(B) and j < len(C):  # Слияние
        if B[i] < C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    # Дополнения конца массива, если остались после слияния
    while i < len(B):
        A[k] = B[i]
        i += 1
        k += 1
    while j < len(C):
        A[k] = C[j]
        j += 1
        k += 1


X = [randint(10, 99) for _ in range(10)]
print(X)
mergesort(X)
print(X)
