import math


def area(r):
    ''' 
	Returns the area of a circle by its radius
	
		Parameters:
			r (int) : radius of the circle

		Returned value:
			radius (int) : area of a circle of given radius 
	'''
    return math.pi * r * r


def perimeter(r):
    ''' 
	Returns the perimeter of a circle by its radius
	
		Parameters:
			r (int) : radius of the circle

		Returned value:
			perimter (int) : perimter of a circle of given radius 
	'''
    return 2 * math.pi * r

