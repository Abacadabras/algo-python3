
"""Доска размером M x N, в каждой клетке лежат монеты (сумма), робот может ходить вправо и вниз. Максимум, который
может собрать робот по пути денег. Также можно по результату построить путь робота"""

A = [[7, 15, 1, 3, 14],
     [2, 3, 0, 0, 1],
     [9, 2, 5, 8, 4],
     [1, 7, 2, 1, 2],
     [12, 3, 6, 5, 2],
     ]  # Доска с суммой монет в каждой клетке

res = [[0] * len(A) for _ in range(len(A[0]))]
res[0][0] = A[0][0]
# заполнение первого строки и первого столбца нарастающей суммой
for i in range(1, len(A)):
    res[i][0] = res[i-1][0] + A[i][0]

for i in range(1, len(A[0])):
    res[0][i] = res[0][i-1] + A[0][i]

for i in range(1, len(res)):
    for j in range(1, len(res[0])):
        res[j][i] = max(res[j-1][i], res[j][i-1]) + A[j][i]


for i in range(len(res)):
    print(*map(lambda x: f'{x:>3}', res[i]))