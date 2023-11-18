"""G-Два хода конем
Вам даны 2 координаты 2 клеток на шахматном поле. Нужно ответить на вопрос, можно ли попасть из одной клетки в другую
за не более чем 2 хода конем. В случае, если попасть возможно, надо вывести количество ходов, за которое это можно
сделать. Если попасть невозможно, следует вернуть -1.

В этой задаче запрещено использование циклов.

Формат входных данных
На вход подаются числа от 1 до 8 в 4 строках. Первые 2 строки задают координаты начальной клетки,
вторые 2 -- координаты конечной клетки.

Формат выходных данных
Одно число — количество ходов, за которые можно попасть из одной клетки во вторую. Если невозможно -- вывести -1."""


def horse(x, y, data, cnt=0):
    if x > 8 or x < 1 or y < 1 or y > 8 or cnt > 2:
        return
    if data[x][y] != -1:
        data[x][y] = min(cnt, data[x][y])
        return
    else:
        data[x][y] = cnt

    horse(x + 2, y + 1, data, cnt + 1)
    horse(x + 2, y - 1, data, cnt + 1)
    horse(x - 2, y + 1, data, cnt + 1)
    horse(x - 2, y - 1, data, cnt + 1)
    horse(x + 1, y + 2, data, cnt + 1)
    horse(x - 1, y + 2, data, cnt + 1)
    horse(x + 1, y - 2, data, cnt + 1)
    horse(x - 1, y - 2, data, cnt + 1)


if __name__ == '__main__':
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    data = list()
    data.append([-1] * 9)
    data.append([-1] * 9)
    data.append([-1] * 9)
    data.append([-1] * 9)
    data.append([-1] * 9)
    data.append([-1] * 9)
    data.append([-1] * 9)
    data.append([-1] * 9)
    data.append([-1] * 9)
    horse(x1, y1, data)
    print(data[x2][y2])
