"""D-Голосование
У каждого первокрусника спросили: "Какой ваш любимый фильм?". Ответы записали. Необходимо вывести рейтинг фильмов с
количеством голосов за каждый в порядке убывания."""


if __name__ == '__main__':
    answers = input().split()
    rate = {}

    for ans in answers:
        if ans in rate:
            rate[ans] += 1
        else:
            rate[ans] = 1

    res = {key: value for key, value in sorted(rate.items(), key=lambda x: x[0], reverse=True)}
    print(res)
