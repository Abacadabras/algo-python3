
def factorial(n: int) -> int:
    if n == 0:
        return 1

    return n * factorial(n - 1)


for i in range(50):
    print(i, factorial(i))
