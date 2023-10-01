"""B-Тест простоты числа
Выяснить, является ли заданное число простым.

Формат входных данных
На вход подается натуральное число.

Формат выходных данных
Вывести 1 - число простое, 0 - число составное."""


def foo_main(x: int) -> int:

    if x % 2 == 0:
        return 0
    for divisor in range(3, (x+1)//2, 2):
        if x % divisor == 0:
            return 0
    return 1


if __name__ == '__main__':
    number = int(input())
    print(foo_main(number))
