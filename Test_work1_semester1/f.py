"""Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 10000 чисел (не
считая завершающего числа 0). Определите, сколько элементов этой последовательности равны ее наименьшему элементу
(включая сам наименьший). Числа, следующие за числом 0, считывать не нужно."""


def foo_main() -> int:

    number = int(input())
    min_n = float('+inf')
    count_min_n = 0
    while number != 0:
        if min_n > number:
            min_n = number
            count_min_n = 0
        if min_n == number:
            count_min_n += 1
        number = int(input())

    return count_min_n


if __name__ == '__main__':
    print(foo_main())
