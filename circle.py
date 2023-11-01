import math
import validation

def area(r):
    '''
    Возвращает площадь круга с заданным радиусом r

        Параметры:
            r (int|float): радиус круга

        Возвращаемое значение:
            (float): площадь круга с радиусом r

    Пример вызова:
        >>> area(10)
        314.1592653589793
    '''

    validation.check_args(r)

    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга с заданным радиусом r

        Параметры:
            r (int|float): радиус круга

        Возвращаемое значение:
            (float): периметр круга с радиусом r
    
    Пример вызова:
        >>> perimeter(10)
        62.83185307179586
    '''

    validation.check_args(r)

    return 2 * math.pi * r

