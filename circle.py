import math


def area(r):
    ''' Принимает радиус круга число r, возвращает площадь круга с радиусом r
        int(r) = 5 -> pi * r * r = 78.524564
    '''
    return math.pi * r * r


def perimeter(r):

    ''' Принимает радиус круга число r, возвращает длину окружности радиусом r
        int(r) = 5 -> 2 * pi * r = 31,436325
    '''
    return 2 * math.pi * r

