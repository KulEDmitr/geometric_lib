import math


def area(r):
    '''
    Возрващает площадь круга
	
	Параметры:
		r (int): радиус круга
	
	Воращаемое значение
		area (float): площадь искомого круга

	Пример вызова:
        circle_area = area(5)
    Результат:
        circle_area = 78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возрващает периметр круга (длина окружности)
	
	Параметры:
		r (int): радиус круга
	
	Воращаемое значение
		perimeter (float): периметр искомого круга (длина окружности)

	Пример вызова:
        circle_perimeter = perimeter(5)
    Результат:
        circle_perimeter = 31.41592653589793
    '''
    return 2 * math.pi * r

