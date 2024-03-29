"""В дощечке в один ряд вбиты гвоздики. Любые два гвоздика можно соединить ниточкой. Требуется соединить некоторые пары
гвоздиков ниточками так, чтобы к каждому гвоздику была привязана хотя бы одна ниточка, а суммарная длина всех ниточек
была минимальна.

Формат входных данных: В строке заданы N (2 <= N <= 100) чисел — координаты всех гвоздиков (неотрицательные целые числа,
не превосходящие 10000).

Формат выходных данных: Выведите единственное число — минимальную суммарную длину всех ниточек."""


def foo_main(data: list) -> int:

    data.sort()

    dp = [0] * (len(data) + 1)
    dp[1] = 10**8

    for i in range(2, len(data) + 1):
        dp[i] = min(dp[i-1], dp[i-2]) + data[i-1] - data[i-2]

    return dp[len(data)]


if __name__ == '__main__':
    path = list(map(int, input().split()))
    print(foo_main(path))
