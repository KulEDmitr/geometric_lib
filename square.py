
def area(a):
    """
    На вход поступает число a, возвращает a в квадрате
    Пример:
        Ввод:
        a=7
        Вывод:
        area=49
    """
    if not isinstance(a, (int, float)):
        raise TypeError()
    if a < 0 or a > 2147483647:
        raise ValueError()
    return a * a


def perimeter(a):
    """
    На вход поступает число a, возвращает a умноженное на 4
    Пример:
        Ввод:
        a=2
        Вывод:
        perimeter=8
    """
    if not isinstance(a, (int, float)):
        raise TypeError()
    if a < 0  or a > 2147483647:
        raise ValueError()
    return 4 * a
