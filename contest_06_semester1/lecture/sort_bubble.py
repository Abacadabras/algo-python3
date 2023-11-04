
import random


def bubble_sort(A):
    """
    Сложность N^2 - сортировка пузырьком (можно сделать небольшие оптимизации)
    """
    n = len(A)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


A = list([random.randint(10, 99) for _ in range(10)])
print(A)
bubble_sort(A)
print(A)
