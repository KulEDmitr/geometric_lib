def rect_area(a, b):
    '''
    Принимает числа a и b, возвращает их произведение

        Параметры:
            a (int, float, etc...) первое число
            b (int, float, etc...) второе число

        Вовзращаемое значение:
            a_b_multiplied (int, float, etc...) произведение чисел а и b

    Пример вызова функции:
    input >> 2, 3
    output << 6
    '''
    if a < 0 or b < 0:
        return "Wrong input parameters"
    return a * b


def rect_perimeter(a, b):
    '''
    Принимает числа a и b, возвращает их удвоенную сумму

        Параметры:
            a (int, float, etc...) первое число
            b (int, float, etc...) второе число

        Вовзращаемое значение:
            a_b_summa_doubled (int, float, etc...) удвоенная сумма чисел а и b

    Пример вызова функции:
    input >> 2, 3
    output << 10
    '''
    if a < 0 or b < 0:
        return "Wrong input parameters"
    if (a == 0 and b > 0) or (b == 0 and a > 0):
        return "Wrong input parameters"
    return (a + b) * 2
