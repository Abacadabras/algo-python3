# Есть модуль heapq в котором есть все эти функции
from random import randint
import math


def heap_print(h):
    n = 1
    m_h = math.ceil(math.log2(len(h))) - 1
    print('   ' * ((2**m_h) - 1), end='')
    m_h += 1
    for i in range(len(h)):
        if i == n:
            m_h -= 2
            print('\n', '   ' * (2**m_h - 1), end='', sep='')
            m_h += 1
            n = n*2 + 1
        print(h[i], end='   ' * (2**m_h - 1))
    print()


def add_to_heap(h, element):
    """Добавление элемента в кучу"""
    h.append(element)
    shift_up(h, len(h) - 1)


def shift_up(h, i):
    """Перемещение элемента на свое место снизу-вверх"""
    if i == 0:
        return

    parent_i = (i-1) // 2

    if h[i] < h[parent_i]:
        h[i], h[parent_i] = h[parent_i], h[i]
        shift_up(h, parent_i)


def pop_from_heap(h):
    """Достает элемент из кучи"""
    if len(h) == 0:
        raise ValueError('heap is empty can\'t pop from it')

    result = h[0]

    if len(h) == 1:
        return h.pop()

    h[0] = h.pop()
    shift_down(h, 0)

    return result


def shift_down(h, i, max_n=None):
    """Двигаем элемент в низ, с учетом того что последние элементы не являются частью кучи. Для парамедиальной
    сортировки"""
    if max_n is None:
        max_n = len(h)

    # m = min([h[i]] + h[2*i + 1:2*i + 3])
    # Условия для сортировки, ограничитель max_n
    m = h[i]

    if 2*i + 1 < max_n and m > h[2*i + 1]:
        m = h[2*i + 1]

    if 2*i + 2 < max_n and m > h[2*i + 2]:
        m = h[2*i + 2]

    if h[i] == m:
        return

    if h[2*i + 1] == m:
        h[i], h[2*i + 1] = h[2*i + 1], h[i]
        shift_down(h, 2 * i + 1, max_n)
    else:
        h[i], h[2*i + 2] = h[2*i + 2], h[i]
        shift_down(h, 2*i + 2, max_n)


def heapify(h):
    """Преобразует массив в кучу. Сложность ~O(N)"""
    for i in range((len(h)-2) // 2, -1, -1):
        shift_down(h, i)


def heap_sort(a):
    heapify(a)
    max_n = len(a) - 1

    while max_n != 0:
        a[0], a[max_n] = a[max_n], a[0]
        shift_down(a, 0, max_n=max_n)  # Т.к. "последний элемент" не является частью кучи!
        max_n -= 1


if __name__ == '__main__':
    h = []
    a = [randint(100, 1000) for _ in range(10)]
    b = [randint(100, 1000) for _ in range(10)]

    for x in a:
        add_to_heap(h, x)

    print(f'a = {a}')
    print(f'h = {h}\n\nh')
    heap_print(h)
    heapify(a)
    print(f'\nheapify(a)')
    heap_print(a)

    for _ in range(10):
        print(pop_from_heap(h), end=', ')
    print()

    for _ in range(10):
        print(pop_from_heap(a), end=', ')
    print()

    print(b)
    heap_sort(b)
    print(b)
