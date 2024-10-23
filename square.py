def area(a):
    '''
    Функция считает и возвращает площадь квадрата.
    Аргументы:
        a (float) или (int) - длина стороны квадрата.
    Возвращаемое значение:
        S (float) или (int) - значение площади квадрата,
            (float), если a (float),
            (int), если a (int).
    Пример вызова:
        area(12)
    Вернёт:
        144
    '''
    return a * a


def perimeter(a):
    '''
    Функция считает и возвращает периметр квадрата.
    Аргументы:
        a (float) или (int) - длина стороны квадрата.
    Возвращаемое значение:
        P (float) или (int) - значение периметра квадрата,
            (float), если a (float),
            (int), если a (int).
    Пример вызова:
        perimeter(12)
    Вернёт:
        48
    '''
    return 4 * a
