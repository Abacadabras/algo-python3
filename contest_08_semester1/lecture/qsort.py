from random import randint


def is_sorted(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            return False
    return True


def qsort(A: list, left=None, right=None):
    """Скорость практическая = N * log2 n, худший случай (если массив уже отсортирован или неудачный выбор разделительного
    элемента = N^2"""

    if left is None:
        left = 0
    if right is None:
        right = len(A) - 1

    if right - left < 1:
        return

    i = left
    j = right
    while i < j:
        while A[i] < A[right]:
            i += 1
        while j > left and A[j] >= A[right]:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[right], A[i] = A[i], A[right]
    print('step :', left, i, right, '\t', ' '.join(map(str, A)))
    qsort(A, left, i-1)
    qsort(A, i+1, right)


A = [randint(100, 999) for _ in range(10)]
print('Start:\t\t', ' '.join(map(str, A)))
qsort(A)
print('Finish\t\t', ' '.join(map(str, A)))
print(is_sorted(A))
