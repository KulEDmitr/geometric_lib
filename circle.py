import math
def area_circle(r):
    '''
    Принимает число r-радиус окружности, возвращает её площадь
    
    Example:
        in : `10`
        out :` 100`
    '''
    return math.pi * r * r


def perimeter_circle(r):
    '''Принимает число r-радиус окружности, возвращает её длину
    Example:

    in : `10`
    out :` 62,83`
    '''
    return 2 * math.pi * r