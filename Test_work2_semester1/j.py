"""Вам необходимо реализовать калькулятор для векторов.

Вектор - трёхмерный.

Возможные операции: сложение двух векторов (знак +) векторное произведение (знак *) Калькулятор использует обратную
польскую нотацию для вычисления всего выражения.

Векторы и операции отделяются одним пробелом. Компоненты вектора - целые числа, записанные через запятую.

Формат входных данных: Одна строка - выражение для вычислений.

Формат выходных данных: Результат выражения - вектор."""


def Pars(data1):
    temp = list()
    tempo = ''
    sign = 1
    for el in data1:
        if el.isdigit():
            tempo = tempo + el
        elif el == '-':
            sign = -1
        else:
            temp.append(sign * int(tempo))
            tempo = ''
            sign = 1
    temp.append(sign * int(tempo))
    return temp


def Vec(data1, data2):
    temp = [0 for i in range(len(data1))]
    temp[0] = data1[1] * data2[2] - data1[2] * data2[1]
    temp[1] = -(data1[0] * data2[2] - data1[2] * data2[0])
    temp[2] = data1[0] * data2[1] - data1[1] * data2[0]
    return temp


def Sum(data1, data2):
    for i in range(len(data1)):
        data1[i] += data2[i]
    return data1


def RPN(data):
    tempo = []
    for x in data:
        if x == '+':
            temp1 = tempo[1]
            temp2 = tempo[0]
            r = Sum(temp1, temp2)
            tempo = [r] + tempo[2:]
        elif x == '*':
            temp1 = tempo[1]
            temp2 = tempo[0]
            r = Vec(temp1, temp2)
            tempo = [r] + tempo[2:]
        else:
            tempo = [x] + tempo
    if len(tempo) == 0:
        tempo.append([])
    return tempo[0]


def main():
    data = list(map(str, input().split()))

    for i in range(len(data)):
        if data[i] != '*' and data[i] != '+':
            data[i] = Pars(data[i])

    data = RPN(data)

    for i in range(len(data)):
        print(data[i], end='')
        if i != len(data) - 1:
            print(',', end='')


main()
