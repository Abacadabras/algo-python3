"""F-Похожие массивы
Два массива называются похожими, если совпадают множества чисел, встречающихся в этих массивах. Требуется написать
программу, которая определит, похожи ли два заданных массива.

Примечание: встроенные сортировки и set использовать запрещено!

Формат входных данных
На первой строке даны два числа N и M – длины массивов (1 ≤ M, N ≤ 1000). Во второй строке записаны N чисел – элементы
первого массива. В третьей строке записаны M чисел – элементы второго массива. Числа в строках разделены пробелами,
элементы массивов – целые числа.

Формат выходных данных
Выведите Yes, если массивы похожи, иначе No."""


def foo_main(N: list, M: list) -> str:

    arr_N = remove_duplicates(hoar_sort(N))
    arr_M = remove_duplicates(hoar_sort(M))

    return 'Yes' if arr_N == arr_M else 'No'


def remove_duplicates(A: list) -> list:

    res, el = [], A[0]

    for i in range(1, len(A)):
        if A[i] > el:
            res.append(el)
            el = A[i]

    return res


def hoar_sort(A):

    if len(A) <= 1:
        return A

    barrier = A[0]
    left = []
    middle = 0
    right = []
    for num in A:
        if num < barrier:
            left.append(num)
        elif num > barrier:
            right.append(num)
        else:
            middle += 1

    hoar_sort(left)
    hoar_sort(right)

    return left + [barrier] + right


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr_N = list(map(int, input().split()))
    arr_M = list(map(int, input().split()))
    print(foo_main(arr_N, arr_M))
