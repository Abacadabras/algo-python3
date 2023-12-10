"""Задача о дипломах размером n x m и количеством k штук на доске размером X x X. И найти минимальный размер доски,
чтобы все дипломы помещались на доске. И дипломы нельзя переворачивать!"""

n, m, k = map(int, input().split())

left = 0
right = (n + m) * k  # Точно поместятся все дипломы (очень большое число

while right - left > 1:
    middle = (right + left) // 2
    if (middle // n) * (middle // m) < k:
        left = middle
    else:
        right = middle

print(right)
