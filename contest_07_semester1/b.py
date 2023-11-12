"""B-Женские и мужские последовательности Хофштадтера
Определить n-ый женский и мужской член последовательности Хофштадтера. Женские (F) и мужские (M) последователи
Хофштадтера определяются следующим образом:

F(0) = 1, M(0) = 0

F(n) = n - M(F(n-1)), M(n) = n - F(M(n-1)), n > 0

Внимание! Нужно передавать на проверку только две функции F(n) и M(n). В этих функциях нельзя использовать циклы.

Описание аргументов функции
Функции F(n) и M(n) принимают на вход целое число n - номер члена последовательности, который нужно вычислить.

Формат возвращаемого функцией значения
F(n) функция возращает женское число (целое) последовательности Хофштадтера. M(n) функция возращает мужское число
(целое) последовательности Хофштадтера."""


def F(n):

    if n == 0:
        return 1
    return n - M(F(n-1))


def M(n):

    if n == 0:
        return 0
    return n - F(M(n-1))
