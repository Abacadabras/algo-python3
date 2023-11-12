
def gen_bin(n: int, prefix):

    if n == 0:
        print(prefix)
        return

    gen_bin(n - 1, prefix + '0')
    gen_bin(n - 1, prefix + '1')


gen_bin(3, 'число: ')
