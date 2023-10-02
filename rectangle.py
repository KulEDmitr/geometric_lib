def area(a: float, b: float) -> float:
    """
    Возвращает площадь прямоугольника со сторонами a и b

    Параметры:
    	a, b (float): стороны прямоугольника

    Возвращаемое значение:
    	rectangle_area (float): Площадь прямоугольника с заданными сторонами
    """
    return a * b

def perimeter(a, b):
    """
    Возвращает периметр прямоугольника со сторонами a и b

    Параметры:
        a, b (float): стороны прямоугольника

    Возвращаемое значение:
        rectangle_perimeter (float): Периметр прямоугольника с заданными сторонами
    """

    return 2 * (a + b)
