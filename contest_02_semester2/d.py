"""D-Хеш-таблица с цепочками - Удаление элемента
Эта задача из серии по реализации ассоциативного массива на хеш-таблице с использованием цепочек для разрешения коллизий.

В задаче необходимо написать удаления элемента по ключу.

В тестах вашей программе будет доступна хеш-таблица следующего формата:

hash_table = [
    [], # это пустая цепочка
    [[hash1, key1, value1]], # это цепочка с одним значением
    [[hash2, key2, value2], [hash3, key3, value3]], # это цепочка с двумя значениями
    ...
]
Она хранится в переменной hash_table (ввод таблицы осуществлять не нужно). Размер таблицы 10. Ключи и значения в таблице
 хранятся в виде строк.

Хеши в таблице получали с помощью полиномиальной хеш-функции с параметрами:

основание 91
модуль 100
Вам необходимо реализовать функцию-интерфейс remove(table, key) , которая удаляет элемент по ключу. Если элемент в
таблице отсутствует, то таблица остается без изменений.

Аргументы
Функция remove(table, key) имеет два аргумента:

table - хеш-таблица формата, как выше
key - ключ, по которому осуществляется удаление (имеет тип str )
Возвращаемое значение
Функция возвращает значение удаляемого элемента, лежащее по ключу key . Если ключа нет, то функция должна вернуть строку
'KeyError'."""


def remove(table, key):

    hash_value = my_hash(91, 100, key)
    mod = hash_value % 10

    for i, elem in enumerate(table[mod]):
        if elem[0] == hash_value and elem[1] == key:
            trash_el = elem[2]
            del table[mod][i]
            return trash_el
    else:
        return 'KeyError'


def my_hash(base: int, degree: int, string: str) -> int:

    value = 0
    for i in range(len(string)-1, -1, -1):
        value += ord(string[i]) * base**(len(string)-1-i)

    return value % degree


if __name__ == '__main__':
    # исходное состояние таблицы
    example_table = [
        [], [],
        [
            [32, 'ONLY', 'pal;cw'],
            [62, 'INDUSTRY', 'lfow'],
            [72, 'LETRASET', 'awdwad'],
            [32, 'BEEN', 'lkawdk'],
        ],
        [], [], [], [], [], [], [],
    ]
    v1 = remove(example_table, 'BEEN')  # v1 == 'lkawdk'
    v2 = remove(example_table, 'PRODUCT')  # v2 == 'KeyError'
    # таблица принимает вид (элемент с ключом 'BEEN' удалён)
    # example_table = [
    #     [], [],
    #     [
    #         [32, 'ONLY', 'pal;cw'],
    #         [62, 'INDUSTRY', 'lfow'],
    #         [72, 'LETRASET', 'awdwad'],
    #     ],
    #     [], [], [], [], [], [], [],
    # ]
    print(example_table)
