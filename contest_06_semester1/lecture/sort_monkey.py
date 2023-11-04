
import random


def is_sorted(A):

    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False

    return True


def monkey_sort(A):
    """
    Сложность N! - сортировка обезьяны
    """
    while not is_sorted(A):
        random.shuffle(A)


A = list([random.randint(100, 999) for _ in range(8)])
print(A)
monkey_sort(A)
print(A)
