"""G-Сортировка по сумме цифр
Отсортировать массив по сумме цифр входного массива.

Формат входных данных
Натуральное число N. Затем N неотрицательных целых чисел - элементов массива.

Формат выходных данных
Нужно вывести N чисел, отсортированные по их сумме цифр. В случае равенства суммы цифр любых двух чисел, вывести
отсортированными по абсолютному значению."""


def foo_main(n: int, arr: list) -> list:

    for top in range(1, n):
        while top > 0 and arr[top - 1][1] > arr[top][1]:
            arr[top], arr[top - 1] = arr[top - 1], arr[top]
            top -= 1
        while top > 0 and arr[top - 1][1] == arr[top][1] and arr[top - 1][0] > arr[top][0]:
            arr[top], arr[top - 1] = arr[top - 1], arr[top]
            top -= 1

    return arr


def summa_numbers(x):
    sum_digit = 0
    while x > 0:
        sum_digit += x % 10
        x //= 10
    return sum_digit


if __name__ == '__main__':
    n = int(input())
    arr = [[0] * 2 for _ in range(n)]
    for _ in range(n):
        digit = int(input())
        arr[_][0] = digit
        arr[_][1] = summa_numbers(digit)
    result = foo_main(n, arr)
    for _ in range(n):
        print(result[_][0])
