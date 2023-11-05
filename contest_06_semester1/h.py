"""H-Сортировка только четных элементов
На вход подается массив из чисел. Вам необходимо отсортировать его так, чтобы нечетные по значению элементы остались
 на своих местах, а четные по значению элементы шли по возрастанию.

Примечание: встроенные сортировки использовать запрещено!

Формат входных данных
На первой строке натуральное число N ≤ 1000 - длина массива. Со следующих N строках вводятся элементы массива - числа не
превосходящие по модулю 10^6.

Формат выходных данных
Необходимо вывести в одной строке отсортированный по заданным правилам массив, элементы разделяются пробелом."""


def foo_main(n: int, arr: list, arr_even_numbers: list) -> list:

    arr_even_numbers.sort()

    numbers = 0
    for _ in range(n):
        if arr[_] % 2 == 0:
            arr[_] = arr_even_numbers[numbers]
            numbers += 1

    return arr


if __name__ == '__main__':
    n = int(input())
    array = [0]*n
    array_even_numbers = []
    for _ in range(n):
        digit = int(input())
        array[_] = digit
        if digit % 2 == 0:
            array_even_numbers.append(digit)

    print(*foo_main(n, array, array_even_numbers))
