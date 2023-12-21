import math


def area(r):
    ''' Принимает радиус окружности, возвращает ее площадь. 
    
        Пример вызова:
            Принимаемое значение: 2 (r)
            Возвращаемое значение: 12.56 (π * r²)
    '''
    if type(r) == str:
        return "Error: Invalid Length"

    if type(r) == float:
        return "Error: Not Integer Length"

    if r == 0:
        return "Error: Zero Length"

    if r < 0:
        return "Error: Negative Length"
        
    return math.pi * r * r


def perimeter(r):
    ''' Пинимает радиус окружности, возвращает ее радиус. 
        
        Пример вызова:
            Принимаемое значение: 2 (r)
            Возвращаемое значение: 12.56 (π * r * 2)
    '''
    if type(r) == str:
        return "Error: Invalid Length"

    if type(r) == float:
        return "Error: Not Integer Length"

    if r == 0:
        return "Error: Zero Length"

    if r < 0:
        return "Error: Negative Length"
        
    return 2 * math.pi * r

