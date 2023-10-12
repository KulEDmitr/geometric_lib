import math

def area(r):
    '''  Принимимает радиус круга, возвращает его площадь   '''
    return math.pi * r * r

def perimeter(r):
    '''  Принимает радиус круга, возвращает его периметр   '''
    return 2 * math.pi * r

"""
Пример работы программы
print(area(10))
print(perimeter(10))
314.1592653589793
62.83185307179586
"""