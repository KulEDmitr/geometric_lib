def area(a, h):
    '''
    Принимает число а - длину стороны и число h - высоту, проведенную к стороне а,
    возвращает площадь треугольника
    Параметры:
        a(float): вещественное число - длина стороны треугольника
        h(float): вещественное число - длина высоты треугольника, проведенной к стороне а
    Возвращаемое значение:
        s(float): вещественное число - площадь прямоугольника
    Пример вызова:
        S = area(2, 5)
    Возвращаемое значение:
        S = 5
    '''
    s = a * h / 2
    return s

def perimeter(a, b, c):
    '''
    Принимает числа а, b, c - длины сторон треугольника,
    возвращает периметр треугольника
    Параметры:
        a(float): вещественное число - длина первой стороны треугольника
        b(float): вещественное число - длина второй стороны треугольника
        c(float): вещественное число - длина третьей стороны треугольника
    Возвращаемое значение:
        p(float): вещественное число - периметр прямоугольника
    Пример вызова:
        P = perimeter(2, 4, 5,)
    Возвращаемое значение:
        P = 11
    '''
    p = a + b + c
    return p
