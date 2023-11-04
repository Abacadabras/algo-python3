
import random


def fool_sort(A):
    """
    Сложность N^3 - сортировка дурака
    """
    i = 1
    while i < len(A):
        if A[i-1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
            i = 0
        i += 1


A = list([random.randint(100, 999) for _ in range(10)])
print(A)
fool_sort(A)
print(A)
