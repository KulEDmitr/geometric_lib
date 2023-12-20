def area(a, b):
    '''Принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b

       Входные данные: 3 2
       Результат: 6

       Входные данные: -3 2
       Результат: Length can't be negative
    '''
    if a < 0 or b < 0:
        raise ValueError("Length can't be negative")
    return a * b 


def perimeter(a, b):
    '''Принимает числа a и b, возвращает пириметр прямоугольника со сторонами a и b

       Входные данные: 3 2
       Результат: 12

       Входные данные: 3 -2
       Результат: Length can't be negative
    '''
    if a < 0 or b < 0:
        raise ValueError("Length can't be negative")
    return 2*(a + b)

