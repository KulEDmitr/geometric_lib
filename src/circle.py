import math


def area(r):
    if r < 0:
        return "Incorrect input"
    '''
    Возвращает площадь круга радиуса r
	Параметры:
	   r - радиус круга
	Возращаемое значение:
	   (float) - площадь круга
	Пример вызова:
	   stdin - area(3)
	   stdout - 28.274333882308138
    '''
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        return "Incorrect input"
    '''
    Возвращает периметр круга радиуса r
	Параметры:
	   r - радиус круга
	Возращаемое значение:
	   (float) - периметр круга
	Пример вызова:
	   stdin - perimeter(3)
	   stdout - 18.84955592153876
    '''
    return 2 * math.pi * r
