import math


def area(r):
	'''Возвращает площадь круга с радиусом r.
	
		Параметры:
			r (int): длина радиуса круга
		
		Возвращаемое значение:
			res (float): площадь круга
	'''
	
	res = math.pi * r * r
	return res


def perimeter(r):
	''' Принимает число r. Возвращает периметр круга с радиусом r'''
    return 2 * math.pi * r
