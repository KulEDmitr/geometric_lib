
def area(a):
    ''' 
    возвращает площадь квадрата со стороной a
        параметры:
            a (float) длина стороны квадрата
        возвращаемое значение:
            area (float) площадь квадрата
    примеры вызова
        area(3) --> 9
        area(1) --> 1
        area(0.45) --> 0.2025
    '''

    return a * a


def perimeter(a):
    ''' 
    возвращает периметр квадрата со стороной a
        параметры:
            a (float) длина стороны квадрата
        возвращаемое значение:
            perimeter (float) периметр квадрата
    примеры вызова
        perimeter(3) --> 12
        perimeter(1) --> 4
        perimeter(0.45) --> 1.8
    '''
    return 4 * a
