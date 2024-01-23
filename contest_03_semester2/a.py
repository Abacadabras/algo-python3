"""A-Студенты
Вам даны три списка (list или set) студентов.

learners_french - изучающие французский язык
pianists - владеющие игрой на фортепиано
swimmers - занимающиеся плаванием

Создайте программу, вычисляющую список пловцов-пианистов, не изучающих французский."""


if __name__ == '__main__':
    learners_french = {1, 2, 3}
    pianists = {3, 4, 5}
    swimmers = {3, 4, 8}

    intersection = (pianists.intersection(swimmers)).difference(learners_french)
    print(intersection)
