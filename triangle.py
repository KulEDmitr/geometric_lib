import unittest


def existing(a, b, c):
    """
    
    Принимает переменные a, b и c, стороны треугольника
    И возвращает true если треугольник существует
    false в обратном случае
    Пример вызова:
    existing(1, 1, 1)
    Возвращаемое значение:
    true
    """
    if a + b > c and a + c > b and c + b > a:
        return True
    return False


def area(a, b, c):
    """
    Принимает переменные a, b и c, стороны треугольника
    И возвращает его площадь, если треугольник существует
    -1 если нет
    Пример вызова:
    area(3, 4, 5)
    Возвращаемое значение:
    8
    """
    half_per = (a + b + c) / 2
    if existing(a, b, c):
        return (half_per * (half_per - a) * (half_per - b) * (half_per - c)) ** 0.5
    return -1


def perimeter(a, b, c):
    """
    Принимает переменные a, b и c, стороны треугольника
    И возвращает его периметр, если треугольник существует
    -1, если нет
    Пример вызова:
    perimeter(1, 1, 1)
    Возвращаемое значение:
    3
    """
    if existing(a, b, c):
        return a + b + c
    return -1

