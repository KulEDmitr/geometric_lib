def area(a, h):
    '''
    Возвращает площадь треугольника

            Параметры:
                    a (int): сторона треугольника
                    h (int): высота треугольника, ортогональная а.

            Возвращаемое значение:
                    a*h/2 (int): одна вторая произведения a*b

    Пример:

            Входные данные:
                    a = 24
                    h = 8

            Выходные данные:
                    96
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника.

            Параметры:
                    a (int): первая сторона треугольника
                    b (int): вторая сторона треугольника
                    c (int): третья сторона треугольника

            Возвращаемое значение:
                    a + b + c (int): сумма a, b и c

    Пример:

            Входные данные:
                    a = 30
                    b = 4
                    c = 15

            Выходные данные:
                    49
    '''
    return a + b + c
