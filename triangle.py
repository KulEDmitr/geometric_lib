
def area(a, h):
	''' 
	Returns the area of a triangle by base and height
	
		Parameters:
			a (int) : base of the triangle
			h (int) : height of the triangle 

		Returned value:
			a * h / 2 (int) : area of a square with given base and height

	Usage:
  		area(10, 7) = 10 * 7 / 2 = 35
	'''
	if (not isinstance(a, (int, float))) or (not isinstance(h, (int, float))):
		raise TypeError
	
	if a <= 0 or h <= 0:
		raise ValueError

	return a * h / 2
	

def perimeter(a, b, c):
	''' 
	Returns the perimeter of a triangle by its 3 sides
	
		Parameters:
			a (int) : a side of the triangle
			b (int) : another side of the triangle
			c (int) : another side of the triangle

		Returned value:
			a + b + c (int) : perimeter of the triangle with 3 given sides

	Usage:
  		perimeter(4, 5, 6) = 4 + 5 + 6 = 15
	'''
	if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))) or (not isinstance(c, (int, float))):
		raise TypeError

	if a <= 0 or b <= 0 or c <= 0:
		raise ValueError

	if (a + b) <= c or (c + a) <= b or (b + c) <= a:
		raise ValueError

	return a + b + c
