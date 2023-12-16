"""F-Шоколадка
Саша, не сделал домашнюю работу, зато купил шоколадку. И, по глупости, начал распечатывать ее прямо на уроке... Шелест
золотинки услышала учительница. Она хотела вызвать в школу родителей, но Саша уговорил ее не вызывать их, а дать
дополнительное задание.

Учительница внимательно посмотрела на шоколадку (она была размером 3х4 плиток), разделила на кусочки по две плитки и
угостила всех, кто сделал домашнюю работу. А Сашу попросила написать программу, которая определяет, сколько существует
способов деления шоколадки размером 3×N плиток на кусочки по две плитки.

Для выполнения задания Саше нужна помощь.

Примечание: все плитки в шоколадке пронумерованы, поэтому способы деления, симметричные относительно точки или оси
могут будут разными.

Формат входных данных
На входе одно число N <= 10000

Формат выходных данных
Вывести одно число, количество способов разделить шоколадку."""


def foo_main(n: int) -> int:

    if n % 2 or not n:
        return 0

    res = [0] * (n+1)
    res[0], res[2] = 1, 3

    for i in range(4, n+1, 2):
        res[i] = 4 * res[i-2] - res[i-4]

    return res[n]


if __name__ == '__main__':
    N = int(input())
    print(foo_main(N))
