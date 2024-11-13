import math


def area(r):
    '''
    Принимает число r (радиус круга), возвращает pi*r*r (площадь круга).

    Пример вызова функции:
        Входное значение r (int/float): 5
        Возвращаемое значение area (int/float): 25 * pi
    '''

    if not isinstance(r, (int, float)): 
        raise TypeError("Error: the function is not passed an int/float type")
    if r <= 0:
        raise ValueError("Error: number less than 0 or equal 0")
    
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r (радиус круга), возвращает 2*pi*r (периметр круга).

    Пример вызова функции:
        Входное значение r (int/float): 5
        Возвращаемое значение perimeter (int/float): 10 * pi
    '''

    if not isinstance(r, (int, float)): 
        raise TypeError("Error: the function is not passed an int/float type")
    if r <= 0:
        raise ValueError("Error: number less than 0 or equal 0")
    
    return 2 * math.pi * r

