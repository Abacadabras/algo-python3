"""B-Рекурсивный бинарный поиск в отсортированном массиве.

Имеется некоторая упорядоченная последовательность неповторяющихся натуральных чисел. Требуется проверить наличие
числа K в ней и вывести его порядковый номер (нумерация с единицы) с помощью рекурсии. Если такого числа нет -
вывести -1. Циклы запрещены!

Формат входных данных
Строка натуральных чисел, разделённых пробелами, на следующей строке число K.

Формат выходных данных
Одно число — результат"""


def foo_main(A: list, value: int, left=None, right=None):
    if left is None:
        left = -1
    if right is None:
        right = len(A)
    if right - left < 2:
        return left
    middle = (right + left) // 2
    if A[middle] < value:
        left = middle
    else:
        right = middle
    return foo_main(A, value, left, right)


if __name__ == '__main__':
    arr, K = list(map(int, input().split())), int(input())
    position = foo_main(arr, K) + 1
    print(position + 1 if position < len(arr) and arr[position] == K else -1)
