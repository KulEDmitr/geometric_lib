from check_value import check_value
def area(a):
	'''Находит площадь квадрата.
	
	Принимает число a, сторону квадрата. 

	Пример использования:
	area(7) #Возвращает 49
	'''

	if check_value(a):
		return a * a
	return -1


def perimeter(a):

	'''Находит периметр квадрата.
	
	Принимает число a, сторону квадрата. 

	Пример использования:
	area(7) #Возвращает 28
	'''


	if check_value(a):
		return a * 4
	return -1