import math

def area(r):
    '''
    Принимает число r - радиус круга.
    Возвращает произведение π * r ^ 2 - площадь круга с радиусом r.
    Если r - отрицательное число, площадь круга мы не можем посчитать, 
        поэтому выводим ошибку "negative numbers are not allowed"
       
    Примеры вызова функции :
    Входные данные         Выходные данные
    area(1)              = 3.141592653589793
    area(5)              = 78.53981633974483
    area(10)             = 314.1592653589793
    area(-6)             = "negative numbers are not allowed"
    area(-0.75)          = "negative numbers are not allowed"
    '''
    if r < 0:
        return "negative numbers are not allowed"

    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r - радиус круга.
    Возвращает произведение 2 * π * r - периметр круга с радиусом r.

    Примеры вызова функции :
    Входные данные         Выходные данные
    perimeter(1)         = 6.283185307179586
    perimeter(5)         = 31.41592653589793
    perimeter(10)        = 62.83185307179586
    '''
    return 2 * math.pi * r

