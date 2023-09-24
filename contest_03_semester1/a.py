"""A-Произведение чисел в строке
Для заданной строки символов вычислить произведение входящих в эту строку целых чисел (без учета их знаков).

Формат входных данных
Одна строка

Формат выходных данных
Произведение чисел в строке."""


def foo_main(string: str) -> int:

    number, result = '', 1
    for symbol in string:
        if '0' <= symbol <= '9':
            number += symbol
        elif number != '':
            result *= int(number)
            number = ''

    return result


if __name__ == '__main__':
    print(foo_main(input() + '_'))
