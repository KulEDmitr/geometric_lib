def area(a: int, b: int) -> int:
    """Returns area of rectangle

		Parameters:
			a (int): length of rectangle
			b (int): width of rectangle
		Returns:
			area (int): area of rectangle

		Example:
		    rectangle.area(1, 2) = 2
		"""
    return a * b


def perimeter(a: int, b: int) -> int:
    """Returns perimeter of rectangle

        Parameters:
            a (int): length of rectangle
            b (int): width of rectangle
        Returns:
            perimeter (int): perimeter of rectangle

        Example:
            rectangle.perimeter(1, 2) = 6
        """
    return 2 * (a + b)
