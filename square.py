
def area(a):
    if (a <= 0):
        raise ValueError('Wrong input')
    '''Принимает значение a, возвращает его квадрат. Example: a = 2 => S = 4'''
    return a * a


def perimeter(a):
    if (a <= 0):
        raise ValueError('Wrong input')
    '''Принимает значение а, возвращает периметр квадрата со стороной а. Example: a = 2 => P = 8'''
    return 4 * a
