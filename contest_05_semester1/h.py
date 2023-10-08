"""H-Треугольник Паскаля
По данному числу N выведите первые N+1 строку треугольника Паскаля.
Формат входных данных
Во входных данных содержится только число N (0 < N ≤ 100).

Формат выходных данных
Выведите N + 1 строку треугольника Паскаля. Числа в строке разделяйте одним пробелом."""


def foo_main(prev_row: list) -> list:

    new_row = [1] + prev_row
    for i in range(1, len(new_row) - 1):
        new_row[i] += new_row[i + 1]
    return new_row


if __name__ == '__main__':
    n = int(input())
    row = []

    for _ in range(n+1):
        row = foo_main(row)
        print(*row)
