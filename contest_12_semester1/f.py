"""F-А-функция
Дана строка S, состоящая из N символов. Определим функцию A(i) от первых i символов этой сроки следующим образом:

A(i) = максимально возможному k, что равны следующие строки:

S[0]+S[1]+S[2]+…+S[k-1]

S[i]+S[i–1]+S[i–2]+…+S[i–k+1]

где S[i] – i-ый символ строки S, а знак + означает, что символы записываются в строчку непосредственно друг за другом.

Напишите программу, которая вычислит значения функции A для заданной строчки для всех возможных значений i от 1 до N.

Примечание. Многократный вызов print в цикле может привести к превышению времени выполнения.

Формат входных данных
В единственной строке записана строка, состоящая только из больших и/или маленьких латинских букв. Длина строки
1 <= N <= 200000.

Формат выходных данных
Массив чисел через пробел, представляющих значения A-функции"""


def z_func(s: str) -> list:

    res = [0] * len(s)
    r = l = 0
    for i in range(1, len(s)):
        z = max(0, min(res[i-l], r-i))
        while i + z < len(s) and s[z] == s[i+z]:
            z += 1
        res[i] = z
        if i + z > r:
            l = i
            r = i + z

    return res


if __name__ == '__main__':
    S = input()
    print(*z_func(S+S[::-1])[len(S):][::-1])