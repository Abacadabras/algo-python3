"""F-Минимальное число
По данному натуральному числу найти минимальное натуральное число, состоящее из тех же цифр, что и данное.

Формат входных данных
Одно натуральное число N ≤ 10 100.

Формат выходных данных
Одно число — минимальное натуральное число, состоящее из тех же цифр, что и N."""


def foo_main(number: str) -> int:

    number = [i for i in number]
    number.sort()
    for i in range(len(number)):
        if number[i] != '0':
            number[0], number[i] = number[i], number[0]
            break
    return number


if __name__ == '__main__':
    n = input()
    print(*foo_main(n), sep='')
