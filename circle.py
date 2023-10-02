import math


def area(r: float) -> float:
    """
    Возвращает площадь круга радиусом r

	Параметры:
	    r (float): радиус круга

	Возвращаемое значение:
	    circle_area (float): Площадь круга заданного радиуса
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Возвращает периметр круга радиусом r

    Параметры:
        r (float): радиус круга

    Возвращаемое значение:
        circle_perimeter (float): Периметр круга заданного радиуса
    """

    return 2 * math.pi * r

