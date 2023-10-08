"""E-Считывание числа в системе счисления майя
Система счисления майя основывалась на 20-ричной системе счисления.

Разряд формируется следующим образом. Для записи нуля использовалась ракушка "@". Для конструирования числа разряда
использовались точки ".", и палочки "|". Точка добавляла к числу разряда 1, а палочка 5. Например, число 13 помещается
в один разряд и выглядит следующим образом: "...||" = 3 + 2*5.

Для отделения разрядов мы воспользуемся пробелом.

Вам предстоит считать число майя и перевести его в десятичную систему счисления.

Формат входных данных
Одна строка - число, записанное в системе счисления майя.

Формат выходных данных
Одно число в десятичной системе счисления."""


def foo_main(num: str) -> int:

    number = 0
    degree_number = 0
    base = 20

    for _ in range(len(num) - 1, -1, -1):
        symbol = num[_]
        if symbol == ' ':
            degree_number += 1
        elif symbol == '|':
            number += 5 * base**degree_number
        elif symbol == '.':
            number += 1 * base**degree_number

    return number


if __name__ == '__main__':
    number_maya = input()
    print(foo_main(number_maya))