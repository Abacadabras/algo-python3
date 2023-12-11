"""A-Бинарный поиск в отсортированном массиве.

Имеется некоторая упорядоченная последовательность размера N неповторяющихся натуральных чисел. Требуется проверить
наличие числа K в ней и вывести его порядковый номер. Если такого числа нет - вывести -1.

Формат входных данных
Натуральное число N. На следующей строчке число K, порядковый номер которого надо найти. Следом идет упорядоченная
последовательность размером N. Если числа K в ней нет - вывести -1.

Формат выходных данных
Одно число - порядковый номер."""


def foo_main():
    N, K, arr = int(input()), int(input()), list(map(int, input().split()))
    position = find_left_bound(arr, K) + 1
    print(position + 1 if position < N and arr[position] == K else -1)


def find_left_bound(A: list, value: int) -> int:
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] < value:
            left = middle
        else:
            right = middle

    return left


if __name__ == '__main__':
    foo_main()
