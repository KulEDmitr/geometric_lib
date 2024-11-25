def area(a, h):
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Values must be numbers")
    if a < 0 or h < 0:
        raise ValueError("Values must be positive")
    return a * h / 2


def perimeter(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float) or not isinstance(c, (int, float))):
        raise TypeError("Values must be numbers")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Values must be positive")
    return a + b + c