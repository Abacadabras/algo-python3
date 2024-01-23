"""B-Уникальные числа
Вам даны два списка (list) чисел. Подсчитайте количество уникальных в каждом по отдельности, и количество уникальных
среди обоих списков."""


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]

    set1 = set(list1)
    set2 = set(list2)

    print(len(set1))
    print(len(set2))
    print(len(set1.union(set2)))
