"""F-Решето Эратосфена
Вам дано число N, которое не превышает 10000 . Выведите все простые числа от 2 до N включительно. Операции умножения
 и деления использовать запрещено!

Формат входных данных
Вводится натуральное число N, 2 ≤ N ≤ 10000.

Формат выходных данных
Последовательность чисел через пробел -- простые числа, не превосходящие N."""


def foo_main(n: int):

    arr = [True for _ in range(n)]
    arr[0] = arr[1] = False

    for i in range(2, n):
        if arr[i]:
            for j in range(i+i, n, i):
                arr[j] = False

    return arr


if __name__ == '__main__':
    n1 = int(input())
    result = foo_main(n1)

    for i in range(n1):
        if result[i]:
            print(i, end=' ')
