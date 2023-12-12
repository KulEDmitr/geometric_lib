def tri_area(a, h):
    '''
    Принимает числа a и h, возвращает их полупроизведение

        Параметры:
            a (int, float, etc...) первое число
            h (int, float, etc...) второе число

        Вовзращаемое значение:
            a_h_multiplied_half (int, float, etc...) полупроизведение чисел а и h

    Пример вызова функции:
    input >> 2, 3
    output << 3
    '''
    if a < 0 or h < 0:
        return "Wrong input parameters"
    return a * h / 2


def tri_perimeter(a, b, c):
    '''
    Принимает числа a b и c, возвращает их сумму

        Параметры:
            a (int, float, etc...) первое число
            b (int, float, etc...) второе число
            c (int, float, etc...) третье число

        Вовзращаемое значение:
            a_b_c_summ (int, float, etc...) сумма чисел а,b,c

    Пример вызова функции:В
    input >> 3, 4, 5
    output << 12
    '''
    if a < 0 or b < 0 or c < 0:
        return "Wrong input parameters"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Wrong input parameters"

    return a + b + c
