import math


def area(r):
    """
    принимает длинну радиуса окружности, возвращает площадь этой окружности
    """
    return math.pi * r * r


def perimeter(r):
    """
    принимает длинну радиуса окружности, возвращает периметр этой окружности
    """
    return 2 * math.pi * r


if __name__ == "__main__":
    print(area(5))
    print(perimeter(5))