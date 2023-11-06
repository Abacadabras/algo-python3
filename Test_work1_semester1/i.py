"""В этой задаче необходимо транспонировать матрицу размера NxN. Транспонирование это часто встречающаяся в линейной
алгебре операция, при которой столбцы матрицы становятся строками, а строки - столбцами."""


def foo_main(n, arr) -> list:
    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[i][j] = arr[j][i]
    return res


if __name__ == '__main__':
    N = int(input())
    matrix = [input().split() for _ in range(N)]

    for i in range(N):
        print(*foo_main(N, matrix)[i])
