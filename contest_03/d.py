"""Задача D-Считывание числа в нега-позиционной системе счисления
Перевести число из него-десятичной системы счисления в десятичную.

Формат входных данных
Число в него-позиционной десятичной системе счисления.

Формат выходных данных
Это же число в десятичой системе счисления."""


def foo_main() -> int:

    x = int(input())
    number = 0
    power = 0
    while x != 0:
        digit = x % 10
        number += digit * (-10) ** power
        power += 1
        x //= 10

    return number


if __name__ == '__main__':
    print(foo_main())
