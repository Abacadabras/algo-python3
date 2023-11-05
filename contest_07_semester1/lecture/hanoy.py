
N = 5
A = [list(range(N, 0, -1)), [], []]


def hanoi(n, i, j, a=A):
    if n == 1:
        a[j-1].append(a[i-1].pop())
        print(f'Переложить с {i} на {j}, {a}')
        return

    hanoi(n-1, i, 6-i-j)
    a[j-1].append(a[i-1].pop())
    print(f'Переложить с {i} на {j}, {a}')
    hanoi(n-1, 6-i-j, j)


hanoi(N, 1, 2)
