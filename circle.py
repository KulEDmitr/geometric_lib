import math


def area(r):
    """
    Принимает число r (радиус окружности), возвращает площадь круга.

        Пример вызова функции:

            radius = 10
            S = area(radius)
            print("Area is equal to", S) # Output: "Area is equal to 31.41592653589793".
    """
    return math.pi * r * r


def perimeter(r):
    """
    Принимает число r (радиус окружности), возвращает периметр круга.

        Пример вызова функции:

            radius = 5
            P = perimeter(radius)
            print("Perimeter is equal to", P) # Output: "Perimeter is equal to 78.53981633974483".
    """
    return 2 * math.pi * r
