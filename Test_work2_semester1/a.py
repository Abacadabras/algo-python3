"""В строке, состоящей из слов, разделенных пробелами, определить длину кратчайшего и самого длинного слов.

Формат входных данных: Одна строка, содержащая слова, записанные через пробел. Длина слов не превышает 1000.

Формат выходных данных: Два числа в одной строке. Длина самого короткого слова и длина самого длинного слова."""


def foo_main(s: str) -> tuple:

    res = []

    for word in s:
        res.append(len(word))

    return min(res), max(res)


if __name__ == '__main__':
    str = input().split()
    print(*foo_main(str))
