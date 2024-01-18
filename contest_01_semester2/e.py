"""E-Скалярное произведение
Одной из важнейших операций в линейной алгебре, аналитической геометрии, математическом анализе, анализе данных,
искусственном интеллекте, компьютерной графике и в огромном количестве других областей математики и информатики является
вычисление скалярного произведения двух векторов.

Вычисляется скалярное произведение, как сумма произведений соответствующих компонент векторов.

В данной задаче вам необходимо написать функцию:

python: dot_product(N, vector1, vector2),
cpp: void dot_product(int N, int *vector1, int *vector2),
вычисляющую скалярное произведение для двух заданных векторов одинаковой размерности N.

Обратите внимание: в решении должно быть только объявление одной функции dot_product и никакого другого кода.

Аргументы функции
Функция принимает в качестве аргументов размерность пространства N и 2 вектора. Гарантируется, что размерности векторов
совпадают. Векторы заданы списками длины N.

Возвращаемое значение
Функция должна возвращать одно число -- скалярное произведение заданных векторов."""


def dot_product(n: int, vector1: list, vector2: list) -> int:

    result = 0

    for i in range(n):
        result += vector1[i] * vector2[i]

    return result
