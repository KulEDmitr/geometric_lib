def area(a, b):
    '''
	 Принимает число a(первую сторону прямоугольника).
	 Принимает число b(вторую сторону прямоугольника).
	 Возвращает площадь прямоугольника (сторона прямоугольника, умноженная на другую)
	 Параметры:
		 a(int/float)
		 b(int/float)
	 Возвращаемое значение:
		 a*b(int/float) - площадь прямоугольника
    '''

    if a < 0:
        return -1

    if b < 0:
        return -2

    return a * b


def perimeter(a, b):
    '''
	 Принимает число a(первую сторону прямоугольника).
	 Принимает число b(вторую сторону прямоугольника).
	 Возвращает периметр прямоугольника (сумма сторон, умноженная на два)
	 Параметры:
		 a(int/float)
		 b(int/float)
	 Возвращаемое значение:
		 2*(a+b):(int/float) - периметр прямоугольника
    '''

    if a < 0:
        return -1

    if b < 0:
        return -2

    return 2 * (a + b)
