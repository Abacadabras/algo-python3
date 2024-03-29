"""A-Полиномиальная хеш-функция
Вам необходимо вычислить полиномиальный хеш от строки.

Вычисления хеша выполнять по схеме справа-налево. То есть символу строки, стоящему на нулевой позиции, будет
соответствовать самая большая степень основания, а символу, стоящему последним, будет соответствовать нулевая степень
основания.

Чтобы узнать порядковый номер (код) символа, воспользуйтесь функцией ord().

Рекомендуется обернуть реализацию хеш-функции в функцию, чтобы воспользоваться ей в задачах по хеш-таблицам.

Формат входных данных
Две строки. В первой два натуральных числа через пробел - основание хеша и его модуль. Во второй строке - строка длины
не менее 1.

Формат выходных данных
Натуральное число - полиномиальный хеш от строки."""


def foo_main(base: int, degree: int, string: str) -> int:

    value = 0
    for i in range(len(string)-1, -1, -1):
        value += ord(string[i]) * base**(len(string)-1-i)

    return value % degree


if __name__ == '__main__':
    b, d = map(int, input().split())
    s = input()
    print(foo_main(b, d, s))
