"""E-Поиск подстроки в строке
Найти все вхождения строки A в строке B. Для решения данной задачи нужно использовать префикс- или z-функцию.

Примечание. Многократный вызов print в цикле может привести к превышению времени выполнения.

Формат входных данных
В первой строке вводится строка A, во второй строка B. Обе строки непустые и состоят из маленьких латинских букв.
Суммарная длина строк не превышает 200000.

Формат выходных данных
Все вхождения через пробел. Нумерация позиций с 0. Если вхождений нет, нужно вывести -1"""


def pref(S: str) -> list:

    pref = [0] * len(S)
    for i in range(1, len(S)):
        p = pref[i-1]
        while S[p] != S[i] and p > 0:
            p = pref[p-1]
        if S[i] == S[p]:
            pref[i] = p+1
        else:
            pref[i] = 0
    return pref


def kmp(subs: str, S: str) -> list:

    S1 = subs + '\0' + S
    P = pref(S1)

    res = []
    n = len(subs)
    for i in range(2 * n, len(S1)):
        if P[i] == n:
            res.append(i - 2 * n)
    return res if len(res) else [-1]


if __name__ == '__main__':
    A, B = [input() for _ in range(2)]
    print(*kmp(A, B))