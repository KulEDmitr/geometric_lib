import math


def area(r):
    '''
    Функция area(r) принимает аргумент r и возвращает площадь окружности с радиусом r
    Параметры:
        r (int): радиус окружности
    Возвращает:
        area(int): Площадь окружности радиуса
    Примеры:
        r = 5
        s = area(r)
        print(s)
    Output:
        78.5398163
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Функция perimeter(r) принимает аргумент r и возвращает периметр окружности с радиусом r
    Параметры:
        r (int): радиус окружности
    Возвращает:
        perimeter(int): периметр окружности радиуса r
    Примеры:
        r = 5
        p = perimeter(r)
        print(p)
    Output:
        31.4159265
    '''
    return 2 * math.pi * r

