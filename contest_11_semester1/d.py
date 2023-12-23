"""D-Алгоритм Левенштейна
Дано две строки. Нужно найти наименьшее количество исправлений, необходимых для получения второй строки из первой.
Исправления бывают трех видов: 1) Вставка символа на произвольное место. 2) Удаление произвольного символа.
3) Замена произвольного символа любым другим символом. (Алгоритм Левенштейна)
"""


def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = [[[0] for _ in range(size_y)] for _ in range(size_x)]

    for x in range(size_x):
        matrix[x][0] = x
    for y in range(size_y):
        matrix[0][y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix[x][y] = min(
                    matrix[x-1][y] + 1,
                    matrix[x-1][y-1],
                    matrix[x][y-1] + 1
                )
            else:
                matrix [x][y] = min(
                    matrix[x-1][y] + 1,
                    matrix[x-1][y-1] + 1,
                    matrix[x][y-1] + 1
                )
    return (matrix[size_x - 1][size_y - 1])
