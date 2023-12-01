def sq_area(a):
    '''
    Принимает число n, возвращает его квадрат

        Параметры:
            a (int, float, etc...) число

        Вовзращаемое значение:
            a_squared (int, float, etc...) квадрат числа а

    Пример вызова функции:
    input >> 2
    output << 4
    '''
    if a < 0:
        return "Wrong input parameters"
    return a * a


def sq_perimeter(a):
    '''
    Принимает число n, возвращает его, умноженное на 4

        Параметры:
            a (int, float, etc...) число

        Вовзращаемое значение:
            a_multiplied_by_4 (int, float, etc...) число а, умноженное на 4

    Пример вызова функции:
    input >> 2
    output << 8
    '''
    if a < 0:
        return "Wrong input parameters"
    return 4 * a

