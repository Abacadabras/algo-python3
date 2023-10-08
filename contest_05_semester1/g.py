"""G-Какое число встречается в массиве наибольшее число раз
На вход программе подается массив чисел. Необходимо найти число, которое чаще всего встречается в массиве.
Гарантируется, что такое число одно.

Формат входных данных
В первой строке задается число N, длина массива, далее идут N чисел -- элементы массива. Все числа больше 0 и меньше 100
Каждое число вводится с новой строки.

Формат выходных данных
Одно число, которое встречается наибольшее количество раз."""


def foo_main(n: int, arr: list) -> int:

    number = 0
    count_number = 0
    for i, elem in enumerate(arr):
        count = 1
        for _ in range(i+1, n):
            if elem == arr[_]:
                count += 1

        if count > count_number:
            count_number = count
            number = elem

    return number


if __name__ == '__main__':
    n1 = int(input())
    arr1 = [int(input()) for _ in range(n1)]
    print(foo_main(n1, arr1))
