"""C-Определение типа треугольника

Формат входных данных
Даны три натуральных числа – стороны треугольника. Каждое число вводится с новой строки.

Формат выходных данных
Необходимо вывести одно из слов:
    right для прямоугольного треугольника,
    acute для остроугольного треугольника,
    obtuse для тупоугольного треугольника,
impossible, если треугольника с такими сторонами не существует."""


def foo_main(num1: int, num2: int, num3: int) -> str:

    c1 = max(num1, num2, num3)
    b1 = min(num1, num2, num3)
    a1 = (num1 + num2 + num3) - b1 - c1
    if c1 >= a1 + b1:
        return 'impossible'
    elif c1 ** 2 == a1 ** 2 + b1 ** 2:
        return 'right'
    elif c1 ** 2 < a1 ** 2 + b1 ** 2:
        return 'acute'
    elif c1 ** 2 > a1 ** 2 + b1 ** 2:
        return 'obtuse'


if __name__ == '__main__':
    a, b, c = int(input()), int(input()), int(input())
    print(foo_main(a, b, c))
