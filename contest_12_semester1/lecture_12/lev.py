
def lev(s: str, g: str) -> list:
    """Редакционное расстояние Левенштейна. 3 вида правок: 1) Удалить букву 2) Вставить букву 3) заменить букву
    Решение с помощью динамического программирования."""
    L = [[i+j if i*j == 0 else 0 for j in range(len(s) + 1)] for i in range(len(g) + 1)]  # Нулевая строка и столбец
    # заполняются 0 1 2...len(s) и 0 1 2...len(g) (по возрастанию короче) Остальное все заполняется нулями

    for i in range(1, len(g) + 1):
        for j in range(1, len(s) + 1):
            if s[j-1] == g[i-1]:
                L[i][j] = L[i-1][j-1]  # если буквы равны берем пред. по диагонали (ничего делать не нужно)
            else:
                L[i][j] = min(L[i-1][j], L[i-1][j-1], L[i][j-1]) + 1   # Выбор из мин условия (удалить, вставить,
                # заменить) букву. Т.к. буквы не равны и + 1 действия в текущую клетку естественно.
    return L  # Ответ в L[-1][-1] - количество изменений


def get_chahges(s: str, g: str) -> list:
    """Редактор изменений, что нужно изменить в редакционном расстоянии Левенштейна по преобразованию слова"""
    L = lev(s, g)
    res = [0] * L[-1][-1]
    k = len(res) - 1  # Счетчик изменений для ответа
    i = len(g)
    j = len(s)
    while i + j != 0:
        if s[i-1] == g[i-1] and L[i][j] == L[i-1][j-1]:
            i -= 1
            j -= 1
        else:  # Найти минимум и определить действие по правке
            if L[i-1][j] - L[i-1][j] == 1:
                res[k] = f'insert {g[i-1]} in pos {i-1}'
                k -= 1
                i -= 1
            elif L[i][j] - L[i][j-1] == 1:
                res[k] = f'delete {s[j-1]} in pos {j-1}'
                k -= 1
                j -= 1
            else:
                res[k] = f'exchange {s[j-1]}({j-1}) on {g[i-1]}({i-1})'
                k -= 1
                i -= 1
                j -= 1
    return res


if __name__ == "__main__":
    S = 'kolbasa'
    G = 'moloko'
    L = lev(S, G)
    print('   ', *S)
    print(' ', *L[0])
    for i in range(len(G)):
        print(G[i], *L[i+1])

    A = get_chahges(S, G)
    for line in A:
        print(line)
