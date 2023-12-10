
a, b, c = map(lambda x: float(x) ** 2, input().split())
print(a, b, c)

my_f = lambda x: x**3

print(my_f(4))

A = [(i, i**2 % 10) for i in range(20)]

A.sort(key=lambda x: x[1])
A.sort(key=lambda x: str(x))
