import doctest


def get_polish(s: str) -> list:
    """convert math string to polish string
    >>> get_polish('2 * ( 3 + 4 ) + 3 - 5 * 6')
    ['2', '3', '4', '+', '*', '3', '5', '6', '*', '-', '+']
    """
    res = []
    stack = ['#']
    for el in s.split():
        if el not in '()+-*/':
            res.append(el)
        else:
            if el == '(':
                stack.append(el)
            elif el == ')':
                el = stack.pop()
                while el != '(':
                    res.append(el)
                    el = stack.pop()
            else:
                op = stack.pop()
                while '()+-*/'.find(op) > '()+-*/'.find(el):
                    res.append(op)
                    op = stack.pop()
                stack.append(op)
                stack.append(el)
    # clearing the stack of operations
    while len(stack) != 1:
        res.append(stack.pop())

    return res


if __name__ == "__main__":
    doctest.testmod()
