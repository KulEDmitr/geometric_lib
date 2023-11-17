def area(a, h):
    '''Принимает числа a и h, возвращает площадь треугольника со стороной a и высотой h

       Входные данные: 3 2
       Результат: 3

       Входные данные: -3 2
       Результат: Length can't be negative

       Входные данные: 3 -2
       Результат: Height can't be negative
    '''
    if a < 0:
        raise ValueError("Length can't be negative")
    if h < 0:
        raise ValueError("Height can't be negative")
    return a * h / 2 


def perimeter(a, b, c):
    '''Принимает числа a, b и c, возвращает перимитр треугольника со сторонами a, b и c

       Входные данные: 3 2 3
       Результат: 8

       Входные данные: 3 -2 3
       Результат: Length can't be negative
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Length can't be negative")
    return a + b + c 

