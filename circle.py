import math


def area(r: int) -> int:
	"""
	Gets radius of circle, returns area

	Example:
		circle.area(2) = 12.566370614359172
	"""
	return math.pi * r * r


def perimeter(r: int) -> int:
	"""
	Gets perimeter of circle, returns perimeter

	Example:
		circle.perimeter(3) = 18.84955592153876
	"""
	return 2 * math.pi * r
