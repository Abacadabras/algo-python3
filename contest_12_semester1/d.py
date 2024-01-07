"""D-Z-функция
Посчитать z-функцию для строки.

Примечание: Многократный вызов print в цикле может привести к превышению допустимого времени работы.

Формат входных данных
В первой строке заданна непустая строка из маленьких букв латинского алфавита. Длина строки не превышает 100000.

Формат выходных данных
Массив чисел через пробел, представляющих значения z-функции"""


def foo_main(s: str) -> list:

    res = [0] * len(s)
    r = l = 0
    for i in range(1, len(s)):
        z = max(0, min(res[i - l], r - i))
        while i + z < len(s) and s[z] == s[i + z]:
            z += 1
        res[i] = z
        if i + z > r:
            l = i
            r = i + z

    return res


if __name__ == '__main__':
    str = input()
    print(*foo_main(str))
