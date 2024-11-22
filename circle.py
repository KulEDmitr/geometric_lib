import math """добавляем библиотеку для использования числа pi"""

def area(r): 
    """
    Принимает число r, возвращает площадь круга радиусом r
    Пример
    input: 2
    output: 12.566
    """
    return math.pi * r * r


def perimeter(r):
    """
    Принимает число r, возвращает периметр окружности радиусом r
    Пример
    input: 3
    output: 18.849
    """
    return 2 * math.pi * r

