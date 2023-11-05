
def russ_doll(n: int):
    if n == 1:
        print('Сделал матрёшку')
        return
    print('Верх матрёшки', n)
    russ_doll(n - 1)
    print('Низ матрёшки', n)


russ_doll(5)
