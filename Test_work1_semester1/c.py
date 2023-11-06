"""На вход подается матрица NxN. Необходимо найти её след.
Напоминание - след матрицы определяется как сумма диагональных элементов:
tr A = a11 + a22 + a33 + … + aNN"""


def foo_main(n, arr) -> int:

    res = 0
    for i in range(n):
        res += arr[i][i]
    return res


if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(foo_main(N, matrix))
