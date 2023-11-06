"""Вам даётся два целых числа, необходимо вывести их сумму и разность."""


def foo_main(num1: int, num2: int) -> int:

    return num1+num2, num1-num2


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(*foo_main(a, b), sep=',')
