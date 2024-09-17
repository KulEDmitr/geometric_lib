def area(a, h):
    """
    Return the area of the triangle.

    Args:
        a (int): triangle side length.
        h (int): triangle altitude length.
          This height must be drawn to the side of length a.

    Example:
        area(3, 4) --> 6
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Return the perimeter of the triangle.

    Args:
        a (int): length of first side of triangle.
        b (int): length of second side of triangle.
        c (int): length of third side of triangle.

    Example:
        perimeter(3, 4, 5) --> 12
    """
    return a + b + c
