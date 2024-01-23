"""F-Генеалогическое древо
Заведите словарь d, в котором ключ - имя человека, а значение - список родителей. Напишите функции, которые по имени
человека name сообщают о его родственниках.

Вот список функций для реализации

parents(d, name) - возвращает список родителей
grandparents(d, name) - возвращает список бабушек и дедушек
sibling(d, name) - возвращает список родных братьев и сестёр
children(d, name) - возвращает список детей
grandchildren(d, name) - возвращает список внуков и внучек"""


def parents(d, name):
    return d[name]


def grandparents(d, name):
    grandpar = []
    for par in parents(d, name):
        if par in d.keys():
            grandpar += parents(d, par)
    return grandpar


def find_name(dictionary, value):
    names = []
    for name, val in dictionary.items():
        if val == value:
            names.append(name)
    return names


def sibling(d, name):
    par = parents(d, name)
    sibl = find_name(d, par)
    sibl.remove(name)
    return sibl


def children(d, name):
    chil = []
    for key, val in d.items():
        if name in val:
            chil.append(key)
    return chil


def grandchildren(d, name):
    grandchil = []
    chil = children(d, name)
    for key, val in d.items():
        for c in chil:
            if c in val:
                grandchil.append(key)
    return (grandchil)


if __name__ == '__main__':
    d = {'alex': ['bob', 'marla'],
         'bob': ['george', 'maria'],
         'fred': ['alex', 'kim'],
         'george': ['alex', 'kim'],
         'michael': ['bob', 'marla']}

    print(parents(d, 'alex'))
