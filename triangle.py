def area(a: int, h: int) -> float:
    """Returns area of triangle

		Parameters:
			a (int): one side of triangle
			h (int): height to given side of triangle
		Returns:
			area (float): area of rectangle
		"""
    return a * h / 2


def perimeter(a: int, b: int, c: int) -> int:
    """Returns perimeter of triangle

		Parameters:
			a (int): first side of triangle
			b (int): second side of triangle
			c (int): third side of triangle
		Returns:
			perimeter (int): perimeter of triangle
	"""
    return a + b + c
