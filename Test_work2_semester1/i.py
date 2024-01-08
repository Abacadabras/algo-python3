"""Дано две строки: A и B.

Вам необходимо вычислить минимальное редакционное расстояние из строки A в строку B, с учётом цен за операции вставки,
удаления и замены символа.

Формат входных данных: Первая строка - три цены, разделённые пробелом: цена за вставку, цена за удаление, цена за замену.
 Вторая строка и третья строки - строки A и B.

Формат выходных данных: Одно число — результат."""


def dist(s1, s2, ins_cost, del_cost, replace_cost):

    dp = [[0] * (len(s1) + 1000) for _ in range(len(s2) + 1000)]
    dp[0][0] = 0

    for i in range(1, len(s2) + 1):
        dp[0][i] = dp[0][i - 1] + ins_cost

    for i in range(1, len(s1) + 1):
        dp[i][0] = dp[i - 1][0] + del_cost

        for j in range(1, len(s2) + 1):
            if s1[i - 1] != s2[j - 1]:
                dp[i][j] = min(dp[i - 1][j] + del_cost, dp[i][j - 1] + ins_cost, dp[i - 1][j - 1] + replace_cost)
            else:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[len(s1)][len(s2)]


def main():
    x, y, z = map(int, input().split())
    s1 = input()
    s2 = input()
    print(dist(s1, s2, x, y, z))


main()
