
def area(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Values must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Values must be positive")
    return a * b


def perimeter(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Values must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Values must be positive")
    return 2 * a + 2 * b