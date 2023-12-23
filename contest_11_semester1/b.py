"""B-Платный аттракцион
В парке развлечений Васе попался аттракцион.
Это прямоугольное поле NxM. Вася начинает свой путь в левой верхней клетке, а заканчивает в правой нижней. По правилам
аттракциона Вася может двигаться только вниз и вправо и должен платить штраф p ij за прохождение клетки. Вася взял с
собой не так уж и много денег, поэтому он хочет пройти аттракцион, потратив как можно меньше.

Помогите Васе узнать, сколько денег у него останется.
"""


if __name__ == '__main__':
    m = int(input())
    n = int(input())

    p = [[int(input()) for _ in range(n)] for _ in range(m)]

    max_money = int(input())

    # situations in limits
    if m == 1 and n == 1:
        print(max_money)
        exit()
    if max_money == 0:
        print(0)
        exit()

    score = [[0] * (n + 1) for _ in range(m + 1)]
    for j in range(1, n + 1):
        score[0][j] = 1000000 + 1
    for i in range(1, m + 1):
        score[i][0] = 1000000 + 1
    # initial conditions
    score[2][1], score[1][2] = p[1][0], p[0][1]

    for i in range(1, m + 1):
        if i == 1:
            for j in range(3, n + 1):
                score[i][j] = p[i - 1][j - 1] + min(score[i - 1][j], score[i][j - 1])
        elif i == 2:
            for j in range(2, n + 1):
                score[i][j] = p[i - 1][j - 1] + min(score[i - 1][j], score[i][j - 1])
        else:
            for j in range(1, n + 1):
                score[i][j] = p[i - 1][j - 1] + min(score[i - 1][j], score[i][j - 1])

    min_score = score[m][n]
    if min_score <= max_money:
        print(max_money - min_score)
    else:
        print('Impossible')
