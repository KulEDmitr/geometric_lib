def area(a):
    '''
    Принимает число а - сторонy квадрата, возвращает площадь квадрата со стороной а
    Параметры:
        a(float): вещественное число - длина стороны квадрата
    Возвращаемое значение:
        s(float): вещественное число - площадь квадрата
    Пример вызова:
        S = area(2)
    Возвращаемое значение:
        S = 4
    '''
    s = a * a
    return s


def perimeter(a):
    '''
    Принимает число а - сторонy квадрата, возвращает периметр квадрата со стороной а
    Параметры:
        a(float): вещественное число - длина стороны квадрата
    Возвращаемое значение:
        p(float): вещественное число - периметр квадрата
    Пример вызова:
        P = perimeter(2)
    Возвращаемое значение:
        P = 8
    '''
    p = 4 * a
    return p
