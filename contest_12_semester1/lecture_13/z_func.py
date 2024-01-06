
def z_func(s: str) -> list:
    """Реализация Z-func O(N^2)"""
    res = [0] * len(s)
    for i in range(1, len(s)):
        z = 0
        while i+z < len(s) and s[z] == s[z+i]:
            z += 1
        res[i] = z
    return res


def z_func_opt(s: str) -> list:
    """Оптимальный алгоритм O(N)!!! Идея не сравнивать полностью строки заново"""
    res = [0] * len(s)
    r = l = 0
    for i in range(1, len(s)):
        z = max(0, min(res[i-l], r-i))
        while i + z < len(s) and s[z] == s[i+z]:
            z += 1
        res[i] = z
        if i + z > r:
            l = i
            r = i + z

    return res


if __name__ == "__main__":
    s = 'ababcababcffffababcabababcababc'
    print(' ', '  '.join(s))
    print(''.join(map(lambda x: f'{x:3}', z_func(s))))
    print(''.join(map(lambda x: f'{x:3}', z_func_opt(s))))

