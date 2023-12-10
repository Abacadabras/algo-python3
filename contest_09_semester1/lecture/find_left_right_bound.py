
def find_left_bound(A: list, value: int) -> int:
    """ find left bound of `value` in `a` """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] < value:
            left = middle
        else:
            right = middle

    return left


def find_right_bound(A: list, value:int) -> int:
    """ find right bound of `value` in `a` """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] <= value:
            left = middle
        else:
            right = middle

    return right


def check(A: list, value):
    """Проверка если или нет в массиве элемент. Проверку на -1 еще надо сделать т.к. может так быть!"""
    return A[find_left_bound(A, value) + 1] == value


a = [i*i for i in range(10)]
print(find_left_bound(a, 21))
print(find_left_bound(a, -4))
print(find_left_bound(a, 10000))
print(find_left_bound([1, 2, 3, 4, 4, 5, 8, 9], 4))

print(find_right_bound(a, 21))
print(find_right_bound(a, -4))
print(find_right_bound(a, 10000))
print(find_right_bound([1, 2, 3, 4, 4, 5, 8, 9], 4))

