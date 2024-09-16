def area(a, h):
	'''
	Возвращает площадь треугольника с высотой длиной h, опущенной к стороне длиной a.
	
		Параметры:
			a (int): длина стороны треугольника
			h (int): длина высоты треугольника
		
		Возвращаемое значение:
			res (float): площадь треугольника
	
	Пример: area(3, 2) # 3.0
	'''
	
	res = a * h / 2 
	return res


def perimeter(a, b, c): 
	'''
	Принимает числа a, b и с. Возвращает периметр треугольника со сторонами a, b и с
	
	Пример: perimeter(3, 2, 4) # 9
	'''
	return a + b + c
