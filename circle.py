import math

def area_circle(r):
    '''
    Возвращает площадь круга с заданным радиусом.

    Параметры:
        r (float): радиус круга

    Возвращаемое значение:
        area (float): площадь круга
    Пример использования:
        >>> area(7)
    153.93804002589985
    '''
    return math.pi * r * r

def perimeter_circle(r):
    '''
    Возвращает периметр (длину окружности) круга с заданным радиусом.

    Параметры:
        r (float): радиус круга

    Возвращаемое значение:
        perimeter (float): периметр круга
    Пример использования:
        >>> perimeter(7)
    43.982297150257104
    '''
    return 2 * math.pi * r
