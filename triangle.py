
def area(a, h):
    """
    На вход поступают числа a и h, возвращает a умноженное на половину h
    Пример:
        Ввод:
        a=5
        h=4
        Вывод:
        area=10
    """
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError()
    if a < 0 or h < 0 or a > 2147483647 or h > 2147483647:
        raise ValueError()
    
    return a * h / 2 

def perimeter(a, b, c):
    """
    На вход поступают числа a, b и c, возвращает сумму этих чисел
    Пример:
        Ввод:
        a=2
        b=3
        c=4
        Вывод:
        perimeter=9
    """
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError()
    if a < 0 or b < 0 or c < 0 or  a > 2147483647 or b > 2147483647 or c > 2147483647:
        raise ValueError()
    
    return a + b + c
