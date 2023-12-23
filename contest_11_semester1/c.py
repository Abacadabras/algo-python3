"""C-Белая пешка
На шахматной доске расставлено несколько черных пешек и одна белая. Черные пешки не подвижны, белая может ходить на одну
 клетку вперед (если там нет черной пешки) или есть черную пешку наискосок (на одну клетку вперед и на одну вправо
 или влево). Посчитайте, сколькими способами белая пешка может дойти до конца поля и стать ферзем.
 Строки шахматной доски пронумерованы числами от 1 до 8, столбцы буквами от a до h. Строка 1 - самая нижняя, столбец
 a - самый левый. Белой пешке надо добраться до строки с номером 8. Eсли она уже стоит на 8й строке, то считается что
 у нее ровно 1 способ (стоять на месте).
"""


letter_set = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

black_amount = int(input())
black = []
if black_amount != 0:
    for i in range(black_amount):
        pos = input()
        black.append((letter_set[pos[0]], int(pos[1])))
pos = input()
white = (letter_set[pos[0]], int(pos[1]))

if white[1] == 8:
    print(1)
    exit()

board = [ [ [0, 0] for _ in range(9) ] for _ in range(9) ]
for el in black:
    board[el[1]][el[0]] = [0, 1]
board[white[1]][white[0]] = [1, 0]

for i in range(white[1] + 1, 9):
    for j in range(1, 9):
        if j + 1 != 9 and board[i][j][1] == 1 and board[i - 1][j + 1][0] != 0:
            board[i][j][0] += board[i - 1][j + 1][0]
        if board[i][j][1] == 1 and board[i - 1][j - 1][0] != 0:
            board[i][j][0] += board[i - 1][j - 1][0]
        if board[i][j][1] == 0 and board[i - 1][j][0] != 0:
            board[i][j][0] += board[i - 1][j][0]

total = 0
for i in range(1, 9):
    total += board[8][i][0]
print(total)
