"""B-InsertionSort
Написать программу, осуществляющую сортировку вставкой введённых целых чисел по возрастанию. Внимание! Сначала
необходимо считать все введённые числа в один список

Формат входных данных
Последовательность целых чисел, разделённая символом пробел.

Формат выходных данных
Набор расстановок чисел в сортируемом массиве. Внимание! Надо выводить весь массив после КАЖДОЙ перестановки элементов в
 нём. Если перестановок не было - НИЧЕГО не выводить"""


def foo_main():
    """Insertion sort"""
    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1, n):
        while i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
            print(*arr)


if __name__ == '__main__':
    foo_main()