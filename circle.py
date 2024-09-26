import math


def area(r):
    '''
    Вычисляет площадь круга.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Площадь круга.

    Вычисление площади круга с радиусом 5
    import circle
    area_result = circle.area(5)
    print("Площадь круга:", area_result)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет длину окружности.

    Args:
        r (float): Радиус окружности.

    Returns:
        float: Длина окружности.

    Вычисление длины окружности с радиусом 7
    import circle
    perimeter_result = circle.perimeter(7)
    print("Длина окружности:", perimeter_result)
    '''
    return 2 * math.pi * r


