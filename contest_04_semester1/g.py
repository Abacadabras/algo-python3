"""G-Минимальное по сумме и количеству цифр
Вам необходимо написать программу, вычисляющую минимальное число, для которого заданы:
    1) сумма цифр
    2) количество цифр
    3) цифры должны быть упорядочены по неубыванию.

Формат входных данных
Сумма и количество цифр через пробел.

Формат выходных данных
Число-ответ или строка 'impossible', если такого числа не существует."""


def foo_main(x: int, y: int):

    number = int('1' * y)
    degree = 0
    if y <= x <= 9 * y:
        remnant = x - y
        while remnant != 0:
            if remnant > 8:
                number += 8 * 10**degree
                degree += 1
                remnant -= 8
            else:
                number += remnant * 10**degree
                remnant = 0
        return number
    else:
        return 'impossible'


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(foo_main(a, b))
