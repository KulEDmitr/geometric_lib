import math
print(90000000000 * 2 * math.pi)
def CircleArea(r):
    """
    Принимает число r - радиус круга;
        Возвращает площадь круга - произведение квадрата числа r и числа Пи

    Call example:
        Input: 10
        Output: 314.1592653589793

    """
    return math.pi * r * r


def CirclePerimeter(r):
    """
    Принимает число r - радиус круга;
        Возвращает периметр круга - произведение удвоенного числа r и числа Пи

    Call example:
        Input: 10
        Output: 62.83185307179586

     """
    return 2 * math.pi * r