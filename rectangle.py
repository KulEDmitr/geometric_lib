
def area(a, b):
    '''
    Вычисляет площадь прямоугольника.

    Args:
        a (float): Длина первой стороны прямоугольника.
        b (float): Длина второй стороны прямоугольника.

    Returns:
        float: Площадь прямоугольника.

    Вычисление площади прямоугольника с длинами сторон 4 и 7
    import rectangle
    area_result = rectangle.area(4, 7)
    print("Площадь прямоугольника:", area_result)
    '''
    return a * b


def perimeter(a, b):
    '''
    Вычисляет периметр прямоугольника.

    Args:
        a (float): Длина первой стороны прямоугольника.
        b (float): Длина второй стороны прямоугольника.

    Returns:
        float: Периметр прямоугольника.

    Вычисление периметра прямоугольника с длинами сторон 3 и 5
    import rectangle
    perimeter_result = rectangle.perimeter(3, 5)
    print("Периметр прямоугольника:", perimeter_result)
    '''
    return (a + b) * 2


