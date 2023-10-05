
def area(a, h): 
    """
    Возвращает площадь треугольника с указанной стороной и высотой, проведенной к ней

        Параметры:
            a (int) - длина стороны (основания)
            h (int) - длина высоты

        Возвращаемое значение:
            triangle_area (int) - площадь треугольника со стороной равной a и высотой, проведенной к ней, равной h
    """
    return a * h / 2 

def perimeter(a, b, c): 
    """
    Возвращает периметр треугольника с указанными сторонами

        Параметры:
            a (int) ┐
            b (int) ╪ - длины сторон
            c (int) ┘

        Возвращаемое значение:
            triangle_perimeter (int) - периметр треугольника со сторонами a, b, c
    """
    return a + b + c 
