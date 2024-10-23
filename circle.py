import math

def area(r):
    '''
    Принимает радиус r и возвращает площадь круга
        Параметры:
            r (int): Радиус круга
            math.pi (floar): Число Pi
        Пример вызова:
            S = area(4)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус r и возвращает периметр круга
    Параметры:
            r (int): Радиус круга
            math.pi (floar): Число π
    Пример вызова:
        P = perimetr(4)
    '''
    return 2 * math.pi * r

