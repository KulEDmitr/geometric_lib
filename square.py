def area(a):
    '''Принимает число a, возвращает площадь квадрата со стороной a

       Входное значение: 4
       Результат: 16

       Входное значение: -4
       Результат: Length can't be negative
    '''
    if a < 0:
        raise ValueError("Length can't be negative")
    return a * a


def perimeter(a):
    '''Принимает число a, возвращает периметр квадрата со стороной a

       Входное значение: 4
       Результат: 16

       Входное значение: -4
       Результат: Length can't be negative
    '''
    if a < 0:
        raise ValueError("Length can't be negative")
    return 4 * a

