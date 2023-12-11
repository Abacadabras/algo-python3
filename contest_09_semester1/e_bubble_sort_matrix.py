"""E-Сортировка пузырьком двумерного массива

В этой задаче необходимо отсортировать двумерный массив целых чисел, используя сортировку пузырьком.

Отсортированным считается массив, в котором отсортированы все строки по неубыванию, при этом последний элемент i-ой
строки не больше, чем первый элемент i+1 строки.

Для этого напишите функцию bubble_sort2d(matrix, N, M), совершающую описанную выше сортировку.

Ограничения
Нельзя:

создавать новые массивы (и срезы, поскольку они создают массивы)
изменять количество элементов в matrix
использовать встроенные сортировки

Аргументы функции
matrix - двумерный массив целых чисел, содержащий N строк, в каждом M элементов (т.е. это матрица NxM)

Формат возвращаемого значения
Функция не возвращает значений, но совершает сортировку в самом массиве matrix и производит печать.

Ваша программа должна напечатать исходный массив и затем печатать массив каждый раз, когда происходит перестановка.

Чтобы печать не слилась в единый поток, после каждой печати массива печатайте одну новую строку (это можно сделать
командой print())."""


def bubble_sort2d(matrix: list, N: int, M: int):

    len_matrix = N * M
    print_arr(matrix)

    for i in range(len_matrix - 1, 0, -1):
        el_column = 0
        for j in range(i):
            el_line = el_line_next = j // M
            el_column_next = el_column + 1
            if el_column == M:
                el_column = 0
                el_column_next = 1
            if el_column == M-1:
                el_line_next = el_line + 1
                el_column_next = 0

            if matrix[el_line][el_column] > matrix[el_line_next][el_column_next]:
                matrix[el_line][el_column], matrix[el_line_next][el_column_next] = \
                    matrix[el_line_next][el_column_next], matrix[el_line][el_column]
                print_arr(matrix)

            el_column += 1


def print_arr(arr):

    for _ in range(len(arr)):
        print(*arr[_])
    print()


# if __name__ == '__main__':
#     matrix = [[0, 3, 4], [1, 0, 2]]
#     print(bubble_sort2d(matrix, 2, 3))
