
def areaSquare(a):
    """
    Для квадрата: принимает число а. возвращает площадь

    Call example
    Input: 5
    Output: 25
    """
    return a * a


def perimeterSquare(a):
    """
    Для квадрата: принимает а, возвращает периметр

    Call example
    Input: 5
    Output: 20
    """
    if a <= 0:
        return ("A should be positive")
    return 4 * a

