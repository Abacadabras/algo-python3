"""F-BubbleSort
Написать программу, осуществляющую сортировку пузырьком введённых целых чисел по возрастанию. Внимание! Сначала
необходимо считать все введённые числа в один список

Формат входных данных
Последовательность целых чисел, разделённая символом пробел.

Формат выходных данных
Набор расстановок чисел в сортируемом массиве. Внимание! Надо выводить весь массив после КАЖДОЙ транспозиции элементов
в нём. Если перестановок не было - НИЧЕГО не выводить"""


def foo_main():
    """Bubble sort"""
    arr = list(map(int, input().split()))
    n = len(arr)
    print(*arr)

    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(*arr)


if __name__ == '__main__':
    foo_main()
