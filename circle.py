import math #подключаем библиотека для использвония математических выражений

def area(r):
	'''
		Вычисляем площадь круга
		Входные значения : r - радиус круга
		Выходные значения : площадь круга
		При вызове функции для r = 10. area(10) вернет нам 3.14 * 10  * 10 = 314
	'''
    return math.pi * r * r  

	 
				


def perimeter(r):
	'''
		Вычисляем периметр круга
		Входные значения : r - радиус круга
		Выходные значения : периметр круга
		При вызовые функции для r = 10. Perimetr(10) вернет нам 2 * 3.14 * 10 = 62.8
 	'''
    return 2 * math.pi * r

