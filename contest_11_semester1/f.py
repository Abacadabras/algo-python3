"""F-Наибольшая возрастающая подпоследовательность
Подпоследовательностью {x n k } называется числовая последовательность, которая составлена из членов последовательности
{x n } и в которой порядок следования её элементов совпадает с их порядком следования в исходной последовательности
{x n }.
Вам необходимо написать функцию lis(s), которая вычисляет наибольшую (строго) возрастающую подпоследовательность (НВП)
для s, где s — непустая числовая последовательность.
"""


def lis(s):
    count = [0 for _ in range(len(s))]

    for i in range(len(s)):
        for j in range(i):
            if s[i] > s[j] and count[j] > count[i]:
                count[i] = count[j]
        count[i] += 1

    last = max(count)
    i = count.index(last)
    ans = [count[i]]

    while count[i] != 1:
        j = i - 1
        while count[j] != count[i] - 1 or s[j] >= s[i]:
            j -= 1
        i = j
        ans.append(s[i])

    return ans[::-1]
