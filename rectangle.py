def area(a, b): 
    """
    Вычисляет площадь прямоугольника.

    Параметры:
        a (float): длина прямоугольника.
        b (float): ширина прямоугольника.

    Возвращаемое значение:
        (float): площадь прямоугольника.

    Пример использования:
        >>> rectangle.area(5, 3)
        15
    """
    if not all(isinstance(x, (int, float)) for x in (a, b)):
        raise TypeError("Длина и ширина должны быть числами")

    if a < 0 or b < 0:
        raise ValueError("Сторона не может быть отрицательной")

    return a * b 

def perimeter(a, b): 
    """
    Вычисляет периметр прямоугольника.

    Параметры:
        a (float): длина прямоугольника.
        b (float): ширина прямоугольника.

    Возвращаемое значение:
        (float): периметр прямоугольника.

    Пример использования:
        >>> rectangle.perimeter(5, 3)
        16
    """
    if not all(isinstance(x, (int, float)) for x in (a, b)):
        raise TypeError("Длина и ширина должны быть числами")

    if a < 0 or b < 0:
        raise ValueError("Сторона не может быть отрицательной")

    return 2*(a + b)
