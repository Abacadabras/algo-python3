
def scd(a, b):
    """НОД алгоритм Евклида, рекурсия"""
    if a == b:
        return a
    if a > b:
        return scd(a - b, b)
    return scd(a, b - a)


print(scd(12432, 123214))
