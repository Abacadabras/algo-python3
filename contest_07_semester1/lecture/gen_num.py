
def gen_num(n: int, base: int, prefix):

    if n == 0:
        print(prefix)
        return

    for digit in range(base):
        gen_num(n - 1, base, prefix + str(digit))


gen_num(3, 4, 'число: ')
