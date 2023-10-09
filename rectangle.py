
def area(a, b):
	''' 
	Returns the area of an rectangle by its side lengths
	
		Parameters:
			a (int) : width of the rectangle
			b (int) : length of the rectangle

		Returned value:
			a * b (int) : area of a rectangle with given sides 

	Usage:
  		area(3, 4) = 3 * 4 = 12	
	'''
	return a * b


def perimeter(a, b):
	''' 
	Returns the perimeter of an rectangle by its side lengths
	
		Parameters:
			a (int) : width of the rectangle
			b (int) : length of the rectangle

		Returned value:
			(a + b) * 2 (int) : perimeter of a rectangle with given sides 

	Usage:
 		perimeter(3, 4) = (3 + 4) * 2 = 14
	'''
	return (a + b) * 2
