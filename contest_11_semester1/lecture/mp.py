from random import randint, random


def mp(weights: list, price: list, W: int) -> list:
    """Задача укладки рюкзака. W кг вещей в рюкзак, и W1 ...Wn (вес) вещей и стоимость этих вещей P1...Pn. Максимальную
    стоимость вещей, которую можно поместить в рюкзак. Ограничение: 1) все вещи в 1 экземпляре 2) Все веса - натуральные
    числа рюкзак и вес предметов"""
    R = [[0.0] * (W+1) for _ in range(len(weights) + 1)]
    for i in range(1, W + 1):
        for j in range(1, len(weights) + 1):
            if weights[j-1] > i:  # Если вещь i можем поместить в рюкзак
                R[j][i] = R[j-1][i]
            else:
                R[j][i] = max(R[j-1][i], price[j-1] + R[j-1][i-weights[j-1]])
    return R  # R[-1][-1] - result


if __name__ == '__main__':
    weights = [randint(1, 5) for _ in range(10)]
    price = [random() + 0.1 for _ in range(10)]
    w = 20

    R = mp(weights, price, w)

    print(weights)
    print(price)
    print(' ', ' '.join(map(lambda x: f'{x:>4}', range(w+1))))
    for j in range(len(weights)+1):
        print(j, *map(lambda x: f'{x:0.02f}', R[j]))
