
def reshet(max_n):
    """
    Алгоритм решета Эрастофена по поиску простых чисел
    """
    A = [True] * max_n
    A[0] = A[1] = False

    for i in range(max_n):
        if A[i]:
            for j in range(2*i, max_n, i):
                A[j] = False

    res = []
    for i in range(max_n):
        if A[i]:
            res.append(i)

    return (res,)  # пример кортежа из 1 элемента
