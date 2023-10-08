def area(a, h):
    '''
    Принимает 2 числа: a и h, - основание треугольника и высота к этому основанию соответственно.
    Возвращает площадь треугольника с основанием a и высотой к этому основанию h (половина произведения чисел a и h):
    print(area(5, 4)) -> 10
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Принимает 3 числа: a, b и c, - стороны треугольника.
    Возвращает периметр треугольника со сторонами (половина произведения чисел a и h):
    print(perimeter(3, 4, 5)) -> 12
    '''
    return a + b + c