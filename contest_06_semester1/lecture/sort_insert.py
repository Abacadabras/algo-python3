
import random


def insert_sort(A):
    """
    Сложность N^2 - сортировка вставками (оптимизации не нужны)
    """
    n = len(A)
    for i in range(1, n):
        while i > 0 and A[i] < A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1


A = list([random.randint(10, 99) for _ in range(10)])
print(A)
insert_sort(A)
print(A)
