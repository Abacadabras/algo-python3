from math import sin


def bin_solve(f, left: float, right: float, epsilon=1E-5):
    """Где функция f(x) = 0 в интервале [left, right] приблизительно равна 0, с заданной точностью.
    Функция непрерывна! В качестве примера, не самый быстрый метод."""
    while right - left > epsilon:
        middle = (left + right) / 2
        if f(middle) == 0:
            return middle
        if f(left) * f(middle) < 0:
            right = middle
        else:
            left = middle

    return (right + left) / 2


def my_f(x):
    return x**3 + 15 * x**2 - 38*x + 125


print(bin_solve(my_f, -100, 100))
print(bin_solve(lambda x: x**3 + 15 * x**2 - 38*x + 125, -100, 100))  # example lambda functions
print(bin_solve(sin, 3, 4))
