"""A-Алгоритм Евклида
Необходимо найти НОД двух чисел, используя алгоритм Евклида.

Формат входных данных
На вход подаются два натуральных числа, по числу в новой строке.

Формат выходных данных
Одно число - НОД входных чисел. """


def foo_main(a: int, b: int) -> int:

    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    number1 = int(input())
    number2 = int(input())
    print(foo_main(number1, number2))
