
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
	if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
		raise TypeError
	
	if a < 0 or b < 0:
		raise ValueError
	
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
	if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
		raise TypeError
	
	if a < 0 or b < 0:
		raise ValueError

	return (a + b) * 2
