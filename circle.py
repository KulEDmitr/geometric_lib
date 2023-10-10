import math


def area(r):
    """
    print(circle.area(10)) # 314.1592653589793 

    Возвращает площадь круга с указанным радиусом

        Параметры:
            r (int) - радиус круга

        Возвращаемое значение:
            circle_area (int) - площадь круга с радиусом r
    """
    return math.pi * r * r


def perimeter(r):
    """                                                  
    print(circle.perimeter(10)) # 62.83185307179586
    
    Возвращает длину окружности с указанным радиусом

        Параметры:
            r (int) - радиус круга

        Возвращаемое значение:
            circle_perimeter (int) - длина окружности с радиусом r
    """
    return 2 * math.pi * r

