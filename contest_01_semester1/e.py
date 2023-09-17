"""E-Длина удава
Требуется найти длину удава, выраженную в мартышках, попугаях или слоненках, по выбору пользователя. "Эффективная длина"
 попугая - 10см, мартышки - 90см, слоненка - 3м. Результат округляйте вниз, однако, если при этом получается ноль,
 выведите 1, чтобы не обижать удава.

Формат входных данных
В первой строке натуральное число - длина удава в сантиметрах. Во второй строке - "в ком измерять", "monkey", "parrot"
или "elephant".

Формат выходных данных
Одно число — результат."""


from typing import Union


def foo_main(length: int, unit: str) -> Union[int, str]:

    p = 10
    m = 90
    sl = 300
    if unit == 'monkey':
        return max(1, length // m)
    elif unit == 'parrot':
        return max(1, length // p)
    elif unit == 'elephant':
        return max(1, length // sl)
    else:
        return 'ERROR!'


if __name__ == '__main__':
    boa, k = int(input()), input()
    print(foo_main(boa, k))
