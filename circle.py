import math


def area(r):
    ''' 
	Returns the area of a circle by its radius
	
		Parameters:
			r (int) : radius of the circle

		Returned value:
			radius (int) : area of a circle of given radius 

	Usage:
  		area(17) = pi * 17 * 17 = 907.9202768874503
	'''
    return math.pi * r * r


def perimeter(r):
    ''' 
	Returns the perimeter of a circle by its radius
	
		Parameters:
			r (int) : radius of the circle

		Returned value:
			perimter (int) : perimter of a circle of given radius 

	Usage:
  		perimeter(17) = 2 * pi * r = 106.81415022205297
	'''
    return 2 * math.pi * r

