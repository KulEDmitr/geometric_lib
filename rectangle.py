def area(a, b):
    """
    На вход поступают числа a и b, возвращает произведение a и b
    Пример:
        Ввод:
        a=2
        b=5
        Вывод:
        area=10
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError()
    if a < 0 or b < 0 or a > 2147483647 or b > 2147483647:
        raise ValueError()
    return a * b 

def perimeter(a, b):
    """
    На вход поступают числа a и b, возвращает удвоенное произведение a и b
    Пример:
        Ввод:
        a=5
        b=7
        Вывод:
        perimeter=24
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError()
    if a < 0 or b < 0 or a > 2147483647 or b > 2147483647:
        raise ValueError()
    return 2*(a + b)   
