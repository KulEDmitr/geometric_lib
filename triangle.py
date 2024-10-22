def area(a, h):
    '''
    Принимает числа a, h, возвращает площадь треугольника со стороной a и высотой h, проведённой к этой стороне.
    Пример вызова:
    a = 3
    h = 6
    result = area(a, h)
    print(result)
    Вывод: 9
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Принимает числа a, b, c, возвращает периметр треугольника со сторонами a, b, с.
    Пример вызова:
    a = 3
    b = 4
    c = 5
    result = perimeter(a, b, c)
    print(result)
    Вывод: 12
    '''
    return a + b + c
