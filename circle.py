import math


def area(r):
    '''Принимает радиус окружности и возвращает её площадь
        Пример: возьмем r = 3, тогда area(3) вернет значение - 28,26.'''

    if type(r) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")
    if r < 0:
        raise ValueError("--Радиус не может быть отрицательным--")

    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус окружности и возвращает его периметр
        Пример: возьмем r = 2, тогда perimeter(2) вернет значение - 12,56'''

    if type(r) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")
    if r < 0:
        raise ValueError("--Радиус не может быть отрицательным--")

    return 2 * math.pi * r
