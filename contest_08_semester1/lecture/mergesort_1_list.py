from random import randint


def mergesort(A, rng=None):
    """Реализация только с дополнительной памятью с размером равным исходному списку, дополнительные ухищрения в
    алгоритме"""
    if rng is None:
        rng = (0, len(A))
        A = [A, list([0] * len(A))]
    if rng[1] - rng[0] < 2:
        return
    center = (rng[0] + rng[1]) // 2

    mergesort(A, (rng[0], center))
    mergesort(A, (center, rng[1]))
    B_in = rng[0]
    i = rng[0]
    j = center
    while i < center or j < rng[1]:
        if i == center:
            A[1][B_in] = A[0][j]
            j += 1
        elif j == rng[1]:
            A[1][B_in] = A[0][i]
            i += 1
        elif A[0][i] < A[0][j]:
            A[1][B_in] = A[0][i]
            i += 1
        else:
            A[1][B_in] = A[0][j]
            j += 1
        B_in += 1
    for i in range(*rng):
        A[0][i] = A[1][i]


A = [randint(100, 999) for _ in range(10)]
print(A)
mergesort(A)
print(A)
