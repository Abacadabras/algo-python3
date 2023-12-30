
def find(subs: str, s: str) -> int:
    """Поиск подстроки subs в строке s. Первое вхождение (позиция)!! Результат: где находиться.
    Сложность O(n * m), где m = len(susb), n = len(s)"""

    for i in range(len(s) - len(subs) + 1):
        flag = True
        for j in range(len(subs)):
            if subs[j] != s[j+i]:
                flag = False
                break
        if flag:
            return i

    return -1


print(find('aaa', 'vvvaaa'))
