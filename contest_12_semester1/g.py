"""G-Циклический сдвиг
Нужно найти сколько раз A надо сдвинуть циклически влево, чтобы получить строку B. Циклический сдвиг влево на 1
превращает строку "abcde" в строку "bcdea".

Примечание. Необходимо решить задачу оптимальным способом. Для этого вам нужно воспользоваться префикс- или Z-функцией.

Формат входных данных
В первой строке вводится строка A, во второй строка B. Длины строк одинаковы. Обе строки состоят из маленьких латинских
букв. Суммарная длина строк не превышает 20000.

Формат выходных данных
Искомый сдвиг, либо -1, если строки не являются циклическим сдвигом друг друга."""


def prefix(string):

    prefix_values = [0] * len(string)
    k = 0
    for i in range(1, len(string)):
        while k > 0 and string[k] != string[i]:
            k = prefix_values[k - 1]
        if string[k] == string[i]:
            k += 1
        prefix_values[i] = k
    return prefix_values


if __name__ == '__main__':
    string, cyclic = input(), input()

    if string == cyclic:
        print(0)
        exit()

    prefix_list = prefix(string + '#' + 2 * cyclic)
    indicator = 0

    for i in range(len(string), len(prefix_list)):
        if prefix_list[i] == len(string):  # example: abcd#cdabcdab
            indicator = 1  # 0000000123[4]12
            print(3 * len(string) - i)
            break

    if indicator == 0:
        print(-1)
