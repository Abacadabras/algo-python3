"""F-Число конечных нулей факториала
Вам необходимо определить количество конечных нулей факториала n!. Например, 5! = 120 - число конечных нулей равно 1;
13! = 6227020800 - число конечных нулей равно 2. Будьте осторожны: запись факториала 1000! уже содержит 2568 цифр...

Формат входных данных
Натуральное n

Формат выходных данных
Количество конечных нулей факториала n!"""


def foo_main(num: int) -> int:

    quantity_0 = 0
    degree = 1
    while num / 5**degree >= 1:
        quantity_0 += int(num / 5**degree)
        degree += 1
    return quantity_0


if __name__ == '__main__':
    number = int(input())
    print(foo_main(number))
