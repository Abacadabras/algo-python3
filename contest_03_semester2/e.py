"""E-Частотный анализ слов в тексте
Напишите программу, подсчитывающую количество каждого слова в тексте. В тексте присутствует пунктуация. Слова с
заглавной и строчной буквы не различать. Итоговый список слов и их количества в тексте выводить в порядке убывания по
количеству."""


if __name__ == '__main__':
    text = input().split(' ')

    for ind, word in enumerate(text):
        text[ind] = word.lower().strip('.,!?:\n ')

    bag = {}

    for word in text:
        if word in bag:
            bag[word] += 1
        elif word != '':
            bag[word] = 1

    res = {key: value for key, value in sorted(bag.items(), key=lambda x: x[1], reverse=True)}

    print(res)
