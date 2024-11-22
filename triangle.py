from check_value import check_value
def area(a, h):
	'''Находит площадь треугольника.
	
	Принимает числа a, h, сторону треугольника и высоту, опущенную к стороне. 

	Пример использования:
	area(7, 8) #Возвращает 28
	'''

	if check_value(a) and check_value(h):
		return a * h / 2
	return -1

def perimeter(a, b, c): 
	'''Находит периметр треугольника.
	
	Принимает числа a, b, c, длины сторон треугольника. 

	Пример использования:
	perimeter(1, 2, 2) #Возвращает 5
	'''

	if check_value(a) and check_value(b) and check_value(c):
		return a + b + c
	return -1