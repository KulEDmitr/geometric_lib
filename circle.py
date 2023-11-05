import math

def area(r):
    '''
    Принимает число r - радиус окружности, возвращает площадь круга радиуса r
    Параметры:
        r(float): вещественное число - радиус окружности
    Возвращаемое значение:
        s(float): вещественное число - площадь круга
    Пример вызова:
        S = area(2)
    Возвращаемое значение:
        S = 12.566370614359172
    '''
    s = math.pi * r * r
    return s



def perimeter(r):
    '''
    Принимает число r - радиус окружности, возвращает периметр круга радиуса r
    Параметры:
        r(float): вещественное число - радиус окружности
    Возвращаемое значение:
        p(float): вещественное число - периметр круга
    Пример вызова:
        P = perimiter(2)
    Возвращаемое значение:
        P = 12.566370614359172
    '''
    p = 2 * math.pi * r
    return p

