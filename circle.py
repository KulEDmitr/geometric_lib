import math


def area(r):
    """
    Получает на вход r, возвращает r в квадрате умноженное на pi.

    При вызове функции area(5)
    5 * 5 * pi = 25pi
    """
    return math.pi * r * r


def perimeter(r):
    """
    Получает на вход r, возвращает r умноженное на 2 и на pi.

    При вызове функции area(5)
    5 * 2 * pi = 10pi
    """
    return 2 * math.pi * r
