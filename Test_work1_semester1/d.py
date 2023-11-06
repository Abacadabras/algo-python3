"""На вход программа получает последовательность чисел, заканчивающихся символом решётки.
Вам требуется найти: - среднее, округлив до трёх знаков с помощью round(x, 3) - максимальное - минимальное - сумму
остатков троек из чисел (см. ниже) последовательности.
Введенные числа образуют тройки. Нужно вывести сумму остатков от деления суммы чисел из тройки на последнее число из
тройки.
То есть, для входных данных: 1 2 3 4 5 6
Первая тройка - 1 2 3, вторая - 4 5 6.
И сумма остатков троек на последнее число из тройки:
(1 + 2 + 3) mod 3 + (4 + 5 + 6) mod 6 = 6 mod 3 + 15 mod 6 = 0 + 3 = 3"""


def foo_main():

    str_n = input()
    min_n = float('+inf')
    max_n = float('-inf')
    sum_n = 0
    count_n = 0
    sum_3 = 0
    arr_3 = [1] * 3
    while str_n != '#':
        number = int(str_n)
        if count_n % 3:
            arr_3[count_n % 3] = number
        else:
            sum_3 += sum(arr_3) % arr_3[2]
            arr_3[0] = number
        count_n += 1
        sum_n += number
        if max_n < number:
            max_n = number
        if min_n > number:
            min_n = number

        str_n = input()

    sum_3 += sum(arr_3) % arr_3[2]

    print(round(sum_n/count_n, 3), max_n, min_n, sum_3)


if __name__ == '__main__':
    foo_main()
