import math
from check_value import check_value

def area(r):
	'''Находит площадь окружности.
	
	Принимает число r, радиус окружности. 

	Пример использования:
	area(7) #Возвращает 153.93804002589985
	'''
	if check_value(r):
		return math.pi * r * r
	return -1

def perimeter(r):
	'''Находит длину окружности.
	
	Принимает число r, радиус окружности. 

	Пример использования:
	perimeter(7) #Возвращает 43.982297150257104
	'''
	if check_value(r):
		return 2 * math.pi * r
	return -1

