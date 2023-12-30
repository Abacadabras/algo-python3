
def comp(s: str, g: str) -> bool:
    """Сравнение строк s и g. Сложность O(n)"""
    if len(s) != len(g):
        return False

    for x, y in zip(s, g):  # zip выдает 1, 2... буквы из строк s и g
        if x != y:
            return False

    return True
