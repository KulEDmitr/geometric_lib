import validation

def area(a, b):
    '''
    Возвращает площадь прямоугольника с заданными сторонами a и b

    Параметры:
        a (int|float): длина одной стороны прямоугольника
        b (int|float): длина стороны прямоугольника смежной a

    Возвращаемое значение:
        (int|float): площадь прямоугольника с заданными сторонами a и b
    
    Пример вызова:
        >>> area(3, 9)
        27
    '''

    validation.check_args(a, b)

    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника с заданными сторонами a и b

    Параметры:
        a (int|float): длина одной стороны прямоугольника
        b (int|float): длина стороны прямоугольника смежной a

    Возвращаемое значение:
        (int|float): периметр прямоугольника с заданными сторонами a и b
    
    Пример вызова:
        >>> perimeter(3, 9)
        24
    '''

    validation.check_args(a, b)

    return 2 * (a + b)