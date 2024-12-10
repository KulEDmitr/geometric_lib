def area_rectangle(a, b):
    '''
    Вычисляет площадь прямоугольника из длин его сторон.

    Параметры:
        a (int/float): длина прямоугольника
        b (int/float): высота прямоугольника

    Возвращаемое значение:
        float: площадь прямоугольника

    Пример вызова:
        area_rectangle(5, 3) -> 15
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both dimensions must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Dimensions must be non-negative")
    if a > 1000000 or b > 1000000:
        raise ValueError("Dimensions are too large")
    return a * b


def perimeter_rectangle(a, b):
    '''
    Вычисляет периметр прямоугольника из длин его сторон.

    Параметры:
        a (int/float): длина прямоугольника
        b (int/float): высота прямоугольника

    Возвращаемое значение:
        float: периметр прямоугольника

    Пример вызова:
        perimeter_rectangle(5, 3) -> 16
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both dimensions must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Dimensions must be non-negative")
    if a > 1000000 or b > 1000000:
        raise ValueError("Dimensions are too large")
    return 2 * (a + b)
