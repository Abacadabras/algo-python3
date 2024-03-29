"""F-Считывание числа в вавилонской системе счисления
В вавилонской системе счисления для записи чисел внутри 60-ричного разряда использовались всего два знака:
стоячий клин "v" (латинская строчная v) для обозначения единиц и лежачий клин "<" (знак строго меньше) для обозначения
десятков. Для формирования разряда сначала выписывалось количество десятков, а затем количество единиц. Разряды
вавилоняне разделяли пустым пространством, однако мы будем использовать для этого точку ".". Если какой-то разряд
отсутствовал, на его месте ничего не писалось. Требуется перевести записанное в вавилонской системе число в десятичную
систему счисления.

Формат входных данных
Одна строка - число, записанное в вавилонской системе счисления.

Формат выходных данных
Одно число в десятичной системе счисления."""


def foo_main(num: str) -> int:

    number = 0
    degree_number = 0
    base = 60

    for _ in range(len(num) - 1, -1, -1):
        symbol = num[_]
        if symbol == '.':
            degree_number += 1
        elif symbol == 'v':
            number += 1 * base**degree_number
        elif symbol == '<':
            number += 10 * base**degree_number

    return number


if __name__ == '__main__':
    number_vav = input()
    print(foo_main(number_vav))
