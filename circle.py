import math

def area(r):
    ''' 
    Возвращает площадь круга
        
        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            area (float): площадь круга с радиусом r
        
        Пример:
            area(3) вернет 28.27
    '''
    if r <= 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r

def perimeter(r):
    '''
    Возвращает периметр круга
        
        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            perimeter (float): периметр круга с радиусом r
        
        Пример:
            perimeter(3) вернет 18.85
    '''
    if r <= 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * r
