from random import randint


def add_to_heap(h, element):
    """Добавление элемента в кучу"""
    h.append(element)
    shift_up(h, len(h) - 1)


def shift_up(h, i):
    """Перемещение элемента на свое место снизу-вверх"""
    if i == 0:
        return

    parent_i = (i - 1) // 2

    if h[i] < h[parent_i]:
        h[i], h[parent_i] = h[parent_i], h[i]
        shift_up(h, parent_i)


def pop_from_heap(h):
    """Достает элемент из кучи"""
    if len(h) == 0:
        raise ValueError('heap is empty can\'t pop from it')

    if len(h) == 1:
        return h.pop()
    # запоминаем 0 элемент, который вернем, берем конечный на 0 (вершину кучи) место и опускаем на свое место
    result = h[0]
    h[0] = h.pop()
    shift_down(h, 0)

    return result


def shift_down(h, i):
    """Двигаем элемент в низ"""
    m = min([h[i]] + h[2*i + 1:2*i + 3])

    if h[i] == m:
        return

    if h[2*i + 1] == m:
        h[i], h[2*i + 1] = h[2*i + 1], h[i]
        shift_down(h, 2*i + 1)
    else:
        h[i], h[2*i + 2] = h[2*i + 2], h[i]
        shift_down(h, 2*i + 2)


def heapify(h):
    """Преобразует массив в кучу. Без использования доп. памяти. Сложность ~O(N)"""
    for i in range((len(h)-2) // 2, -1, -1):
        shift_down(h, i)


if __name__ == '__main__':
    h = []
    a = [randint(100, 1000) for _ in range(10)]

    for x in a:
        add_to_heap(h, x)

    print(a)
    print(h)
    heapify(a)
    print(a)

    for _ in range(10):
        print(pop_from_heap(h), end=', ')
    print()

    for _ in range(10):
        print(pop_from_heap(a), end=', ')
    print()
