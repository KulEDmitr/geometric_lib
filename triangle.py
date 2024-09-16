def area(a, h):
    if a <= 0 or h <= 0:
        raise ValueError('Wrong input')
    '''Принимает значение a, h, возвращает площадь треугольника со стороной а и проведенной к ней высотой h. Example: a = 3, b = 4 => S = 6'''
    return a * h / 2

def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a>= b+c or b >= a+c or c>= a+b:
        raise ValueError('Wrong input')
    '''Принимает значения a, b, c, возвращает их сумму. Example: a = 4, b = 2, c = 3 => P = 9'''
    return a + b + c 
