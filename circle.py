import math


def area(r):
    """
    На вход поступает число r, возвращает r^2*pi
    Пример:
        Ввод:
        r=2
        Вывод:
        area=12.56
    """
    return math.pi * r * r
    


def perimeter(r):
    """
    На вход поступает число r, возвращает r*2*pi
    Пример:
        Ввод:
        r=4
        Вывод:
        perimeter=25.132
    """
    return 2 * math.pi * r

