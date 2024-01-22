"""E-Алгоритм Рабина-Карпа
Найти все вхождения строки A в строке B, используя алгоритм Рабина-Карпа. Строки состоят из строчных и прописных
английских букв.

Примечание: для вывода массива чисел рекомендуется использовать print(" ".join(map(str, numbers))). Многократный вызов
print в цикле может привести к TL.

Формат входных данных
В первой строке вводится строка A, во второй строка B. Обе строки непустые и состоят из маленьких латинских букв.
Суммарная длина строк не превышает 200000.

Формат выходных данных
Все вхождения через пробел. Нумерация позиций с 0. Если вхождений нет нужно вывести -1."""

base = 91
mod = 1000000321


def code(symbol):
    return ord(symbol) - ord('a') + 1


def poly_hash(string):
    values = [0]
    for elem in string:  # последовательно считаем значения хеш-функции на префиксах строки
        values.append(((values[-1] * base) + code(elem)) % mod)
    return values


target = input()  # ввод данных
text = input()
len_target = len(target)
len_text = len(text)

hash_target = poly_hash(target)[-1]  # хеш искомой строки
hash_text = poly_hash(text)  # хеши префиксов строки, в которой ищем таргет

indexes = []  # массив с местами вхождения таргета в тексте
tmp = base ** len_target % mod  # смотри ссылку
for i in range(0, -len_target + len_text + 1):  # сравниваем хеши подстрок с хешем таргета
    if (hash_target ==
            (hash_text[i + len_target] - hash_text[i] * tmp) % mod):  # если совпадает, то записываем позицию
        indexes.append(i)

if indexes:  # печать позиций
    print(" ".join(map(str, indexes)))
else:
    print(-1)
