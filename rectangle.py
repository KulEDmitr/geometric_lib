from check_value import check_value


def area(a, b):
    '''Находит площадь прямоугольника.
	
	Принимает число a, b, стороны прямоугольника. 

	Пример использования:
	area(7, 8) #Возвращает 56
	'''

    if check_value(a) and check_value(b):
        return a * b
    return -1


def perimeter(a, b):
    '''Находит периметр прямоугольника.
	
	Принимает число a, b, стороны прямоугольника. 

	Пример использования:
	area(7, 8) #Возвращает 30
	'''

    if check_value(a) and check_value(b):
        return (a + b) * 2
    return -1
