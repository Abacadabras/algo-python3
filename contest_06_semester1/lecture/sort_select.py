
import random


def sel_sort(A):
    """
    Сложность N^2 - сортировка выбором
    """
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]


A = list([random.randint(10, 99) for _ in range(10)])
print(A)
sel_sort(A)
print(A)
