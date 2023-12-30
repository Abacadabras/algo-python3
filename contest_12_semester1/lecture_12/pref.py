
def pref(S: str) -> list:
    """Префикс функция - длина максимального собственного суффикса, который является префиксом. Собственный суффикс -
    суффикс, не равный самой строке. """
    pref = [0] * len(S)
    for i in range(1, len(S)):
        p = pref[i-1]
        while S[p] != S[i] and p > 0:
            p = pref[p-1]
        if S[i] == S[p]:
            pref[i] = p+1
        else:
            pref[i] = 0
    return pref


if __name__ == "__main__":
    s = 'abacabadabacabac'
    print(' ', '  '.join(s))
    print(''.join(map(lambda x: f'{x:3}', pref(s))))
